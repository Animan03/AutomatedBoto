import boto3

ec2 = boto3.client('ec2')


#You need to run 'aws configure' before executing this file

def ec2_creation():
    creation = ec2.run_instances( ImageId = 'ami-04a81a99f5ec58529', InstanceType = 't2.micro', MinCount = 1, MaxCount = 1, KeyName = '<specify-key-name')
    instance_id = creation['Instances'][0]['InstanceId']
    print("The Instance ID of the launched EC2 is",instance_id)

def ec2_stopping():
    instance_id = '<specify-instance-id>'
    response = ec2.stop_instances(InstanceIds=[instance_id])
    state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(instance_id," is now ",state)

def ec2_termination():
    instance_id = '<specify-instance-id>'
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    state = response['TerminatingInstances'][0]['CurrentState']['Name']
    print(instance_id," is now ",state)
