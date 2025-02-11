import logging
from typing import Tuple
from zenml import step
import pandas as pd




@step
def clean_df(data: pd.DataFrame) -> None:
    pass