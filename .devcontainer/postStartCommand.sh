#!/bin/bash
if [ -f "docker-compose.yml" ]; then
  docker compose up -d --pull always --build
fi

# Active the Python venv for every shell
echo "source /workspace/.venv/python/bin/activate" >> ~/.bashrc.d/61-python-venv
