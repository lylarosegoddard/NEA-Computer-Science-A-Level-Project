from app.evaluation.csv_loader import load_csv
from app.bullycatcher import Bullycatcher
from app.evaluation.evaluation import Evaluation

evaluation_data = load_csv("evaluation_set.csv")
bully_catcher = Bullycatcher()
evaluation = Evaluation(bully_catcher)


precision, recall = evaluation.evaluate(evaluation_data)
print(f"\nPrecision: {precision:.3f}")
print(f"Recall: {recall:.3f}")

false_positives = evaluation.false_positives()
if false_positives:
    print("\nFalse Positives(incorrectly flagged as bullying):")
    for result in false_positives:
        print(f"message: {result.message} Expected: {result.expected}, actual: {result.actual}")


false_negatives = evaluation.false_negatives()
if false_negatives:
    print("\nFalse Negatives(missed bullying):")
    for result in false_negatives:
        print(f"message: {result.message} Expected: {result.expected}, actual: {result.actual}")
