#Write a function that prints a string in a frame, such as: frame('Hello World in a frame') prints:

#*********
#* Hello *
#* World *
#* in    *
#* a     *
#* frame *
#*********

#Hello is the phrase that we want print and put in a frame
#Frame needs to start before and after the first letter
#Need to print each word on its own line
#Need to be able to put a frame around the word


def frame(phrase):
    
    size = max([len(word) for word in phrase.split()])
    #For word in phrase:
       #return the length of a word in that list
    # then return the longest word in that list
    print('*' * (size+4))
    for word in phrase.split():
        print(f'* {word.center(size)} *')
    print('*' * (size+4))
       
def main():
    phrase = input("Enter a phrase: ")
    frame(phrase)
    
if __name__ == '__main__':
    main()

#for length of the biggest word print that amount of borders
#size = max length of the longest word in phrase and then print as many * as that word
#size = max(len(word) for word in phrase):
#print (*)
#antidisestablishmentarianism - opposition to the disestablishment of the Church of England - 28