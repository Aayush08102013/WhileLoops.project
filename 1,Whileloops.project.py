# While loop project
# Formula of using a while loop:
# to use while loop statment we will have to floolow the steps below
# While condition : #There is your while loop.
a = int(input("Enter a number to check how many digits it has : "))
b = 10
c = 100
d = 1000
e = 10000
f = 100000
g = 1000000
h = 10000000
if a > 0:
    if a < b:
        print(f"{a}, only contians 1 digit")
    elif a > b and a < c:
        print(f"{a}, contains 2 digits")
    elif a > c and a < d:
        print(f"{a}, contians 3 digit")
    elif a > d and a < e:
        print(f"{a}, contains 4 digits")
    elif a > e and a < f:
            print(f"{a}, contains 5 digits")
    elif a > f and a < g:
        print(f"{a}, contians 6 digit")
    elif a > g and a < h:
        print(f"{a}, contains 7 digits")
    else:
        print(f"{a}, contains more than 8 digits")
else:
    print("invalid input!")