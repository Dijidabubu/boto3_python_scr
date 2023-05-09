import boto3

iam = boto3.client('iam')

trust_policy = '''{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "*"
            },
            "Action": "*"
        }
    ]
}
'''


response = iam.create_role(
    RoleName='master_role_lambda',
    AssumeRolePolicyDocument=trust_policy
)

print(response)