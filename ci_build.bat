set JAVA_HOME=%BUILD_BINARIESDIRECTORY%\jdk
set PATH=C:\Tools\msys64\usr\bin;%JAVA_HOME%\bin;C:\IntelPython3;C:\IntelPython3\scripts;%PATH%
set BAZEL_SH=C:/Tools/msys64/usr/bin/bash.exe
set MSYS2_PATH_TYPE=inherit
set BAZEL_PYTHON=C:\IntelPython3\python.exe
%BUILD_BINARIESDIRECTORY%\packages\python.3.5.3\tools\python.exe ci_build.py --build_binaries_directory %BUILD_BINARIESDIRECTORY% --root %BUILD_SOURCESDIRECTORY% --out %BUILD_ARTIFACTSTAGINGDIRECTORY%  --commitid %BUILD_SOURCEVERSION% --buildid %BUILD_BUILDNUMBER%