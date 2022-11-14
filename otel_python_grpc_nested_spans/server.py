"""
Derived from https://github.com/grpc/grpc/blob/master/examples/python/wait_for_ready/asyncio_wait_for_ready_example.py
"""
import asyncio
from opentelemetry import trace
import logging
from numpy.random import normal
import grpc
from otel_python_grpc_nested_spans import sleeper_pb2, sleeper_pb2_grpc
from otel_python_grpc_nested_spans import tracing
from grpc_health.v1.health import HealthServicer
from grpc_health.v1 import health_pb2
from grpc_health.v1.health_pb2_grpc import add_HealthServicer_to_server
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer


tracing.instrument()

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

tracer = trace.get_tracer(__name__)
"See https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/grpc/grpc.html"
grpc_server_instrumentor = GrpcAioInstrumentorServer()
grpc_server_instrumentor.instrument()


async def sleep(amount: float) -> None:
    _LOGGER.info(f'sleeping {amount}s')
    await asyncio.sleep(amount)


class Sleeper(sleeper_pb2_grpc.SleeperServicer):
    async def Sleep(self, request: sleeper_pb2.SleepRequest, _context) -> sleeper_pb2.SleepResponse:
        with tracer.start_as_current_span("sleep-request-amount"):
            await sleep(request.amount)
        with tracer.start_as_current_span("sleep-deterministic"):
            await sleep(0.5)
        amount = max(0.25, normal(loc=1.0, scale=0.5))
        return sleeper_pb2.SleepResponse(amount=amount)


def create_server(server_address: str):
    server = grpc.aio.server()
    sleeper_pb2_grpc.add_SleeperServicer_to_server(Sleeper(), server)

    health = HealthServicer()
    health.set(
        sleeper_pb2.DESCRIPTOR.services_by_name["Sleeper"].full_name,
        health_pb2.HealthCheckResponse.SERVING,
    )
    add_HealthServicer_to_server(health, server)

    bound_port = server.add_insecure_port(server_address)
    assert bound_port == int(server_address.split(':')[-1])
    return server


async def main() -> None:
    # Start the server to handle the RPC
    server = create_server('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
