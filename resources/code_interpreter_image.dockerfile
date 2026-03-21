FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        tini \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip \
    && pip install \
        ipykernel \
        jupyter_client \
        matplotlib \
        seaborn \
        numpy \
        pandas \
        scipy \
        sympy \
        scikit-learn \
        pillow

WORKDIR /workspace
