import requests
from bs4 import BeautifulSoup

# URL of the Google Docs documents
google_doc_url = "https://docs.google.com/document/d/1I2wAZOsE8BuX-YJi8u0Qhxqzq5rfHwdw_WMc3eyAmA0/edit?usp=sharing"


def print_character_grid(url):

    #helper function to read html into coordinates_char_map
    def read_html_to_map(url):
        # Fetch HTML content from the URL
        response = requests.get(url)
        content = response.text

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Initialize the data list of <td> content
        data = []
    
        # Skip the first row (header) and process the rest
        # Extract table rows
        rows = soup.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) == 3:
                try:
                    x = int(cells[0].get_text(strip=True))
                    char = cells[1].get_text(strip=True)
                    y = int(cells[2].get_text(strip=True))
                    data.append((x, char, y))
                except ValueError:
                    continue
        coordinates_char_map = {(x, y): char for x, char, y in data} 
        return coordinates_char_map
    

    # call helper function to read html into coordinates_char_map
    coordinates_char_map = read_html_to_map(url)

    # Determine map max x and max y
    max_x = max(x for x, y in coordinates_char_map.keys())
    max_y = max(y for x, y in coordinates_char_map.keys())


    # Print coordinates_char_map from (0,max_y)(1,may_y)....(max_x,max_y) moving downward in the y axis to (0,0)
    for y in range(max_y, -1, -1):
        line = ""
        for x in range(max_x + 1):
            line += coordinates_char_map.get((x, y), ' ')
        print(line)
        print()


# execute the function to print unicode char grid to form charater
print_character_grid(google_doc_url)
    

    
