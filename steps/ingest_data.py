import logging
import pandas as pd
from zenml import step

class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self, data_path: str) -> None:
        """Initialize the data ingestion class with a data path."""
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
        logging.info("Ingesting data from %s", self.data_path)
        df = pd.read_csv(self.data_path)
        return df


@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingest data from a given file path.

    Args:
        data_path (str): Path to the CSV file.

    Returns:
        df (pd.DataFrame): Dataframe containing ingested data.
    """
    try:
        ingest_data_instance = IngestData(data_path)
        df = ingest_data_instance.get_data()
        return df
    except Exception as e:
        logging.error("Error ingesting data: %s", str(e))
        raise e
