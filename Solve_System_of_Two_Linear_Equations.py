#System of Equation in Python
import numpy as np

print("Program solves a system of two linear equations ")
print("""\nSample equation
      4x + 3y = 20      
     -5x + 9y = 26
      """)
print("""You will be asked to enter the coefficients:
      a1 x + b1 y = c1      
      a2 x + b2 y = c2
      """)

a1=int(input("a1: "))
b1=int(input("b1: "))
c1=int(input("c1: "))
a2=int(input("a2: "))
b2=int(input("b2: "))
c2=int(input("c2: "))


A=np.array([[a1,b1],[a2,b2]])
B=np.array([c1,c2])

print("\nMatrix A:")
print(np.matrix(A))
print("Matrix B:")
print(np.matrix(B))

print("\nResult: ")
print(np.linalg.solve(A,B))

