'''
Created on Apr 29, 2014

@author: Anna
'''
import urllib.request as urlRequest
import constants.SolrConstants as solrConstants
import json

def insertEvent(eventId, eventName, eventPlace, eventTime, eventDate):
    bodyToPersist = {'id' : eventName + 'day', 
                     'eventName': eventName + 'day', 
                     'eventPlace' : eventPlace, 
                     'eventTime' : eventTime + ':00Z', 
                     'eventDate' : eventDate + 'T' + eventTime}
    responseRead = persist(bodyToPersist)
    print("insertEvent implementation")
    return responseRead
    
def selectEvent(query): 
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + query + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    responseRead = querySelect(query)    
    print("selectEvent implementation")
    return responseRead
    
    



def selectAllEvents():
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + 'eventName:*day' + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    responseRead = querySelect(query)
    print("selectAllEvents implementation")
    return responseRead
    
def login(userName):
    login = solrConstants.SOLR_LOGIN_SUER_NAME + userName
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + login + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    responseRead = querySelect(query)      
    print("login implementation")
    return responseRead
    
def signup(userName, newUserEmail, newUserPhomeNumber, userPassword):
    bodyToPersist = {'id' : 'login_' + userName, 
                     'userName': userName, 
                     'userPassword' : userPassword, 
                     'userPhomeNumber' : newUserPhomeNumber, 
                     'userEmail' : newUserEmail}
    responseRead = persist(bodyToPersist)
    print("sign up implementation")
    return responseRead
    
def subscribeForEvent(eventName, participantName, participantEmail):
    idEvent = '' +  participantName + 'AT' + eventName
    bodyToPersist = {'id' : idEvent, 
                     'eventParticipant': idEvent, 
                     'participantName' : participantName, 
                     'participantEmail' : participantEmail}
    responseRead = persist(bodyToPersist) 
    print("subscribeForEvent implementation")
    return responseRead

def querySelect(query):
    response = urlRequest.urlopen(query)
    responseRead = response.read()
    return responseRead

def persist(bodyToPersist):
    persistUrl = solrConstants.SOLR_ULR + solrConstants.SOLR_PERSIST
    bodyToPersist = json.dumps(bodyToPersist).encode('ascii')
    response = urlRequest.urlopen(persistUrl, bodyToPersist)
    responseRead = response.read()
    return responseRead
