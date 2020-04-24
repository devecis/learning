#Chatbot asks a question
#If question is lower case, but ends in a ? answer with "Sure"
#If YELL (all Caps) respond 'Whoa, chill out!'
#If YELL with ? respond with Calm down, I know what I'm doing!'
#if nothing is entered respond 'Fine. Be that way!'
#Any else pass 'Whatever.'


answer = input("Hey Bud, my name is Bob, what's up you got a question? ")
if answer.isupper and answer.endswith('?'):
    print("Calm down, I know what I'm doing!")
elif answer.endswith('?'):
    print('sure')
elif not answer:
    print('Fine! Be that way!')
elif answer.isupper():
    print('Whoa, chill out!')
else:
    print('whatever')
    