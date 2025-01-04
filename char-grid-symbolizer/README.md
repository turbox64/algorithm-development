# Character Grid Symbolizer

This repository contains a Python solution that reads a character grid from an HTML table hosted on a public Google Docs link and displays it as a structured grid in the console. This tool is useful for visualizing character-based symbols or patterns from coordinate data, particularly those that form visual representations of capital letters using ASCII characters.

## Features

- Fetches HTML content from a provided URL.
- Extracts table data containing coordinates and character mappings.
- Constructs and displays a character grid based on the extracted data.
- Supports ASCII characters to visually form capital letters.
- Handles missing or incomplete data gracefully.

## How It Works

1. The script fetches the HTML content from a publicly accessible Google Docs URL.
2. It uses BeautifulSoup to parse the HTML and extract relevant table rows containing coordinate and character information.
3. The table is expected to have three columns:
   - **X-coordinate**: Integer representing the column index.
   - **Character**: A single ASCII character (e.g., `|`, `-`, `/`, `\`) that contributes to a visual representation.
   - **Y-coordinate**: Integer representing the row index.
4. The extracted data is processed into a dictionary mapping coordinate pairs `(x, y)` to characters.
5. The grid is constructed by iterating over the coordinate space and printing characters at their respective positions.
6. The grid is displayed from the highest Y-coordinate to the lowest, simulating a Cartesian coordinate system.

## Input Table Format

The input table must have the following structure:

| X-coordinate | Character | Y-coordinate |
|--------------|-----------|--------------|
| 0            | -         | 2            |
| 1            | |         | 1            |
| 2            | -         | 1            |
| 0            | -         | 0            |
| 1            | |         | 0            |
| 2            | -         | 0            |

## Example Output

For the above table, the output grid would look like this:

```
 -
|-
 -
```

This grid visually represents the letter "E" using ASCII characters.

## Prerequisites

- Python 3.6 or higher
- Libraries: `requests`, `beautifulsoup4`

You can install the required libraries using:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/character-grid-symbolizer.git
   cd character-grid-symbolizer
   ```

2. Ensure the script has access to a public Google Docs URL containing the character grid in the specified format.

3. Run the script:
   ```bash
   python character_grid_symbolizer.py
   ```

4. The character grid will be displayed in the console.

## Code Overview

### Main Components

1. **`read_html_to_map(url)`**
   - Fetches and parses the HTML content from the URL.
   - Extracts coordinate-character mappings from the table.

2. **`print_character_grid(url)`**
   - Constructs and prints the character grid using the data from `read_html_to_map`.

### Key Libraries

- `requests`: For fetching HTML content from the web.
- `BeautifulSoup` (from `bs4`): For parsing HTML and extracting table data.

## Customization

- Modify the `google_doc_url` variable to point to your desired Google Docs URL.
- Adjust the table parsing logic if the input format changes.

## Example Use Case

This script can be adapted for:

- Visualizing character-based art or patterns.
- Generating coordinate-based symbolic grids for games or designs.
- Forming capital letters or shapes using ASCII characters.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request for enhancements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)

---

Happy coding!
