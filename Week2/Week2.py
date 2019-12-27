lo = 0
hi = 100
ans = ""
print("Please think of a number between 0 and 100!")
while ans != "c":
    mid = int((lo + hi) / 2)
    print("Is your secret number", mid, "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to "
                "indicate the guess is too low. Enter 'c' to indicate I "
                "guessed correctly.")
    if ans == "h":
        hi = mid
    elif ans == "l":
        lo = mid
    elif ans == "c":
        print("Game over. Your secret number was:", ans)
        break
    else:
        print("Sorry, I did not understand your input.")
