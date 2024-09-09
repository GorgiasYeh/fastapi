from typing import List, Optional
from pydantic import BaseModel

class BaseUser(BaseModel):
    userName : str
    email : str
    password : str

class CreateUser(BaseUser):
    pass

class LoginUser(BaseModel):
    userName : str
    password : str
    
    
class User(BaseUser):
    pass

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    
class InfoPydantic(BaseModel):
    # id: int
    deviceName: str
    power: Optional[int] = None
    trackingModeColor: Optional[str] = None
    connected: str
    connectStatus: str
    step: Optional[int] = None
    lockMode: str
    frequency: str

    class Config:
        from_attributes = True
        
        
class TripPydantic(BaseModel):
    
    # id: int
    trip_theme: str
    transportation: str
    departure_location: str
    departure_time: str
    return_location: str
    return_time: str
    
    class Config:
        from_attributes = True

class TripOverview(BaseModel):
    location: str
    start_date: str
    end_date: str
    description: str

class Transportation(BaseModel):
    mode: str
    travel_time: str

class Activity(BaseModel):
    location: str
    start_time: str
    end_time: str
    activity: str
    stay_duration: Optional[str] = None
    address: Optional[str] = None
    transportation: Optional[Transportation] = None

class Day(BaseModel):
    label: str
    date: str
    activities: List[Activity]

class GeneratedTripInfo(BaseModel):
    trip_overview: TripOverview
    days: List[Day]

class TripResponse(BaseModel):
    generated_trip_info: GeneratedTripInfo