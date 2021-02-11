FROM public.ecr.aws/lambda/python:3.8

COPY access_sample.py ./

RUN python3.8 -m pip install "snowflake-connector-python[pandas]" -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["access_sample.handler"]
