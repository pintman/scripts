@echo off

REM setup a default environment in a new and fresh windows installation.

REM install chocolately.org
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

choco install chromium -y
choco install git -y
choco install putty -y
choco install pdfcreator -y
choco install cygwin cyg-get -y
choco install wireshark -y
choco install foxitreader -y
choco install totalcommander -y
choco install wget -y

wget http://releases.0x539.de/gobby/gobby-stable.exe
start /wait gobby-stable.exe
del gobby-stable.exe

pause
