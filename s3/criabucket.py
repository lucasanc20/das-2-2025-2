import boto3

s3_cliente = boto3.client("s3", region_name="us-east-1")

s3_cliente.create_bucket(Bucket="lucascunha2000")

print("Bucket criado com sucesso")
