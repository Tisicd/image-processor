class S3Repository:
    def upload_image(self, base64_data: str, filename: str, content_type: str) -> str:
        # MOCK: Implementación real se hará en otro sprint
        print(f"Simulando subida a S3: {filename}")
        return f"https://mocked-s3.amazonaws.com/{filename}"
