@echo off
setlocal

REM Backup des Benutzerprofils auf ein externes USB-Laufwerk.
REM Das Skript liegt auf dem USB-Laufwerk und wird dort per Doppelklick
REM gestartet. Es spiegelt %USERPROFILE% (ohne AppData, Caches etc.) nach
REM <USB>\Backup\<COMPUTERNAME>\<USERNAME>. Im Profil geloeschte Dateien
REM werden auch im Backup geloescht (robocopy /MIR).

chcp 65001 >nul

set USB=%~d0
set ZIELBASIS=%USB%\Backup\%COMPUTERNAME%
set ZIEL=%ZIELBASIS%\%USERNAME%
set LOG=%ZIELBASIS%\%USERNAME%_backup.log

REM Schutz: nicht vom Systemlaufwerk aus spiegeln.
if /I "%USB%"=="%SystemDrive%" (
    echo FEHLER: Skript muss vom USB-Laufwerk gestartet werden, nicht von %SystemDrive%.
    pause
    exit /b 1
)

echo Quelle: %USERPROFILE%
echo Ziel:   %ZIEL%
echo Log:    %LOG%
echo.

if not exist "%ZIELBASIS%" mkdir "%ZIELBASIS%"

robocopy "%USERPROFILE%" "%ZIEL%" /MIR /XJ /R:1 /W:1 /FFT /MT:8 ^
    /XD AppData "OneDrive*" iCloudDrive .cache node_modules __pycache__ ^
    /XF NTUSER.DAT* ntuser.* UsrClass.dat* *.tmp ~$* desktop.ini Thumbs.db ^
    /NP /TEE /LOG:"%LOG%"
set RC=%ERRORLEVEL%

echo.
if %RC% GEQ 8 (
    echo FEHLER beim Backup ^(robocopy-Code %RC%^), siehe %LOG%
) else (
    echo Backup OK ^(robocopy-Code %RC%^).
)

pause
exit /b %RC%
