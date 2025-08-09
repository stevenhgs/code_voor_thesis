import math
import time

from src.custom_classes.Relation import Relation
from src.custom_classes.Literal import Literal
from src.custom_classes.Rule import Rule
from math import log2, inf
from collections import defaultdict
import heapq


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


def get_candidate_literals(base_relations, nb_current_variables):
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

    """
    # equals
    variable_combinations_for_equals = get_all_variable_combinations_for_equals(nb_current_variables)
    for variable_combination in variable_combinations_for_equals:
        candidate_literals.append(Literal(True, "_Equals", 2, variable_combination))
        candidate_literals.append(Literal(False, "_Equals", 2, variable_combination))
    """

    return candidate_literals


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
    # literal (0, 1, 3, 2, 2) and previously 0..2 already existed
    # anchored_variable_indices = {0, 1, 3, 4}
    # anchored_variables = [0, 1, 2, 2]
    anchored_variable_indices = set()
    anchored_variables = []
    for index, variable in enumerate(literal.variables):
        if variable < nb_of_variables:
            anchored_variable_indices.add(index)
            anchored_variables.append(variable)

    # example assume relation Q has (a, b, c) as an example
    # and the anchored indices are (0, 2) then the anchored example would become (a, c)
    # and the extension would be (b) so new example would become (a, c, b)
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

def get_nb_of_truncated_examples(examples, arity):
    seen = set()
    for example in examples:
        # + 1 because of context
        seen.add(example[:arity])
    return len(seen)


def get_new_uncovered_positive_examples(positive_examples_before, current_positive_examples, arity):
    covered_examples = set()
    for current_positive_example in current_positive_examples:
        shortened_positive_example = []
        # + 1 because of context
        for i in range(arity):
            shortened_positive_example.append(current_positive_example[i])
        covered_examples.add(tuple(shortened_positive_example))

    uncovered_examples = []
    for positive_example_before in positive_examples_before:
        if positive_example_before not in covered_examples:
            uncovered_examples.append(positive_example_before)

    return uncovered_examples


def calculate_laplace_estimate(nb_covered_positive_examples, nb_covered_negative_examples):
    if nb_covered_positive_examples == 0:
        return 0
    return (nb_covered_positive_examples + 1) / (nb_covered_positive_examples + nb_covered_negative_examples + 2)


def calculate_m_estimate(nb_covered_positive_examples, nb_covered_negative_examples, m, prior_positive_probability):
    if nb_covered_positive_examples == 0:
        return 0
    return (nb_covered_positive_examples + m * prior_positive_probability) / (nb_covered_positive_examples + nb_covered_negative_examples + m)


def calculate_significance(nb_covered_positive_examples, nb_covered_negative_examples, prior_positive_probability):
    if nb_covered_negative_examples == 0:
        return -2 * nb_covered_positive_examples * math.log10(prior_positive_probability)
    nb_total_covered = nb_covered_positive_examples + nb_covered_negative_examples
    positive_ratio = nb_covered_positive_examples / nb_total_covered
    negative_ratio = 1 - positive_ratio
    # QUESTION: log10 or log2 or ln?
    positive_term = positive_ratio * math.log10(positive_ratio / prior_positive_probability)
    negative_term = negative_ratio * math.log10(negative_ratio / (1 - prior_positive_probability))
    likelihood = 2 * nb_total_covered * (positive_term + negative_term)
    return likelihood


