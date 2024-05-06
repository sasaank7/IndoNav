# Project Documentation for IndoNav

## Overview
**IndoNav** is a web-based navigation system designed specifically for the CMR Institute of Technology's 2nd floor. It uses Flask to provide path-finding services from one location to another within the building.

## Technologies Used
- **Python 3**: Main programming language for server-side logic.
- **Flask**: A lightweight WSGI web application framework to serve web pages and handle backend logic.
- **JavaScript**: For client-side user interaction and AJAX requests to the server.
- **HTML/CSS**: For structuring and styling the user interface.
- **jQuery**: Simplifies HTML document traversing, event handling, and Ajax interactions.

## Algorithm
The application uses Dijkstra's algorithm to find the shortest path between two points on the map. This algorithm ensures that the shortest path is found by considering all possible paths between the start and destination points and selecting the path with the lowest cumulative weight.

## Running the Application
To run IndoNav, execute the following command in the project directory:

```bash
python webpage_flask.py
```


# How to Use
- Open the application in a web browser.
- Input your starting location and destination on the CMRIT 2nd floor in the respective fields.
- Click the Search button to display the path.
- The path and total distance will be shown below the input fields.

# Contributing
- Contributions to IndoNav are encouraged! Please fork the repository and submit a pull request with your changes, or open an issue if you find bugs or have suggestions.
