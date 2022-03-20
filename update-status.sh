#!/usr/bin/env bash

set -e

STATUS="$1"

DEFAULT_HOST="rpi-zero-light.local"
HOST="${2:-$DEFAULT_HOST}"

r=0
g=0
b=0

if [ "$STATUS" = "available" ]; then  # Green
  g=255
elif [ "$STATUS" = "focus" ]; then    # Yellow
  r=255
  g=48
elif [ "$STATUS" = "meeting" ]; then  # Red
  r=255
else
  printf "Unreocgnized staus: '%s', turning off light...\n", "$STATUS"
fi

curl -X PUT -H "Content-Type: application/json" "$HOST:5000/color" -d "{\"r\":$r,\"g\":$g,\"b\":$b}"

