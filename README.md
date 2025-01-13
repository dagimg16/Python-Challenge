# Python-Challenge

## Project Description

This repository contains two distinct Python projects: **PyBank** and **PyPoll**. The repository is organized into two main folders:

- `PyBank`
- `PyPoll`

### Folder Structure

Each folder (`PyBank` and `PyPoll`) contains the following:

- **main.py**: The main script for each analysis. This file contains the logic to perform the analysis for the respective project (PyBank or PyPoll).
  
- **Resources** folder: This folder contains the dataset CSV files used in the analysis:
  - `budget_data.csv` for **PyBank**
  - `election_data.csv` for **PyPoll**

- **Analysis** folder: This folder contains the results of the analysis saved in a text file (e.g., `analysis_results.txt`), summarizing the outcome of the respective project.

Each project is designed to analyze financial or election data, and the folder structure is organized to keep all related files together for clarity and easy access.

### PyBank
In the **PyBank** project, the task is to create a Python script to analyze financial records from a dataset called `budget_data.csv`. The dataset consists of two columns: **Date** and **Profit/Losses**. The goal of this project is to:

- Calculate the total number of months included in the dataset.
- Compute the net total amount of **Profit/Losses** over the entire period.
- Calculate the changes in **Profit/Losses** over the entire period, and determine the average change.
- Identify the greatest increase in profits (date and amount) over the entire period.
- Identify the greatest decrease in profits (date and amount) over the entire period.

### PyPoll
The **PyPoll** project focuses on modernizing the vote-counting process for a small, rural town. In this project, the dataset provided is called `election_data.csv` and consists of three columns: **Voter ID**, **County**, and **Candidate**. The objectives for this project are to:

- Calculate the total number of votes cast.
- List all candidates who received votes.
- Calculate the percentage of votes each candidate won.
- Determine the total number of votes each candidate received.
- Identify the winner of the election based on the popular vote.
  
## What You Need

To run the **PyBank** and **PyPoll** projects, you will need the following:

- **Python**: Ensure that Python 3.x is installed on your system. You can download Python from [here](https://www.python.org/downloads/).
- **pip**: Python's package installer (usually installed with Python).

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/dagimg16/Python-Challenge.git
   ```
2. In the terminal, navigate to the folder containing the respective Python script:
  - PyBank: PyBank_main.py
  - PyPoll: PyPoll_main.py
    
3. Run the Python script for each project:
   - For **PyBank**:
     ```bash
     python PyBank/PyBank_main.py
     ```

   - For **PyPoll**:
     ```bash
     python PyPoll/PyPoll_main.py
     ```
## Acknowledgments
- Thanks to SMU and my instructors for guiding me through this learning journey!
- And a big thank you to everyone checking out this project.

## License
Feel free to use and modify this script for your own learning.
