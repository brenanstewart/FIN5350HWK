print ("In this program you will enter a number between 1 - 100."
       "\nAfter the computer will try to guess your number!")
high_guess = 101
low_guess = 0
tries = 1
print("\n\nEnter a number between 1 and 100.")
the_number = int(input("Number: "))
while the_number < 1 or the_number > 100:
    print("The number must be between 1 and 100.")
    the_number = int(input("Number: "))
guess = 50

while guess != the_number:
    if guess > the_number:
        high_guess = guess
        guess = guess - int((high_guess - low_guess)/2)
    else:
        low_guess = guess
        guess = guess + int((high_guess - low_guess)/2)
    tries += 1
    print(guess)

print(f"\nThe computer guessed the number in {tries} tries.")
print(f"The number was {the_number}.")
