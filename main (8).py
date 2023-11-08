str_1 = 'BIGUS DVIGOZAVRI CASH EKATERINBURG'

a = ''

a += str_1[0]

for x in range(0,len(str_1)):
    if str_1[x] == ' ':
        a += str_1[x+1]
    else:
        continue

print(a)