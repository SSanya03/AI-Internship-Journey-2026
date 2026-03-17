import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day6-Machine-Learning\students.csv")
print("Students data:\n", data)
x = data[["math", "science", "english"]]
y = data["math"]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
import pandas as pd
new_data = pd.DataFrame([[80, 85, 82]], columns = ["math", "science", "english"])
prediction = model.predict(new_data)
print("Predicted math scores:", prediction)
