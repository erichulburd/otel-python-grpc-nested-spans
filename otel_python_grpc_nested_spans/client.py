"""
Derived from https://github.com/grpc/grpc/blob/master/examples/python/wait_for_ready/asyncio_wait_for_ready_example.py
"""
import asyncio
import logging
from opentelemetry import trace
import grpc
from numpy.random import normal
from otel_python_grpc_nested_spans import sleeper_pb2, sleeper_pb2_grpc
from otel_python_grpc_nested_spans import tracing
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorClient

tracing.instrument()
"See https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/grpc/grpc.html"
grpc_client_instrumentor = GrpcAioInstrumentorClient()
grpc_client_instrumentor.instrument()


_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

tracer = trace.get_tracer(__name__)


async def sleep(amount: float) -> None:
    await asyncio.sleep(amount)


async def main():
    with tracer.start_as_current_span('client-process'):
        async with grpc.aio.insecure_channel('server:50051') as channel:
            stub = sleeper_pb2_grpc.SleeperStub(channel)
            for i in range(5):
                amount = max([0.25, normal(loc=1.0, scale=0.5)])
                response = await stub.Sleep(sleeper_pb2.SleepRequest(amount=amount))
                _LOGGER.info(f'sleeping {response.amount}s')
                with tracer.start_as_current_span('sleep-response-amount'):
                    await sleep(response.amount)
                with tracer.start_as_current_span("sleep-deterministic"):
                    await sleep(0.5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
