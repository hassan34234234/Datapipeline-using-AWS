import boto3

# Replace with your AWS credentials and bucket info
BUCKET_NAME = "my-unique-bucket-2024-07-15"
FILE_NAME = "Superstore.csv"  # Replace with your actual file name
FILE_PATH = "C:/Users/HASSAN/Downloads/Data Engineering Project/Data-Engineering-Project/Python script/Superstore.csv"  # Replace with your actual path

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file
try:
  s3.upload_file(FILE_PATH, BUCKET_NAME, FILE_NAME)
  print(f"Successfully uploaded {FILE_NAME} to S3 bucket {BUCKET_NAME}")
except Exception as e:
  print(f"Error uploading file: {e}")
