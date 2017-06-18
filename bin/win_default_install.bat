@echo off

REM Setup a default environment in a new/fresh windows installation.

REM Install chocolately.org
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

REM Tools
choco install cygwin cyg-get geany git putty python3 winscp win32diskimager -y
cyg-get mc

REM upgrade pip (from python)
python -m pip install --upgrade pip

REM install eapi for the eamodule
pip install eapi

REM Applications
choco install chromium foxitreader notepadplusplus sharpdevelop visualstudiocommunity2013 wireshark -y

REM Install scapy via pip - needs Pcap (via wireshark)
pip install scapy-python3

REM choco install unity -y
REM choco install unity4 -y

wget https://www.apachefriends.org/xampp-files/5.6.30/xampp-win32-5.6.30-1-VC11-installer.exe
start /wait xampp-win32-5.6.30-1-VC11-installer.exe
del xampp-win32-5.6.15-1-VC11-installer.exe

pause
