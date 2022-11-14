.PHONY: schema
schema:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. otel_python_grpc_nested_spans/*.proto