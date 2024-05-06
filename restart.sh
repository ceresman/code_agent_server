#!/bin/bash

# 服务的进程名称，可以根据实际情况调整
SERVICE_NAME="uvicorn"

# 服务监听的端口，可以根据实际情况调整
PORT=9999

# 服务的日志文件，可以根据实际情况调整
LOG_FILE="agent.log"

# 找到并停止正在运行的 uvicorn 服务
echo "Stopping $SERVICE_NAME..."
pid=$(ps aux | grep uvicorn | grep -v grep | awk '{print $2}')
if [ -n "$pid" ]; then
    kill $pid
    if [ $? -eq 0 ]; then
        echo "$SERVICE_NAME stopped."
    else
        echo "Failed to stop $SERVICE_NAME."
        exit 1
    fi
fi

# 等待几秒钟，确保服务已经完全停止
sleep 2

# 启动新的 uvicorn 服务
echo "Starting $SERVICE_NAME..."
uvicorn server:app --reload --host 0.0.0.0 --port $PORT > $LOG_FILE 2>&1 &
if [ $? -eq 0 ]; then
    echo "$SERVICE_NAME started."
else
    echo "Failed to start $SERVICE_NAME."
    exit 1
fi

# 获取新启动服务的 PID
NEW_PID=$!
echo "$SERVICE_NAME PID: $NEW_PID"
cat agent.log
