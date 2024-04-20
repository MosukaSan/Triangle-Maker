x = "*"
y = " "
z = ""
print("Choose the length of the triangle base:")
lenght = int(input())
print()

if lenght % 2 != 0:
    for b in range(lenght, 0, -2):
        z = int(b/2-0.5)*y
        a = str(z) + str(x)
        print(a)
        x = str(x) + "**"
else:
    x = x + "*"
    for b in range(lenght, 0, -2):
        z = int(b/2-0.5)*y
        a = str(z) + str(x)
        print(a)
        x = str(x) + "**"
