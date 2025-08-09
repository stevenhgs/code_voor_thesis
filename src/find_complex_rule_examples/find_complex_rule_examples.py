from src.custom_classes.Relation import Relation
from src.custom_classes.Literal import Literal
from src.custom_classes.Rule import Rule


def generate_all_tuples(all_objects, size):
    output = []
    arr = []

    def dfs():
        if len(arr) == size:
            output.append(tuple(arr))
            return
        for obj in all_objects:
            arr.append(obj)
            dfs()
            arr.pop()

    dfs()
    return output


def find_complex_rule_examples(rules, base_relation_name_to_base_relations, all_objects):
    complex_relation_name_to_complex_relation = dict()

    for rule in rules:
        head = rule.head
        body = rule.body
        if complex_relation_name_to_complex_relation.get(head.name) is None:
            complex_relation_name_to_complex_relation[head.name] = Relation(head.name, head.arity, set())
        nb_variables = max(head.variables) + 1
        for literal in body:
            nb_variables = max(nb_variables, max(literal.variables) + 1)
        if nb_variables > 5:
            rule.nb_negative_train += 1
            continue
        all_tuples = generate_all_tuples(all_objects, nb_variables)

        for candidate_tuple in all_tuples:
            for literal in body:
                if base_relation_name_to_base_relations.get(literal.name) is None:
                    base_relation_name_to_base_relations[literal.name] = Relation(literal.name, literal.arity, set())
                base_relation_name_to_base_relations[literal.name].generate_negative_examples(all_objects)
                candidate_tuple_example = []
                for variable in literal.variables:
                    candidate_tuple_example.append(candidate_tuple[variable])
                candidate_tuple_example = tuple(candidate_tuple_example)
                if literal.is_negated:
                    if candidate_tuple_example not in base_relation_name_to_base_relations[literal.name].negative_examples:
                        break
                else:
                    if candidate_tuple_example not in base_relation_name_to_base_relations[literal.name].positive_examples:
                        break
            else:
                candidate_tuple_example = []
                for variable in head.variables:
                    candidate_tuple_example.append(candidate_tuple[variable])
                candidate_tuple_example = tuple(candidate_tuple_example)
                complex_relation_name_to_complex_relation[head.name].positive_examples.add(candidate_tuple_example)

    return complex_relation_name_to_complex_relation


if __name__ == "__main__":
    relation_name_to_relation = {
        "Q": Relation("Q", 2, {(4, 5), (1, 5)})
    }
    head = Literal(False, "P", 2, [0, 1])
    lit1 = Literal(False, "Q", 2, [1, 0])
    all_objects = [1, 4, 5]
    rules = [Rule(head, [lit1])]
    print(find_complex_rule_examples(rules, relation_name_to_relation, all_objects))
