#!/usr/bin/env bash

set -e

DEFAULT_HOST="rpi-zero-light.local"
HOST="${1:-$DEFAULT_HOST}"

color="$(curl -s "$HOST":5000/color)"

r="$(echo "$color" | jq '.r')"
g="$(echo "$color" | jq '.g')"
b="$(echo "$color" | jq '.b')"

printf "\x1b[38;2;%d;%d;%dm■■■■■\x1b[0m\n" "$r" "$g" "$b"


