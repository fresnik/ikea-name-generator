# IKEA Name Generator

A REST API that generates new product names based on existing IKEA product names.

## Setup

### Virtual environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Docker

```bash
$ docker build -t <tag> .
```

## Running the service

### Virtual environment

```bash
$ source venv/bin/activate
$ export NAME_DATA_FILE=data/ikea_name_matrix_norm.json
$ PYTHONPATH=src python -m main
```

### Run docker image

```bash
$ docker run --rm -p 4532:4532 <tag>
```

## Usage

Perform a GET call on the `/name` endpoint to retrieve generated name(s):

```bash
$ curl http://localhost:4532/name
```

To request multiple names at once, add the `count` query parameter.
The default is 1.

```bash
$ curl "http://localhost:4532/name?count=3"
```

You can control the maximum length of the generated name using
the `max-length` query parameter. You can still get shorter names,
but never longer than the given parameter. The default is 20.

```bash
$ curl "http://localhost:4532/name?max-length=7"
```
