import boto3
from datetime import date

ce = boto3.client('ce')
s3 = boto3.client('s3')

BUCKET = "aws-cost-reports-arman"

def lambda_handler(event, context):
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': '2024-01-01',
            'End': '2024-01-31'
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    cost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']

    s3.put_object(
        Bucket=BUCKET,
        Key='report.txt',
        Body=f"Monthly Cost: ${cost}"
    )
