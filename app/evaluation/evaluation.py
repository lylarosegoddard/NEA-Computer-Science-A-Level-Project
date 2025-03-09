from traceback import print_list
from app.evaluation.evaluation_result import EvaluationResult

class Evaluation:
    def __init__(self, bully_catcher):
        self.bully_catcher = bully_catcher


    def evaluate(self, testcases):
        self.evaluation_results = list(map(
            self.create_result,
            testcases
        ))
        return self.precision(), self.recall()
    
    def precision(self):
        true_positive_count = len([r for r in self.evaluation_results if r.true_positive()])
        false_positive_count = len([r for r in self.evaluation_results if r.false_positive()])
        if true_positive_count + false_positive_count == 0:
            return 0
        return true_positive_count / (true_positive_count + false_positive_count)
    
    def recall(self):
        true_positive_count = len([r for r in self.evaluation_results if r.true_positive()])
        false_negative_count = len([r for r in self.evaluation_results if r.false_negative()])
        if true_positive_count + false_negative_count == 0:
            return 0
        return true_positive_count / (true_positive_count + false_negative_count)

    def create_result(self, testcase):
        messages = testcase["input"].split("\n")
        return EvaluationResult(
            expected = testcase["output"],
            actual = str(self.bully_catcher.detect_bullying(messages) is not None)
        )