
from sklearn.ensemble import RandomForestClassifier
import joblib

X = [[10],[200],[500],[2000]]
y = [0,0,1,1]
model = RandomForestClassifier()
model.fit(X,y)
joblib.dump(model,"model.pkl")
