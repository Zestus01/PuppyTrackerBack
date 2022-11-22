#!/bin/bash
python -m venv /workspace/.venv/python
source /workspace/.venv/python/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest
