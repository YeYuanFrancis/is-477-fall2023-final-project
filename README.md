# is-477-fall2023-final-project
# Workflow
![Workflow Diagram](image.png)
## Reproducing
Here are instructions for you to set up your enviroment and run the script

### Prerequisites

Ensure you have Python 3.x installed on your machine.
If you decide to use Docker:
Install Docker Desktop on your machine.
Create a Docker Hub account if you don't already have one.

### 1. Clone the Repository
First, clone the repository to your local machine:
git clone https://github.com/YeYuanFrancis/is-477-fall2023-final-project.git
cd is-477-fall2023-final-project

### 2. Set Up the Environment
Create and activate a virtual environment, and install the required dependencies:

Create a virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

Create a virtual environment (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

### 3. Download and Prepare the Data
Run the prepare_data.py script to download and prepare the dataset:

python scripts/prepare_data.py
This script will download the dataset and perform initial preprocessing steps, saving the processed data in the data directory.

### 4. Generate the Data Profiling Report
To generate a profiling report of the dataset, run:

python scripts/profile.py
This will create a detailed data profiling report and save it as profiling/report.html.

### 5. Conduct the Analysis
Execute the analysis script to perform the data analysis:

python scripts/analysis.py
This will run the analysis defined in analysis.py and save the results in the results directory.

### 6. Run the Complete Workflow with Snakemake
Alternatively, you can run the entire workflow using Snakemake:

snakemake --cores 1
This command will execute the entire workflow, from data preparation to analysis, as defined in the Snakefile.
