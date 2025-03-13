#Evaluation class

from app.evaluation.evaluation_result import EvaluationResult


class Evaluation:
    def __init__(self, bully_catcher):
        self.bully_catcher = bully_catcher

    def evaluate(self, testcases):
        self.evaluation_results = list(map( #mapping
            self.create_result,
            testcases
        ))
        #stores the evaluation results
        return self.precision(), self.recall()
        #returns the calculated precision and recall
    


    def precision(self):
        true_positive_count = len(self.true_positives())
        false_positive_count = len(self.false_positives())
        #stores the number of true positives and false positives
        try:
            return true_positive_count / (true_positive_count + false_positive_count) 
        except ZeroDivisionError: #exception handling
            return 0
        #returns the calculated precision unless there is a ZeroDivisionError 

    def recall(self):
        true_positive_count = len(self.true_positives())
        false_negative_count = len(self.false_negatives())
        #stores the number of true positives and false negatives
        try:
            return true_positive_count / (true_positive_count + false_negative_count) 
        except ZeroDivisionError: #exception handling
            return 0
        #returns the calculated recall unless there is a ZeroDivisionError
        
    

    def false_positives(self):
        return [r for r in self.evaluation_results if r.false_positive()] #for loops
        #returns the false positives

    def false_negatives(self):
        return [r for r in self.evaluation_results if r.false_negative()]
        #returns the false negatives

    def true_positives(self):
        return [r for r in self.evaluation_results if r.true_positive()]
        #returns the true positives

    def create_result(self, testcase):
        messages = testcase["input"].split("\n")
        #splits the input into messages
        actual = str(self.bully_catcher.detect_bullying(messages) is not None)
        #stores the actual value - the LLMs prediction
        print(".")
        return EvaluationResult(
            expected = testcase["output"],
            actual = actual,
            message = "\n".join(messages)
            #outputs the expected and actual values and the message as a block when called
        )
        