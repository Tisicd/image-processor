class S3Repository:
    def upload_image(self, base64_data: str, filename: str, content_type: str) -> str:
        # MOCK: Implementación real se hará en otro sprint
        print(f"Simulando subida a S3: {filename}")
        return f"https://mocked-s3.amazonaws.com/{filename}"
import boto3
import base64
import os
from botocore.exceptions import BotoCoreError, ClientError

class S3Repository:
    def __init__(self):
        self.bucket_name = os.getenv("AWS_S3_BUCKET")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )

    def upload_image(self, base64_data: str, filename: str, content_type: str) -> str:
        try:
            image_bytes = base64.b64decode(base64_data)
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=image_bytes,
                ContentType=content_type,
                ACL="public-read"  # ⚠️ Seguridad: público para pruebas, luego restringir
            )
            url = f"https://{self.bucket_name}.s3.amazonaws.com/{filename}"
            return url
        except (BotoCoreError, ClientError, base64.binascii.Error) as e:
            raise Exception(f"Error al subir imagen a S3: {e}")
