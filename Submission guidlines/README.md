# Instructions
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
11. **All you need is Vision**
