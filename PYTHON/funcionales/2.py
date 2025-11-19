A = list(map(int, input("Lista A: ").split()))
B = list(map(int, input("Lista B: ").split()))

producto = 0
for i in range(len(A)):
    producto += A[i] * B[i]

print("Producto escalar =", producto)