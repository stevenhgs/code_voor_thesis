def get_follows_examples(order):
    examples = set()
    for i in range(len(order) - 1):
        base_group = order[i]
        for j in range(i+1, len(order)):
            other_group = order[j]
            for element1 in base_group:
                for element2 in other_group:
                    examples.add((element2, element1))
    return examples


def get_together_examples(order):
    examples = set()
    for group in order:
        for i in range(len(group) - 1):
            for j in range(i + 1, len(group)):
                base = min(group[i], group[j])
                other = max(group[i], group[j])
                examples.add((base, other))
    return examples

def get_score(data, index, check_follows, atleast_one_follows):
    orders = data[f"{index}"]["order_data"]
    found_examples_key = "sequential_order_found_examples"
    true_examples_key = "sequential_order_true_examples"

    filtered_orders = dict()
    for key, val in orders.items():
        if atleast_one_follows:
            if len(val[true_examples_key]) > 1:
                filtered_orders[key] = val
        else:
            filtered_orders[key] = val

    if len(filtered_orders.keys()) == 0:
        return 0, 0, 0

    get_examples_func = None
    if check_follows:
        get_examples_func = get_follows_examples
    else:
        get_examples_func = get_together_examples

    nb_true_positives = 0
    nb_false_positives = 0
    nb_false_negatives = 0
    used_slides = 0
    for key, order in filtered_orders.items():
        used_slides += 1
        found_examples = get_examples_func(order[found_examples_key])
        true_examples = get_examples_func(order[true_examples_key])
        for found_example in found_examples:
            if found_example in true_examples:
                nb_true_positives += 1
            else:
                nb_false_positives += 1
        for true_positive in true_examples:
            if true_positive not in found_examples:
                # print(f'false negative: {pdf_file_name} {true_positive=}')
                nb_false_negatives += 1

    f1_score = (2 * nb_true_positives) / (2 * nb_true_positives + nb_false_positives + nb_false_negatives)
    return f1_score, 1, used_slides


def get_nb_rules(data, index, check_follows):
    rules = data[f"{index}"]["filtered rules"]
    key = "DirectlyFollows"
    if not check_follows:
        key = "Together"
    return len(rules[key]), 1


def get_rule_size(data, index, check_follows):
    key = "DirectlyFollows"
    if not check_follows:
        key = "Together"
    rules = data[f"{index}"]["filtered rules"][key]
    literal_count = 0
    for rule in rules:
        literal_count += rule[0].count("(") - 1
    nb_rules = max(1, len(rules))
    return literal_count / nb_rules, 1



if __name__ == "__main__":
    some_order = [[0,1],[4,3,2],[5]]
    print(get_follows_examples(some_order))
    print(get_together_examples(some_order))