#!/bin/bash

set -e

CMD_STR="fastapi dev fastapi_customers.py --host 0.0.0.0 --port 82"

exec /bin/bash -c "$CMD_STR"
