import boto3
session = boto3.Session(profile_name="mfa")
s3 = session.client('s3')
response = s3.list_buckets()
print(response['Buckets'])
#s3 = session.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)
