import random
import time

from matplotlib import pyplot as plt

from simulation_targets.controller import SingleParameterController

END = 200
c = SingleParameterController(0, 0.05, 0.6, 0)
feedback = 30
for i in range(1, END):
	c.PID.SetPoint = 15
	
	c.update(feedback)
	feedback = c.feedback

print('done')
acc = []
t = 0
last = 0
all_time_max = 0
#
#
# air_area = 60 * 60 * 3
# air_P = air_area * 29
# riceWeight = 1.452 * 60 * 60 * 1
# rice_P = 0.782 * riceWeight
# total_P = air_P + rice_P
#
# conditioner_W = (2.5 * 750_000)
# J_perH = 25_321_340.5
#
# ratio = conditioner_W / J_perH
#
# for (i, v) in enumerate(c.feedback_list):
# 	if i == 0:
# 		last = v
# 		all_time_max = v
# 		continue
# 	diff = abs(v - last) + random.uniform(0, 0.1)
# 	t += (diff * total_P / J_perH * conditioner_W)
# 	acc.append(t)
# 	last = v
#
# acc.append(acc[-1])
# print(t)
# print(acc)
# print(total_P)
# plt.xlabel('Time (s)')
# plt.ylabel('W')
# plt.plot(c.time_list, acc)
#
# plt.grid(True)
# plt.savefig('W.png')
# plt.show()
c.show_analytic()
