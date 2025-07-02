# huggingface-datasets-with-tigris

A quick getting started guide to using Huggingface datasets stored in Tigris

To get started locally you need:

1. A [Tigris account](https://storage.new/)
2. An [access keypair](https://storage.new/accesskey)
3. A computer running Python 3.10 (or later) that has internet access (OS and CPU architecture does not matter)
4. A tigris bucket
5. [uv](https://docs.astral.sh/uv/) or another python dependency manager installed

If you us [VS Code](https://code.visualstudio.com/) and have the [Development Containers](https://code.visualstudio.com/docs/devcontainers/containers) extension installed, clone this repository to your machine and run the command `Dev Containers: Reopen in Container`. This will automatically set up all of the dependencies you need to get started.

If you are doing this manually, install the requisite Python version:

```text
uv python install 3.10 # or however you manage python
uv venv # or however you create virtual environments
uv sync # or pip3 install -r requirements.txt
```

Copy `.env.example` to `.env` and customize the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` variables. For example, if your access key is `tid_NotKbzPHpJuoX` and your secret access key is `tsec_r++Q9iocfdf7Th`:

```patch
 ## Tigris configuration

 # Change these based on the access key you got from the web console
-AWS_ACCESS_KEY_ID=tid_access_key_id
-AWS_SECRET_ACCESS_KEY=tsec_secret_access_key
+AWS_ACCESS_KEY_ID=tid_NotKbzPHpJuoX
+AWS_SECRET_ACCESS_KEY=tsec_r++Q9iocfdf7Th
```

Make sure to change your bucket and dataset name:

```patch
 ## Dataset and bucket
 # Bucket name to store data and models in
-BUCKET_NAME=xe-datasets-demo
+BUCKET_NAME=your-bucket-name-here

 # Dataset to copy over
 DATASET_NAME=mlabonne/FineTome-100k
```

Then make sure you have everything configured with `scripts/ensure-dotenv.py`:

```text
uv run scripts/ensure-dotenv.py # or however you run python scripts in your venv
```

Import the dataset to Tigris with `scripts/import-to-tigris.py`:

```text
uv run scripts/import-to-tigris.py
```

You can read it back and do a transformation with `scripts/read-from-tigris.py`. This example script removes any conversations mentioning the color blue.

```text
uv run scripts/read-from-tigris.py
```

