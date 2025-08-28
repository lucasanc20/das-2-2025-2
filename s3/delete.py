import boto3

s3_cliente = boto3.client("s3", region_name="us-east-1")

bucket = s3_cliente.Bucket("lucascunha2000")

obj = bucket.Object("exemplo.txt")

obj.delete()

print(f"Obj exemplo.txt excluido")