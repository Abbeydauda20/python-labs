"""
boto3 is a python package that aws has provided to interact with AWS services

"""
# import os
# access_key = os.getenv("ACCESS_KEY")
# shared_secret = os.getenv("SHARED_SECRET")
# s3_client = boto3.client('s3',access_key,shared_secret)
# print(a)
import json

import boto3

# # create a s3 client
# s3_client = boto3.client('s3')

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


# uploading file to bucket - you have a file and you want to upload to s3

# create a s3 client
# s3_client = boto3.client('s3')
#
# bucket = 'ashish-test-2023'
# key = 'folder3/folder33/folder333/test.json'
# with open('data.json','rb') as file:
#     s3_client.upload_fileobj(file,bucket,key)


# generating some data in our code and we want to write that data to s3 - uploading object

# 1st method
# create a s3 client
# s3_client = boto3.client('s3')
# bucket = 'ashish-test-2023'
# key = 'user.json'
# mydata = {'id': 123, 'firstname': 'John', 'lastname': 'Smith', 'age': 32}
# mydata_json = json.dumps(mydata)  # this converts a dict to json/str
# # print(mydata) # dict
# # print(mydata_json) # converts dict to json
# # print(json.loads(mydata_json)) # converts the json back to a dict
# s3_client.put_object(Body=bytes(mydata_json.encode('UTF-8')), Bucket=bucket, Key=key)


#2nd method -- first write to a file then upload the file
# s3_client = boto3.client('s3')
# bucket = 'ashish-test-2023'
# key = 'user.json'
# mydata = {'id': 123, 'firstname': 'John', 'lastname': 'Smith', 'age': 32}
# with open('user.json','w') as f:
#     f.write(json.dumps(mydata))
# with open('user.json','rb') as file:
#     s3_client.upload_fileobj(file,bucket,key)


# Reading data from s3
# s3_client = boto3.client('s3')
# bucket = 'ashish-test-2023'
# key = 'data.json'
#
# response = s3_client.get_object(Bucket=bucket, Key=key)
# response_body = response['Body']
# response_dict = json.loads(response_body.read())
#
# transactions = response_dict['transactions']
# for record in transactions:
#     # print(record)
#     print(f"Transaction Type : {record['transactionType']}  |  Amount : {record['amount']}")







