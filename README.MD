# S3 Image Resizer Lambda Function

This project demonstrates how to automatically resize images uploaded to an S3 bucket using an AWS Lambda function and save the resized images in a different S3 bucket.

## Prerequisites

- AWS Account
- S3 Buckets (Source and Destination)
- AWS Lambda

## Setup

### Step 1: Set Up the S3 Buckets

1. Create two S3 buckets in the AWS Management Console:
    - Source bucket: `my-source-bucket`
    - Destination bucket: `my-destination-bucket`

### Step 2: Create the Lambda Function

1. Go to the AWS Lambda Console.
2. Create a new function and choose "Author from scratch".
3. Provide a name (e.g., `ImageResizer`).
4. Set the runtime to Python 3.x.

### Step 3: Set Up Permissions

1. Attach a policy to the Lambda function's execution role to allow read/write access to the S3 buckets. The policy can look like this:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:PutObject"
          ],
          "Resource": [
            "arn:aws:s3:::my-source-bucket/*",
            "arn:aws:s3:::my-destination-bucket/*"
          ]
        }
      ]
    }
    ```

### Step 4: Configure S3 Event Notification

1. Go to the S3 Management Console.
2. Navigate to the source bucket and set up an event notification to trigger the Lambda function on object creation events.

### Step 5: Install the `Pillow` Library Using a Lambda Layer

1. **Create a `Pillow` package**:
    - Create a directory for the package:
      ```sh
      mkdir python
      cd python
      ```
    - Install `Pillow` into this directory:
      ```sh
      pip install Pillow -t .
      ```

2. **Create a Lambda Layer**:
    - Zip the directory:
      ```sh
      zip -r9 ../pillow_layer.zip .
      cd ..
      ```
    - Go to the AWS Lambda Console and navigate to the "Layers" section.
    - Create a new layer, upload the `pillow_layer.zip` file, and choose the appropriate runtime (e.g., Python 3.x).

3. **Attach the Layer to Your Lambda Function**:
    - In the AWS Lambda Console, navigate to your `ImageResizer` function.
    - In the "Layers" section of your function, click "Add a layer".
    - Select "Custom layers" and choose the `Pillow` layer you created.

### Step 6: Upload Your Code

1. Copy the code from the Python file `lambda_function.py`.

2. In the AWS Lambda Console:
    - Navigate to your `ImageResizer` function.
    - In the "Code" tab, select "Edit code inline".
    - Paste the copied code into the inline editor.
    - Change the destination bucket name if you are using you own naming.
    - Click "Deploy" to save and deploy the changes.

### Step 7: Deploy and Test the Lambda Function

1. Deploy the Lambda function.
2. Test it by uploading an image to the source bucket and verifying that a resized image appears in the destination bucket.

## Additional Considerations

- **Error Handling**: Implement error handling to manage potential issues like missing files, permission errors, and invalid image formats.
- **Logging**: Add logging to help with debugging and monitoring.

## Conclusion

This setup will automatically resize images uploaded to the source S3 bucket and store the resized versions in the destination S3 bucket using AWS Lambda.
