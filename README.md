# poetry-docker-playground
Um projeto para se fazer experimentos com Python, Poetry e Docker

## Dependências

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl

curl https://pyenv.run | bash

cat << 'EOF' >> ~/.bashrc
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH="$HOME/.local/bin:$PATH"
EOF
cat << 'EOF' >> ~/.profile
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH="$HOME/.local/bin:$PATH"
EOF
exec "$SHELL"

pyenv install -l | less
pyenv install -v 3:latest

curl -sSL https://install.python-poetry.org | python -
poetry config virtualenvs.in-project true
```