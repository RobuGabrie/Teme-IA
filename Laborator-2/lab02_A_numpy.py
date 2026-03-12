import numpy as np

np.random.seed(42)

A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))
C = A @ B

print("Matricea A (4x3):")
print(A)
print("\nMatricea B (3x5):")
print(B)
print("\nProdusul C = A @ B (4x5):")
print(C)

print("\nSuma tuturor elementelor din C:", C.sum())
print("Media pe fiecare coloana din C:", C.mean(axis=0))
print("Valoarea maxima globala din C:", C.max())

M = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0],
], dtype=float)

inv_M = np.linalg.inv(M)
det_M = np.linalg.det(M)
identity_check = np.allclose(M @ inv_M, np.eye(3))

print("\nMatricea M (3x3):")
print(M)
print("\nInversa lui M:")
print(inv_M)
print("\nDeterminantul lui M:", det_M)
print("M @ inv(M) este aproape identitate:", identity_check)
