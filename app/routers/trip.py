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

from fastapi import APIRouter

from app import schemas
from enum import Enum


router = APIRouter(
    prefix="/Trip",
    tags=['Trip']
)

class Transportation(str, Enum):
    car = "car"
    walk = "walk"
    train = "train"
    bus = "bus"
    bike = "bike"
    
class ActivityType(str, Enum):
    departure = "departure"
    destination = "destination"
    activity = "activity"
    rest = "rest"
    return_trip = "return"
    
    
@router.post("/", response_model=schemas.TripResponse)
def generate_trip(new_trip: schemas.TripPydantic):
    resp = schemas.TripResponse(
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
    return resp
