from app.evaluation.csv_loader import load_csv
from app.bullycatcher import Bullycatcher
from app.evaluation.evaluation import Evaluation

evaluation_data = load_csv("evaluation_set.csv")

bully_catcher = Bullycatcher()

evaluation = Evaluation(bully_catcher)

evaluation.evaluate(evaluation_data)
print(evaluation_data)

precision, recall = evaluation.evaluate(evaluation_data)

print(f"Precision: {precision}")
print(f"Recall: {recall}")

