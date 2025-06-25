from concurrent import futures
import grpc
from app.interfaces.grpc import image_processor_pb2_grpc, image_processor_pb2
from app.application.use_cases.process_image import ProcessImageUseCase
from app.infrastructure.s3.s3_repository import S3Repository


# Servidor que implementa el servicio definido en el proto
class ImageProcessorServicer(image_processor_pb2_grpc.ImageProcessorServiceServicer):
    def ProcessImage(self, request, context):
        # Por ahora solo retornamos la info recibida, como test
        return image_processor_pb2.ImageResponse(
            image_url="https://mocked-s3-url.com/" + request.filename,
            message="Imagen procesada exitosamente"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_processor_pb2_grpc.add_ImageProcessorServiceServicer_to_server(ImageProcessorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("🔌 Servidor gRPC corriendo en puerto 50051...")
    server.start()
    server.wait_for_termination()

class ImageProcessorServicer(image_processor_pb2_grpc.ImageProcessorServiceServicer):
    def __init__(self):
        self.use_case = ProcessImageUseCase(S3Repository())

    def ProcessImage(self, request, context):
        image = self.use_case.execute(request.image_base64, request.filename, request.content_type)
        return image_processor_pb2.ImageResponse(
            image_url=image.url,
            message="Imagen procesada y almacenada correctamente"
        )