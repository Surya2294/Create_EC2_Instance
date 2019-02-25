import boto3
ec2 = boto3.resource("ec2")
instance = ec2.create_instance(
    ImageId = "AWS-AMI ID"            # AWS_AMI_ID
    MinCount=1,                      # minimum no. of instances
    MaxCount=1,                      # maximum no. of instances
    InstanceType= "t2.micro"
)
print(instance[0].id)

"""
# for terminate or stop the instance

instance_id = "EC2_ ID"
instance=ec2.instance(instance_id)
response=instance.terminate()
print(response)

"""