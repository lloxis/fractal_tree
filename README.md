# Fractal tree generator
![alt text](https://github.com/lloxis/fractal_tree/blob/main/tree_example.png)
Play around with the tree parameters to create all different types of fractal tree.

### Exe setup
Put the exe file on an empty folder. The first startup can be a little bit long.

### Window parameters
The win_params.json file let you change the default height and width of the window. When you make a change on this file save it and relaunch the app to see the changes. Please notice that this is just the default window resolution, you can resize the window whenever you want and wait for the tree to be regenerated.

### Fractal tree control panel
The fractal tree control panel window let you change the tree aspect to create many different types of trees.

Here is a description of all the parameters you can play around with. Please note that some parameters could make the tree generation to take a while.
| Param Name  | Default Value  | Recommended values | Description |
| ------------ |---------------|-----|-----|
| branches_nb | 2 | very small integer > 0 |The number of branches a branch is divide by. If this is an odd number the tree will not be symmetrical. |
| trunk_length | 200 | integer > 0 |the length of the trunk (in pixels) |
| additional_trunk_length | 0 | integer >= 0 | In tree calculation, the trunk is considered as a branch with is length beeing divided by the length dividor, however the additional_trunk_length is not is not counted when dividing the trunk length. This parameter is to be used to get a taller trunck and raise the tree without affecting the branches |
| length_dividor | 1.4 | float, > 1, very small | When a new branch is created on another (starting from the trunk) the new branch length is calculated by dividing the parent branch length by the length_dividor |
| branch_min_size | 20 | integer, > 1 and not too small | When the branch begin to be smaller then this value (in pixels), no more branches are generated. If this the number is to small this could make the app crash. Increase this number if this app is lagging |
| semi_angle | 25 | integer, from 1 to 360 | This angle added to the new branch from his parent branch, if there a multiple branches the angle is added multiple times to the rigth or to the left |
| trunk_thickness | 20 | integer, > 0 | When a new branch is created on another the new branch length is calculated by dividing the parent branch length by the length_dividor |
| thickness_dividor | 1.28 | float, > 1, very small | This can be a float, and must stay bigger than 1 | When a new branch is created on another (starting from the trunk) the new branch thickness is calculated by dividing the parent branch thickness by the thickness_dividor |
| animate_generation | false | true or false | If set to true the window is fully animating to tree generation. Note that it will greatly slow down the generation process |

You can also change the tree and background color and save the current tree as a png file on your computer.
