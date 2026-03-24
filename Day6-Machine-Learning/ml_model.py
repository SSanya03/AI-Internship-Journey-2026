#prgrm15: First ML model
import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day6-Machine-Learning\students.csv")
print("Students data:\n", data)
x = data[["science", "english"]]
y = data["math"]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
import pandas as pd
new_data = pd.DataFrame([[80, 85, 82]], columns = ["math", "science", "english"])
predictions = model.predict(x_train)
print("Predicted:", prediction)
print("Actual:", list(y_test))
from sklearn.metrics import mean_absolute_error
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)
sample = [[80,85]]
prediction = model.predict(sample)
print("Predicted math score:", prediction)
