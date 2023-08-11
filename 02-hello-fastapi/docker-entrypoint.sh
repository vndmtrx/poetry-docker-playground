#!/usr/bin/env bash

set -eou pipefail

# ativação do virtualenv
source /opt/pysetup/.venv/bin/activate

# execução do comando passado
exec "$@"