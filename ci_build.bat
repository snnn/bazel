set JAVA_HOME=%BUILD_BINARIESDIRECTORY%\jdk
cd %BUILD_BINARIESDIRECTORY%\packages
cmd /c start /wait %BUILD_BINARIESDIRECTORY%\packages\miniconda\Miniconda3-4.3.21-Windows-x86_64.exe /S /AddToPath=0 /RegisterPython=0 /D=%BUILD_BINARIESDIRECTORY%\packages\python
set PATH=C:\Tools\msys64\usr\bin;%JAVA_HOME%\bin;%BUILD_BINARIESDIRECTORY%\packages\python;%BUILD_BINARIESDIRECTORY%\packages\python\scripts;%PATH%
set BAZEL_SH=C:/Tools/msys64/usr/bin/bash.exe
set MSYS2_PATH_TYPE=inherit
set BAZEL_PYTHON=%BUILD_BINARIESDIRECTORY%\packages\python\python.exe
cd %BUILD_SOURCESDIRECTORY%
%BUILD_BINARIESDIRECTORY%\packages\python\python.exe ci_build.py --build_binaries_directory %BUILD_BINARIESDIRECTORY% --root %BUILD_SOURCESDIRECTORY% --out %BUILD_ARTIFACTSTAGINGDIRECTORY%  --commitid %BUILD_SOURCEVERSION% --buildid %BUILD_BUILDNUMBER%