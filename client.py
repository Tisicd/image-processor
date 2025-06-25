import grpc
from app.interfaces.grpc import image_processor_pb2, image_processor_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = image_processor_pb2_grpc.ImageProcessorServiceStub(channel)

response = stub.ProcessImage(image_processor_pb2.ImageRequest(
    image_base64="fakebase64",
    filename="imagen.png",
    content_type="image/png"
))

print(response.image_url)
print(response.message)
