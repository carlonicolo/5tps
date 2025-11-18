FROM python:3.11-slim
WORKDIR /app
COPY server.py ./
RUN mkdir -p /data && chmod 777 /data
EXPOSE 5000
ENV HOST=0.0.0.0 PORT=5000 DATA_FILE=/data/store.json AUTO_FLUSH_SEC=5
CMD ["python", "server.py"]
