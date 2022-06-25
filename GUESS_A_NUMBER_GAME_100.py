def search_high_divider(current_guess, current_max_high):
    if current_guess == 99:
        return 100, 100
    else:
        new_guess = (current_max_high - current_guess)//2 + current_guess
        new_max_low = current_guess
    return new_guess, new_max_low


def search_low_divider(current_guess, current_max_low):
    if current_guess == 1:
        return 0, 0
    else:
        new_guess = current_max_low + (current_guess - current_max_low)//2
        new_max_high = current_guess
    return new_guess, new_max_high


#  until first L after H, max_high = 101
#  or until first H after L, the max_low = 0

rounds = 0
guess = 50
max_high = 101
max_low = 0
answer = "N"
print("Please pick a number between 0 and 100.")
while answer != "Y":
    print("Is your number: ", guess)
    answer = input("Enter Y for yes or N for no.")  # my not work w sentence split.  Sep is nec
    if answer == "Y":
        print("Done.")
    else:
        answer = input("Is your number higher (H) or lower (L)?")
        if answer == "H":
            guess, max_low = search_high_divider(guess, max_high)
        else:
            guess, max_high = search_low_divider(guess, max_low)
    rounds += 1
print("You completed ", rounds," rounds")
