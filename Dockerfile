FROM python:3-alpine3.21 AS builder
ADD . /app
WORKDIR /app

RUN apk add --update curl && \
    curl https://get.psono.com/psono/psono-ci/x86_64-linux/psonoci --output /app/psonoci >/dev/null && \
    chmod +x /app/psonoci

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app requests

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH=/app
CMD ["/app/main.py"]
