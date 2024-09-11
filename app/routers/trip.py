# request body
# {
#   "trip_theme": "南投",
#   "transportation": "car",
#   "departure_location": "台中",
#   "departure_time": "2024-12-10T08:00:00",
#   "return_location": "台中",
#   "return_time": "2024-12-10T19:00:00"
# }
# response body
# {
#   "generated_trip_info": {
#     "trip_overview": {
#       "location": "南投",
#      "start_date": "2024-12-10T08:00:00",
#       "end_date": "2024-12-10T19:00:00",

#       "description": "這趟一日遊將帶您探索南投的自然景觀和文化特色，從日月潭遊湖到九族文化村，適合喜愛自然與文化體驗的旅客。"
#     },
#     "days": [
#       {
#         "label": "第一天",
#         "date": "2024-12-10",
#         "activities": [
#           {
#             "location": "台中",
#             "start_time": "2024-12-10T08:00:00",
#             "end_time": "2024-12-10T09:00:00",

#             "activity": "出發",
#            "transportation": {
#               "mode": "car",
#               "travel_time": "60"
#             }

#           },
#           {
#             "location": "日月潭遊湖",
#             "start_time": "2024-12-10T09:00:00",
#             "end_time": "2024-12-10T11:00:00",

#             "stay_duration": "120",
#             "address": "南投縣魚池鄉日月潭",
#            "transportation": {
#               "mode": "car",
#               "travel_time": "10"
#             }

#           },
#           {
#             "location": "伊達邵老街",
#             "start_time": "2024-12-10T11:30:00",
#             "end_time": "2024-12-10T13:00:00",

#             "stay_duration": "90",
#             "address": "南投縣魚池鄉",
#             "transportation": {
#               "mode": "walk",
#               "travel_time": "5"
#             }

#           },
#           {
#             "location": "九族文化村",
#             "start_time": "2024-12-10T13:30:00",
#             "end_time": "2024-12-10T15:30:00",

#             "stay_duration": "120",
#             "address": "南投縣魚池鄉大林村",
#             "transportation": {
#               "mode": "car",
#               "travel_time": "20分鐘"
#             }

#           },
#           {
#             "location": "台中",
#             "start_time": "2024-12-10T16:00:00",
#             "end_time": "2024-12-10T17:30:00",

#             "activity": "返回",
#             "transportation": {
#               "mode": "car",
#               "travel_time": "90"
#             }

#           }
#         ]
#       }
#     ]
#   }
# }

import random
from fastapi import APIRouter

from app import schemas
from enum import Enum


router = APIRouter(
    prefix="/Trip",
    tags=['Trip']
)

class Transportation(str, Enum):
    car = "car"  # 汽車
    walk = "walk"  # 步行
    train = "train"  # 火車
    bus = "bus"  # 公車
    bike = "bike"  # 自行車
    
class ActivityType(str, Enum):
    departure = "departure"  # 出發
    destination = "destination"  # 目的地
    activity = "activity"  # 活動
    rest = "rest"  # 休息
    return_trip = "return"  # 返回
    check_in = "check_in"  # 入住
    arrival = "arrival"  # 到達
    
    
