#!/usr/bin/env bash

set -euo pipefail

HOST=$1
PORT=$2

exec 9<>"/dev/tcp/${HOST}/${PORT}"
echo -e "HEAD /health HTTP/1.1\r\nConnection: close\r\n\r\n" >&9
grep -q "200 OK" <&9
ret_code=$?

exec 9<&-
exec 9>&-

exit $ret_code