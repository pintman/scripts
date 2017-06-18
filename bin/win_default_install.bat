@echo off

REM Setup a default environment in a new/fresh windows installation.
REM This script must be run as administrator

REM Install chocolately.org
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

REM Tools
choco install cygwin cyg-get geany git putty python3 winscp win32diskimager -y
cyg-get mc wget
REM alternative: choco install mc wget --source cygwin

REM upgrade pip (from python)
python -m pip install --upgrade pip
REM alternative: choco install pip --source python

REM install eapi for the eamodule
pip install eapi
REM alternative: choco install eapi --source python

REM Applications
choco install 7zip foxitreader libreoffice notepadplusplus tightvnc wireshark -y

REM Install scapy via pip - needs Pcap (via wireshark)
pip install scapy-python3
REM alternative: choco install scapy-python3 --source python

wget https://www.apachefriends.org/xampp-files/5.6.30/xampp-win32-5.6.30-1-VC11-installer.exe
start /wait xampp-win32-5.6.30-1-VC11-installer.exe
del xampp-win32-5.6.15-1-VC11-installer.exe

pause
