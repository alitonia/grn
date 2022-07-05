import random
import time

from matplotlib import pyplot as plt

from simulation_targets.controller import SingleParameterController

END = 200
# c = SingleParameterController(0, 0.05, 0.6, 0)
c = SingleParameterController(0, 0.03, 0.6, 0)

feedback = 30
for i in range(1, END):
	c.PID.SetPoint = 4.4
	
	c.update(feedback)
	feedback = c.feedback

print('done')
acc = []
t = 0
last = 0
all_time_max = 0

area = 10 * 10
air_area = area * 3
air_P = air_area * 29

riceWeight = 1.452 * area * 1
cornWeight = 1.486 * area * 1
soybeanWeight = 1.393 * area * 1
sunflowerWeight = 0.864 * area * 1

rice_P = 0.782 * riceWeight
corn_P = 1.27 * cornWeight
soybean_P = 1.3934 * soybeanWeight
sunflower_P = 0.15 * sunflowerWeight

total_P = air_P + corn_P

conditioner_W = (2.5 * 750_000) / 0.9
J_perH = 25_321_340.5

ratio = conditioner_W / J_perH

for (i, v) in enumerate(c.feedback_list):
	if i == 0:
		last = v
		all_time_max = v
		continue
	diff = abs(v - last) + random.uniform(0, 0.1)
	t += (diff) * total_P / J_perH * conditioner_W
	acc.append(t)
	last = v

acc.append(acc[-1])
print(t)
print(acc)
print(total_P)
plt.xlabel('Time (s)')
plt.ylabel('W')
plt.plot(c.time_list, acc)
# plt.plot(c.time_list, [acc[-1]] * len(acc))
plt.annotate('%0.2f' % max(acc), xy=(1, max(acc)), xytext=(4, 0), xycoords=('axes fraction', 'data'),
             textcoords='offset points')
plt.grid(True)
plt.savefig('W.png')
plt.show()
# c.show_analytic()
