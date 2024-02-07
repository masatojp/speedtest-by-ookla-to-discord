import requests
import datetime

import subprocess
from subprocess import PIPE
import json

webhook_url = 'DISCORD_ENDPOINT'

speedtest = subprocess.run("speedtest -s 48463 -f json", shell=True, stdout=PIPE, stderr=PIPE, text=True)
speedtest_result = speedtest.stdout

speedtest_json = json.loads(speedtest_result)

#data get and input
ping = speedtest_json['ping']['latency']
download_bps = speedtest_json['download']['bandwidth']
upload_bps = speedtest_json['upload']['bandwidth']
url = speedtest_json['result']['url']
#packetloss = speedtest_json['packetLoss']

#bps to Mbps
download = download_bps/125000
upload = upload_bps/125000

#Debug print
#print(ping)
#print(download)
#print(upload)
#print(url)

#Rounding
download_round = round(download, 4)
upload_round = round(upload, 4)

#Debug print
#print(download_round)
#print(upload_round)

#result text
ping_text = str(ping) + "ms"
download_text = str(download_round) + "Mbps"
upload_text = str(upload_round) + "Mbps"
#packetloss_text = str(packetloss) + "%"

#Debug print
#print(ping_text)
#print(download_text)
#print(upload_text)

#image url
image_url = str(url) + ".png"

#Debug print
#print(image_url)

#date get
dt_now = datetime.datetime.now()

year = dt_now.year
month = dt_now.month
day = dt_now.day
hour = dt_now.hour

date_get = str(year) + "年" + str(month) + "月" + str(day) + "日" + str(hour) + "時"

#Debug print
#print(year)
#print(month)
#print(day)
#print(hour)
#print(date_get)

#footer
footer_text = "© " + str(year) + "YourName"

#Debug print
#print(footer_text)

#content
content="Home Network\n【定期スピードテスト】\n" + str(date_get) + "の結果は以下の通りです"

#Debug print
#print(content)

main_content = {
    "content": content,
    "embeds": [
        {
            "title": "Speedtest by ookla",
            "url": url,
            "color": 5620992,
            "footer": {
                "text": footer_text
            },
            "image": {
                "url": image_url
            },
            "fields": [
                {
                    "name": "Ping",
                    "value": ping_text,
                    "inline": True
                },
                {
                    "name": "Download",
                    "value": download_text,
                    "inline": True
                },
                {
                    "name": "Upload",
                    "value": upload_text,
                    "inline": True
                #},
		#{
                #    "name": "PacketLoss",
                #    "value": packetloss_text,
                #    "inline": True
                }
            ]
        }
    ]
}

requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
