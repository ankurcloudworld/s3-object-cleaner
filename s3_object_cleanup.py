import boto3
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    # Replace with your S3 bucket name and region
    bucket_name = 'mys3bucket'
    region_name = 'us-east-1'

    # Initialize the S3 client
    s3 = boto3.client('s3', region_name=region_name)

    # Calculate the date 90 days ago from the current date (offset-aware)
    deletion_threshold_date = datetime.now(timezone.utc) - timedelta(days=90)

    # List objects in the S3 bucket
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix='db-backup')

    if 'Contents' in objects:
        for obj in objects['Contents']:
            # Get the last modified date of the object (offset-aware)
            last_modified = obj['LastModified'].replace(tzinfo=timezone.utc)

            # If the object is older than the threshold, delete it
            if last_modified <= deletion_threshold_date:
                object_key = obj['Key']
                s3.delete_object(Bucket=bucket_name, Key=object_key)
                print(f"Deleted: {object_key} (Age: {deletion_threshold_date - last_modified})")

    return {
        'statusCode': 200,
        'body': 'Objects older than 90 days have been removed.'
    }
