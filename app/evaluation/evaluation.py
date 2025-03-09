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
        true_positive_count = len([r for r in self.evaluation_results if r.true_positive()]) #list comprehension
        false_positive_count = len([r for r in self.evaluation_results if r.false_positive()])
        try:
            return true_positive_count / (true_positive_count + false_positive_count) #exception handling
        except ZeroDivisionError:
            return 0


    
    def recall(self):
        true_positive_count = len([r for r in self.evaluation_results if r.true_positive()])
        false_negative_count = len([r for r in self.evaluation_results if r.false_negative()])
        try:
            return true_positive_count / (true_positive_count + false_negative_count)
        except ZeroDivisionError:
            return 0
        

    def create_result(self, testcase):
        messages = testcase["input"].split("\n")
        actual = str(self.bully_catcher.detect_bullying(messages) is not None)
        print(f"message: {messages[-1]} - expected: {testcase['output']} - actual: {actual}")
        return EvaluationResult(
            expected = testcase["output"],
            actual = actual
        )
        