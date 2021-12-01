# Airflow

## CLI examples

```
airflow -h

airflow webserver

airflow db -h

airflow users -h

airflow users create -h

airflow users create -u admin -p admin -f Keon -l Kim -r Admin -e admin@admin.com

```

커맨드

```
이미 돌려본 커맨드
airflow db init 

airflow db upgrade

airflow db reset 

airflow webserver

airflow scheduler

airflow dags list

airflow tasks list example_trigger_target_dag

airflow dags trigger -e 20220-01-01 example_trigger_target_dag
```

