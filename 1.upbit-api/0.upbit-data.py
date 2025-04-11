from datetime import datetime
import requests
import time
import csv

# 데이터 수집
upbit_url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'

start_time = time.time()

bit_data_list = []

while time.time() - start_time < 60:
    res = requests.get(upbit_url)
    data = res.json()[0]

    bit_data = [
        data['market'],
        data['trade_date'],
        data['trade_time'],
        data['trade_price']
    ]
    bit_data_list.append(bit_data)
    time.sleep(5)

# 파일 저장
local_file_path = '/home/ubuntu/damf2/data/bitcoin/'

now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv'

# open(): 파일을 열어줌 as 변수에 저장
with open(local_file_path + file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bit_data_list)