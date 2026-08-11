#!/bin/bash
# 用本地 HTTP 服务打开学习页面（避免 file:// 的安全限制）
cd "$(dirname "$0")"
PORT=8080
echo "启动学习服务器: http://localhost:$PORT/index.html"
open "http://localhost:$PORT/index.html" 2>/dev/null || true
python3 -m http.server "$PORT"
