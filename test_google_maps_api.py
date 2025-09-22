import requests
from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import json

def read_and_write_in_txt_file(list_ids=None):
    if list_ids is not None:
        with open('location_ids.txt', 'w', encoding='utf-8') as file:
            for line in list_ids:
                file.write(line + '\n')
    else:
        list_ids = []
        with open('location_ids.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                point = line.strip('\n') 
                list_ids.append(point)
        return list_ids


class URL(Enum):
    DOMEN = 'https://rahulshettyacademy.com'
    KEY = {'key':'qaclick123'}
    GET = '/maps/api/place/get/json'
    POST = '/maps/api/place/add/json'
    PUT = '/maps/api/place/update/json'
    DELETE = '/maps/api/place/delete/json'

class PostResponse(BaseModel):
    status:str = Field(default='OK', description= 'Cheak status response')
    place_id:str
    scope: str
    reference: str
    id: str

class GetResponse(BaseModel):
    location: Dict[str,str]
    accuracy: str
    name: str
    phone_number: str
    address: str
    types: str
    website: str
    language: str

@dataclass
class BodyRequest:
    location: Dict[str, float]
    accuracy: int
    name: str
    phone_number: str
    address: str
    types: List[str]
    website: str
    language: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
    
def post_request(json,count,schema,url = f'{URL.DOMEN.value}{URL.POST.value}', params = URL.KEY.value, key = "place_id"):
    try:
        list_ids = []
        for x in range(count):
            response = requests.post(url = url,json = json, params=params)
            assert response.status_code == 200, f'ERROR: status code {response.status_code}'
            assert schema(**response.json()), f'ERROR: schema is not valid {response.json()}'
            list_ids.append(response.json().get(key))
            print(f'{response.json().get(key)} add in list')
        read_and_write_in_txt_file(list_ids)
    except:
        print('Fail create a new txt-file with ids')

def get_request(list_ids,schema,url = f'{URL.DOMEN.value}{URL.GET.value}', params = URL.KEY.value):
    try:
        for ids in list_ids:
            params['place_id'] = ids
            response = requests.get(url,params=params)
            assert response.status_code == 200, f'ERROR: status code {response.status_code}'
            assert schema(**response.json()), f'ERROR: schema is not valid {response.json()}'
            print(f'{ids} in Database')
    except:
        print(f'Fail check {ids} in Database')


body_1 = BodyRequest(location={"lat": -38.383494,"lng": 33.427362},accuracy=50,name = "Frontline house",
phone_number = "(+91) 983 893 3937",address = "29, side layout, cohen 09",types = ["shoe park"],
website = "http://google.com", language ="French-IN" )

post_request(json=body_1.to_dict(),schema=PostResponse,count=5)
get_request(read_and_write_in_txt_file(),GetResponse)