#Determine if a word or phrase is an isogram.
#An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
#Examples of isograms:
    #lumberjacks
    #background
    #downstream
    #six-year-old
#The word isograms, however, is not an isogram, because the s repeats.

def isogram(word):
    fuck = []
    for letter in word:
        fuck.append(letter)
    if fuck.count(letter) > 1:
            print("Nah dawg that shit ain't no isogram")
    else:
            print("You're muthafuckin right it's an isogram")    

def main():
    word = input('Enter a word to see if it is a isogram: ').lower()
    isogram(word)

if __name__ == '__main__':
    main()
    