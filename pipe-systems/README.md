# Pipe Connection Analyzer

This repository contains an algorithm designed to analyze pipe connections in a grid-based layout. It determines the connectivity between a source (`*`) and various sinks (denoted by uppercase letters) using a set of defined pipe symbols. This tool is useful for visualizing and analyzing pipe-based networks or systems.

## Features

- Parse a grid layout from an input file.
- Define pipe connectivity using directional symbols.
- Determine connections between a source and sinks.
- Trace and print paths from the source to connected sinks.

## How It Works

1. The algorithm reads a grid layout from an input text file, where each line specifies:
   - **Character**: Represents a pipe, source, or sink.
   - **X-coordinate**: Column index of the character in the grid.
   - **Y-coordinate**: Row index of the character in the grid.

2. It maps each pipe symbol to its valid connection directions:
   - `═`: Connects left and right.
   - `║`: Connects up and down.
   - Other pipe symbols (`╔`, `╗`, etc.) represent corner or junction connections.

3. A traversal is initiated from the source (`*`) to explore all reachable paths. During this process:
   - The algorithm checks if two adjacent cells are connected based on the pipe symbols.
   - It keeps track of visited cells to avoid redundant processing.
   - It identifies and stores the paths leading to each connected sink.

4. The final output lists the connected sinks and the paths taken to reach them.

## Input File Format

The input file (`input.txt`) should contain one entry per line, formatted as:

```
<char> <x> <y>
```

Where:
- `<char>`: A pipe symbol, source (`*`), or sink (uppercase letter).
- `<x>`: X-coordinate (column index).
- `<y>`: Y-coordinate (row index).

### Example Input

```
* 0 0
═ 1 0
═ 2 0
╔ 3 0
║ 3 1
A 3 2
``` 
###  input.txt, input2.txt examples are included inside reposotory folder.

### Example Grid Representation

```
*══╔
   ║
   A
```

## Pipe Symbols and Connections

| Symbol | Connections                  |
|--------|------------------------------|
| `═`    | Left, Right                  |
| `║`    | Up, Down                     |
| `╔`    | Right, Down                  |
| `╗`    | Left, Down                   |
| `╚`    | Right, Up                    |
| `╝`    | Left, Up                     |
| `╠`    | Up, Down, Right              |
| `╣`    | Up, Down, Left               |
| `╦`    | Left, Right, Down            |
| `╩`    | Left, Right, Up              |

## Prerequisites

- Python 3.6 or higher

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pipe-connection-analyzer.git
   cd pipe-connection-analyzer
   ```

2. Ensure the input file (`input.txt`) is in the repository folder and formatted correctly.

3. Run the script:
   ```bash
   python pipe_analyzer.py
   ```

4. View the output in the console. It will display:
   - The source location.
   - Connected sinks.
   - Paths to each connected sink.

### Example Output

For the above input example, the output might be:
```
Source is at: (0, 0)
Connected sinks: ['A']
Path to sink '(3, 2)': [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]
```

## Code Overview

### Key Components

1. **Pipe Connections**:
   A dictionary defines the valid connections for each pipe symbol.

2. **Direction Offsets**:
   A mapping of movement directions (`left`, `right`, `up`, `down`) to their respective coordinate changes.

3. **Traversal Algorithm**:
   - Starts from the source (`*`).
   - Explores all reachable cells while maintaining a path history.
   - Checks connections between adjacent cells using the defined pipe connections.

4. **Output**:
   - Lists connected sinks and their respective paths.

## Customization

- Modify the `pipes` dictionary to add or change pipe symbols.
- Adjust the `input.txt` file to test with different grid layouts.

## Example Use Case

This algorithm can be adapted for:
- Simulating fluid flow or electrical circuits in a grid.
- Pathfinding in structured networks.
- Visualizing connectivity in game mechanics.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- ASCII and Unicode pipe symbols reference.
- Pathfinding and connectivity concepts.
