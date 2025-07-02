import os
import s3fs

from dotenv import load_dotenv
from typing import Dict, Tuple


def setup() -> Tuple[Dict[str, str], s3fs.S3FileSystem]:
    # Load secrets from .env
    load_dotenv()

    # Populate storage options for huggingface datasets and s3fs
    storage_options = {
        "key": os.getenv("AWS_ACCESS_KEY_ID"),
        "secret": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "endpoint_url": os.getenv("AWS_ENDPOINT_URL_S3"),
    }

    # Ensure all environment variables are set
    errs = []
    for k, v in storage_options.items():
        if v is None:
            errs.append(f"{k} is not set, got {v} but wanted something")

    # If any keys are None, throw an error message and stop the program
    assert len(errs) == 0, f"validation errors in config: \n{errs}"

    # Create the S3 filesystem for other parts of the stack to use
    fs = s3fs.S3FileSystem(**storage_options)

    # Ensure that BUCKET_NAME is set
    bucket_name = os.getenv("BUCKET_NAME")
    assert bucket_name is not None

    # Ensure we have write access to the bucket
    fs.write_text(f"/{bucket_name}/test.txt", "this is a test")
    fs.rm(f"/{bucket_name}/test.txt")

    return (storage_options, fs)
