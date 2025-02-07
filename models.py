# from typing import Optional
import datetime

from fastapi import File, UploadFile
from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email:str|None
    phoneNumber:str|None
    DetailsFromOtherSignInMethods:dict|None
    password:str|None
    firstName: str|None
    signUpType:str
    # Optional[str] = None
    lastName: str|None
    # Optional[str] = None
    deviceID: str|None
    # Optional[str] = None
    # PhoneNumber: Optional[str] = None
    # birthday: Optional[str] = None
    # gender: Optional[str] = None
    
    class Config:
        schema_extra={
            'example':{
                'UID':'samplUID@gmail.com',
                'password':'samplePassword1234',
                
            }
        }
class recieveEmailSchema(BaseModel):
    userName:str
    clientEmail:str
    
    password:str
class sendPushNotificationSchema(BaseModel):
    tokens:list
    title:str
    body:str
    data:dict
class sendEmailSchema(BaseModel):
    message:str
    # email:str
    
    # body:str
    # data:dict
    
    


class verifyAndCredit(BaseModel):
    userEmail:str
    userID:str
    amount:str

class debitModel(BaseModel):
    # {"Content-Type": "application/json"}
    userID:str
    amount:str

class AmountModel(BaseModel):
    # {"Content-Type": "application/json"}
    userID:str

class createCardBINModelSchema(BaseModel):
    cardBIN:str
 