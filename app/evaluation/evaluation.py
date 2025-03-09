from traceback import print_list
from app.evaluation.evaluation_result import EvaluationResult

class Evaluation:
    def __init__(self, bully_catcher):
        self.bully_catcher = bully_catcher


    def evaluate(self, testcases):
        self.evaluation_results = list(map( #mapping
            self.create_result,
            testcases
        ))
        return self.precision(), self.recall()
    


    def precision(self):
        true_positive_count = len(self.true_positives())
        false_positive_count = len(self.false_positives())
        try:
            return true_positive_count / (true_positive_count + false_positive_count) #exception handling
        except ZeroDivisionError:
            return 0

    def recall(self):
        true_positive_count = len(self.true_positives())
        false_negative_count = len(self.false_negatives())
        try:
            return true_positive_count / (true_positive_count + false_negative_count)
        except ZeroDivisionError:
            return 0
    

    def false_positives(self):
        return [r for r in self.evaluation_results if r.false_positive()]

    def false_negatives(self):
        return [r for r in self.evaluation_results if r.false_negative()]

    def true_positives(self):
        return [r for r in self.evaluation_results if r.true_positive()]

    def create_result(self, testcase):
        messages = testcase["input"].split("\n")
        actual = str(self.bully_catcher.detect_bullying(messages) is not None)
        print(".")
        return EvaluationResult(
            expected = testcase["output"],
            actual = actual,
            message = messages[-1]
        )
        