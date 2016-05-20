@echo off

REM Setup a default environment in a new/fresh windows installation.

REM Install chocolately.org
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

REM Tools
choco install cygwin cyg-get geany git putty python3 winscp -y
cyg-get mc
REM Install scapy via pip - needs Pcap (via wireshark)
pip install scapy-python3

REM Applications
choco install chromium foxitreader notepadplusplus sharpdevelop visualstudiocommunity2013 wireshark -y
REM choco install unity -y
REM choco install unity4 -y

choco install wget -y
wget http://releases.0x539.de/gobby/gobby-stable.exe
start /wait gobby-stable.exe
del gobby-stable.exe

wget https://www.apachefriends.org/xampp-files/5.6.21/xampp-win32-5.6.21-0-VC11-installer.exe
start /wait xampp-win32-5.6.15-1-VC11-installer.exe
del xampp-win32-5.6.15-1-VC11-installer.exe

pause
