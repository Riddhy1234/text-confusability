@echo off
setlocal

echo =====================================================
echo   Phase 1 - Download Required Data Repositories
echo =====================================================
echo.

if not exist data mkdir data
if not exist data\raw mkdir data\raw

echo [1/3] Cloning PGFA...
git clone https://github.com/kaai520/PGFA.git data\raw\pgfa

echo.
echo [2/3] Cloning SMIE...
git clone https://github.com/YujieOuO/SMIE.git data\raw\smie

echo.
echo [3/3] Cloning SA-DVAE...
git clone https://github.com/pha123661/SA-DVAE.git data\raw\sa_dvae

echo.
echo =====================================================
echo Download complete.
echo =====================================================
echo.

echo Verifying MD5 hashes...
echo.

echo -------- PGFA --------
certutil -hashfile data\raw\pgfa\descriptions\ntu60_des.txt MD5

echo.
echo -------- SMIE --------
certutil -hashfile data\raw\smie\descriptions\ntu60_des.txt MD5

echo.
echo -------- SA-DVAE --------
certutil -hashfile data\raw\sa_dvae\class_lists\ntu60_llm.txt MD5

echo.
echo =====================================================
echo Expected MD5 for all three files:
echo 811755f481a375b345dd9f2268493a0c
echo =====================================================
echo.

echo If all three hashes match the expected value,
echo the description files are byte-identical and verified.

echo.
echo NOTE:
echo STAR repository does not contain a unified NTU-60
echo description file, so it is intentionally excluded
echo from this download script.

echo.
pause
endlocal