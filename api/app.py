from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from jaeger_client import Config

app = FastAPI()

# Instrumentação do Prometheus
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app, endpoint="/metrics")

# Inicialização do Jaeger
def init_tracer(service):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
            'reporter': {
                'log_spans': True,
                'agent_host': 'jaeger-agent',  # Substitua pelo serviço Jaeger correto
                'agent_port': 6831,
            },
        },
        service_name=service,
    )
    return config.initialize_tracer()

tracer = init_tracer('my-service')

@app.get('/')
def read_root():
    with tracer.start_span('read_root') as span:
        span.log_kv({'event': 'request', 'value': 'Hello World!'})
        return {'message': 'Hello World!'}

@app.on_event("shutdown")
def shutdown_event():
    tracer.close()
