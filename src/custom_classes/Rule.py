from src.custom_classes.Literal import Literal


class Rule:
    def __init__(self, head: Literal, body: list[Literal], nb_positive_mfoil=None, nb_negative_mfoil=None, significance=None, nb_positive_train=0, nb_negative_train=0):
        self.head = head
        self.body = body
        self.nb_positive_examples_during_mfoil = nb_positive_mfoil
        self.nb_negative_examples_during_mfoil = nb_negative_mfoil
        self.mfoil_significance = significance
        self.nb_positive_train = nb_positive_train
        self.nb_negative_train = nb_negative_train

    def set_positive_and_negative_examples_during_mfoil(self, nb_positive_examples, nb_negative_examples):
        self.nb_positive_examples_during_mfoil = nb_positive_examples
        self.nb_negative_examples_during_mfoil = nb_negative_examples

    def set_mfoil_significance(self, significance):
        self.mfoil_significance = significance

    def add_literal_to_body(self, new_literal):
        self.body.append(new_literal)

    def __str__(self):
        output =  f'{self.head} <-- ' + " ∧ ".join([str(literal) for literal in self.body])
        return output

    def __repr__(self):
        output = f'Rule({repr(self.head)}, {repr(self.body)}'
        if self.nb_positive_examples_during_mfoil is not None:
            output += f', {self.nb_positive_examples_during_mfoil}, {self.nb_negative_examples_during_mfoil}'
        if self.mfoil_significance is not None:
            output += f', {self.mfoil_significance}'
        output += f', {self.nb_positive_train}, {self.nb_negative_train}'
        output += ')'
        return output