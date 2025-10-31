# DouyinLiveRecorder 修改版（含 WebUI）

本项目基于 DouyinLiveRecorder 进行二次开发，**新增了 WebUI（网页界面）功能**，用户可以通过网页界面方便地进行配置和管理，无需手动编辑配置文件。（代码全部由 Trae 中的 Gemini-2.5-Flash 生成 ）

---

## 项目简介

DouyinLiveRecorder 是一款简易的多平台直播录制工具，基于 FFmpeg 实现，支持抖音、快手、虎牙、斗鱼、B 站、TikTok 等众多主流平台的直播录制。支持循环值守、推送通知、画质选择、代理设置等功能。

### 项目地址

- 原项目 Github：https://github.com/ihmily/DouyinLiveRecorder
- 本项目 DockerHub：https://hub.docker.com/r/sqing33/douyin-live-recorder-webui

### 主要功能

- 支持多平台直播录制
- 支持循环监测与自动录制
- 支持自定义画质、推送、代理等配置
- 录制文件自动保存
- **新增 WebUI：可通过网页界面管理和修改配置文件**

### 2025.10.31 更新

- **新增**：onebot 协议通知推送

<img width="367" height="268" alt="image" src="https://github.com/user-attachments/assets/6ba3f5aa-b33f-4f7e-b898-e488a6070c58" />


### WebUI 简介

- 访问方式：运行 `webui.py` 后，浏览器访问 [http://localhost:5000](http://localhost:5000)
- 可视化管理：支持对直播间列表、录制设置、推送设置、Cookie、账号密码等配置的可视化管理
- 新增 `Gotify` 渠道推送
- WebUI 启动后会自动启动录制，无需手动点击按钮

### 使用说明

1. 克隆或下载本项目源码
2. 安装依赖：`pip install -r requirements.txt`
3. 运行 WebUI：`python webui.py`
4. 浏览器访问 [http://localhost:5000](http://localhost:5000) 进行配置和录制

### Docker 镜像下载地址

- DockerHub：`sqing33/douyin-live-recorder-webui`
- Github：`ghcr.io/sqing33/douyin-live-recorder-webui`

### docker-compose 示例（适配 WebUI 版本）

```yaml
services:
  recorder:
    image: sqing33/douyin-live-recorder-webui # 带WebUI的镜像
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
  sqing33/douyin-live-recorder-webui
```

- 这样可直接通过 http://ip:5001 访问 WebUI。

### WebUI 界面

![image](https://github.com/user-attachments/assets/ba5bebda-8276-4b54-888c-a20c4ce160a8)
![image](https://github.com/user-attachments/assets/b206051a-79f1-4b89-a581-1e764970dd59)
![image](https://github.com/user-attachments/assets/73a4bc56-b72a-46d2-be9c-8bbff8a21d53)
![image](https://github.com/user-attachments/assets/9bcb0a54-cb94-401e-9394-640266c72ad5)
![image](https://github.com/user-attachments/assets/87673fe8-4173-423f-bb1d-04beb9a01ba4)
![image](https://github.com/user-attachments/assets/ab89e902-6bc8-4e46-bac8-2c02f34d1934)


---

本项目为个人二次开发，仅供学习交流使用。如有问题欢迎提 issue。
