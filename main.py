
# main.py

from datetime import datetime


from typing import Annotated, Any, Optional

from fastapi import FastAPI, File, Request, UploadFile



import firebase_admin.auth
import firebase_admin.storage
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from google.cloud import firestore as queriableFirestore



import uvicorn

import smtplib, ssl


# dfnkfdsfdkhfsdkfdfsf sdfsdfdsfsdf sfs df sf ds fs f dsfsf
import time
from itertools import chain



# firebase 

# main.py

import json
import random
import time

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn




import firebase_admin




from firebase_admin import credentials,auth



import pyrebase



from models import (createCardBINModelSchema, debitModel, recieveEmailSchema, sendEmailSchema, sendPushNotificationSchema, verifyAndCredit)
import paystackapi as pay
from paystackapi.paystack import Paystack
from paystackapi.verification import Verification
import google.cloud.firestore_v1.base_document as dcmnt




app = FastAPI(title='Inspect234 Server')
# db = firestore.client()










# class DatabaseHandler:
    
#     def __init__(self,collectionName:any,collectionRef:Optional[any]=None):
#         # document id will be user email for the user collections.
#         # self.ref = db.reference('docPath')
#         if collectionRef:
#             self.collection_ref=collectionRef
#         else:
#             self.collection_ref = db.collection(collectionName)
        
        
        
#         # db.collections.
#         # ref.
#     def createDoc(self,new_data:dict,doc_unique_name:str):        
#         '''fresh from the pot'''
#         doc_ref=self.collection_ref.document(doc_unique_name)
        
#         doc_ref.set(new_data)
#     def getDocList(self,filterDetail:list=[],orderDetail:list=[],limit: Optional[int] = None):
#         # for the filterDetail param it is a list of list which should have the field 
#         # the comparing sig
#         query=self.collection_ref
#         if len(filterDetail)!=0:
#             for i in filterDetail:
#                 query=query.where(filter=FieldFilter(str(i[0],i[1],i[2])))
                
            
#         if len(orderDetail)!=0:
#             descendOrAscend=None
#             if orderDetail[1]=='ascending':
#                 descendOrAscend =queriableFirestore.Query.DESCENDING
#             else:
#                 descendOrAscend =queriableFirestore.Query.ASCENDING
            
#             query=query.order_by("name", direction=descendOrAscend)
            
   
    
#         if limit:
#             query.limit(limit)
        
#         docs = (
#             query
#             .stream()
#         )
#         result:list =[]

#         for doc in docs:
#             print(f"{doc.id} => {doc.to_dict()}")
#             result.append(doc.to_dict())
                
#         return result
#     def getDocContent(self,doc_id:str):
#         # Note: Use of CollectionRef stream() is prefered to get()
#         doc_ref = self.collection_ref.document(doc_id)

#         doc = doc_ref.get()
#         result:dict={}
#         if doc.exists:
#             result=doc.to_dict()
        
            

#         return result
    
#     def updateDoc(self,update_data:dict,doc_id:str):
        
#         doc_ref=self.collection_ref.document(doc_id)
#         doc_ref.update(update_data)

#     def deleteDoc(self,new_data:dict,document_id:str):
#         doc_ref = self.collection_ref.document(document_id)
#         doc_ref.delete()


@app.post("/sendEmail")
# async def sendPushNotification(data:sendPushNotificationSchema):
async def sendEmail(data:sendEmailSchema):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "danoritic@gmail.com"
    # data.email
    # "my@gmail.com"  # Enter your address
    receiver_email = "info@ectinum.com"  # Enter receiver address
    password = "dxnh vjod jdbj vwej"
    # input("Type your password and press enter: ")
    message = data.message
    # """\
    # Subject: Hi there

    # This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



@app.get("/")
async def do():
    return "inspect"


def validate_token(request:Request):
    headers=request.headers
    jwt=headers.get('authorization')
    user=auth.verify_id_token(jwt)
    return user.uid





if __name__=="__main__":
    # docker tag yomserver us-docker.pkg.dev/yomcoin-75160/gcr.io/yomserver:1.0
    # us-docker.pkg.dev/yomcoin-75160/gcr.io/yomserver:1.0
    # uvicorn.run('main:app', host='192.168.43.239',reload=True)
    # docker run --name localContainer --rm -d -p 8080:80 yomserver
    # docker run --name server22 --rm -d -p 8080:80 gcr.io/yomcoin-75160/yomserver2:1.0
    # gcr.io/yomcoin-75160/yomserver2:1.0
    # uvicorn.run('main:app',reload=True,host="0.0.0.0", port=8080)
    uvicorn.run('main:app',reload=True,host="192.168.43.239", port=8080)
    
    # r=requests.post("http://192.168.43.239/getCompanyAddress",data={'userId':"dhsdjh"})
    # print(r)                                                                                                                                                            
    # print(r.text)
    

    
    
    
    
