import random

easy_words=["apple","banana","mango","ltchi","pineapple","strawberry"]
medium_words=["mountain","sea","coast","beach","tracking","swimming"]
hard_words=["umbrella","diamond","computer","laptop","flying","elephant"]

print("Welcome to the guessing game")
print("Choose a difficulty level: easy,medium,hard")

level=input("enter difficulty level:").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid choice!")
    secret=random.choice(easy_words)

attempts=0
print("\n Guess the secret word")

while True:
    guess=input("enter guess:").lower()
    attempts+=1

    if guess == secret:
        print(f"Congratulations! You gussed it right in {attempts}")
        break
    hint=""
    for i in range(len(secret)):
        if i < len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint:",hint)
print("Game Over!")

