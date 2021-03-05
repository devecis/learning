separtor = ' '
with open('output.txt', 'r') as f:
    content = f.read().split('/n')
    new_lst = sorted(content)
for i in content:
    with open('ordered_output.txt', 'a') as a:
        a.write(str(separtor.join(i)))
print(content)
