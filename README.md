# Pandas Dataset Demo

This project demonstrates how to handle large datasets in Python using the `pandas` library. It specifically focuses on techniques for reading, processing, and aggregating large datasets in an efficient way. For this demo, we use the [Full HBO Max Dataset from Kaggle](https://www.kaggle.com/datasets) to showcase practical data handling methods.

## Project Overview

The main goal of this project is to show how to:
- Read large datasets in chunks, reducing memory usage.
- Aggregate and summarize data by grouping on specific columns.
- Randomize and sample data for analysis and display purposes.

## Features

- **Chunk Processing**: The dataset is read in chunks of 100 rows to handle memory constraints when working with large data.
- **Data Aggregation**: For each chunk, we aggregate data by grouping by `title` and `genres` to count occurrences.
- **Random Sampling**: The final output is randomized, allowing us to see a varied sample of entries.

## Data

The dataset used for this project is the HBO Max Dataset from Kaggle, which includes information about HBO Max's content catalog, such as titles, genres, release years, ratings, and more.

**Columns Used in This Project**:
- `title`
- `genres`

Additional columns are available in the dataset but are not used in this demo.

## Installation

To run this project, you’ll need Python and `pandas`. Install dependencies with:

```bash
pip install pandas

## Usage

1. Clone this repository and navigate to the project directory.
2. Place the `data.csv` file (HBO Max Dataset) in the project folder.
3. Run the Python script:

   ```bash
   python main.py

## Example Output

                                       count
title           genres
#BringBackAlice Crime, Drama, Mystery      1
#FBF            Drama, Family              1
#FameTime       Comedy, Romance            1
#Luimelia       Drama, Romance, Short      1

