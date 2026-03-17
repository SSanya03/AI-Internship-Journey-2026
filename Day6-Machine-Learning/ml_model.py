import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day4-Pandas-Data-Analysis\students.csv")
print("Students data:\n", data)
x = data[["math", "science", "english"]]
y = data["math"]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)
prediction = model.predict([[80, 85, 82]])
print("Predicted math scores:", prediction)
