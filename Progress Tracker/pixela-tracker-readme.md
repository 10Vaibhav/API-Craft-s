# Pixela Progress Tracker

A Python application for tracking and visualizing progress using the Pixela API. This tool allows you to create and manage a pixel-based visualization graph where each pixel represents a quantitative measurement of your progress (e.g., number of commits, hours worked, tasks completed).

## Features

- Create a Pixela user account
- Create custom graphs
- Add daily progress pixels
- Update existing pixels
- Delete pixels
- Interactive command-line interface

## Configuration

Before using the application, you need to set up your Pixela credentials:

1. Sign up for a Pixela account at [https://pixe.la/](https://pixe.la/)
2. Open `main.py`
3. Fill in your credentials:
```python
self.TOKEN = ""  # Your Pixela user token
self.USERNAME = ""  # Your Pixela username
```

The interactive menu provides the following options:

1. **Create New User**: Set up a new Pixela account
2. **Create New Graph**: Create a new progress tracking graph
3. **Add Pixel**: Add a new progress entry
   - Option to use current date or specify a date
   - Enter quantity for the progress
4. **Update Pixel**: Modify an existing entry
5. **Delete Pixel**: Remove an entry
6. **Exit**: Close the application

## Graph Configuration

The default graph is configured with the following settings:
- ID: "progresstracker"
- Name: "Progress Graph"
- Unit: "commit"
- Type: "int"
- Color: "ajisai" (purple)

You can modify these settings in the `create_graph` method of the `PixelaTracker` class.

## Date Format

When entering dates manually, use the format: YYYYMMDD
Example: 20241221 (for December 21, 2024)

## Error Handling

The application will display the API response for each operation, including any error messages from the Pixela service.

## Documentation and References

- [Pixela Homepage](https://pixe.la/) - The official Pixela website
- [Pixela API Documentation](https://docs.pixe.la/) - Complete API documentation and guides
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/api/) - Python Requests library API reference

## Acknowledgments

- [Pixela API](https://pixe.la/) for providing the visualization service
- Built using Python's `requests` library
