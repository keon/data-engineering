# Kafka

## 설치 방법

1. Kafka 다운로드 페이지로 들어간다 (https://kafka.apache.org/downloads)
2. 다운로드 받은 파일을 압축을 풀고 원하는 디렉토리로 옮긴다 

## CLI examples

Zookeeper 실행
```
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
```

카프카 브로커 실행
```
bin/kafka-server-start.sh -daemon config/server.properties
```

실행 확인
```
netstat -an | grep 2181
```

이때 TCP46이 LISTEN인 경우 카프가가 잘 실행된 것
```
tcp46      0      0  *.2181                 *.*                    LISTEN 
```

새 토픽 만들기
```
bin/kafka-topics.sh --create --topic first-topic --bootstrap-server localhost:9092  --partitions 1 --replication-factor 1
```

카프카 토픽 리스트 
```
 ./bin/kafka-topics.sh --list --bootstrap-server localhost:9092 
```

카프카 토픽 확인
```
 ./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092
```

카프카 토픽 삭제
```
 ./bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic first-topic
```

콘솔 프로듀서
```
./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic
```

콘솔 컨슈머
```
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic
```

콘솔 컨슈머 + 컨슈머 그룹
```
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --group first-group
```

컨슈머 그룹 리스트
```
./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list  
```

## Docker Cluster

설정 리셋

```
docker-compose rm -svf
```

```
docker exec -it 03-kafka_kafka1_1 kafka-topics --bootstrap-server=localhost:19091 --create --topic first-cluster-topic --partitions 1 --replication-factor 1
```