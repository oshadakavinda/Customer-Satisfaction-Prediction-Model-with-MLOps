import logging

import mlflow
import pandas as pd


from sklearn.base import RegressorMixin
from zenml import step
from zenml.client import Client



@step 
def train_model(df: pd.DataFrame) -> None:
    """
    Trains the model on the ingested data
    Args:
        df: the ingested data
    """
    pass

