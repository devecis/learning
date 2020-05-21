#list comperhension and explanation below using .isalpha()
word='hold my beer'
print([letter for letter in word if letter.isalpha()])

hold=[]
for letter in word:
    if letter.isalpha():
        hold.append(letter)
print(hold)