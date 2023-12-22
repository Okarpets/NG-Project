import json
import requests
url = "https://www.youtube.com/watch?v=INySzPs9Zns"

msg = "собрать запрос так"
data = {"prompt": msg}

response = requests.post(url, data=json.dumps(data))
answer = response.get("replies")
print(*answer)