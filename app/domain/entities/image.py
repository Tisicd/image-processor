from dataclasses import dataclass
from typing import Optional

@dataclass
class Image:
    base64_data: str
    filename: str
    content_type: str
    url: Optional[str] = None

    def validate(self):
        if not self.base64_data or not self.filename or not self.content_type:
            raise ValueError("Todos los campos son requeridos")
        if not self.content_type.startswith("image/"):
            raise ValueError("El tipo de contenido debe ser una imagen")
