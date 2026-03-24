#prgrm15: First ML model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
# load data
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day6-Machine-Learning\students.csv")
print("Students data:\n", data)
# features(inputs)
x = data[["science", "english"]]
# label(output)
y = data["math"]
# split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
# train model
model = LinearRegression()
model.fit(x_train, y_train)
# predictions
predictions = model.predict(x_test)
# evaluate model
error = mean_absolute_error(y_test, predictions)
print("Predicted:", predictions)
print("Actual:", list(y_test))
print("Mean Absolute Error:", error)
# custom prediction
sample = pd.DataFrame([[80,85]], columns = ["science", "english"])
prediction = model.predict(sample)
print("Predicted math score:", prediction)
