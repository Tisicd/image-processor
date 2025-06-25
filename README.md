python -m grpc_tools.protoc -I./protos --python_out=./app/interfaces/grpc --grpc_python_out=./app/interfaces/grpc ./protos/image_processor.proto
