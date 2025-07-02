import os
import tigris

from datasets import load_dataset
from dotenv import load_dotenv


def main():
    storage_options, fs = tigris.setup()

    bucket_name = os.getenv("BUCKET_NAME")
    assert bucket_name is not None

    dataset_name = os.getenv("DATASET_NAME")
    assert dataset_name is not None

    assert fs.exists(f"/{bucket_name}/datasets/{dataset_name}"), f"{dataset_name} does not exist in {bucket_name}, have you run import-to-tigris.py?"

    dataset = load_dataset(f"s3://{bucket_name}/datasets/{dataset_name}", storage_options=storage_options)

    # do something with the dataset

