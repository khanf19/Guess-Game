import random
n = random.randint(1, 100)
print("Guess The Number Between 1 To 100")
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
        guesses +=1
print(f"You Have Guessed The Number {n} Correctly in {guesses} Attempts")
print("Congratulations💐💐💐")
