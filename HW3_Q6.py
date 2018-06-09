# Anne Harris harranne@oregonstate.edu
# CS325 - 400
# Homework 3 - Question 6
# Find the minimum number of coins needed to make change

import math
import random
import time

# Implementation of making change algorithm
# Based off of Tushar Roy's video: "Coin Changing Minimum Coins Dynamic Programming"
# link to video: https://www.youtube.com/watch?v=NJuKJ8sasGk&feature=youtu.be
# Array V where V[i] is the value of the coin of the i denomination
# value amt which is the amount of change we are asked to make
def makingChange(V, amt):
    amt2 = amt + 1
    # define lists to hold results
    numCoins = [0] * (amt2)
    coinDenom = [0] * (amt2)
    # initialize lists with infinity and -1
    for i in range(1, amt2):
        numCoins[i] = float('inf')
        coinDenom[i] = -1
    # search coins
    for j in range(len(V)):
        for k in range(1, amt2):
            # see if coin j can be used to form k
            if k >= V[j]:
                # see if coin is better than existing
                if (numCoins[k - V[j]] + 1) < numCoins[k]:
                    numCoins[k] = 1 + numCoins[k-V[j]]
                    coinDenom[k] = j

    # create list of coins C to return
    c = [0]* len(V)     # list to return
    while amt > 0:
        val = coinDenom[amt]
        c[val] = c[val]+1
        print("val = ", val)
        print("c[val] = ", c[val])
        amt -= V[val]

    # return list of number of each coin needed
    return c


# Test Data
amount = 100
n = 2500       # number of coins
coins = []
temp = 1
# fill the array in sequential order
for x in range(n):
    coins.append(temp)
    temp += 1

# call making change algorithm
start = time.time()
coinsNeeded = makingChange(coins, amount)
finish = time.time()
elapsed = int((finish-start)*1000)
# print("coins: ", coins)
# print("amount: ", amount)
# print("coins needed: ", coinsNeeded)
print("Time taken to make change: ", elapsed)


