from matplotlib import pyplot as plt

lapCount = int(input("How many laps will there be? "))
lapDelta = int(input("What is your initial lap delta in second(s)? "))
lapWear = round(float(input("What will your tire wear per lap be like in second(s)? ")), 2)
tyreChoice = input("What is your tire choice? e.g. Soft, Medium, Hard ")
tyre = {'Soft': 0.25, 'Medium': 0.2, 'Hard': 0.13}
sumValue = lapDelta
array = [0] * lapCount
lapArray = [0] * lapCount
totalLaptime = 0
lapCountforArray = lapCount
value = 1

for i in range(lapCount):
    lapArray[i] = lapCountforArray - (lapCountforArray - value)
    lapCountforArray -= 1
    value += 1


for i in range(lapCount):
    array[i] = round(sumValue, 2)
    lapWear += tyre[tyreChoice]
    sumValue += lapWear

for q in range(len(array)):
    totalLaptime += array[q]

print(array)
print(round(totalLaptime, 2))
print(lapArray)
plt.plot(lapArray, array)
plt.ylabel("Lap Time (s)")
plt.xlabel("Lap Count")
plt.show()
