import boto3
from botocore.exceptions import ClientError
import click

class ec2:

    resource = boto3.resource('ec2')
    client = boto3.client('ec2')

    def __init__(self, state):
        self.state = state

    def launch_ec2(self, dry_run=True):
        try:
            instances = self.resource.create_instances(
                DryRun=eval(dry_run),
                ImageId='ami-9887c6e7',
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='mykeypair',
                SubnetId='subnet-9bce3afc',
                SecurityGroupIds=['sg-083680c77ab4f3823'],
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'boto3-instance'
                            }
                        ]
                    }
                ]
            )
            #print(instances)
            return instances[0].instance_id
        except ClientError as e:
            print("ClientError:" + str(e))
            return ""
    
    def stop_ec2(self, instance_id):
        try:
            print(self.client.stop_instances(InstanceIds=instance_id))
        except ClientError as e:
            print("ClientError:" + str(e))

    def start_ec2(self, instance_id):
        try:
            print(self.client.start_instances(InstanceIds=instance_id))
        except ClientError as e:
            print("ClientError:" + str(e))

    def reboot_ec2(self, instance_id):
        try:
            print(self.client.reboot_instances(InstanceIds=instance_id))
        except ClientError as e:
            print("ClientError:" + str(e))

    def terminate_ec2(self, instance_id):
        try:
            print(self.client.terminate_instances(InstanceIds=instance_id))
        except ClientError as e:
            print("ClientError:" + str(e))

@click.command()
@click.option("--state", "-s", help='Instance State. Alternatives: Launch|Start|Stop|Reboot|Terminate')
@click.option("--instance_id", "-i", default = '', help='Instance Id. Ignore for Launch option.')
@click.option("--dry_run", "-i", default = True, help='Dry run or not.')

def handle_ec2(state, instance_id, dry_run):
    e = ec2(state=state)
    if state == 'Launch':
        instance_id = e.launch_ec2(dry_run=dry_run)
        print(instance_id)
    elif state == 'Stop':
        e.stop_ec2([instance_id])
    elif state == 'Start':
        e.start_ec2([instance_id])
    elif state == 'Reboot':
        e.reboot_ec2([instance_id])
    elif state == 'Terminate':
        e.terminate_ec2([instance_id])
    else:
        print("ERROR: Wrong instance state: {}".format(state))

if __name__ == '__main__':
    handle_ec2()