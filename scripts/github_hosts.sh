#!/bin/bash
# GitHub Hosts 更新脚本 (macOS / Linux)

set -e

HOSTS_FILE="/etc/hosts"
BACKUP_FILE="/tmp/hosts.bak"

# 检查是否有 root 权限
if [ "$EUID" -ne 0 ]; then
    echo "正在请求管理员权限 (sudo)..."
    exec sudo bash "$0" "$@"
fi

echo "========================================"
echo "  GitHub Hosts 配置脚本"
echo "========================================"
echo ""

# 备份原 hosts 文件
if [ ! -f "$BACKUP_FILE" ]; then
    echo "[信息] 正在备份原 hosts 文件到 $BACKUP_FILE"
    cp "$HOSTS_FILE" "$BACKUP_FILE"
else
    echo "[信息] 备份文件已存在，跳过备份"
fi

# 检查是否已包含 GitHub 配置
if grep -q "# GitHub Start" "$HOSTS_FILE"; then
    echo "[警告] 检测到 hosts 文件中已存在 GitHub 配置。"
    read -rp "是否要重新添加？(y/N): " choice
    if [ "$choice" != "y" ] && [ "$choice" != "Y" ]; then
        echo "已取消操作。"
        exit 0
    fi
    # 清除旧的 GitHub 配置
    echo "[信息] 正在清除旧配置..."
    sed -i '/^# GitHub Start$/,/^# GitHub End$/d' "$HOSTS_FILE"
fi

# 添加新配置
echo "[信息] 正在写入 GitHub Hosts 配置..."

cat >> "$HOSTS_FILE" << 'EOF'

# GitHub Start
140.82.113.26                 alive.github.com
20.205.243.168                api.github.com
140.82.113.21                 api.individual.githubcopilot.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.113.21                 central.github.com
185.199.111.133               cloud.githubusercontent.com
20.205.243.165                codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
20.205.243.166                gist.github.com
54.231.163.249                github-cloud.s3.amazonaws.com
52.217.74.148                 github-com.s3.amazonaws.com
16.15.207.193                 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.171.185                github-production-repository-file-5c1aeb.s3.amazonaws.com
16.15.212.196                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
20.205.243.166                github.com
140.82.113.18                 github.community
185.199.110.215               github.githubassets.com
151.101.193.194               github.global.ssl.fastly.net
185.199.109.153               github.io
185.199.111.133               github.map.fastly.net
185.199.109.153               githubstatus.com
140.82.114.26                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
150.171.110.70                vscode.dev
140.82.112.21                 education.github.com
185.199.111.133               private-user-images.githubusercontent.com

# GitHub End
EOF

echo ""
echo "[成功] GitHub Hosts 配置已更新！"
echo ""

# 刷新 DNS 缓存
echo "[信息] 正在刷新 DNS 缓存..."
OS="$(uname)"
if [ "$OS" = "Darwin" ]; then
    # macOS
    dscacheutil -flushcache
    killall -HUP mDNSResponder 2>/dev/null || true
    echo "[成功] DNS 缓存已刷新 (macOS)。"
elif [ "$OS" = "Linux" ]; then
    # Linux
    if command -v systemd-resolve &> /dev/null; then
        systemd-resolve --flush-caches 2>/dev/null || true
    elif command -v nscd &> /dev/null; then
        nscd -K 2>/dev/null || true
    elif command -v rndc &> /dev/null; then
        rndc flush 2>/dev/null || true
    fi
    echo "[成功] DNS 缓存已刷新 (Linux)。"
fi

echo ""
echo "操作完成！现在可以正常访问 GitHub 了。"
echo ""
