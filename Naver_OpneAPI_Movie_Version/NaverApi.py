from urllib.request import Request,  urlopen
from urllib.parse import quote
import datetime
import json

class NaverApi:
    def __init__(self) -> None:
        print(f'[{datetime.datetime.now()}] Naver API Creation')    
        
    def get_request_url(self, url):
        req = Request(url)

        req.add_header('X-Naver-Client-Id', 'SQqJyKQTKTlV_nAnylvw')
        req.add_header('X-Naver-Client-Secret', 'Y8w_59XP0C')

        try:
            res = urlopen(req)
            if res.getcode() == 200:
                print(f'[{datetime.datetime.now()}] NaverAPI Request Successful')
                return res.read().decode('utf-8')
            else:
                print(f'[{datetime.datetime.now()}] NaverAPI Request failed')
                return None
        except Exception as e:
            print(f'[{datetime.datetime.now()}] Exception Occurred : {e}')
            return None
    
    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None:
            return None
        else:
            return json.loads(retData)