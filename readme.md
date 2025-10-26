
# Customer Satisfaction Prediction Model with MLOps

## Project Description
This project implements a machine learning pipeline to predict customer satisfaction scores based on e-commerce order data. The pipeline is built using ZenML to enable reproducible and scalable MLOps workflows. The project includes data ingestion, data cleaning, model training, and model evaluation steps.

## Dataset
The dataset used is the Olist customers dataset (`data/olist_customers_dataset.csv`), which contains e-commerce order information and customer reviews.

## Project Structure
- `run_pipeline.py`: Entry point to run the training pipeline.
- `pipelines/training_pipeline.py`: Defines the ZenML pipeline with steps for ingestion, cleaning, training, and evaluation.
- `steps/`: Contains individual pipeline steps:
  - `ingest_data.py`: Data ingestion step.
  - `clean_data.py`: Data cleaning step 
  - `model_train.py`: Model training step 
  - `evaluation.py`: Model evaluation step 
- `model/`: Contains data cleaning strategies and evaluation metric implementations.
- `data/`: Contains the dataset CSV file.

## Installation
Ensure you have Python 3.7+ installed. Install the required dependencies using:

### 3. Activate Virtual Environment

**Windows:**

```bash
# Command Prompt
mlops\Scripts\activate


# PowerShell
mlops\Scripts\Activate

```bash
pip install -r requirements.txt
```

(Note: Create a `requirements.txt` file if not present, including packages like `zenml`, `pandas`, `scikit-learn`, `mlflow`, and others as needed.)

## Usage
To run the training pipeline, execute:

```bash
python run_pipeline.py
```

zenml login --local --blocking

zenml experiment-tracker register mlflow_tracker --flavor=mlflow

zenml model-deployer register mlflow --flavor=mlflow

zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set

This will run the ZenML pipeline which ingests data, cleans it, trains the model, and evaluates the model.

## Pipeline Steps
1. **Data Ingestion**: Loads the dataset from the CSV file.
2. **Data Cleaning**: Applies preprocessing such as dropping unnecessary columns and filling missing values.
3. **Model Training**: Trains a machine learning model on the cleaned data. (Implementation pending)
4. **Model Evaluation**: Evaluates the trained model using metrics like MSE, RMSE, and R2 Score. (Implementation pending)

## Dependencies
- ZenML
- pandas
- scikit-learn
- mlflow
- numpy

## License
This project is licensed under the MIT License. (Adjust as necessary)
