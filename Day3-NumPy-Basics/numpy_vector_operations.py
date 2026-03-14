#prgrm12: Vector Operations using NumPy
import numpy as np
a = np.array([1,2,3])
b = np.array({4,5,6])
sum = a + b
product = a * b
print("Vector addition:", sum)
print("Vector multiplication:", product)
import numpy as np
x = np.array([
  [1,2],
  [3,4]
])
y = np.array([
  [5,6],
  [7,8]
])
print(f"Matrix multiplication: {np.dot(x, y)}")
import numpy as np
data = np.random.randint(1,100,size=(5,3))
print("Matrix using random data:", data)
