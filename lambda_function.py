import boto3
from PIL import Image
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = "my-destination-bucket"
    
    # Download the image from the source bucket
    response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
    image_data = response['Body'].read()
    
    # Open the image with PIL
    image = Image.open(io.BytesIO(image_data))
    
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # Resize the image
    resized_image = image.resize((300, 300))  # Resize to 300x300 for example
    
    # Save the resized image to a BytesIO object
    buffer = io.BytesIO()
    resized_image.save(buffer, format="JPEG")
    buffer.seek(0)
    
    # Define the destination key
    destination_key = f"resized-{source_key}"
    
    # Upload the resized image to the destination bucket
    s3_client.put_object(Bucket=destination_bucket, Key=destination_key, Body=buffer, ContentType='image/jpeg')
    
    return {
        'statusCode': 200,
        'body': f"Image {source_key} resized and uploaded to {destination_bucket} as {destination_key}"
    }
