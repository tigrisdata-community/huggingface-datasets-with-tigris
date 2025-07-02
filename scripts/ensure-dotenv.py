import os

from dotenv import load_dotenv


load_dotenv()

dotenv_errs = []
for key in [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_ENDPOINT_URL_S3",
    "AWS_ENDPOINT_URL_IAM",
    "AWS_REGION",
    "BUCKET_NAME",
    "DATASET_NAME",
]:
    assert os.getenv(key) is not None, f"Environment variable {key} is not defined, please define it in .env"

print("Your .env file is good to go!")