#!/usr/bin/env python3
"""
AWS S3 Bucket Creation Script

Prerequisites:
- Install boto3: pip install boto3
- Configure AWS credentials using 'aws configure' or set environment variables:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - AWS_DEFAULT_REGION (optional)
"""

import boto3
import sys
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region

    Args:
        bucket_name (str): Name of the bucket to create
        region (str): AWS region to create bucket in (e.g., 'us-east-1', 'eu-west-1')

    Returns:
        bool: True if bucket created successfully, False otherwise
    """
    try:
        # Create S3 client
        s3_client = boto3.client('s3', region_name=region)

        # Create bucket
        if region is None or region == 'us-east-1':
            # us-east-1 doesn't need LocationConstraint
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # Other regions need LocationConstraint
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )

        print(f"✓ Bucket '{bucket_name}' created successfully in region '{region or 'us-east-1'}'")
        return True

    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'BucketAlreadyExists':
            print(f"✗ Bucket name '{bucket_name}' is already taken globally")
        elif error_code == 'BucketAlreadyOwnedByYou':
            print(f"✓ Bucket '{bucket_name}' already exists and is owned by you")
        else:
            print(f"✗ Error creating bucket: {e}")

        return False

    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def main():
    """Main function to handle command-line usage"""

    # Get bucket name from command line or prompt
    if len(sys.argv) > 1:
        bucket_name = sys.argv[1]
    else:
        bucket_name = input("Enter bucket name: ").strip()

    # Get region (optional)
    if len(sys.argv) > 2:
        region = sys.argv[2]
    else:
        region = input("Enter AWS region (press Enter for us-east-1): ").strip() or None

    # Validate bucket name
    if not bucket_name:
        print("✗ Bucket name cannot be empty")
        sys.exit(1)

    # Create the bucket
    success = create_s3_bucket(bucket_name, region)

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
