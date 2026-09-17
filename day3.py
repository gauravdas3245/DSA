n=int(input("enter a number"))
a=[]
for i in range(n):
    x=int(input("enter a number"))
    a.append(x)
print("list is:",a)

x=int(input("enter a number to insert:"))
pos=int(input("enter index position:"))
a.insert(pos,x)
print("list after insertion:",a)

x=int(input("enter a number to remove:"))
pos=int(input("enter index position:"))
a.remove(x)
print("list after deletion:",a)

x=int(input("enter an element to delete:"))
pos=int(input("enter index position:"))
a.pop(pos)
print("list after deletion:",a)

a.sort()
print("list after sorting:",a)

a.reverse()
print("list after reversing:",a)

c=a.count(x)
print("list after counting:",c)

pos=a.index(x)
print("the inddex of an element is :",pos)

n=int(input("enter a number"))
b=[]
for i in range(n):
    x=int(input("enter a number"))
    b.append(x)
print("list is:",b)

a.extend(b)
print("after adding element to another list:",a)

a.clear()
print("after clearing the list:",a)

a.copy()
print("after copying the list:",a)













A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
C = [[0, 0], [0, 0]]

print("Enter elements of Matrix A:")
for i in range(2):
    for j in range(2):
        A[i][j] = int(input("Enter element: "))

print("Enter elements of Matrix B:")
for i in range(2):
    for j in range(2):
        B[i][j] = int(input("Enter element: "))

   
print("Sum of matrices:")
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("Difference of matrices:")
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] - B[i][j]

 


print("transpose of matrix A:")
for i in range(2):
    for j in range(2):
        print(A[j][i], end=" ")
    print() 


print("Multiplication of matrices AB:")
for i in range(2):
    for j in range(2):
        C[i][j] = 0
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]








n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

key = int(input("Enter element to search: "))

found = False

for i in range(n):
    if a[i] == key:
        print("Element found at index:", i)
        found = True
        break

if found == False:
    print("Element not found")















n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

a.sort()
print("Sorted list:", a)

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Element found at index:", mid)
        found = True
        break

    elif key > a[mid]:
        low = mid + 1

    else:
        high = mid - 1

if found == False:
    print("Element not found")