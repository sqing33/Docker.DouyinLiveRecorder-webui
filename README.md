# DouyinLiveRecorder 修改版（含 WebUI）

本项目基于 DouyinLiveRecorder 进行二次开发，**新增了 WebUI（网页界面）功能**，用户可以通过网页界面方便地进行配置和管理，无需手动编辑配置文件。（代码全部由 Trae 中的 Gemini-2.5-Flash 生成 ）

---

## 项目简介

DouyinLiveRecorder 是一款简易的多平台直播录制工具，基于 FFmpeg 实现，支持抖音、快手、虎牙、斗鱼、B 站、TikTok 等众多主流平台的直播录制。支持循环值守、推送通知、画质选择、代理设置等功能。

### 原项目

- Github：https://github.com/ihmily/DouyinLiveRecorder

### 主要功能

- 支持多平台直播录制
- 支持循环监测与自动录制
- 支持自定义画质、推送、代理等配置
- 录制文件自动保存
- **新增 WebUI：可通过网页界面管理和修改配置文件，启动录制任务**

### WebUI 简介

- 访问方式：运行 `webui.py` 后，浏览器访问 [http://localhost:5000](http://localhost:5000)
- 可视化管理：支持对直播间列表、录制设置、推送设置、Cookie、账号密码等配置的可视化管理
- 一键启动录制，无需命令行操作

### 使用说明

1. 克隆或下载本项目源码
2. 安装依赖：`pip install -r requirements.txt`
3. 运行 WebUI：`python webui.py`
4. 浏览器访问 [http://localhost:5000](http://localhost:5000) 进行配置和录制

### docker-compose 示例（适配 WebUI 版本）

```yaml
services:
  recorder:
    image: sqing33/douyin-live-recorder-webui:0.1 # 带WebUI的镜像
    container_name: douyin-live-recorder-webui
    environment:
      - TERM=xterm-256color
    tty: true
    stdin_open: true
    ports:
      - "5001:5000" # 开放WebUI端口
    volumes:
      - /vol1/1000/Docker/douyin-live-recorder/config:/app/config
      - /vol1/1000/Docker/douyin-live-recorder/logs:/app/logs
      - /vol3/1000/直播录像/douyin-live-recorder:/app/downloads
    restart: always
```

### 完整 docker run 示例

```cmd
docker run -d \
  --name douyin-live-recorder-webui \
  -e TERM=xterm-256color \
  -v /vol1/1000/Docker/douyin-live-recorder/config:/app/config \
  -v /vol1/1000/Docker/douyin-live-recorder/logs:/app/logs \
  -v /vol3/1000/直播录像/douyin-live-recorder:/app/downloads \
  -p 5001:5000 \
  sqing33/douyin-live-recorder-webui:0.1
```

- 这样可直接通过 http://ip:5001 访问 WebUI。

---

本项目为个人二次开发，仅供学习交流使用。如有问题欢迎提 issue。
