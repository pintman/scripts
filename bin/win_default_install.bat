@echo off

REM Setup a default environment in a new/fresh windows installation.

REM Install chocolately.org
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

REM Tools
choco install git -y
choco install putty -y
choco install cygwin cyg-get -y
cyg-get mc

REM Applications
choco install notepadplusplus -y
choco install chromium -y
choco install wireshark -y
choco install foxitreader -y
choco install totalcommander -y
choco install visualstudiocommunity2013 -y

choco install wget -y
wget http://releases.0x539.de/gobby/gobby-stable.exe
start /wait gobby-stable.exe
del gobby-stable.exe

wget https://www.apachefriends.org/xampp-files/5.6.12/xampp-win32-5.6.12-0-VC11-installer.exe
start /wait xampp-win32-5.6.12-0-VC11-installer.exe
del xampp-win32-5.6.12-0-VC11-installer.exe

pause
