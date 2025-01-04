# File path to input data
file_path = 'input.txt'

# Define the pipe connections
pipes = {
    '═': {'left', 'right'},
    '║': {'up', 'down'},
    '╔': {'right', 'down'},
    '╗': {'left', 'down'},
    '╚': {'right', 'up'},
    '╝': {'left', 'up'},
    '╠': {'up', 'down', 'right'},
    '╣': {'up', 'down', 'left'},
    '╦': {'left', 'right', 'down'},
    '╩': {'left', 'right', 'up'},
}

# Opposite direction mappings for easy traversal
opposite_direction = {
    'left': 'right',
    'right': 'left',
    'up': 'down',
    'down': 'up',
}

# Define movement direction offsets
directions = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, 1),
    'down': (0, -1),
}

# Load data from file and parse it
grid = {}
sinks = set()
source = None

# Read the input file
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        char, x, y = line.strip().split()
        x, y = int(x), int(y)
        grid[(x, y)] = char
        if char == '*':
            source = (x, y)
        elif 'A' <= char <= 'Z':
            sinks.add((x, y))

# Helper function to find a position of a given cell
def find_position(cell):
    for position, c in grid.items():
        if c == cell:
            return position
    return None

# Function to determine if openings can connect
def is_connected_openings(direction, pipe_opening):
    connected = opposite_direction[direction] in pipe_opening
    print(f"Checking if openings connect in direction '{direction}': {connected}")
    return connected

# Function to check if two cells are connected
def are_connected(cell1, cell2, direction):

    # direction= opposite_direction[direction]

    if cell1 not in grid.values() or cell2 not in grid.values():
        return False

    # print(f"Checking connection from '{cell1}' at ({i}, {j}) to '{cell2}' in direction '{direction}'")

    # Direct connection from source or to sink
    if cell1 == '' or cell2 == '':
        return True
    if 'A' <= cell1 <= 'Z' and 'A' <= cell2 <= 'Z':
        return True

    # Check pipe openings
    if cell1 in pipes and cell2 in pipes:
        if direction in pipes[cell1] and opposite_direction[direction] in pipes[cell2]:
            print(f"Connection found between pipes '{cell1}' and '{cell2}'")
            return True

    if 'A' <= cell1 <= 'Z' and cell2 in pipes:
        if opposite_direction[direction] in pipes[cell2]:
            print(f"Connection found between pipes '{cell1}' and '{cell2}'")
            return True 

    if 'A' <= cell2 <= 'Z' and cell1 in pipes:
        if direction in pipes[cell1]:
            print(f"Connection found between pipes '{cell1}' and '{cell2}'")
            return True               

    if cell1 == '*' or 'A' <= cell1 <= 'Z':
        if cell2 in pipes and opposite_direction[direction] in pipes[cell2]:
            print(f"Connection found from '{cell1}' to pipe '{cell2}'")
            return True
    if cell2 == '*' or 'A' <= cell2 <= 'Z':
        if cell1 in pipes and direction in pipes[cell1]:
            print(f"Connection found from pipe '{cell1}' to '{cell2}'")
            return True

    return False

# List to store connected sinks and visited cells
connected_sinks = []
paths_to_sinks = {}  # Dictionary to store paths to each sink
visited_cells = set()  # Use set for faster lookup

# Function to check adjacent cells for connected sinks
def check_connected_sinks(current_cell, path=[]):
    i, j = current_cell
    visited_cells.add(current_cell)
    current_path = path + [current_cell]  # Add the current cell to the path

    print(f"Visiting cell '{grid[current_cell]}' at position ({i}, {j})")

    def visit_neighbor(neighbor_cell, direction):
        if neighbor_cell in grid:
            # neighbor_cell = grid[cell]
            # neighbor_cell_coordinates=(i,j)
            if neighbor_cell not in visited_cells:
                print(f"Considering neighbor '{grid[neighbor_cell]}' at {neighbor_cell} in direction '{direction}'")
                if are_connected(grid[current_cell], grid[neighbor_cell], direction):
                    visited_cells.add(neighbor_cell)
                    if 'A' <= grid[neighbor_cell] <= 'Z':
                        if neighbor_cell not in paths_to_sinks:
                            paths_to_sinks[neighbor_cell] = current_path
                        # if neighbor_cell not in connected_sinks:
                        #     connected_sinks.append(grid[neighbor_cell])
                        #     print(f"Connected sink '{grid[neighbor_cell]}' found at ({i}, {j})")        
                    check_connected_sinks(neighbor_cell, current_path)

    # Check all four directions
    for direction, (di, dj) in directions.items():
        ni, nj = i + di, j + dj
        visit_neighbor((ni, nj), direction)

# Group cells by row index
row_groups = {}
for (x, y), cell in grid.items():
    if x not in row_groups:
        row_groups[x] = []
    row_groups[x].append(((x, y), cell))

# Traverse each row and then check connections
for i in sorted(row_groups.keys()):
    print(f"Processing row with i = {i}")
    for (x, y), cell in row_groups[i]:
        if (x,y) not in visited_cells:
            print(f"Starting traversal from cell '{cell}' at position ({x}, {y})")
            check_connected_sinks((x,y))

for sink,path  in paths_to_sinks.items():
    if source in path:
        connected_sinks.append(grid[sink])            

# Output the result
print(f"Source is at: {source}")
print(f"Connected sinks: {connected_sinks}")
for sink, path in paths_to_sinks.items():
    print(f"Path to sink '{sink}': {path}")