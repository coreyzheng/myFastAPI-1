#!/bin/bash

set -e

CMD_STR="fastapi dev fastapi_invoices.py --host 0.0.0.0 --port 83"

exec /bin/bash -c "$CMD_STR"
