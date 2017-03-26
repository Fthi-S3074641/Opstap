#!/bin/bash

#pip install -r requirements.txt

gunicorn  --worker-class=gevent -t 99999 app:app
