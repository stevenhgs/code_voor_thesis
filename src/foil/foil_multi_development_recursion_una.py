from src.foil.foil import *

SMALL_VALUE = 0.000001


def generate_candidate_literals_for_target_relation(target_relation, nb_existing_variables):
    """
    Generates all possible tuples of variables where at least one current_variable is present.
    Does not generate the tuple for (0, 1, ..., n) because this is in the head.
    """
    variable_combinations = []
    relation_arity = target_relation.arity
    head_variable_combination = tuple([i for i in range(relation_arity)])

    def get_all_variable_combinations(current_variables_for_literal, used_an_existing_variable, variable_counter):
        if len(current_variables_for_literal) == relation_arity:
            if used_an_existing_variable and tuple(current_variables_for_literal) != head_variable_combination:
                variable_combinations.append(current_variables_for_literal)
            return
        # use existing variables
        for i in range(nb_existing_variables):
            get_all_variable_combinations(current_variables_for_literal + [i], True, variable_counter)
        # use newly used variables again
        for i in range(nb_existing_variables, variable_counter):
            get_all_variable_combinations(current_variables_for_literal + [i], used_an_existing_variable,
                                          variable_counter)
        # use a completely new variable
        get_all_variable_combinations(current_variables_for_literal + [variable_counter], used_an_existing_variable, variable_counter + 1)

    get_all_variable_combinations([], False, nb_existing_variables)
    candidate_literals = []
    for variable_combination in variable_combinations:
        candidate_literals.append(Literal(True, target_relation.name, target_relation.arity, variable_combination))
        candidate_literals.append(Literal(False, target_relation.name, target_relation.arity, variable_combination))

    return candidate_literals


def get_candidate_literals_recursive(base_relations, target_relation, nb_current_variables):
    """
    This method generates all candidate literals.
    This is done in such a way that each base relation is considered and its negation.
    The variables used in each literal are made up in such a way that the literal should have at least one variable from
    current_variables.
    Also Equals(X_i, X_j) for all 0 <= i < j < nb_current_variables is added and all its negations.
    """
    candidate_literals = []
    for _, base_relation in base_relations.items():
        candidate_literals += generate_candidate_literals_from_base_relation(base_relation, nb_current_variables)

    # equals
    variable_combinations_for_equals = get_all_variable_combinations_for_equals(nb_current_variables)
    for variable_combination in variable_combinations_for_equals:
        candidate_literals.append(Literal(True, "_Equals", 2, variable_combination))
        candidate_literals.append(Literal(False, "_Equals", 2, variable_combination))

    # recursion
    recursive_literals = generate_candidate_literals_for_target_relation(target_relation, nb_current_variables)
    candidate_literals += recursive_literals
    return candidate_literals

def get_positive_and_negative_tuples_from_literal_una(literal, relation, positive_examples, negative_examples, nb_of_variables):
    """
    It is important that all the newly introduced variables in the literal are all in ascending order.
    For example literal Q(P3,P2,P4) with the newly introduced variables P3 and P4.
    Say there is a positive example tuple (a, b, c) from the previous variables (P0, P1, P2).
    For this example we want to find all examples in the relation where (_, c, _).
    Let's say there is an example (y, c, x) in relation Q.
    Then the new positive example would become (a, b, c, y, x)
    """
    if literal.name == "_Equals":
        return get_positive_and_negative_tuples_from_equals(literal, positive_examples, negative_examples)
    nb_covered_old_positive_examples = 0
    new_positive_examples = []
    new_negative_examples = []
    if literal.is_negated:
        relation_examples = relation.negative_examples
    else:
        relation_examples = relation.positive_examples

    # anchored variables are variables that are not newly introduced by this literal
    anchored_variable_indices = set()
    anchored_variables = []
    for index, variable in enumerate(literal.variables):
        if variable < nb_of_variables:
            anchored_variable_indices.add(index)
            anchored_variables.append(variable)

    # example: assume relation Q has (a, b, c) as an example
    # and the anchored indices are (0, 2) then the anchored example would become (a, c)
    # and the extension would be (b)
    anchored_examples_to_extension_of_examples_from_relation = defaultdict(list)
    for positive_example_from_relation in relation_examples:
        anchored_positive_example_from_relation = []
        extension = []
        for index in range(len(positive_example_from_relation)):
            if index in anchored_variable_indices:
                anchored_positive_example_from_relation.append(positive_example_from_relation[index])
            else:
                extension.append(positive_example_from_relation[index])
        anchored_examples_to_extension_of_examples_from_relation[tuple(anchored_positive_example_from_relation)].append(extension)

    for positive_example in positive_examples:
        anchored_positive_example = []
        for variable in anchored_variables:
            anchored_positive_example.append(positive_example[variable])
        anchored_positive_example = tuple(anchored_positive_example)
        extensions = anchored_examples_to_extension_of_examples_from_relation[anchored_positive_example]
        if len(extensions) > 0:
            nb_candidates_passed = 0
            for extension in extensions:
                # filter if a tuple has same bindings for different variables))
                candidate = tuple(list(positive_example) + extension)
                seen = set()
                for binding in candidate:
                    if binding in seen:
                        break
                    seen.add(binding)
                else:
                    new_positive_examples.append(candidate)
                    nb_candidates_passed += 1
            if nb_candidates_passed > 0:
                nb_covered_old_positive_examples += 1

    for negative_example in negative_examples:
        anchored_negative_example = []
        for variable in anchored_variables:
            anchored_negative_example.append(negative_example[variable])
        anchored_negative_example = tuple(anchored_negative_example)
        extensions = anchored_examples_to_extension_of_examples_from_relation[anchored_negative_example]
        if len(extensions) > 0:
            for extension in extensions:
                # filter if a tuple has same bindings for different variables))
                candidate = tuple(list(negative_example) + extension)
                seen = set()
                for binding in candidate:
                    if binding in seen:
                        break
                    seen.add(binding)
                else:
                    new_negative_examples.append(tuple(list(negative_example) + extension))

    return nb_covered_old_positive_examples, new_positive_examples, new_negative_examples


