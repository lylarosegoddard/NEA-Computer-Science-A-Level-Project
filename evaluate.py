#python evaluate.py to run the evaluation

from app.evaluation.csv_loader import load_csv
from app.bullycatcher import Bullycatcher
from app.evaluation.evaluation import Evaluation

evaluation_data = load_csv("evaluation_set.csv")
#loads the csv file and allows the evaluation set to be sent to the Bullycatcher
bully_catcher = Bullycatcher("Lyla") #example user to test the Bullycatcher prompt
evaluation = Evaluation(bully_catcher)
#evaluates the Bullycatcher prompt in terms of precision and recall


precision, recall = evaluation.evaluate(evaluation_data)
print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
#outputs the precision and recall rounded to 2 decimal places

false_positives = evaluation.false_positives()
if false_positives:
    print("\nFalse Positives(incorrectly flagged as bullying):")
    for result in false_positives:
        print(f"message: {result.message} Expected: {result.expected}, actual: {result.actual}")
        #outputs the false positives showing the message, expected value and actual value so I can see where the Bullycatcher prompt is failing 


false_negatives = evaluation.false_negatives()
if false_negatives:
    print("\nFalse Negatives(missed bullying):")
    for result in false_negatives:
        print(f"message: {result.message} Expected: {result.expected}, actual: {result.actual}")
        #outputs the false negatives showing the message, expected value and actual value so I can see where the Bullycatcher prompt is failing


