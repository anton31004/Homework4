m=-10000000
maxindex=0
size=int(input("Введите размерность массива - "))
B=[0]*size
print("Вводите значения")
for i in range(size):
    print("B[", i,"] = ", end="")
    B[i]=float(input())
for i in range(size):
    if B[i]>m:
        m=B[i]
        maxindex=i
for j in range(maxindex+1, size):
    B[j]=0
print(B)
