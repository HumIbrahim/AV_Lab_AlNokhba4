#! /usr/bin/python3

import os
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
import base64

matplotlib.use('Agg')


print("Content-type: text/html\n\n")


URL_name = os.getenv('QUERY_STRING')

with open("setup.csv") as file:
    for line in file:
        pass

coords = line
coords = coords.split(',')
coord_list = [i for i in coords]
coord_list[-1] = coord_list[-1].strip()

robot_name = coord_list[0]
x = float(coord_list[1])
y = float(coord_list[2])

plt.plot(x,y, 'ro')
plt.title(robot_name)
plt.savefig(str(robot_name) + '.png')

data_uri = base64.b64encode(open(robot_name+'.png', 'rb').read()).decode('utf-8')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

if robot_name == URL_name:
    print(img_tag)
else:
    print("No robot named ", URL_name, " exists")
