#StubBullyCatcher and TestEvaluation class - TDD

import unittest
from app.evaluation.evaluation import Evaluation
#testing the Evaluation class

class StubBullyCatcher:
     def detect_bullying(self, messages):
        if messages[-1] == "Bob: Your ugly": #looks at last message in array
          return "bullying"


class TestEvaluation(unittest.TestCase):
    def test_evaluation_metrics(self):
        testcases = [ #list of dictionaries - did this as its much easier to test 
            { # TRUE POSITIVE
                "input" : "Bill Hi\nBob: Your ugly",
                "output" : "True"
            },
            { # FALSE POSITIVE
                "input" : "Bill Hi\nBob: Your ugly",
                "output" : "False"
            },
            { # FALSE NEGATIVE
                "input" : "Bill Hi\nNot bullYing",
                "output" : "True"
            },
            { # FALSE NEGATIVE
                "input" : "Not bullying",
                "output" : "True"
            },
            { # FALSE NEGATIVE
                "input" : "Not bullying",
                "output" : "True"
            }
        ]
        #list of test cases
        evaluation = Evaluation(StubBullyCatcher()) #dependency injecting the StubBullyCatcher
        precision, recall = evaluation.evaluate(testcases)
        self.assertEqual(precision, 0.5)
        self.assertEqual(recall, 0.25)
        #tests if the precision and recall are correct

    def test_handles_zero_values(self):
        evaluation = Evaluation(StubBullyCatcher())
        precision, recall = evaluation.evaluate([])
        self.assertEqual(precision, 0)
        self.assertEqual(recall, 0)
        #tests that zero values are correctly handled by the try/except block