# AI-Based Emergency Evacuation Route Planner Using A* Search

## 1. Project Overview

The AI-Based Emergency Evacuation Route Planner is an interactive Python application that uses the **A* Search Algorithm** to find an efficient evacuation route from a starting location to a designated exit.

The system represents a building as a grid containing a starting point, an exit, and blocked cells representing dangerous or inaccessible areas. When a path becomes blocked, the algorithm can search for an alternative route.

## 2. Objectives

- Find efficient evacuation routes using the A* Search Algorithm.
- Visualize the building layout and calculated evacuation path.
- Allow users to mark and unblock dangerous areas.
- Demonstrate how intelligent search algorithms can support emergency evacuation planning.

## 3. Features

- **Interactive Grid:** Represents the building layout.
- **Set Starting Location:** Select the evacuation starting point.
- **Set Exit:** Choose the destination exit.
- **Block/Unblock Cells:** Simulate obstacles or dangerous areas.
- **Find Route:** Calculate an evacuation route using A*.
- **Step-by-Step Search:** Visualize the search process.
- **Path Visualization:** Display the calculated route and explored cells.
- **Reset Options:** Clear the current path or reset the grid.

*Note: The features listed above should match the functionality implemented in your actual project.*

## 4. Technologies Used

- **Programming Language:** Python
- **Algorithm:** A* Search Algorithm
- **Interface:** Interactive grid-based user interface
- **Search Strategy:** Heuristic-based pathfinding

## 5. How to Run the Project

### Prerequisites

- Python 3 installed on your computer.
- The project source code downloaded or extracted.
- Any additional dependencies required by the application.

### Step 1: Download the Project

Download the project ZIP file or clone the GitHub repository.

Extract the ZIP file if you downloaded it.

### Step 2: Open the Project Folder

Open Terminal on macOS and navigate to the project directory.

Example:

```bash
cd path/to/AISC_Project
```

Replace `path/to/AISC_Project` with the actual location of your project folder.

### Step 3: Create a Virtual Environment (Optional)

```bash
python3 -m venv venv
```

Activate it on macOS:

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

If the project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If the application uses only Python's standard library, additional packages may not be required.

### Step 5: Run the Application

Run the Python file that contains the application's entry point.

For example, if the main file is named `main.py`:

```bash
python3 main.py
```

Replace `main.py` with the actual filename if your project uses a different entry point.

The application interface should open, allowing you to interact with the evacuation grid.

## 6. How to Use the Application

1. Launch the application.
2. Select the starting location.
3. Select the destination exit.
4. Mark any dangerous or blocked cells.
5. Run the A* search to calculate the evacuation route.
6. Observe the explored cells and the resulting path.
7. Block a cell on the existing route and search again to test alternative routing.
8. Reset the grid to begin a new simulation.

## 7. Working Principle

The A* Search Algorithm evaluates possible paths using the following function:

**f(n) = g(n) + h(n)**

Where:

- **g(n):** Actual cost of reaching the current node from the starting point.
- **h(n):** Estimated cost from the current node to the destination.
- **f(n):** Estimated total cost of the path through the current node.

The algorithm explores promising nodes and uses these costs to identify an efficient path to the exit.

Blocked cells are excluded from the available routes. If a valid route cannot be found, the system should indicate that no route is available.

## 8. Testing

The application can be tested using the following scenarios:

| Test Case | Expected Result |
|---|---|
| Valid start and exit | A route is calculated |
| Blocked cells on the grid | The route avoids blocked cells |
| Obstacle added to the current route | An alternative route is found, if available |
| No valid path exists | A no-route message is displayed |
| Grid reset | The grid returns to its initial state |

## 9. Limitations

- The building layout is represented as a simplified grid.
- The simulation does not automatically receive real-time sensor data.
- Route calculations depend on the grid configuration and obstacle information supplied by the user.
- The application is a prototype and does not replace professional emergency evacuation systems.

## 10. Future Scope

- Integration with real building floor plans.
- Dynamic hazard updates using sensors.
- Multiple-exit selection and route optimization.
- Multi-agent evacuation simulation.
- Integration with IoT-based fire and smoke detection systems.

## 11. Conclusion

The project demonstrates the application of artificial intelligence search techniques to emergency evacuation planning. By using A* Search, the system identifies efficient routes while accounting for blocked areas and demonstrates how route planning can adapt to changing conditions.

## 12. Project Information

**Project Title:** AI-Based Emergency Evacuation Route Planner Using A* Search

**Domain:** Artificial Intelligence and Soft Computing

**Programming Language:** Python

**Algorithm:** A* Search Algorithm

**Institution:** Manipal University Jaipur