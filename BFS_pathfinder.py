from world import gridworld
import random

class BFS_pathfinder:
    def __init__(self, world, start, goal):
        self.world = world
        self.start = start
        self.end = goal
        # Run the placement logic immediately
        self.set_start(self.start)
        self.set_goal(self.end)

    def set_start(self, start_pos):
        """Validates and places the start 'S' on the grid."""
        if self.world.in_cell(start_pos) and self.world.is_free(start_pos):
            self.start = start_pos
            x, y = self.start
            self.world.grid[x][y] = "S"
        else:
            # Fallback to (0,0)
            if self.world.is_free((0, 0)):
                print("Invalid starting point, setting point to (0,0)")
                self.start = (0, 0)
                self.world.grid[0][0] = "S"
            else:
                # Random search for an empty spot
                placed = False
                while not placed:
                    a = random.randint(0, self.world.size - 1)
                    b = random.randint(0, self.world.size - 1)
                    if self.world.is_free((a, b)):
                        self.start = (a, b)
                        self.world.grid[a][b] = "S"
                        placed = True
                        print(f"Invalid starting point, randomized to ({a},{b})")

    def set_goal(self, goal_pos):
        """Validates and places the goal 'G' on the grid."""
        if self.world.in_cell(goal_pos) and self.world.is_free(goal_pos):
            self.end = goal_pos
            x, y = self.end
            self.world.grid[x][y] = "G"
        else:
            last_idx = self.world.size - 1
            # Fallback to bottom-right corner
            if self.world.is_free((last_idx, last_idx)):
                print(f"Invalid goal, setting to ({last_idx},{last_idx})")
                self.end = (last_idx, last_idx)
                self.world.grid[last_idx][last_idx] = "G"
            else:
                # Random search for an empty spot
                placed = False
                while not placed:
                    a = random.randint(0, self.world.size - 1)
                    b = random.randint(0, self.world.size - 1)
                    # Make sure we don't overwrite the start!
                    if self.world.is_free((a, b)) and (a, b) != self.start:
                        self.end = (a, b)
                        self.world.grid[a][b] = "G"
                        placed = True
                        print(f"Invalid goal, randomized to ({a},{b})")

    