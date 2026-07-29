@echo off
chcp 65001 >nul
title GitHub Hosts Updater

:: 检查管理员权限
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在请求管理员权限...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

set "HOSTS_FILE=C:\Windows\System32\drivers\etc\hosts"
set "BACKUP_FILE=%HOSTS_FILE%.bak"

echo ========================================
echo   GitHub Hosts 配置脚本
echo ========================================
echo.

:: 备份原 hosts 文件
if not exist "%BACKUP_FILE%" (
    echo [信息] 正在备份原 hosts 文件到 %BACKUP_FILE%
    copy "%HOSTS_FILE%" "%BACKUP_FILE%" >nul
) else (
    echo [信息] 备份文件已存在，跳过备份
)

:: 检查是否已包含 GitHub 配置
findstr /C:"# GitHub Start" "%HOSTS_FILE%" >nul
if %errorlevel% equ 0 (
    echo [警告] 检测到 hosts 文件中已存在 GitHub 配置。
    choice /C YN /M "是否要重新添加（选择 Y 将先清除旧配置）"
    if errorlevel 2 (
        echo 已取消操作。
        pause
        exit /b
    )
    :: 清除旧的 GitHub 配置
    echo [信息] 正在清除旧配置...
    powershell -Command "$c = Get-Content '%HOSTS_FILE%' -Raw; $c = $c -replace '(?s)# GitHub Start.*?# GitHub End\r?\n?', ''; Set-Content '%HOSTS_FILE%' -Value $c -NoNewline"
)

:: 添加新配置
echo [信息] 正在写入 GitHub Hosts 配置...

(
    echo.
    echo # GitHub Start
    echo 140.82.113.26                 alive.github.com
    echo 20.205.243.168                api.github.com
    echo 140.82.113.21                 api.individual.githubcopilot.com
    echo 185.199.111.133               avatars.githubusercontent.com
    echo 185.199.111.133               avatars0.githubusercontent.com
    echo 185.199.111.133               avatars1.githubusercontent.com
    echo 185.199.111.133               avatars2.githubusercontent.com
    echo 185.199.111.133               avatars3.githubusercontent.com
    echo 185.199.111.133               avatars4.githubusercontent.com
    echo 185.199.111.133               avatars5.githubusercontent.com
    echo 185.199.111.133               camo.githubusercontent.com
    echo 140.82.113.21                 central.github.com
    echo 185.199.111.133               cloud.githubusercontent.com
    echo 20.205.243.165                codeload.github.com
    echo 140.82.113.22                 collector.github.com
    echo 185.199.111.133               desktop.githubusercontent.com
    echo 185.199.111.133               favicons.githubusercontent.com
    echo 20.205.243.166                gist.github.com
    echo 54.231.163.249                github-cloud.s3.amazonaws.com
    echo 52.217.74.148                 github-com.s3.amazonaws.com
    echo 16.15.207.193                 github-production-release-asset-2e65be.s3.amazonaws.com
    echo 52.217.171.185                github-production-repository-file-5c1aeb.s3.amazonaws.com
    echo 16.15.212.196                 github-production-user-asset-6210df.s3.amazonaws.com
    echo 192.0.66.2                    github.blog
    echo 20.205.243.166                github.com
    echo 140.82.113.18                 github.community
    echo 185.199.110.215               github.githubassets.com
    echo 151.101.193.194               github.global.ssl.fastly.net
    echo 185.199.109.153               github.io
    echo 185.199.111.133               github.map.fastly.net
    echo 185.199.109.153               githubstatus.com
    echo 140.82.114.26                 live.github.com
    echo 185.199.111.133               media.githubusercontent.com
    echo 185.199.111.133               objects.githubusercontent.com
    echo 13.107.42.16                  pipelines.actions.githubusercontent.com
    echo 185.199.111.133               raw.githubusercontent.com
    echo 185.199.111.133               user-images.githubusercontent.com
    echo 150.171.110.70                vscode.dev
    echo 140.82.112.21                 education.github.com
    echo 185.199.111.133               private-user-images.githubusercontent.com
    echo.
    echo # GitHub End
) >> "%HOSTS_FILE%"

echo.
echo [成功] GitHub Hosts 配置已更新！
echo.

:: 刷新 DNS 缓存
echo [信息] 正在刷新 DNS 缓存...
ipconfig /flushdns >nul
echo [成功] DNS 缓存已刷新。

echo.
echo 操作完成！现在可以正常访问 GitHub 了。
echo.
pause
