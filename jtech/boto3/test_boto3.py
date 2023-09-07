"""
boto3 is a python package that aws has provided to interact with AWS services

"""
# import os
# access_key = os.getenv("ACCESS_KEY")
# shared_secret = os.getenv("SHARED_SECRET")
# s3_client = boto3.client('s3',access_key,shared_secret)
# print(a)


import boto3

# create a s3 client
s3_client = boto3.client('s3')

# list buckets
# response = s3_client.list_buckets()
# for item in response['Buckets']:
#     print(item['Name'])


# create buckets -- not recommended to create resources using boto3 but we will explore the option

# def create_bucket(bucket_name,region='us-west-2'):
#     try:
#         s3_client = boto3.client('s3')
#         location = {'LocationConstraint': region}
#         s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
#         return True
#     except Exception as e:
#         print(f"Error occured while bucket creating : {e}")
#         return False


# response = create_bucket('ashish-test-2020')
# print(response)

# print("Hi")
# uploading file to bucket - you have a file and you want to upload to s3





# generating some data in our code and we want to write that data to s3 - uploading object


A = s3_client.list_buckets()
print(A)
print(type(A))






