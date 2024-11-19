# Pandas Dataset Demo

This project demonstrates how to handle large datasets in Python using the `pandas` library. It specifically focuses on techniques for reading, processing, and aggregating large datasets in an efficient way. For this demo, we use the [Full HBO Max Dataset from Kaggle](https://www.kaggle.com/datasets) to showcase practical data handling methods.

## Project Overview

The main objectives of this project are to:
- Efficiently process large datasets using chunking.
- Perform data aggregation and summarization using `pandas`.
- Visualize the results to provide insights into the dataset.

## Features

- **Chunk Processing**: Handles large datasets by processing data in chunks, reducing memory usage.
- **Data Aggregation**: Groups data by `title` and `genres` to count occurrences and identify trends.
- **Visualizations**:
  - Bar chart showing the top 5 most common genres.
  - Pie chart illustrating genre distribution.
- **Database Storage**: Saves the aggregated results to a SQLite database for persistence.

## Data

The dataset used for this project is the HBO Max Dataset from Kaggle, which includes details about HBO Max's content catalog, such as:
- Titles
- Genres
- Release years
- Ratings

**Columns Used in This Project**:
- `title`
- `genres`

Additional columns are available but are not utilized in this demo.

## Usage

1. Clone this repository and navigate to the project directory.
2. Place the `data.csv` file (HBO Max Dataset) in the project folder.
3. Run the Python script:

   ```bash
   python main.py
## Installation

To run this project, you’ll need Python and `pandas`. Install dependencies with:

```bash
pip install pandas
```

## Example Output
```bash
title           genres                    count
#BringBackAlice Crime, Drama, Mystery      1
#FBF            Drama, Family              1
#FameTime       Comedy, Romance            1
#Luimelia       Drama, Romance, Short      1