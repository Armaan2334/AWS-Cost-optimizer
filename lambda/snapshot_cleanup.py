import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    threshold = datetime.utcnow() - timedelta(days=30)

    for snap in snapshots:
        if snap['StartTime'].replace(tzinfo=None) < threshold:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