def mfoil_with_context(target_relation, base_relation_name_to_base_relations, context_to_all_objects, beam_size, min_significance):
    # print(f'{beam_size=}')
    print("learning rules")
    MAX_LENGTH = 8
    MAX_TIME = 30
    start = time.time()
    target_relation_arity = target_relation.arity
    target_relation.generate_negative_examples_in_context(context_to_all_objects)
    negative_examples = target_relation.negative_examples
    positive_examples = target_relation.positive_examples
    prior_positive_probability = len(positive_examples) / len(negative_examples)
    head = Literal(False, target_relation.name, target_relation.arity, [i for i in range(target_relation_arity)])
    for _, base_relation in base_relation_name_to_base_relations.items():
        base_relation.generate_negative_examples_in_context(context_to_all_objects)

    learned_rules = []
    while positive_examples and time.time() - start < MAX_TIME:
        new_rule = []
        current_negative_examples = set(negative_examples)
        current_positive_examples = set(positive_examples)
        nb_current_variables = target_relation_arity
        expected_accuracy = calculate_laplace_estimate(len(current_positive_examples), len(current_negative_examples))
        # tuple of expected accuracy, counter (for pq), rule, current_pos, current_neg, current_nb_variables
        best_clauses = [(expected_accuracy, 0, [], current_positive_examples, current_negative_examples, nb_current_variables)]
        counter = 1
        length = 0
        best_rule = best_clauses[0]

        while best_clauses and length < MAX_LENGTH:
            # print(f'Section {len(learned_rules)}.{len(new_rule)}')
            new_best_clauses = []
            for expected_accuracy, _, rule, current_positive_examples, current_negative_examples, nb_current_variables in best_clauses:
                if len(current_negative_examples) == 0:
                    continue
                literal_candidates = get_candidate_literals(base_relation_name_to_base_relations, nb_current_variables)

                for literal_candidate in literal_candidates:
                    if literal_candidate.name == "_Equals":
                        associated_relation = None
                    else:
                        associated_relation = base_relation_name_to_base_relations[literal_candidate.name]
                    covered_old_positive_examples, new_positive_examples, new_negative_examples = get_positive_and_negative_tuples_from_literal(literal_candidate, associated_relation, current_positive_examples, current_negative_examples, nb_current_variables)
                    nb_positive_examples = get_nb_of_truncated_examples(new_positive_examples, target_relation_arity)
                    nb_negative_examples = get_nb_of_truncated_examples(new_negative_examples, target_relation_arity)

                    new_expected_accuracy = calculate_laplace_estimate(nb_positive_examples, nb_negative_examples)
                    # if no improvement do not include in new beam
                    if new_expected_accuracy <= expected_accuracy:
                        continue
                    if len(new_best_clauses) == beam_size and new_best_clauses[0][0] < new_expected_accuracy:
                        heapq.heappop(new_best_clauses)
                    if len(new_best_clauses) < beam_size:
                        new_rule = list(rule) + [literal_candidate]
                        new_nb_variables = max(nb_current_variables, max(literal_candidate.variables) + 1)
                        heapq.heappush(new_best_clauses, (new_expected_accuracy, counter, new_rule, new_positive_examples, new_negative_examples, new_nb_variables))
                        counter += 1

            for clause_info in new_best_clauses:
                expected_accuracy, _, rule, current_positive_examples, current_negative_examples, nb_current_variables = clause_info
                nb_positive_examples = get_nb_of_truncated_examples(current_positive_examples, target_relation_arity)
                nb_negative_examples = get_nb_of_truncated_examples(current_negative_examples, target_relation_arity)
                if clause_info[0] > best_rule[0]:
                    best_rule = clause_info
            best_clauses = new_best_clauses
            for clause in best_clauses:
                break
                # print(clause[0], clause[2])
            length += 1

        expected_accuracy, _, rule, current_positive_examples, current_negative_examples, nb_current_variables = best_rule

        if expected_accuracy > prior_positive_probability:
            learned_rule_class = Rule(head, rule)
            nb_positive_examples = get_nb_of_truncated_examples(current_positive_examples, target_relation_arity)
            nb_negative_examples = get_nb_of_truncated_examples(current_negative_examples, target_relation_arity)
            # set the nb positive and negative examples
            learned_rule_class.set_positive_and_negative_examples_during_mfoil(nb_positive_examples, nb_negative_examples)
            # set the nb positive and negative examples
            rule_significance = calculate_significance(nb_positive_examples, nb_negative_examples, prior_positive_probability)
            print(rule, rule_significance)
            if rule_significance < min_significance:
                # break
                pass

            learned_rule_class.set_mfoil_significance(rule_significance)
            learned_rules.append(learned_rule_class)
        else:
            break

        size_positive_examples_before = len(positive_examples)
        positive_examples = get_new_uncovered_positive_examples(positive_examples, current_positive_examples, target_relation_arity)
        if len(positive_examples) == size_positive_examples_before:
            break

    print("done learning rules")
    return learned_rules


if __name__ == "__main__":
    """
    lit1 = Literal(False, "A", 3, [3, 2, 4])
    rel1 = Relation("A", 3, [("y", "c", "x"), ("k", "c", "l"), ("k", "d", "m")])
    print(get_positive_and_negative_tuples_from_literal(lit1, rel1, [("a", "b", "c"), ("a", "b", "d")], [("r", "s", "c")], 3))
    """
    # should be "a": [(0, 3), (1, 4), (2, 4), (1, 5), (2, 5)]
    # should be "b": [(0, 2)]
    target_relation = Relation("2hop", 2, [(("a", 0), ("a", 3)), (("a", 1), ("a", 4)), (("a", 2), ("a", 4)), (("a", 1), ("a", 5)), (("a", 2), ("a", 5)), (("b", 0), ("b", 2))])
    base_relations = {
        "DirectlyConnected": Relation("DirectlyConnected", 2, [(("a", 0), ("a", 1)), (("a", 0), ("a", 2)), (("a", 1), ("a", 3)), (("a", 2), ("a", 3)), (("a", 3), ("a", 4)), (("a", 3), ("a", 5)),
                                                                                        (("b", 0), ("b", 1)), (("b", 1), ("b", 2))])
    }
    print(mfoil_with_context(target_relation, base_relations, {"a": [0, 1, 2, 3, 4, 5], "b": [0, 1, 2]}, beam_size=5))


