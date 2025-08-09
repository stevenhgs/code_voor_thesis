class Relation:
    def __init__(self, name, arity, positive_examples):
        self.name = name
        self.arity = arity
        # ideally should be a set
        self.positive_examples = positive_examples
        self.negative_examples = None

    def add_positive_examples(self, extra_positive_examples):
        self.positive_examples |= extra_positive_examples

    def generate_negative_examples(self, all_objects):
        if self.negative_examples is not None:
            return
        self.negative_examples = set()
        arr = []

        def dfs(i):
            if i == self.arity:
                new_example = tuple(arr)
                if new_example not in self.positive_examples:
                    self.negative_examples.add(new_example)
                return
            for obj in all_objects:
                arr.append(obj)
                dfs(i + 1)
                arr.pop()
        dfs(0)

    def generate_negative_examples_in_context(self, context_to_all_objects):
        if self.negative_examples is not None:
            return
        self.negative_examples = set()

        def dfs(i):
            if i == self.arity:
                new_example = tuple(arr)
                if new_example not in self.positive_examples:
                    self.negative_examples.add(new_example)
                return
            for obj in all_objects:
                arr.append((context_name, obj))
                dfs(i + 1)
                arr.pop()

        for context_name, all_objects in context_to_all_objects.items():
            arr = []
            dfs(0)

    def __str__(self):
        if len(self.positive_examples) == 0:
            return f'{self.name}: {"{}"}'
        return f'{self.name}: {self.positive_examples}'

    def __repr__(self):
        if len(self.positive_examples) == 0:
            return f'{self.name}: {"{}"}'
        return f'{self.name}{self.positive_examples}'
