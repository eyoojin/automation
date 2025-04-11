# cron

- cron job 등록 `crontab -e`

- 기본 문법
```shell
* * * * * <실행할 명령어>
*/5 * * * * /home/ubuntu/damf2/automation/venv/bin/python /home/ubuntu/damf2/automation/0.log/0.log_generate.py   
```
- `python`으로 `0.log_generate.py`를 5분마다 반복
- 분 시 일 월 요일
    - 분: 0-59
    - 시: 0-23
    - 일: 1-31
    - 월: 1-12
    - 요일: 0-6, 0은 일요일

- cron 리스트 확인 `crontab -l`
