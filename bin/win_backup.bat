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

REM Achtung: /MIR ist ein Spiegel, keine Versionierung. Im Profil
REM geloeschte oder beschaedigte Dateien (z.B. Ransomware) sind nach dem
REM naechsten Lauf auch im Backup weg.
REM
REM Optionen:
REM   /MIR      Ziel exakt spiegeln (inkl. Loeschen ueberzaehliger Dateien)
REM   /XJ       Junctions auslassen (vermeidet Schleifen wie "Anwendungsdaten")
REM   /R:1 /W:1 gesperrte Dateien nur einmal nach 1s erneut versuchen
REM   /FFT      2s-Zeitstempel-Toleranz fuer FAT/exFAT-Laufwerke
REM   /DST      1h-Zeitverschiebung (Sommer-/Winterzeit) auf FAT/exFAT
REM             ignorieren, sonst wird zweimal jaehrlich alles neu kopiert
REM   /MT:8     8 Kopier-Threads
REM   /UNILOG   Log in Unicode, damit Umlaute in Dateinamen lesbar bleiben
REM
REM Ausschluesse: AppData, Caches und Registry-Hives (im Betrieb gesperrt).
REM OneDrive/iCloud werden ausgelassen, da die Dateien in der Cloud liegen
REM und Platzhalter sonst heruntergeladen wuerden. Bei aktivierter
REM OneDrive-Ordnerumleitung (Dokumente/Desktop/Bilder) werden diese
REM Ordner daher NICHT gesichert.
REM
REM Geoeffnete Dateien (z.B. Outlook-.pst) koennen nicht kopiert werden und
REM fuehren zu robocopy-Code >= 8; vorher alle Programme schliessen.
robocopy "%USERPROFILE%" "%ZIEL%" /MIR /XJ /R:1 /W:1 /FFT /DST /MT:8 ^
    /XD AppData "OneDrive*" iCloudDrive .cache node_modules __pycache__ ^
    /XF NTUSER.DAT* ntuser.* UsrClass.dat* *.tmp ~$* desktop.ini Thumbs.db ^
    /NP /TEE /UNILOG:"%LOG%"
set RC=%ERRORLEVEL%

echo.
if %RC% GEQ 8 (
    echo FEHLER beim Backup ^(robocopy-Code %RC%^), siehe %LOG%
) else (
    echo Backup OK ^(robocopy-Code %RC%^).
)

pause
exit /b %RC%
