import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day4-Pandas-Data-Analysis\students.csv")
print("Student Marks:\n", data)
data["math"].plot()
plt.show()
data.plot(x="name", y="math", kind="bar")
plt.show()