@router.post("/", response_model=schemas.TripResponse)
def generate_trip(new_trip: schemas.TripPydantic):
    trip1 = schemas.TripResponse(
        generated_trip_info=schemas.GeneratedTripInfo(
            trip_overview=schemas.TripOverview(
                location=new_trip.trip_theme,
                start_date=new_trip.departure_time,
                end_date=new_trip.return_time,
                description="這趟一日遊將帶您探索南投的自然景觀和文化特色，從日月潭遊湖到九族文化村，適合喜愛自然與文化體驗的旅客。"
            ),
            days=[
                schemas.Day(
                    label="第一天",
                    date="2024-12-10",
                    activities=[
                        schemas.Activity(
                            location="台中",
                            start_time="2024-12-10T08:00:00",
                            end_time="2024-12-10T09:00:00",
                            activity=ActivityType.departure,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="60"
                            )
                        ),
                        schemas.Activity(
                            location="日月潭遊湖",
                            start_time="2024-12-10T09:00:00",
                            end_time="2024-12-10T11:00:00",
                            stay_duration="120",
                            address="南投縣魚池鄉日月潭",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="伊達邵老街",
                            start_time="2024-12-10T11:30:00",
                            end_time="2024-12-10T13:00:00",
                            activity=ActivityType.activity,
                            stay_duration="90",
                            address="南投縣魚池鄉",
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="5"
                            )
                        ),
                        schemas.Activity(
                            location="九族文化村",
                            start_time="2024-12-10T13:30:00",
                            end_time="2024-12-10T15:30:00",
                            activity=ActivityType.activity,
                            stay_duration="120",
                            address="南投縣魚池鄉大林村",
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="20"
                            )
                        ),
                        schemas.Activity(
                            location="台中",
                            start_time="2024-12-10T16:00:00",
                            end_time="2024-12-10T17:30:00",
                            activity=ActivityType.return_trip,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="90"
                            )
                        )
                    ]
                )
            ]
        )
    )
    
    trip2 = schemas.TripResponse(
        generated_trip_info=schemas.GeneratedTripInfo(
            trip_overview=schemas.TripOverview(
                location="台中",
                start_date="2024-12-01",
                end_date="2024-12-02",
                description="這趟兩日行程將帶您探索台中的美食和文化景點，結合歷史與現代的體驗，讓您度過充實的兩天。"
            ),
            days=[
                schemas.Day(
                    label="第一天",
                    date="2024-12-01",
                    activities=[
                        schemas.Activity(
                            location="台北",
                            start_time="2024-12-01T09:00:00",
                            end_time="2024-12-01T10:30:00",
                            activity=ActivityType.departure,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="90"
                            )
                        ),
                        schemas.Activity(
                            location="宮原眼科",
                            start_time="2024-12-01T10:30:00",
                            end_time="2024-12-01T11:30:00",
                            stay_duration="60",
                            address="台中市中區中山路20號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="第四信用合作社",
                            start_time="2024-12-01T12:00:00",
                            end_time="2024-12-01T13:30:00",
                            stay_duration="90",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="彩虹眷村",
                            start_time="2024-12-01T14:00:00",
                            end_time="2024-12-01T15:30:00",
                            stay_duration="90",
                            address="台中市南屯區春安路56巷25號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="30"
                            )
                        ),
                        schemas.Activity(
                            location="酒店",
                            start_time="2024-12-01T16:00:00",
                            end_time="2024-12-01T18:00:00",
                            activity=ActivityType.check_in,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="15"
                            )
                        )
                    ]
                ),
                schemas.Day(
                    label="第二天",
                    date="2024-12-02",
                    activities=[
                        schemas.Activity(
                            location="台中大遠百",
                            start_time="2024-12-02T10:00:00",
                            end_time="2024-12-02T12:00:00",
                            stay_duration="120",
                            address="台中市西屯區台灣大道三段251號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="20"
                            )
                        ),
                        schemas.Activity(
                            location="台中市立美術館",
                            start_time="2024-12-02T12:30:00",
                            end_time="2024-12-02T14:00:00",
                            stay_duration="90",
                            address="台中市西區五權西路1號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="台中草悟道",
                            start_time="2024-12-02T14:30:00",
                            end_time="2024-12-02T16:00:00",
                            stay_duration="90",
                            address="台中市西區美村路一段",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="台北",
                            start_time="2024-12-02T16:30:00",
                            end_time="2024-12-02T18:00:00",
                            activity=ActivityType.return_trip,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="90"
                            )
                        )
                    ]
                )
            ]
        )
    )

    trip3 = schemas.TripResponse(
        generated_trip_info=schemas.GeneratedTripInfo(
            trip_overview=schemas.TripOverview(
                location="台南",
                start_date="2024-11-15",
                end_date="2024-11-17",
                description="這趟文化旅遊將帶您探索台南的歷史名勝與美食，結合文化與放鬆，是一趟充實的三日行程。"
            ),
            days=[
                schemas.Day(
                    label="第一天",
                    date="2024-11-15",
                    activities=[
                        schemas.Activity(
                            location="台中",
                            start_time="2024-11-15T08:00:00",
                            end_time="2024-11-15T10:00:00",
                            activity=ActivityType.departure,
                            transportation=schemas.Transportation(
                                mode=Transportation.train,
                                travel_time="120"
                            )
                        ),
                        schemas.Activity(
                            location="台南車站",
                            start_time="2024-11-15T10:00:00",
                            end_time="2024-11-15T10:30:00",
                            stay_duration="30",
                            activity=ActivityType.destination,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="赤崁樓",
                            start_time="2024-11-15T11:00:00",
                            end_time="2024-11-15T12:30:00",
                            stay_duration="90",
                            address="台南市中西區民族路2段212號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="15"
                            )
                        ),
                        schemas.Activity(
                            location="台南美食街",
                            start_time="2024-11-15T13:00:00",
                            end_time="2024-11-15T14:30:00",
                            stay_duration="90",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="酒店",
                            start_time="2024-11-15T15:00:00",
                            end_time="2024-11-15T17:00:00",
                            activity=ActivityType.check_in,
                            stay_duration="120",
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        )
                    ]
                ),
                schemas.Day(
                    label="第二天",
                    date="2024-11-16",
                    activities=[
                        schemas.Activity(
                            location="安平古堡",
                            start_time="2024-11-16T09:00:00",
                            end_time="2024-11-16T11:30:00",
                            stay_duration="150",
                            address="台南市安平區國勝路82號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="20"
                            )
                        ),
                        schemas.Activity(
                            location="安平老街",
                            start_time="2024-11-16T12:00:00",
                            end_time="2024-11-16T13:30:00",
                            stay_duration="90",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="台南美術館",
                            start_time="2024-11-16T14:00:00",
                            end_time="2024-11-16T16:00:00",
                            stay_duration="120",
                            address="台南市中西區中正路1號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="15"
                            )
                        ),
                        schemas.Activity(
                            location="酒店",
                            start_time="2024-11-16T16:30:00",
                            end_time="2024-11-16T18:30:00",
                            activity=ActivityType.check_in,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="15"
                            )
                        )
                    ]
                ),
                schemas.Day(
                    label="第三天",
                    date="2024-11-17",
                    activities=[
                        schemas.Activity(
                            location="孔廟",
                            start_time="2024-11-17T09:00:00",
                            end_time="2024-11-17T11:00:00",
                            stay_duration="120",
                            address="台南市中西區南門路2號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="10"
                            )
                        ),
                        schemas.Activity(
                            location="藍晒圖文創園區",
                            start_time="2024-11-17T11:30:00",
                            end_time="2024-11-17T13:00:00",
                            stay_duration="90",
                            address="台南市中西區海安路2段158號",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.walk,
                                travel_time="15"
                            )
                        ),
                        schemas.Activity(
                            location="花園夜市（午市）",
                            start_time="2024-11-17T13:30:00",
                            end_time="2024-11-17T15:00:00",
                            stay_duration="90",
                            activity=ActivityType.activity,
                            transportation=schemas.Transportation(
                                mode=Transportation.car,
                                travel_time="15"
                            )
                        ),
                        schemas.Activity(
                            location="台南火車站",
                            start_time="2024-11-17T17:00:00",
                            end_time="2024-11-17T19:00:00",
                            activity=ActivityType.return_trip,
                            transportation=schemas.Transportation(
                                mode=Transportation.train,
                                travel_time="120"
                            )
                        ),
                        schemas.Activity(
                            location="台中",
                            start_time="2024-11-17T19:00:00",
                            end_time="2024-11-17T21:00:00",
                            activity=ActivityType.arrival
                        )
                    ]
                )
            ]
        )
    )
    
    selected_trip = random.choice([trip1, trip2, trip3])
    
    return selected_trip
