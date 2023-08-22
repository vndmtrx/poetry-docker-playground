#!/usr/bin/env bash

set -o pipefail

HOST=$1
PORT=$2

exec 9<>/dev/tcp/"${HOST}"/"${PORT}"
echo -e "GET /health HTTP/1.1\r\nConnection: close\r\n\r\n" >&9
grep -q "HTTP/1.1 200 OK" <&9
ret_code=$?

exec 9<&-
exec 9>&-

exit $ret_code