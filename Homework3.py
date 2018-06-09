# Anne Harris harranne@oregonstate.edu
# CS325 - 400
# Homework 3
# Find the minimum number of coins needed to make change


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
        amt -= V[val]

    # return list of number of each coin needed
    return c


# IMPORT FILE
data = []
with open("amount.txt", "r") as f:
    for x in f:
        if x.strip():
            var = x.split(" ")
            for y in range(len(var)):
                var[y] = int(var[y])    # string into integer
            data.append(var)

f.close()

# create file to write to
fOut = open("change.txt", "w+")
# call making change function
for i in range(0, len(data), 2):
    a = data[i]
    b = data[i+1]
    b0 = b[0]
    coinsNeeded = makingChange(a, b0)
    for num in range(len(a)):
        fOut.write(str(a[num]))
        fOut.write(" ")
    fOut.write("\n")
    fOut.write(str(b0))
    fOut.write("\n")
    for coin in range(len(coinsNeeded)):
        fOut.write(str(coinsNeeded[coin]))
        fOut.write(" ")
    fOut.write("\n")
    print("Coin denomination: ", a)
    print("Amount of change: ", b0)
    print("Number of coins needed: ", coinsNeeded)
