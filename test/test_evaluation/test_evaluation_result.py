#TestEvaluationResult class - TDD

import unittest
from app.evaluation.evaluation_result import EvaluationResult
#testing the EvaluationResult class

class TestEvaluationResult(unittest.TestCase):
    def test_true_positive(self):
        result = EvaluationResult(expected = "True", actual = "True")
        self.assertTrue(result.true_positive())
        self.assertFalse(result.false_positive())
        self.assertFalse(result.false_negative())
        #tests if the result is true positive

    def test_false_positive(self):
        result = EvaluationResult(expected ="False", actual = "True")
        self.assertFalse(result.true_positive())
        self.assertTrue(result.false_positive())
        self.assertFalse(result.false_negative())
        #tests if the result is false positive

    def test_false_negative(self):
        result = EvaluationResult(expected = "True", actual = "False")
        self.assertFalse(result.true_positive())
        self.assertFalse(result.false_positive())
        self.assertTrue(result.false_negative())
        #tests if the result is false negative
