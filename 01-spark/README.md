## Spark


스파크 환경 설정에 어려움이 있다면 docker를 사용해서 모든 디펜던시를 한꺼번에 설치할 수 있습니다.

먼저 docker 설치를 해주세요

도커 설치는 아래 링크에서 가능합니다.

https://www.docker.com/products/docker-desktop


인스톨러를 따라서 설치를 하고나면 restart를 해주세요.

그리고 아래 커맨드로 터미널에서 도커 사용이 가능한지 확인해주세요.

```
docker version
```

도커가 설치가 되었다면 아래 커맨드로 주피터 노트북을 킬 수 있습니다.

```
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```

도커로 커맨드를 돌리고 나면 아래와 같이 메시지가 뜰겁니다

```
[I 04:27:19.672 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 04:27:19.672 NotebookApp] Jupyter Notebook 6.4.6 is running at:
[I 04:27:19.672 NotebookApp] http://f7a5384f2282:8888/?token=9e495b3cbcc68413167e12d358bdaaf8c8e35c7d4f06f904
[I 04:27:19.672 NotebookApp]  or http://127.0.0.1:8888/?token=9e495b3cbcc68413167e12d358bdaaf8c8e35c7d4f06f904
[I 04:27:19.672 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 04:27:19.676 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-8-open.html
    Or copy and paste one of these URLs:
        http://f7a5384f2282:8888/?token=9e495b3cbcc68413167e12d358bdaaf8c8e35c7d4f06f904
     or http://127.0.0.1:8888/?token=9e495b3cbcc68413167e12d358bdaaf8c8e35c7d4f06f904
```

여기서 토큰 정보와 같이 (http://127.0.0.1:8888/?token=9e495b3cbcc68413167e12d358bdaaf8c8e35c7d4f06f904) URL을 복사한 다음 브라우저에 붙여넣기 해서 들어가면 주피터를 볼 수 있습니다. 

마지막으로 pyspark를 import해서 파이스파크 디펜던시가 깔렸는지 확인해주세요

```
import pyspark 
sc = pyspark.SparkContext('local[*]')
```

새로운 dependency를 설치하고 싶다면 주피터 안에 코드블락을 만들고 sys 패키지를 import 한 후 아래와 같이 설치하고픈 패키지를 입력해주시기 바랍니다.

```
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install <설치하고 싶은 패키지>
```