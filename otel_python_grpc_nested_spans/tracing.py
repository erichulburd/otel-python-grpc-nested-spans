import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def instrument():
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: os.environ["SERVICE_NAME"]})
        )
    )

    # For example, see https://opentelemetry-python.readthedocs.io/en/latest/exporter/jaeger/jaeger.html
    # create a JaegerExporter
    jaeger_exporter = JaegerExporter(
        collector_endpoint='jaeger:14250',
        insecure=True,
        credentials=None,
        max_tag_value_length=9999,
        timeout=5000,
    )

    # Create a BatchSpanProcessor and add the exporter to it
    span_processor = BatchSpanProcessor(jaeger_exporter)

    # add to the tracer
    trace.get_tracer_provider().add_span_processor(span_processor)
