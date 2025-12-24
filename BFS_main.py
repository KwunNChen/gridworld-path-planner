from world import gridworld
from BFS_pathfinder import BFS_pathfinder
from flavor_texts import title

do_again = "y"
def main():
    # Display title and prompt user for grid parameters
    print(title)
    print("Starting Grid World Pathfinding using BFS Algorithm...\n")
    size = int(input("Enter grid size (e.g., 5 for 5x5 grid): "))
    obstacles = int(input("Enter number of obstacles: "))
    world = gridworld(size, obstacles)
    #BFS Pathfinding args
    start_x = int(input("Enter starting X coordinate (0-based index): "))
    start_y = int(input("Enter starting Y coordinate (0-based index): "))
    goal_x = int(input("Enter goal X coordinate (0-based index) : "))
    goal_y = int(input("Enter goal Y coordinate (0-based index): "))
    #Set start and goal positions
    start = (start_x, start_y)
    goal = (goal_x, goal_y)
    #Initialize BFS pathfinder
    pathfinder = BFS_pathfinder(world, start, goal)
    path = pathfinder.find_path()
    if path:
        pathfinder.mark_path(path)
    world.display_grid()

main()
#Asks user if they want to run another session
while do_again == "y":
    do_again = input("Would you like to run another pathfinding session? (y/n): ").strip().lower().lower()
    if do_again == "y":
        main()
    else:
        print("Exiting program. Goodbye!")
        do_again = "n"
