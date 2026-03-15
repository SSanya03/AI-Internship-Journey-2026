import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT0001\Desktop\AI-Internship -Journey-2026\Day4-Pandas-Data-Analysis\students.csv")
print(f"Student data: {data}")
print(f"Data head: {(data.head())}")
print(f"Data info: {(data.info())}")
print(f"Data describe: {(data.describe())}")
print("Math columns:", (data["math"]))
                    
