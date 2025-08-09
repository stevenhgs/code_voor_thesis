from src.custom_classes.Relation import Relation
from src.custom_classes.Literal import Literal
from math import log2, inf
from collections import defaultdict


def get_negative_examples(positive_examples, target_relation_arity, all_objects):
    negative_examples = set()

    def dfs(current_path):
        if len(current_path) == target_relation_arity:
            new_candidate = tuple(current_path)
            if new_candidate not in positive_examples:
                negative_examples.add(new_candidate)
            return
        for obj in all_objects:
            dfs(current_path + [obj])

    dfs([])
    return negative_examples


def generate_candidate_literals_from_base_relation(base_relation, nb_existing_variables):
    variable_combinations = []
    relation_arity = base_relation.arity

    def get_all_variable_combinations(current_variables_for_literal, used_an_existing_variable, variable_counter):
        if len(current_variables_for_literal) == relation_arity:
            if used_an_existing_variable:
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
        candidate_literals.append(Literal(True, base_relation.name, base_relation.arity, variable_combination))
        candidate_literals.append(Literal(False, base_relation.name, base_relation.arity, variable_combination))

    return candidate_literals


def get_all_variable_combinations_for_equals(nb_current_variables):
    equal_combinations = []
    for i in range(nb_current_variables):
        for j in range(i + 1, nb_current_variables):
            equal_combinations.append((i, j))
    return equal_combinations


def get_candidate_literals(base_relations, target_relation, nb_current_variables):
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

    return candidate_literals


def calculate_value(nb_positive_examples, nb_negative_examples):
    return -log2(nb_positive_examples / (nb_positive_examples + nb_negative_examples))


def get_positive_and_negative_tuples_from_equals(equals_literal, positive_examples, negative_examples):
    """
    Precondition: equals_literal introduces no new variables.
    """
    nb_covered_old_positive_examples = 0
    new_positive_examples = []
    new_negative_examples = []
    variable1, variable2 = equals_literal.variables

    for positive_example in positive_examples:
        if equals_literal.is_negated:
            if positive_example[variable1] != positive_example[variable2]:
                new_positive_examples.append(positive_example)
                nb_covered_old_positive_examples += 1
        else:
            if positive_example[variable1] == positive_example[variable2]:
                new_positive_examples.append(positive_example)
                nb_covered_old_positive_examples += 1

    for negative_example in negative_examples:
        if equals_literal.is_negated:
            if negative_example[variable1] != negative_example[variable2]:
                new_negative_examples.append(negative_example)
        else:
            if negative_example[variable1] == negative_example[variable2]:
                new_negative_examples.append(negative_example)

    return nb_covered_old_positive_examples, new_positive_examples, new_negative_examples



def get_positive_and_negative_tuples_from_literal(literal, relation, positive_examples, negative_examples, nb_of_variables):
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

    # example assume relation Q has (a, b, c) as an example
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
            for extension in extensions:
                new_positive_examples.append(tuple(list(positive_example) + extension))
            nb_covered_old_positive_examples += 1

    for negative_example in negative_examples:
        anchored_negative_example = []
        for variable in anchored_variables:
            anchored_negative_example.append(negative_example[variable])
        anchored_negative_example = tuple(anchored_negative_example)
        extensions = anchored_examples_to_extension_of_examples_from_relation[anchored_negative_example]
        if len(extensions) > 0:
            for extension in extensions:
                new_negative_examples.append(tuple(list(negative_example) + extension))

    return nb_covered_old_positive_examples, new_positive_examples, new_negative_examples


def calculate_foil_gain(covered_old_examples, old_positive_examples, old_negative_examples, new_positive_examples, new_negative_examples, arity_of_target_relation):
    nb_old_positive_examples = len(old_positive_examples)
    nb_old_negative_examples = len(old_negative_examples)
    nb_new_positive_examples = len(new_positive_examples)
    nb_new_negative_examples = len(new_negative_examples)
    # print(f'{covered_old_examples=}, {nb_old_positive_examples=}, {nb_old_negative_examples=}, {nb_new_positive_examples=}, {nb_new_negative_examples=}')
    if nb_new_positive_examples == 0 or (nb_new_positive_examples == 0 and nb_new_negative_examples == 0):
        return -inf
    return covered_old_examples * (calculate_value(nb_old_positive_examples, nb_old_negative_examples) - calculate_value(nb_new_positive_examples, nb_new_negative_examples))


def get_nb_of_truncated_examples(examples, arity):
    seen = set()
    for example in examples:
        seen.add(example[:arity])
    return len(seen)


