import logging

import mlflow
import numpy as np
import pandas as pd
from model.evaluation import MSE, RMSE, R2Score
from sklearn.base import RegressorMixin
from typing_extensions import Annotated
from zenml import step
from zenml.client import Client
from typing import Tuple


@step()
def evaluate_model(df: pd.DataFrame) -> None:
    """"
    Evaluates the model on the ingested data.
    Args:
        df: the ingested data
    """
    pass

