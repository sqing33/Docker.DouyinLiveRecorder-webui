from flask import Flask, render_template, request, redirect, url_for
import configparser
import os
import subprocess
from streamget.logger import logger

app = Flask(__name__)

CONFIG_FILE = 'config/config.ini'
URL_CONFIG_FILE = 'config/URL_config.ini'


def read_config(file_path):
    config = configparser.ConfigParser(interpolation=None)
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            if not content.strip().startswith('['):
                content = '[DEFAULT]\n' + content
                config.read_string(content)
            else:
                config.read(file_path, encoding='utf-8-sig')
    except FileNotFoundError:
        pass  # Return empty config if file not found
    return config


def write_config(config, file_path):
    with open(file_path, 'w', encoding='utf-8-sig') as configfile:
        config.write(configfile)


@app.route('/')
def index():
    return redirect(url_for('home_page'))


@app.route('/home', methods=['GET'])
def home_page():
    return render_template('index.html', active_tab='home')


recording_process = None


@app.route('/url_config', methods=['GET', 'POST'])
def url_config_page():
    url_config_path = os.path.join(os.getcwd(), 'config', 'URL_config.ini')
    if request.method == 'POST':
        new_content = request.form['url_config_content']
        with open(url_config_path, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        return redirect(url_for('url_config_page', success='true'))
    try:
        with open(url_config_path, 'r', encoding='utf-8-sig') as f:
            url_config_content = f.read()
    except FileNotFoundError:
        url_config_content = ''
    return render_template('index.html',
                           url_config_content=url_config_content,
                           active_tab='url_config')


@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording_process
    if recording_process is None or recording_process.poll() is not None:
        try:
            logger.info("开始录制...")
            recording_process = subprocess.Popen(['python', 'main.py'],
                                                 cwd=os.getcwd())
            return redirect(url_for('home_page', success='true'))
        except Exception as e:
            return str(e), 500
    return redirect(url_for('home_page'))


@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global recording_process
    if recording_process is not None and recording_process.poll() is None:
        try:
            logger.info("停止录制...")
            recording_process.terminate()
            recording_process.wait()
            recording_process = None
            logger.info("录制已停止。")
            return redirect(url_for('home_page', success='true'))
        except Exception as e:
            return str(e), 500
    return redirect(url_for('home_page'))


@app.route('/recording_settings', methods=['GET', 'POST'])
def recording_settings_page():
    config_path = os.path.join(os.getcwd(), 'config', 'config.ini')
    if request.method == 'POST':
        config = read_config(config_path)
        for key, value in request.form.items():
            if '录制设置' in config and key in config['录制设置']:
                config.set('录制设置', key, value)
        write_config(config, config_path)
        return redirect(url_for('recording_settings_page', success='true'))
    config = read_config(config_path)
    return render_template('index.html',
                           config=config,
                           active_tab='recording_settings',
                           section='录制设置')


@app.route('/push_settings', methods=['GET', 'POST'])
def push_settings_page():
    config_path = os.path.join(os.getcwd(), 'config', 'config.ini')
    if request.method == 'POST':
        config = read_config(config_path)
        for key, value in request.form.items():
            if '推送配置' in config and key in config['推送配置']:
                config.set('推送配置', key, value)
        write_config(config, config_path)
        return redirect(url_for('push_settings_page', success='true'))
    config = read_config(config_path)
    return render_template('index.html',
                           config=config,
                           active_tab='push_settings',
                           section='推送配置')


@app.route('/cookie_settings', methods=['GET', 'POST'])
def cookie_settings_page():
    config_path = os.path.join(os.getcwd(), 'config', 'config.ini')
    if request.method == 'POST':
        config = read_config(config_path)
        for key, value in request.form.items():
            if 'Cookie' in config and key in config['Cookie']:
                config.set('Cookie', key, value)
        write_config(config, config_path)
        return redirect(url_for('cookie_settings_page', success='true'))
    config = read_config(config_path)
    return render_template('index.html',
                           config=config,
                           active_tab='cookie_settings',
                           section='Cookie')


@app.route('/account_settings', methods=['GET', 'POST'])
def account_settings_page():
    config_path = os.path.join(os.getcwd(), 'config', 'config.ini')
    if request.method == 'POST':
        config = read_config(config_path)
        for key, value in request.form.items():
            if '账号密码' in config and key in config['账号密码']:
                config.set('账号密码', key, value)
        write_config(config, config_path)
        return redirect(url_for('account_settings_page', success='true'))
    config = read_config(config_path)
    return render_template('index.html',
                           config=config,
                           active_tab='account_settings',
                           section='账号密码')


@app.route('/log')
def get_log():
    log_content = []
    log_files = [
        os.path.join(os.getcwd(), 'logs', 'streamget.log'),
        os.path.join(os.getcwd(), 'logs', 'PlayURL.log')
    ]
    for log_file in log_files:
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    # 读取所有行并只保留最后100行
                    lines = f.readlines()
                    log_content.extend(lines[-100:] if len(lines) >
                                       100 else lines)
            except Exception as e:
                log_content.append(f"Error reading {log_file}: {e}\n")
    return "".join(log_content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
