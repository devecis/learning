import random

verbs = [
    "leverage",
    "Sync",
    "Target",
    "Gamify",
    "Offline",
    "Crowdsourced",
    "24/7",
    "lean-in",
    "30,000 foot",
]
adjectives = [
    "a/b tested",
    "Freemium",
    "Hyperlocal",
    "Siloed",
    "B-to-B",
    "Oriented",
    "Cloud-based",
    "API-based",
]
nouns = [
    "Early Adopters",
    "Low-hanging Fruit",
    " Pipeline",
    " Splash page",
    "Productivity",
    "Process",
    "Tipping Point",
    "Paradigm",
]
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
phrase = verb + " " + adjective + " " + noun
print(phrase)