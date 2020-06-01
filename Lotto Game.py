import random

LottoDefaultDrawNumbers = 6
LottoDefaultMaxNumbers = 40

def singleDraw(numbers = LottoDefaultDrawNumbers, maximum=LottoDefaultMaxNumbers): #draw specified amount of numbers from one to max
    return random.sample(list(range(1, maximum+1, 1)), numbers)


def oneGame(PlayerDraw, GameDraw): #checks how many times number from player's draw is in GameDraw
    hits = []
    for numb in PlayerDraw:
        if numb in GameDraw:
            hits.append(numb)
    return hits

print("\n------- WELCOME TO LOTTO SIMULATOR ver 2.0 -------\n")
LottoDraw = singleDraw()
print("Lotto has drawn numbers: ", LottoDraw) #drawing the numbers of Lotto

while True: #loop to ask for a number of coupons
    PlayerChoice = input("How many random coupons do you want to buy?")
    if PlayerChoice.isnumeric():
        PlayerChoice = int(PlayerChoice)
        break
    else:
        print('Error - give an integer!')

hitsLensList = [] #now empty - then needed to summarise
zerohits = 0


for i in range(1,PlayerChoice+1,1): #loop to compare each coupon with Lotto numbers
    roundPlayerNums = singleDraw()
    hits = oneGame(roundPlayerNums, LottoDraw)
    print("\nGame number {}, your numbers: {}".format(i, roundPlayerNums))
    print("numbers hit:", hits)
    if len(hits)>0:
        hitsLensList.append(len(hits))
    else:
        zerohits+=1

print("\n____ SUMMARY _____\n")
#print(hitsLensList)
winTypes = sorted(set(hitsLensList), reverse=True)
for winType in winTypes:
    print("Type of win: {} - won {} times".format(winType, hitsLensList.count(winType)))
print("Zero hits - {} times".format(zerohits))
