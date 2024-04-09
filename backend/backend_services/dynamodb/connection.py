import boto3

def get_dynamodb_client():
    
    return boto3.client('dynamodb')

def get_dynamodb_resource():

    return boto3.resource('dynamodb')

def get_s3_client():
    return boto3.client('s3')

def get_s3_resource():

    return boto3.resource('s3')

def get_sns_client():
    return boto3.client('sns')

def get_sns_resource():

    return boto3.resource('sns')

def get_sqs_client():
    return boto3.client('sqs')

def get_sqs_resource():

    return boto3.resource('sqs')

def get_ssm_client():
    return boto3.client('ssm')

def get_ssm_resource():

    return boto3.resource('ssm')

def get_lambda_client():
    return boto3.client('lambda')

def get_lambda_resource():

    return boto3.resource('lambda')

def get_iam_client():
    return boto3.client('iam')

def get_iam_resource():

    return boto3.resource('iam')

def get_ec2_client():
    return boto3.client('ec2')

def get_ec2_resource():

    return boto3.resource('ec2')

def get_ecs_client():
    return boto3.client('ecs')

def get_ecs_resource():

    return boto3.resource('ecs')

def get_ecr_client():
    return boto3.client('ecr')

def get_ecr_resource():

    return boto3.resource('ecr')

def get_cloudwatch_client():
    return boto3.client('cloudwatch')

def get_cloudwatch_resource():

    return boto3.resource('cloudwatch')

def get_cloudformation_client():
    return boto3.client('cloudformation')

def get_cloudformation_resource():

    return boto3.resource('cloudformation')

def get_cloudtrail_client():
    return boto3.client('cloudtrail')

def get_cloudtrail_resource():

    return boto3.resource('cloudtrail')

