This AWS Lambda function automatically deletes objects from an S3 bucket that are older than 7 days. The function scans the specified bucket, checks the last modified date of each object, and removes any object that exceeds the 7-day threshold.

## Features
- **Automated cleanup**: The function runs to keep your S3 bucket clean by deleting objects that are older than 90 days.
- **Timezone-aware**: The function correctly handles timezones using `timezone.utc` to avoid issues with time comparisons.

## Prerequisites

1. **AWS Lambda**: Ensure that this function is deployed in AWS Lambda.
2. **IAM Role**: The Lambda function should have the necessary permissions to interact with S3. Attach a role with `s3:ListBucket` and `s3:DeleteObject` permissions.

## Deployment Instructions

1. **Create the Lambda function** in the AWS Management Console or via the AWS CLI.
2. **Configure the Lambda function** with the following environment variables:
   - `bucket_name`: The name of your S3 bucket.
   - `region_name`: The AWS region where the S3 bucket is located.
3. **Attach the IAM Role** with the necessary S3 permissions to the Lambda function.

## Function Logic

The Lambda function does the following:

1. Initializes an S3 client using the provided `region_name`.
2. Lists all objects in the specified S3 bucket with the prefix `db-backup`.
3. Iterates through each object and checks if the object is older than 7 days using the `LastModified` property.
4. Deletes objects that are older than given threshold days.
