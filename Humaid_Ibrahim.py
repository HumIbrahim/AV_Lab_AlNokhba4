#!/usr/bin/env python3

import rospy
import requests
from turtlesim.msg import Pose

class Listener(object):

	def __init__(self):
		rospy.init_node('robot_coords', anonymous=True)
		self.sub = rospy.Subscriber("/turtle1/pose", Pose, self.getCoords)
		self.x = 0
		self.y = 0

	def getCoords(self, coords):
		self.x = coords.x
		self.y = coords.y

	def read(self):
		r = rospy.Rate(1)
		while not rospy.is_shutdown():
			self.post(self.x, self.y)
			r.sleep()

	def post(self, x, y):
		mycoords = {'robot_name': robot_name, 'x': x, 'y': y}
		requests.post('http://' + str(address) + '/' + str(mycoords["robot_name"]) + '/' + str(mycoords["x"]) + '/' + str(mycoords["y"]))

if __name__ == "__main__":
	address = input("Please type in the server address (without http or any forward slashes): \n")
	robot_name = input("Please type in the robot name: \n")
	obj = Listener()
	obj.read()