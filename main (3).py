x = [1,3,-5,10,-4,7,8,9,10,-15]
p = []

a=len(x)

print(a)
print()

for elem in x:
    print(x.index(elem))
    if x.index(elem)>a:
        break
    else:
        print(elem)
        if elem>0:
          p.append(elem)

print()
print ("Кол-во положительных чисел в строке =",len(p))

