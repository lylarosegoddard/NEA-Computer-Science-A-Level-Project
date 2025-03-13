#EvaluationResult class

class EvaluationResult:
    def __init__(self, expected, actual, message = ""):
        self.expected = expected
        self.actual = actual
        self.message = message
        #stores the expected and actual values and the message

    def true_positive(self):
        return self.expected == "True" and self.actual == "True"
        #returns true if the expected and actual values are both true

    def false_positive(self):
        return self.expected == "False" and self.actual == "True"
        #returns true if the expected is false and the actual is true

    def false_negative(self):
        return self.expected == "True" and self.actual == "False"
        #returns true if the expected is true and the actual is false