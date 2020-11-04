import argparse
import random
import time

from flask import Flask, redirect, url_for
from google.cloud import logging

# TRACE
from opencensus.ext.stackdriver import trace_exporter as stackdriver_exporter
import opencensus.trace.tracer

def initialize_tracer(project_id):
    exporter = stackdriver_exporter.StackdriverExporter(
        project_id=project_id
    )
    tracer = opencensus.trace.tracer.Tracer(
        exporter=exporter,
        sampler=opencensus.trace.tracer.samplers.AlwaysOnSampler()
    )

    return tracer

# APP
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('index'))


# [START trace_setup_python_quickstart]
@app.route('/index.html', methods=['GET'])
def index():
    tracer = app.config['TRACER']
    tracer.start_span(name='index')

    # Add up to 1 sec delay, weighted toward zero
    time.sleep(random.random() ** 2)
    result = "Tracing requests"

    tracer.end_span()
    return result
# [END trace_setup_python_quickstart]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--project_id', help='Project ID you want to access.', required=True)
    args = parser.parse_args()

    tracer = initialize_tracer(args.project_id)
    app.config['TRACER'] = tracer

    app.run()
