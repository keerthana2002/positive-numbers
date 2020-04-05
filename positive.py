list = []
n=int(input("Enter the number of elements and the elements"))
for i in range(0,n):
    elements=int(input())
    list.append(elements)
print("List = ",list)
print("Positive integers:")
for i in list:
    if i>=0:
        print(i)
