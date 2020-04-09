#Write a magic eightball function. It should return strings instead of printing to the console. 
# The possible answers for an eightball are here: https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers

def eightball():
    phrasedict = {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Yes-definitely",
        5: "You may rely on it",
        6: "As I see it, yes",
        7: "Most liklely",
        8: "Outlook good",
        9: "Yes",
        10: "Signs point yes",
        11: "Reply hazy, try again",
        12: "Ask again later",
        13: "Better not tell you now",
        14: "Cannot predict now",
        15: "Concentrate and ask again",
        16: "Don't count on it",
        17: "My reply is no",
        18: "My source says no",
        19: "Outlook not so good",
        20: "Very doubtful",
    }

    return phrasedict.get(int(random() * 20))