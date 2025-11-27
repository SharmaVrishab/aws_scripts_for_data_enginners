"""
list_buckets.py
Lists all S3 buckets in your AWS account with their creation dates.
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError


def list_s3_buckets():
    """
    Lists all S3 buckets in the AWS account.

    Returns:
        list: List of bucket dictionaries containing name and creation date
    """
    try:
        # Create S3 client
        s3_client = boto3.client("s3")

        # List all buckets
        response = s3_client.list_buckets()

        # Extract bucket information
        buckets = response.get("Buckets", [])

        if not buckets:
            print("No S3 buckets found in your account.")
            return []

        print(f"\n{'=' * 70}")
        print(f"Found {len(buckets)} S3 bucket(s) in your account:")
        print(f"{'=' * 70}\n")

        # Display bucket information
        for idx, bucket in enumerate(buckets, 1):
            bucket_name = bucket["Name"]
            creation_date = bucket["CreationDate"]

            # Format the creation date
            formatted_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

            print(f"{idx}. Bucket Name: {bucket_name}")
            print(f"   Created On: {formatted_date}")
            print(f"   Region: {get_bucket_region(s3_client, bucket_name)}")
            print("-" * 70)

        return buckets

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
        print("Please configure your credentials using 'aws configure'")
        return []

    except ClientError as e:
        print(f"Error accessing S3: {e}")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def get_bucket_region(s3_client, bucket_name):
    """
    Get the region of a specific S3 bucket.

    Args:
        s3_client: Boto3 S3 client
        bucket_name: Name of the bucket

    Returns:
        str: Region name or 'Unknown' if unable to determine
    """
    try:
        response = s3_client.get_bucket_location(Bucket=bucket_name)
        region = response.get("LocationConstraint")

        # us-east-1 returns None as LocationConstraint
        if region is None:
            return "us-east-1"

        return region

    except ClientError:
        return "Unknown"


def get_bucket_details(bucket_name):
    """
    Get detailed information about a specific bucket.

    Args:
        bucket_name: Name of the bucket to inspect
    """
    try:
        s3_client = boto3.client("s3")

        print(f"\nDetails for bucket: {bucket_name}")
        print("=" * 70)

        # Get bucket region
        region = get_bucket_region(s3_client, bucket_name)
        print(f"Region: {region}")

        # Get bucket versioning status
        try:
            versioning = s3_client.get_bucket_versioning(Bucket=bucket_name)
            status = versioning.get("Status", "Disabled")
            print(f"Versioning: {status}")
        except ClientError:
            print("Versioning: Unable to retrieve")

        # Count objects in bucket (limited to first 1000)
        try:
            objects = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=1000)
            object_count = objects.get("KeyCount", 0)
            print(f"Object Count (first 1000): {object_count}")
        except ClientError:
            print("Object Count: Unable to retrieve")

        print("=" * 70)

    except Exception as e:
        print(f"Error getting bucket details: {e}")


if __name__ == "__main__":
    print("AWS S3 Bucket Lister")
    print("=" * 70)

    # List all buckets
    buckets = list_s3_buckets()

    # Optional: Get details for a specific bucket
    if buckets:
        print("\n" + "=" * 70)
        choice = input(
            "\nEnter bucket name for details (or press Enter to skip): "
        ).strip()

        if choice:
            get_bucket_details(choice)
