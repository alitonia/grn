import time

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

from simulation_targets.PID import PID


class _Controller:
	pass


class SingleParameterController(_Controller):
	def __init__(self, set_point, P=0.2, I=0.0, D=0.0):
		self.PID = PID(P, I, D)
		self._setPoint = set_point
		self._setSampleTime = 0.01
		self.feedback = 0
		
		self.END = 200
		self.feedback_list = []
		self.time_list = []
		self.setpoint_list = []
		self.i = 0
	
	@property
	def setPoint(self):
		return self._setPoint
	
	@property
	def setSampleTime(self):
		return self._setSampleTime
	
	@setPoint.setter
	def setPoint(self, set_point):
		self._setPoint = set_point
		self.PID.SetPoint = set_point
	
	@setSampleTime.setter
	def setSampleTime(self, set_sample_time):
		self._setSampleTime = set_sample_time
		self.PID.setSampleTime(set_sample_time)
	
	def update(self, feedback):
		self.feedback = feedback
		self.PID.update(self.feedback)
		
		output = self.PID.output
		if self.PID.SetPoint > 0 and self.i > 0:
			self.feedback += (output - (1 / self.i))
		# time.sleep(0.02)
		print(self.feedback)
		self.feedback_list.append(self.feedback)
		self.setpoint_list.append(self.PID.SetPoint)
		self.time_list.append(self.i)
		self.i += 1
	
	def show_analytic(self):
		time_sm = np.array(self.time_list)
		time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
		
		# feedback_smooth = spline(time_list, feedback_list, time_smooth)
		# Using make_interp_spline to create BSpline
		helper_x3 = make_interp_spline(self.time_list, self.feedback_list)
		feedback_smooth = helper_x3(time_smooth)
		
		plt.plot(time_smooth, feedback_smooth)
		plt.plot(self.time_list, self.setpoint_list)
		plt.xlim((0, self.END))
		plt.ylim((min(self.feedback_list) - 1.5, max(self.feedback_list) + 0.5))
		plt.xlabel('Time (s)')
		plt.ylabel('Temperature')
		
		# plt.ylim((1 - 0.5, 1 + 0.5))
		
		plt.grid(True)
		plt.savefig('temp.png')
		plt.show()


class DoubleParameterController(SingleParameterController):
	pass
