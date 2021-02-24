@echo off
rem 提供Windows下nginx的启动，重启，关闭功能
 
echo ==================begin========================
 
cls 
::ngxin 所在的盘符
set NGINX_PATH=D:
 
::nginx 所在目录
set NGINX_DIR=D:\Study\VMS\nginx_1.13.6\
color 0a 
TITLE Nginx 管理程序增强版
 
CLS 
 
echo. 
echo. ** Nginx 管理程序  *** 
echo. *** create 2017-09-22 *** 
echo. 
 
:MENU 
 
echo. ***** nginx 进程list ****** 
::tasklist|findstr /i "nginx.exe"
tasklist /fi "imagename eq nginx.exe"
 
echo. 
 
    if ERRORLEVEL 1 (
        echo nginx.exe不存在
    ) else (
        echo nginx.exe存在
    )
 
echo. 
::*************************************************************************************************************
echo. 
	echo.  [1] 启动Nginx  
	echo.  [2] 关闭Nginx  
	echo.  [3] 重启Nginx 
	echo.  [0] 退 出 
echo. 
 
echo.请输入选择的序号:
set /p ID=
	IF "%id%"=="1" GOTO start 
	IF "%id%"=="2" GOTO stop 
	IF "%id%"=="3" GOTO restart 
	IF "%id%"=="0" EXIT
PAUSE 
 
::*************************************************************************************************************
::启动
:start 
	call :startNginx
	GOTO MENU
 
::停止
:stop 
	call :shutdownNginx
	GOTO MENU
 
::重启
:restart 
	call :shutdownNginx
	call :startNginx
	GOTO MENU
 

	
::*************************************************************************************
::底层
::*************************************************************************************
:shutdownNginx
	echo. 
	echo.关闭Nginx...... 
	taskkill /F /IM nginx.exe > nul
	echo.OK,关闭所有nginx 进程
	goto :eof
 
:startNginx
	echo. 
	echo.启动Nginx...... 
	IF NOT EXIST "%NGINX_DIR%nginx.exe" (
        echo "%NGINX_DIR%nginx.exe"不存在
        goto :eof
     )
 
	%NGINX_PATH% 
	cd "%NGINX_DIR%" 
 
	IF EXIST "%NGINX_DIR%nginx.exe" (
		echo "start '' nginx.exe"
		start "" nginx.exe
	)
	echo.OK
	goto :eof
	
 

