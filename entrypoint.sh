#!/bin/bash

set -ex

poetry run alembic upgrade head

poetry run streamlit run src/main.py
