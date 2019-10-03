import boto3

s3 = boto3.resource('s3')

##########################################################
print("\nList all buckets in S3:\n")
for bucket in s3.buckets.all():
    print(bucket.name)

##########################################################
print("\nSave file to S3:\n")
home = '/tmp/'
file = 'test.txt'
bucket = 'hdp-hive-s3'

data = open(home + file, 'rb')
s3.Bucket(bucket).put_object(Key = file, Body = data)

##########################################################

print("\nMessaging Queue with SQS:\n")
# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

print("\nList all queues in SQS:\n")
for queue in sqs.queues.all():
    print(queue.url)