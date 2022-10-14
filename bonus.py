Delta=int(input("Введите delta - "))
k=0
m=1000000000
size=int(input("Введите размерность массива A - "))
a=[0]*size
print("Вводите значения")
for i in range(size):
    print("a[", i,"] = ", end="")
    a[i]=int(input())

for i in range(size):
    if a[i]<m:
        m=a[i]
for j in range(size):
    if a[j]-m==4:
        k+=1
print("Результат: ", k)