import boto3
import gzip
import json
from io import BytesIO

BUCKET_NAME = "<bucket_name>"
PREFIX = "<CloudTrail_prefix>"
REGION = "<your_region>"

s3 = boto3.client("s3", region_name=REGION)


def fetch_logs(max_files=150):  # 🔥 read more files
    logs = []

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=PREFIX
    )

    if "Contents" not in response:
        print("❌ No logs found")
        return logs

    # Sort latest first
    files = sorted(response["Contents"], key=lambda x: x["LastModified"], reverse=True)

    for obj in files[:max_files]:
        key = obj["Key"]

        if not key.endswith(".gz"):
            continue

        try:
            file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
            bytestream = BytesIO(file_obj["Body"].read())

            with gzip.GzipFile(fileobj=bytestream) as f:
                content = json.loads(f.read().decode("utf-8"))

                for record in content.get("Records", []):
                    logs.append(record)

        except Exception as e:
            print("❌ Error:", e)

    print(f"✅ Logs fetched: {len(logs)}")
    return logs