import matplotlib.pyplot as plt
import math
from collections import OrderedDict
import random


temperatutes_of_months = OrderedDict()

temperatutes_of_months['January'] = random.sample(range(-10,60),31)
temperatutes_of_months['February'] = random.sample(range(-10,60),28)
temperatutes_of_months['March'] = random.sample(range(-10,60),31)
temperatutes_of_months['April'] = random.sample(range(-10,60),30)
temperatutes_of_months['May'] = random.sample(range(-10,60),31)
temperatutes_of_months['June'] = random.sample(range(-10,60),30)
temperatutes_of_months['July'] = random.sample(range(-10,60),31)
temperatutes_of_months['August'] = random.sample(range(-10,60),31)
temperatutes_of_months['September'] = random.sample(range(-10,60),30)
temperatutes_of_months['October'] = random.sample(range(-10,60),31)
temperatutes_of_months['November'] = random.sample(range(-10,60),30)
temperatutes_of_months['December'] = random.sample(range(-10,60),31)




mean = OrderedDict()
for a, b in temperatutes_of_months.items():
    average = sum(b) / len(b)
    mean[a] = average



myvariance = OrderedDict()

for a,b in temperatutes_of_months.items():
    print(b)
    for c in b:
        variance = list()
        print(mean[a])
        variance.append(((mean[a] - c) ** 2))
    myvariance[a] = sum(variance)

print(myvariance)


deviation = OrderedDict({})
for a,b in myvariance.items():
    deviation[a] = math.sqrt(b / len(temperatutes_of_months[a]))

# months = *range(1,13)


plt.scatter([*range(1,13)] ,list(deviation.values()))
plt.title('standard deviation of temperature ')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()
