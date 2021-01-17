# README

* About the App

This is a program for processing images, hosted on AWS Elastic Beanstalk and includes a Lambda Function that resizes an image, triggered with a picture upload in an S3 bucket. I used the EB CLI and AWS CLI to implement all of these services on the cloud.


* Running the Photo Processing Program

Clone this repository

Activate the virtual environment:

`cd aws-image-processing`

`python -m pip install virtualenv`

`virtualenv venv -p python`

`cd venv`

`.\Scripts\activate`

Now that the virtual environment is activated:

`cd ..`

`cd imagepro`

`pip install django`\
`pip install Pillow`

`python manage.py runserver`

Once server is running go to `http://127.0.0.1:8000/` and upload your photos.

Use `deactivate` to deactivate the virtual environment. 

# AWS Lambda resize function project with Node.js can be found [hare](https://github.com/aabiro/aws-lambda-image-resize "GitHub Repo")

* Also, using the Lambda Function included in this repo:

The lambda function I include here works with two S3 buckets, the source and destination.

The code expects to find a destination bucket with the same name as the
source bucket with the word "resized" appended to it.

Make an EC2 instance to connect with on the AWS CLI, with a user having the appropriate Lambda and S3 access permissions.

When connected create and activate the virtual environment, Install the needed libraries, Create a deployment package, copy the `lambda_function.py` file from the local drive to the EC2 instance, Add the function’s code to the archive, and deactivate your virtual environment. 

Then you can create and deploy the Lambda function with:

`aws lambda create-function --function-name <YOUR-FUNCTION-NAME> --zip-file fileb://<FUNCTION-CODE-ZIP-FILE-IN-ARCHIVE> --handler lambda_function.lambda_handler --runtime python3.6 --timeout 10 --memory-size 1024 --role arn:aws:iam::<YOUR-ACCOUNT-ID>:role/<ROLE-NAME-WITH-LAMBDA-PERMISSION>`

More details about the `create-function` command are available here:
[create-function documentation](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html "AWS CLI Command Reference")


Then give the S3 bucket the permission to invoke a lambda function with:

`aws lambda add-permission --function-name <YOUR-FUNCTION-NAME> --principal s3.amazonaws.com --statement-id s3invoke --action "lambda:InvokeFunction" --source-arn arn:aws:s3:::<SOURCE-BUCKET-NAME> --source-account <YOUR-ACCOUNT-ID>`

Add Event notification configuration to the source bucket.

You will see a resized photo object in the S3 destination bucket when loading a picture in the source bucket.
