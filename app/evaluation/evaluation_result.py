class EvaluationResult:
    def __init__(self, expected, actual, message = ""):
        self.expected = expected
        self.actual = actual
        self.message = message

    def true_positive(self):
        return self.expected == "True" and self.actual == "True"

    def false_positive(self):
        return self.expected == "False" and self.actual == "True"

    def false_negative(self):
        return self.expected == "True" and self.actual == "False"