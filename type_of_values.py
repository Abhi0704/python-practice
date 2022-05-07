dict = {"z1":900,'t1':1100,'p1':2300,'q1':4300}
lst =[]
for x in dict:
    if dict[x] > 1000:
        lst.append(dict[x]-1000)
    
print(lst)