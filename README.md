# Simple Python Test Server

Just a simple python server that listens on port 8000 and returns a simple message.
This is a fast way to test if a fluentbit is sending logs to a server.

https://docs.fluentbit.io/manual/pipeline/outputs/http

## How to build image

```bash
docker build -t python_server . 
```

## How to run image
```bash
docker run -p 8000:8000 -d python_server
```