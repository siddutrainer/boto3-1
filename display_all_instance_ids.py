import boto3

client = boto3.client('ec2')

instances = client.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        print("Id is {} and Type is {} ".format(instance_id, instance_type))

