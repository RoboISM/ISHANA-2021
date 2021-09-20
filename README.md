# ISHANA 

## Problem Statement
There is a autonomous car driving around on a security mission on ground. It's a high tension time <br>
in the country and its known that the enemy has highly skilled hacker who can penetrate into the <br>
car's navigation system and carry out adverserial attacks. So a drone flys above the car and provides it<br>
the starting and destination point at regular intervals. Help the car reach it's destination in <br>
smallest time possible.<br>

## Data
The competition is now live with 40% of the whole data. <br>
Your code will be tested for rest 60% data in last 3 days. <br>
The images are extracted from Google Earth at an elevation of 600m to 1200m elevation. <br>
JSON file contains the initial and final points. <br>
You are allowed to use any dataset you like. <br>

## Instructions
1. Extract the zip file provided in releases of this repo.
2. Images with json having same name are provided
3. Extract the starting co-ordinate and final co-ordinate from json for the respective image
4. Provide the pixel values so as to start from the starting point and reach final point while sticking
on the road. Penalty will awarded if the pixel lies outside the road.
5. Goal is to reach the final point in least step.
6. Maximum possible score one can get is **0**.
7. For every step you take you are penalised **0.5**
8. If you are at (x, y) then next possible pixel values are (x+1, y), (x-1, y), (x, y+1), (x, y-1) only.
9. Each skip in pixel is penalised too. Penalty per skip will increase with number of consecutive skipped step.
For example if there are 3 occurences of skip with 5, 8, 18 skips in pixels respectively the penalty can be 10, 28, 135. 
10. Leaving the road will be penalised in the same fashion.

## Rules
This is a coding contest. <br>
You are allowed to use only open source tools. <br>
You can submit as many submission files each day as a json file. <br>
Json file has to named as team name. If your team name is XYZ then filename has to be XYZ.json <br>
Sample code and submission file has been provided. <br>
Leaderboard will be refreshed every 2 hour from 10:00 IST to 02:00 IST. <br>
You have to submit your code in a specified format in last 3 days. <br>
Code can submitted a maximum of 3 times each day. <br>
The leaderboard will show your result in the whole dataset in last 3 days. <br>

[Discord Server Link](https://discord.gg/Zt5t6gHv) <br>
[Website](https://takshak.roboism.in/competitions/ishana)
# Happy Coding
