import random

subjects=[
    "Virat Kohli",
    "Shahrukh khan",
    "Prime Minister Modi",
    "A cat",
    "A group of monkeys",
    "Auto Rickshaw from Delhi",
]
actions=[
    "launches",
    "cancels",
    "plays cricket",
    "eat food on streets of delhi",
    "flying in the sky",
    "sits as a beggar on street"
]
places_or_things=[
    "at red fort",
    "in mumbai local train",
    "during IPL match",
    "a plate of samosa",
    "at ganga ghat",
    "at India Gate"
]
while True:
    sub=random.choice(subjects)
    act=random.choice(actions)
    place=random.choice(places_or_things)

    headline=f" BREAKING NEWS: {sub} {act} {place}"
    print("\n" + headline)

    user=input("\n Do you want to generate another fake news:").strip().lower()
    if user=="no":
        break

print("\n Thanks for using Fake News Headline Generator")