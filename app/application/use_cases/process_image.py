from app.domain.entities.image import Image

class ProcessImageUseCase:
    def __init__(self, s3_repository):
        self.s3_repository = s3_repository

    def execute(self, base64_data: str, filename: str, content_type: str) -> Image:
        image = Image(base64_data, filename, content_type)
        image.validate()

        url = self.s3_repository.upload_image(
            image.base64_data, image.filename, image.content_type
        )

        image.url = url
        return image
