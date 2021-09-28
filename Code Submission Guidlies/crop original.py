import os 
import numpy as np
import cv2
import json

ans={}

def find_points(start_point, end_point):
    '''
    Write your code to find the points ie pixels to connect
    start_point with  end_point. Remember to include both
    the points too. If you are at (x, y) then next possible 
    pixel values are (x+1, y), (x-1, y), (x, y+1), (x, y-1)
    only. Penalty will be awarded if there is a skip or you leave 
    the road. 
    '''
    path= []
    for i in range(start_point[0], end_point[0]):
        path.append([i, start_point[1]])
    for j in range(start_point[1], end_point[1]-1, -1):
        path.append([end_point[0], j])
    
    return path
 

"""Remember your code should read all the images in 
Image folder. Image name and the corresponding json 
file name from JSON folder. Your code should generate a
single Json file in the same fashion as said for all
images. Name of the json should be the team name.
"""

filenames= os.listdir()
imagenames=[]
for file in filenames:
    if file.split('.')[-1] == 'png':
        imagenames.append(file)

for name in imagenames:
    img= cv2.imread(name)
    json_name= name.split(".")[0]+'.json'
    f = open(json_name)
    data = json.load(f)
    f.close()
    start_point= data['Start']
    end_point= data['End']
    path= find_points(start_point, end_point)
    ans[name]= path

json_object = json.dumps(ans, indent = 4)
  
# Writing to sample.json
with open("Sample Submission.json", "w") as outfile:
    outfile.write(json_object)


