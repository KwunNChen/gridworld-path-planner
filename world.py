import random

#This is the class to make grid world
class gridworld:
    def __init__(self, size, obstacle_count):
        self.size = size
        self.obstacle_count = obstacle_count
        self.grid = []
        for i in range(self.size):
            self.grid.append(["."] * self.size)
        #Add obstacles randomly
        altered = 0
        while altered < (self.obstacle_count):
            x = random.randint(0,self.size-1)
            y = random.randint(0,self.size-1)
            if self.grid[x][y] != "#":
                self.grid[x][y] = "#"
                altered += 1
        self.display_grid()


    def display_grid(self):
        print(f"--- {self.size}x{self.size} Grid World ---")
        for x in range(self.size):
            print(self.grid[x])

    #Used for quickly checking if something is within bounds
    def in_cell(self,cell):
        (x,y) = cell
        if 0 <= x < self.size and 0 <= y < self.size:
            return True
        else:
            return False
    
    #Check if a cell is free to move
    def is_free(self,cell):
        (x,y) = cell
        if self.in_cell(cell):
            if self.grid[x][y] != "#":
                return True
            else:
                return False
        else:
            return False
    
    #Check which side can be moved
    def neighbors(self,cell):
        (x,y) = cell
        can_move = []
        #Move up,down,left,right?
        temp_cells = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
        for i in range(len(temp_cells)):
            if self.in_cell(temp_cells[i]):
                if self.is_free(temp_cells[i]):
                    can_move.append(temp_cells[i])
        return can_move
