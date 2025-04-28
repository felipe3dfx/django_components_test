# syntax=docker/dockerfile:1
FROM debian:bookworm-slim AS builder

WORKDIR /opt

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

FROM debian:bookworm-slim AS final
LABEL org.opencontainers.image.source=https://github.com/grupo-ilao/vertechww-website

COPY --from=builder /opt/rye /opt/rye

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"
ENV PYTHONUNBUFFERED=True
ENV PNPM_HOME="/usr/local/bin/"
ENV PNPM_VERSION="9.3.0"


RUN mkdir /code
WORKDIR /code
COPY ./bin/install_extra_packages ./

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
       ca-certificates \
       git \
       libmagic-dev \
       libproj-dev \
       libc6-dev \
       gcc \
       gettext \
       curl \
    && ./install_extra_packages \
    && curl -fsSL https://get.pnpm.io/install.sh | SHELL="$(which bash)" bash - \
    && pnpm env use --global lts \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user with UID/GID 1000
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g 1000 -ms /bin/bash appuser && \
    chown -R appuser:appuser /code && \
    # Give permissions to user for rye directory
    chown -R appuser:appuser /opt/rye && \
    # Create node_modules directory with correct permissions
    mkdir -p /code/node_modules && \
    chown -R appuser:appuser /code/node_modules

# Set default user for containers
USER appuser
