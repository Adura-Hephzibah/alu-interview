# rain
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

* Prototype: `def rain(walls)`
* `walls` is a list of non-negative integers.
* Return: Integer indicating total amount of rainwater retained.
* Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
* If the list is empty return `0`.

> Visual representation of the walls [0, 1, 0, 2, 0, 3, 0, 4]
<img width="342" alt="rain1" src="https://user-images.githubusercontent.com/99495592/221211046-bdf50859-258d-4b7c-988c-7f6d7e67722e.png">

<br>

> Visual representation of the walls [2, 0, 0, 4, 0, 0, 1, 0]
<img width="341" alt="rain2" src="https://user-images.githubusercontent.com/99495592/221211224-f46a765c-2faa-473c-b1c6-d834be827213.png">

<br>

# Solution Breakdown
> `for i, ele in enumerate(walls):` - where i is index of each element, and ele is each element

> `high_left = max(walls[:i + 1])` - Find the highst wall to the left

> `high_right = max(walls[i:])` - Find the high wall to the right of each element

>`units += (min(high_left, high_right) - walls[i])` - To get the amount of rain stored: 
* first compare the hight wall to left and the highest wall to the right and find the shorter one. 
* Then subtract the height of the current all from shorter wall.