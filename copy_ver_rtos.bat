@echo off
setlocal

set "SOURCE=D:\rtosver"
set "DEST=\\192.168.112.170\rtosver"

for /f "delims=" %%F in ('dir "%SOURCE%\*.exe" /b /o:-d /a:-d 2^>nul') do (
    echo Copying latest file: %%F
    robocopy "%SOURCE%" "%DEST%" "%%F" /Z /R:3 /W:5
    goto :done
)

echo No files found.
:done
pause
