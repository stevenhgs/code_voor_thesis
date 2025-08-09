class Literal:
    def __init__(self, is_negated, name, arity, variables):
        self.is_negated = is_negated
        self.name = name
        self.arity = arity
        self.variables = variables

    def __str__(self):
        negation_symbol = ''
        if self.is_negated:
            negation_symbol = '¬'
        return f'{negation_symbol}{self.name}{tuple(["P" + str(i) for i in self.variables])}'

    def __repr__(self):
        return f'Literal({self.is_negated}, "{self.name}", {self.arity}, {self.variables})'

    def __eq__(self, other):
        return self.name == self.name and self.arity == other.arity

    def __hash__(self):
        return hash((self.name, self.arity))

