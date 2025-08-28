import boto3

s3_cliente = boto3.client("s3", region_name="us-east-1")
s3_cliente.upload_file("./s3/exemplo.txt", "lucascunha2000", "exemplo.txt")

print("arquivo carregado com sucesso")