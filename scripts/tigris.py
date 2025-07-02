import os
import s3fs

from dotenv import load_dotenv
from typing import Dict, Tuple


def setup() -> Tuple[Dict[str, str], s3fs.S3FileSystem]:
    pass

    load_dotenv()

    storage_options = {
        "key": os.getenv("AWS_ACCESS_KEY_ID"),
        "secret": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "endpoint_url": os.getenv("AWS_ENDPOINT_URL_S3"),
    }

    errs = []
    for k, v in storage_options.items():
        if v is None:
            errs.append(f"{k} is not set, got {v} but wanted something")

    assert len(errs) == 0, f"validation errors in config: \n{errs}"

    fs = s3fs.S3FileSystem(**storage_options)

    return (storage_options, fs)
