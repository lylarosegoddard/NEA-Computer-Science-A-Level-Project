class EvaluationResult:
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def true_positive(self):
        return self.expected and self.actual

    def false_positive(self):
        return not self.expected and self.actual

    def false_negative(self):
        return self.expected and not self.actual