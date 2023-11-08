str_1 = 'BIGUS WINTER TIRES'

a = ''

a += str_1[0]

for x in range(len(str_1)):
    if str_1[x] == '':
        z = x+1
        a += str_1[z]

print(a)