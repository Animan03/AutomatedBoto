import boto3
import os 

AWS_REGION = "ap-south-1"
resource = boto3.resource("s3", region_name = AWS_REGION)

def s3_creation():
    bucket_name = "task-trial-bucket"
    location = {'LocationConstraint' : AWS_REGION}
    bucket = resource.create_bucket( Bucket = bucket_name, CreateBucketConfiguration = location)
    print("The S3 bucket has been created")

def s3_list_buckets():
    iterator = resource.buckets.all()
    print("The S3 buckets present right now are:")
    for i in iterator:
        print(i)

def s3_delete_buckets():
    bucket_name = "task-trial-bucket"
    s3_bucket = resource.Bucket(bucket_name)
    s3_bucket.delete()
    print("The S3 bucket has been deleted")

def s3_uploading_file(file_name, bucket, object_name = None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    print("The file is done uploading")

def s3_list_files():
    s3_bucket = resource.Bucket("task-trial-bucket")
    print("The files present in the bucket are-")
    for i in s3_bucket.objects.all():
        print(i)

def s3_download_file():
    #for downloading objects present in the bucket
    s3_object = resource.Object("task-trial-bucket",'<object-name>')
    s3_object.download_file('<Location-to-be-downloaded>/<file-name>')
    print('Download completed')