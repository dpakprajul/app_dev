# Geospatial Data Visualization Web App

## Overview

This GitHub repository hosts a Django web application that provides a robust platform for retrieving, visualizing, and interacting with geospatial data sourced from a Web Feature Service (WFS). By leveraging the Leaflet JavaScript library, this application offers an engaging and interactive map interface for exploring geospatial datasets.

## Key Components

### `get_wfs_data` View

- **Function**: `get_wfs_data(request)`
- **Purpose**: This Django view interacts with a specified WFS service, retrieves geospatial data, and formats it as a JSON response. The function is responsible for data retrieval.

### `map_page` View

- **Function**: `map_page(request)`
- **Purpose**: This Django view orchestrates the application's functionality by invoking `get_wfs_data` to fetch geospatial data. The data is then passed to the 'map.html' template for rendering.

### `map.html` Template

- **Purpose**: 'map.html' is an HTML template that structures the web page and incorporates JavaScript code to create an interactive map. Key features include the inclusion of Leaflet JavaScript and CSS files, initialization of the Leaflet map, AJAX data retrieval, and dynamic rendering of GeoJSON data on the map.

### JavaScript Integration

- **Purpose**: JavaScript plays a pivotal role in this codebase. It handles asynchronous data retrieval, map creation and customization, popup functionality for feature interaction, and automatic map zoom and center adjustments to fit the data's boundaries.

## Getting Started

To run this web application locally, follow these steps:

1. Clone the repository to your local machine.
2. Set up a Python environment and install the required dependencies (Django, Leaflet, etc.).
3. Configure the Django settings and database as needed.
4. Run the Django development server.
5. Access the application in your web browser and explore the geospatial data.

## Usage

This application is designed to make it easy to interact with geospatial data from WFS services. Use it to visualize and explore various datasets with a user-friendly map interface.

## Contributions

Contributions to this repository are welcome. Feel free to open issues, submit pull requests, or provide feedback to enhance the application's capabilities.

## License

This project is licensed under the [MIT License](LICENSE), allowing for both personal and commercial use.

---

You can use this template to create the README for your GitHub repository. Modify it as needed to suit your specific project details and preferences.

![image](https://user-images.githubusercontent.com/38970123/229232549-e825247c-ae90-4c5f-86a1-0042229a0b9d.png)
