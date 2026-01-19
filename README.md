# gridworld-path-planner
## A grid-based world with obstacles, where an agent finds a path from a start cell to a goal using Breadth First Search (BFS)
### Run this mini-project in the BFS_main.py file, but you still have to put every class here in a folder, because BFS_main imports everything from every class here!

This is being split up into separate parts:

---------------------------------------------------IMPLEMENTATION PHASE---------------------------------------------------
1) First, I have created a class that creates the actual grid, and checks if each spot allows for the agent to move
2) Second, I allowed the user to create a start and end goal in the form of a tuple. If the user inputs an illegal tuple, the start and end cells will be randomized. I then imported deque and utilized its functionality to implement BFS.
3) Thirdly, I added some ASCII text in order to make the programn look better for the implementation phase. This is a separate class because I wanted to keep each step of the code organized.
4) Lastly for the implementation, I put together all three classes and asked the user for input. This program will continue to repeat until the user types "n", in which the program will halt.

This is an intro exercise which allows me to warm up my Python skills after Data C88C has ended (Dec 2025).
