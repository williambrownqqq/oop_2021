capacity = input("capacity of the bag: ")
barAmount = input("enter amount of bars: ")
# barWeight = input("enter weigth of bars 'till {0}: ".format(capacity))
barAmount = int(barAmount)
capacity = int(capacity)
bars = []
i = 0
# fill
while i < barAmount:
    ind = True
    while ind:
        value = input("weigth of {0} bar 'till {1}: ".format(i + 1, capacity))
        value = int(value)
        if value > 0 and value < capacity:
            bars.append(value)
            ind = False
        else:
            print("error")
    i += 1

print("our bars: ", bars)

max_weight = [0] * (capacity + 1)  # weight of all bars
max_weight[0] = 1  # we start from zero weight, which can be collected 0 bars
bar = [0] * (capacity + 1)  # weight of one bar
for i in range(len(bars)):
    for k in range(capacity, bars[i] - 1, -1):
        if max_weight[k - bars[i]] == 1:
            max_weight[k] = 1
            bar[k] = bars[i]
i = capacity
while max_weight[i] == 0:
    i -= 1

print(i)
# i - max weigth of bars in backpack
