@echo off 
cd /D %~dp0
cd build
COPY /Y ..\backend.jprc .
COPY /Y/B ..\ATRC\libs\win\*.dll .
COPY /Y/B ..\libs\*.dll .
COPY /Y ..\nuke_facts.json .
call cpp-backend-server.exe
echo %ERRORLEVEL%
