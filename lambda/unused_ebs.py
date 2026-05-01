import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )['Volumes']

    for v in volumes:
        ec2.delete_volume(VolumeId=v['VolumeId'])