def inner_foil_loop(target_relation, base_relation_name_to_base_relations, current_positive_examples, current_negative_examples, nb_base_variables, nb_current_variables):
    if len(current_negative_examples) == 0:
        return [(current_positive_examples, [])]
    literal_candidates = get_candidate_literals_recursive(base_relation_name_to_base_relations, target_relation, nb_current_variables)
    best_foil_gain = -inf
    best_literals = []
    best_new_positive_examples = []
    best_new_negative_examples = []
    for literal_candidate in literal_candidates:
        if literal_candidate.name == "_Equals":
            associated_relation = None
        elif literal_candidate.name == target_relation.name:
            associated_relation = target_relation
        else:
            associated_relation = base_relation_name_to_base_relations[literal_candidate.name]
        covered_old_positive_examples, new_positive_examples, new_negative_examples = get_positive_and_negative_tuples_from_literal_una(literal_candidate, associated_relation, current_positive_examples, current_negative_examples, nb_current_variables)
        foil_gain = calculate_foil_gain(covered_old_positive_examples,
                                        current_positive_examples,
                                        current_negative_examples,
                                        new_positive_examples,
                                        new_negative_examples,
                                        nb_base_variables)
        if foil_gain > best_foil_gain + SMALL_VALUE:  # greater_than
            best_literals = [literal_candidate]
            best_new_positive_examples = [new_positive_examples]
            best_new_negative_examples = [new_negative_examples]
            best_foil_gain = foil_gain
        elif foil_gain >= best_foil_gain - SMALL_VALUE:
            best_literals.append(literal_candidate)
            best_new_positive_examples.append(new_positive_examples)
            best_new_negative_examples.append(new_negative_examples)

    # output is a list of rules and their current_positive_examples_sub
    output = []
    for i in range(len(best_literals)):
        current_positive_examples = best_new_positive_examples[i]
        current_negative_examples = best_new_negative_examples[i]
        new_nb_current_variables = max(nb_current_variables, max(best_literals[i].variables) + 1)
        sub_output = inner_foil_loop(target_relation, base_relation_name_to_base_relations, current_positive_examples, current_negative_examples, nb_base_variables, new_nb_current_variables)
        for current_positive_examples_sub, new_rule_sub in sub_output:
            output.append((current_positive_examples_sub, [best_literals[i]] + new_rule_sub))
    return output


def outer_foil_loop(target_relation, base_relation_name_to_base_relations, positive_examples, negative_examples, nb_base_variables):
    # this returns a disjunction of rules, a rule is a conjunction of literals
    if len(positive_examples) == 0:
        return [[]]
    current_negative_examples = set(negative_examples)
    current_positive_examples = set(positive_examples)
    nb_current_variables = nb_base_variables
    # inner_loop_output is a list of rules with their positive_examples still to handle
    inner_loop_output = inner_foil_loop(target_relation, base_relation_name_to_base_relations, current_positive_examples, current_negative_examples, nb_base_variables, nb_current_variables)
    # output should be a list of rule groups
    # a rule group is a list of rules
    # a rule is a list of literals
    output = []
    for current_positive_examples, new_rule in inner_loop_output:
        positive_examples = get_new_uncovered_positive_examples(positive_examples, current_positive_examples, nb_base_variables)
        new_rule_groups_sub = outer_foil_loop(target_relation, base_relation_name_to_base_relations, positive_examples, negative_examples, nb_base_variables)
        for new_rule_group in new_rule_groups_sub:
            output.append([new_rule] + new_rule_group)
    return output


def foil_multi_development_recursion_una(target_relation, base_relation_name_to_base_relations, all_objects):
    target_relation_arity = target_relation.arity
    target_relation.generate_negative_examples(all_objects)
    negative_examples = target_relation.negative_examples
    positive_examples = target_relation.positive_examples
    head = Literal(False, target_relation.name, target_relation.arity, [i for i in range(target_relation_arity)])
    nb_base_variables = target_relation_arity
    for _, base_relation in base_relation_name_to_base_relations.items():
        base_relation.generate_negative_examples(all_objects)
    learned_rules_groups = outer_foil_loop(target_relation, base_relation_name_to_base_relations, positive_examples, negative_examples, nb_base_variables)
    output = []
    for learned_rules_group in learned_rules_groups:
        output.append((head, learned_rules_group))
    return output


if __name__ == "__main__":
    """
    lit1 = Literal(False, "A", 3, [3, 2, 4])
    rel1 = Relation("A", 3, [("y", "c", "x"), ("k", "c", "l"), ("k", "d", "m")])
    print(get_positive_and_negative_tuples_from_literal(lit1, rel1, [("a", "b", "c"), ("a", "b", "d")], [("r", "s", "c")], 3))
    """

    target_relation = Relation("2hop", 2, [(0, 3), (1, 4), (2, 4), (1, 5), (2, 5)])
    base_relations = {
        "DirectlyConnected": Relation("DirectlyConnected", 2, [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5)])
    }
    print(foil_multi_development_recursion_una(target_relation, base_relations, [0, 1, 2, 3, 4, 5]))