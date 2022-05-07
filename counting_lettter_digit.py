str = input("input a string")
d = 0
l = 0
for c in str:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("letters" ,l)
print("digits",d)