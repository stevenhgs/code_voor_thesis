from collections import defaultdict

class DUS:
    def __init__(self, all_objects):
        self.all_objects = all_objects
        self.object_to_id = dict()
        id = 0
        for object in all_objects:
            self.object_to_id[object] = id
            id += 1
        self.id_to_group = [i for i in range(id)]

    def join(self, obj_a, obj_b):
        to_bring_up = []
        obj_a_id = self.object_to_id[obj_a]
        curr_id = obj_a_id
        while self.id_to_group[curr_id] != curr_id:
            to_bring_up.append(curr_id)
            curr_id = self.id_to_group[curr_id]
        top_id_a = curr_id

        obj_b_id = self.object_to_id[obj_b]
        curr_id = obj_b_id
        while self.id_to_group[curr_id] != curr_id:
            to_bring_up.append(curr_id)
            curr_id = self.id_to_group[curr_id]
        top_id_b = curr_id

        self.id_to_group[top_id_a] = top_id_b
        for id in to_bring_up:
            self.id_to_group[id] = top_id_b

    def generate_groups_from_connections(self, object_connections):
        """
        object_connections: should be a list of tuples with two elements consisting of objects used to init this DUS.
        """
        for obj_a, obj_b in object_connections:
            self.join(obj_a, obj_b)

    def get_top(self, obj):
        curr_id = self.object_to_id[obj]
        while self.id_to_group[curr_id] != curr_id:
            curr_id = self.id_to_group[curr_id]
        return curr_id

    def get_object_to_group_map(self):
        object_to_group_map = dict()
        for obj in self.all_objects:
            group = self.get_top(obj)
            object_to_group_map[obj] = group
        return object_to_group_map

    def get_group_to_objects_map(self):
        group_to_objects_map = defaultdict(list)
        object_to_group_map = self.get_object_to_group_map()
        for obj, group in object_to_group_map.items():
            group_to_objects_map[group].append(obj)
        return group_to_objects_map

    def get_all_groups(self):
        groups = set()
        for obj in self.all_objects:
            group = self.get_top(obj)
            groups.add(group)
        return groups


def topological_sort(different_groups, dus, to_from_pairs):
    object_to_group_map = dus.get_object_to_group_map()
    group_to_objects_map = dus.get_group_to_objects_map()
    group_to_nb_incoming_map = defaultdict(int)
    from_group_going_to_group_map = defaultdict(list)

    for to_obj, from_obj in to_from_pairs:
        if object_to_group_map[to_obj] == object_to_group_map[from_obj]:
            continue
        group_to_nb_incoming_map[object_to_group_map[to_obj]] += 1
        from_group_going_to_group_map[object_to_group_map[from_obj]].append(object_to_group_map[to_obj])

    no_incoming_groups = []
    handled_groups = set()
    for group in different_groups:
        nb_incoming = group_to_nb_incoming_map[group]
        if nb_incoming == 0:
            no_incoming_groups.append(group)
            handled_groups.add(group)

    sub_order = []
    for no_incoming_group in no_incoming_groups:
        sub_order.extend(group_to_objects_map[no_incoming_group])
    order = [sub_order]

    while no_incoming_groups:
        new_no_incoming_groups = []
        sub_order = []
        for group in no_incoming_groups:
            for going_to in from_group_going_to_group_map[group]:
                group_to_nb_incoming_map[going_to] -= 1
                if group_to_nb_incoming_map[going_to] == 0:
                    new_no_incoming_groups.append(going_to)
                    sub_order.extend(group_to_objects_map[going_to])
                    handled_groups.add(going_to)
        no_incoming_groups = new_no_incoming_groups
        if len(sub_order) > 0:
            order.append(sub_order)

    all_included = True
    sub_order = []
    for going_to, freq in group_to_nb_incoming_map.items():
        if freq > 0:
            all_included = False
            sub_order.extend(group_to_objects_map[going_to])
    if len(sub_order) > 0:
        order.append(sub_order)
    return order, all_included


def get_sequential_order(all_objects, complex_relation_name_to_complex_relation):
    dus = DUS(all_objects)
    if complex_relation_name_to_complex_relation.get("Together") is not None:
        together_pairs = complex_relation_name_to_complex_relation["Together"].positive_examples
        dus.generate_groups_from_connections(together_pairs)
    # print(f'group id to objects map: ')
    # print(dus.get_group_to_objects_map())

    different_groups = dus.get_all_groups()
    if complex_relation_name_to_complex_relation.get("DirectlyFollows") is not None:
        to_from_pairs = complex_relation_name_to_complex_relation["DirectlyFollows"].positive_examples
    else:
        to_from_pairs = []

    sequential_order = topological_sort(different_groups, dus, to_from_pairs)
    return sequential_order