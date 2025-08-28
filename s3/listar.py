import boto3

s3_cliente = boto3.resource("s3", region_name="us-east-1")

bucket = s3_cliente.Bucket("lucascunha2000")

for obj in bucket.objects.all():
    print(f"- {obj.key} - {obj.size}")