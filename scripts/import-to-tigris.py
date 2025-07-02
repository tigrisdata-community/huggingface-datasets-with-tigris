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

    assert not fs.exists(f"/{bucket_name}/dataset/{dataset_name}"), f"{dataset_name} is already present in {bucket_name}"

    dataset = load_dataset(dataset_name, split="train")
    dataset.save_to_disk(f"s3://{bucket_name}/dataset/{dataset_name}", storage_options=storage_options)


if __name__ == "__main__":
    main()
