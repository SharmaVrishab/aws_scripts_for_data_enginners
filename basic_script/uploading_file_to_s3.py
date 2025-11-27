import sys
from pathlib import Path

import boto3


def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    Args:
        file_path: Path to the file to upload
        bucket_name: Name of the S3 bucket
        object_name: S3 object name (if None, uses file name)

    Returns:
        True if successful, False otherwise
    """
    if object_name is None:
        object_name = Path(file_path).name

    try:
        s3_client = boto3.client("s3")
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(
            f"✓ Successfully uploaded {file_path} to s3://{bucket_name}/{object_name}"
        )
        return True
    except FileNotFoundError:
        print(f"✗ Error: File '{file_path}' not found")
        return False
    except Exception as e:
        print(f"✗ Error uploading file: {e}")
        return False


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python uploading_file_to_s3.py <file_path> <bucket_name> [object_name]"
        )
        print("\nExample:")
        print("  python uploading_file_to_s3.py myfile.txt my-bucket")
        print("  python uploading_file_to_s3.py myfile.txt my-bucket custom-name.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    bucket_name = sys.argv[2]
    object_name = sys.argv[3] if len(sys.argv) > 3 else None

    success = upload_file_to_s3(file_path, bucket_name, object_name)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
