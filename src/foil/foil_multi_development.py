from src.foil.foil import *

SMALL_VALUE = 0.000001


def inner_foil_loop(target_relation, base_relation_name_to_base_relations, current_positive_examples, current_negative_examples, nb_base_variables, nb_current_variables):
    if len(current_negative_examples) == 0:
        return [(current_positive_examples, [])]
    literal_candidates = get_candidate_literals(base_relation_name_to_base_relations, target_relation, nb_current_variables)
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
        covered_old_positive_examples, new_positive_examples, new_negative_examples = get_positive_and_negative_tuples_from_literal(literal_candidate, associated_relation, current_positive_examples, current_negative_examples, nb_current_variables)
        foil_gain = calculate_foil_gain_truncated(covered_old_positive_examples,
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


def foil_multi_development(target_relation, base_relation_name_to_base_relations, all_objects):
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
    print(foil_multi_development(target_relation, base_relations, [0, 1, 2, 3, 4, 5]))