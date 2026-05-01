import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

TOPIC_ARN = "PASTE_YOUR_SNS_ARN"

def lambda_handler(event, context):
    instances = ec2.describe_instances()

    for r in instances['Reservations']:
        for i in r['Instances']:
            instance_id = i['InstanceId']

            ec2.stop_instances(InstanceIds=[instance_id])

            sns.publish(
                TopicArn=TOPIC_ARN,
                Message=f"Stopped EC2: {instance_id}"
            )
