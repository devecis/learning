# Write a function that flips a coin. It should return a string that reads 'Heads' or 'Tails'. Bonus points if you add the ability to make the coin unfair.
import random


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
