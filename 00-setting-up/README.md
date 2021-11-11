
install java 8

brew cask install homebrew/cask-versions/adoptopenjdk8


```
==> Installation successful!
```


brew cask install homebrew/cask-versions/adoptopenjdk8


brew를 통해 자바 개발 킷을 설치하는 도중
아래와 같은 에러를 만났다.

terminal에서 
brew cask install adoptopenjdk8 명령어를 입력했는데
Error: Unknown command: cask 와 같은 에러가 나왔다.

brew install --cask homebrew/cask-versions/adoptopenjdk8




sudo rm -rf /Library/Java/JavaVirtualMachines/jdk-16.jdk

🍺  adoptopenjdk8 was successfully installed!


check java

ls /Library/java/JavaVirtualMachines/


check spark version

ls /usr/local/Cellar/apache-spark



export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
export JRE_HOME=/Library/java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/jre/
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.2.0/libexec
export PATH=/usr/local/Cellar/apache-spark/3.2.0/bin:$PATH
export PYSPARK_PYTHON=/Users/keon/.pyenv/versions/3.7.2/bin/python


which python

/Users/keon/.pyenv/versions/3.7.2/bin/python

export PYSPARK_PYTHON=/Users/keon/.pyenv/versions/3.7.2/bin/python


/Users/maelfabien/opt/anaconda3/bin/python



keon@macpro ~ % vim .zshrc
keon@macpro ~ % source .zshrc


python

```
>>> import pyspark
>>> from pyspark import SparkContext
>>> sc = SparkContext()
nUsing Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
^R
21/10/24 18:15:01 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
>>> n = sc.parallelize([4, 10, 9, 7])
>>> n.take(3)
[4, 10, 9]   
```


pyspark

>>> data = [1, 2, 3, 4, 5, 8, 9]
>>> data
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD = sc.parallelize(data)
>>> myRDD.collect()
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD.count()
7



export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
export JRE_HOME=/Library/java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/jre/
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.2.0/libexec
export PATH=/usr/local/Cellar/apache-spark/3.2.0/bin:$PATH
export PYSPARK_PYTHON=/Users/keon/opt/anaconda3/bin/python
export PATH="$HOME/anaconda/bin:$PATH"
export PATH="/Users/keon/opt/anaconda3/bin:$PATH"




export SOMA_SERVICE_ACCOUNT='soma-318106'
