import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

reddit_data = pd.read_csv("data.csv", names=["ID","Start Of Title", "Ace In Title", "Ace In Self Text", "Question In Title", "Question In Self Text", "Tagged As Ace", "Is an Ace Post"])
X = reddit_data.drop(["ID", "Start Of Title", "Is an Ace Post"], axis=1)
y = reddit_data["Is an Ace Post"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.joblib")

