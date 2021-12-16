# Flink

## Download 

1. flink download 링크로 들어가서 최신 버전 (Apache Flink 1.14.0 for Scala 2.12) 다운로드 https://flink.apache.org/downloads.html
2. 다운로드 후 압축을 풀고 원하는 디렉토리로 옮겨주세요 (예 ~/)


클러스터를 실행하려면
```
$ ./bin/start-cluster.sh
Starting cluster.
Starting standalonesession daemon on host.
Starting taskexecutor daemon on host.
```

잘 실행되었는지 확인하려면 아래 커맨드 실행 후 플링크 UI가 실행되고 있는지 확인

```
$ ps aux | grep flink
```


클러스터를 멈추려면

```
$ ./bin/stop-cluster.sh
```


example 코드를 돌려보려면 
```
// java 버전
$ ./bin/flink run examples/streaming/WordCount.jar
$ tail log/flink-*-taskexecutor-*.out
  (nymph,1)
  (in,3)
  (thy,1)
  (orisons,1)
  (be,4)
  (all,2)
  (my,1)
  (sins,1)
  (remember,1)
  (d,4)

// 파이썬 버전
$ ./bin/flink run --python examples/python/table/word_count.py
$ Job has been submitted with JobID cc2541ee4ded7e34d7b12d812134fd96
```


그리고 이렇게 돌린 example code는 웹 ui 로 확인이 가능합니다

http://localhost:8081/#/overview


## Apache Kafka Connector

https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/connectors/table/kafka/