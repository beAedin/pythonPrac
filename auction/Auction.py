import os
import art

clear = lambda: os.system('cls')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for i in dict:
        bid_amount = dict[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of {highest_bid}")


dict = {}
isPlay = True

print(art.logo)
print("Welcome to the secret auction program.")



while isPlay:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict[name] = bid
    
    keep = input("other users who want to bid(yes OR no): ")
    if keep == "no" :
        isPlay = False
    clear()

find_highest_bidder(dict)