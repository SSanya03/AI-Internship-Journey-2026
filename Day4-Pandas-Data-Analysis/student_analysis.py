#prgrm13: Practice using Pandas and MatplotLib
import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day4-Pandas-Data-Analysis\students.csv")
print(f"Student data: {data}")
print(f"Data head:\n {(data.head())}")
print(f"Data info:\n {(data.info())}")
print(f"Data describe:\n {(data.describe())}")
print("Math columns:\n", (data["math"]))
print("Sort by math score:\n", data.sort_values(by="math", ascending= False)) 
print("Average science score:\n", (data["science"].mean())
import matplotlib.pyplot as plt
data.plot(x="name", y=["math","science","english"], kind="bar")
plt.title("Student scores")
plt.show()
