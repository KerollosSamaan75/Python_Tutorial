n = int(input("Enter the number of terms: "))

for i in range(n):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        a, b = 0, 1
        for j in range(2, i+2):
            a, b = b, a + b
        print(b)
