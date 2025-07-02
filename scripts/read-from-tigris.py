import os
import tigris

from datasets import load_from_disk


def remove_blue(row):
    """
    You can do any filtering or transformation here. This example transformation
    removes any conversations that mention the color "blue" so you can understand
    how to do advanced filtering or processing.
    """
    assert row['conversations'] is not None
    for conv in row['conversations']:
        assert conv['value'] is not None
        if "blue" in conv['value']:
            return False # remove the row

    return True # leave the row in


def main():
    storage_options, fs = tigris.setup()

    bucket_name = os.getenv("BUCKET_NAME")
    assert bucket_name is not None

    dataset_name = os.getenv("DATASET_NAME")
    assert dataset_name is not None

    assert fs.exists(f"/{bucket_name}/datasets/{dataset_name}"), f"{dataset_name} does not exist in {bucket_name}, have you run import-to-tigris.py?"

    dataset = load_from_disk(f"s3://{bucket_name}/datasets/{dataset_name}", storage_options=storage_options)

    filtered_ds = dataset.filter(remove_blue)
    filtered_ds.save_to_disk(f"s3://{bucket_name}/no-blue/{dataset_name}", storage_options=storage_options)

    print(f"Your dataset {dataset_name} is now in Tigris at {bucket_name}/no-blue/{dataset_name} sans mentions of the colour blue")


if __name__ == "__main__":
    main()