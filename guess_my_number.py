min=0
max=100
mid=50
guess="Is your secret number: "
print("Please think of a number between 0 and 100!")
print(guess + str(mid) + "?")
ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while ans != 'c':
    if ans=='h':
        max=mid
        mid=int((max+min)/2)
    elif ans=='l':
        min=mid
        mid=int((max+min)/2)
    else:
        print("Sorry, I did not understand your input.")
    print(guess + str(mid) + "?")
    ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
if ans=='c':
    print("Game over. Your secret number was:" + str(mid))