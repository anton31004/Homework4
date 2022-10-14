same=0
result=[]
sizeA=int(input("Введите размерность массива A - "))
A=[0]*sizeA
print("Вводите значения")
for i in range(sizeA):
    print("A[", i,"] = ", end="")
    A[i]=int(input())

sizeB=int(input("Введите размерность массива B - "))
B=[0]*sizeB
print("Вводите значения")
for i in range(sizeB):
    print("B[", i,"] = ", end="")
    B[i]=int(input())


for i in range(sizeA):
    for j in range(sizeB):
        if A[i]==B[j]:
            same=B[j]
            result.append(same)
print(result)

