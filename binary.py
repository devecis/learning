i = int(input('What number do you want in binary?'))
num=[]
binary=[256, 128, 64, 32, 16, 2]
for x in binary:
    if x > i:
        num.append(0)
        
    else:
        num.append(1)
        i -= x
        print(x)
print(num)