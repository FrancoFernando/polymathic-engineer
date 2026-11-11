# Run the calculator service

This Python sample implements addition and subtraction over gRPC.

[Read the issue](https://newsletter.francofernando.com/p/remote-procedures).

Use Python 3.10+ and install `grpcio-tools`; its dependencies include `grpcio` and `protobuf`. Generate the Python bindings before starting the service.

From this folder:

```sh
cd calculator-microservice/calculator
python -m pip install -r requirements.txt
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/calculator.proto
python calculator.py
```

The sample listens on port 50051 on all interfaces, without TLS. Run it only in a trusted local development environment. Stop it with Ctrl+C.

[The Polymathic Engineer](https://newsletter.francofernando.com) | [Subscribe](https://newsletter.francofernando.com/subscribe)