def calculate_foil_gain_truncated(covered_old_examples, old_positive_examples, old_negative_examples, new_positive_examples, new_negative_examples, arity_of_target_relation):
    nb_old_positive_examples = get_nb_of_truncated_examples(old_positive_examples, arity_of_target_relation)
    nb_old_negative_examples = get_nb_of_truncated_examples(old_negative_examples, arity_of_target_relation)
    nb_new_positive_examples = get_nb_of_truncated_examples(new_positive_examples, arity_of_target_relation)
    nb_new_negative_examples = get_nb_of_truncated_examples(new_negative_examples, arity_of_target_relation)
    # print(f'{covered_old_examples=}, {nb_old_positive_examples=}, {nb_old_negative_examples=}, {nb_new_positive_examples=}, {nb_new_negative_examples=}')
    if nb_new_positive_examples == 0 or (nb_new_positive_examples == 0 and nb_new_negative_examples == 0):
        return -inf
    return covered_old_examples * (calculate_value(nb_old_positive_examples, nb_old_negative_examples) - calculate_value(nb_new_positive_examples, nb_new_negative_examples))


def get_new_uncovered_positive_examples(positive_examples_before, current_positive_examples, nb_base_variables):
    covered_examples = set()
    for current_positive_example in current_positive_examples:
        shortened_positive_example = []
        for i in range(nb_base_variables):
            shortened_positive_example.append(current_positive_example[i])
        covered_examples.add(tuple(shortened_positive_example))

    uncovered_examples = []
    for positive_example_before in positive_examples_before:
        if positive_example_before not in covered_examples:
            uncovered_examples.append(positive_example_before)

    return uncovered_examples


def foil(target_relation, base_relation_name_to_base_relations, all_objects):
    target_relation_arity = target_relation.arity
    target_relation.generate_negative_examples(all_objects)
    negative_examples = target_relation.negative_examples
    positive_examples = target_relation.positive_examples
    head = Literal(False, target_relation.name, target_relation.arity, [i for i in range(target_relation_arity)])
    nb_base_variables = target_relation_arity
    for _, base_relation in base_relation_name_to_base_relations.items():
        base_relation.generate_negative_examples(all_objects)
    learned_rules = []

    while positive_examples:
        new_rule = []
        current_negative_examples = set(negative_examples)
        current_positive_examples = set(positive_examples)
        nb_current_variables = nb_base_variables
        while current_negative_examples:
            print(f'{len(learned_rules)}.{len(new_rule)}')
            literal_candidates = get_candidate_literals(base_relation_name_to_base_relations, target_relation, nb_current_variables)
            best_foil_gain = -inf
            best_literal = None
            best_new_positive_examples = None
            best_new_negative_examples = None
            for literal_candidate in literal_candidates:
                if literal_candidate.name == "_Equals":
                    associated_relation = None
                elif literal_candidate.name == target_relation.name:
                    associated_relation = target_relation
                else:
                    associated_relation = base_relation_name_to_base_relations[literal_candidate.name]
                covered_old_positive_examples, new_positive_examples, new_negative_examples = get_positive_and_negative_tuples_from_literal(literal_candidate, associated_relation, current_positive_examples, current_negative_examples, nb_current_variables)
                print(f'{literal_candidate=}')
                print(f'positive: {new_positive_examples}')
                print(f'negative: {new_negative_examples}')
                foil_gain = calculate_foil_gain(covered_old_positive_examples,
                                                current_positive_examples,
                                                current_negative_examples,
                                                new_positive_examples,
                                                new_negative_examples,
                                                nb_base_variables)
                print(f'{foil_gain=}')
                if foil_gain >= best_foil_gain:
                    best_literal = literal_candidate
                    best_new_positive_examples = new_positive_examples
                    best_new_negative_examples = new_negative_examples
                    best_foil_gain = foil_gain
            new_rule.append(best_literal)
            current_positive_examples = best_new_positive_examples
            current_negative_examples = best_new_negative_examples
            nb_current_variables = max(nb_current_variables, max(best_literal.variables) + 1)
            print("pos: ", current_positive_examples)
            print("neg: ", current_negative_examples)
            print("nb variables: ", nb_current_variables)
            print(f'{new_rule=}\n')
        learned_rules.append(new_rule)
        positive_examples = get_new_uncovered_positive_examples(positive_examples, current_positive_examples, nb_base_variables)
    return head, learned_rules


if __name__ == "__main__":
    """
    lit1 = Literal(False, "A", 3, [3, 2, 4])
    rel1 = Relation("A", 3, [("y", "c", "x"), ("k", "c", "l"), ("k", "d", "m")])
    print(get_positive_and_negative_tuples_from_literal(lit1, rel1, [("a", "b", "c"), ("a", "b", "d")], [("r", "s", "c")], 3))
    """
    target_relation = Relation("2hop", 2, [(2, 5)])
    base_relations = {
        "DirectlyConnected": Relation("DirectlyConnected", 2, [(1, 3), (1, 4), (2, 4), (3, 5), (4, 5)])
    }
    print(foil(target_relation, base_relations, [1, 2, 3, 4, 5]))
