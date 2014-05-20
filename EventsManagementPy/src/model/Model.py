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
    persistUrl = solrConstants.SOLR_ULR + solrConstants.SOLR_PERSIST;
    response = urlRequest.urlopen(persistUrl, json.dumps(bodyToPersist))
    responseRead = response.read()  
    print("insertEvent implementation")
    return responseRead
    
def selectEvent(query): 
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + query + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    response = urlRequest.urlopen(query)
    responseRead = response.read()    
    print("selectEvent implementation")
    return responseRead
    
    
def selectAllEvents():
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + 'eventName:*day' + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    response = urlRequest.urlopen(query)
    responseRead = response.read()
    print("selectAllEvents implementation")
    return responseRead
    
def login(userName):
    login = solrConstants.SOLR_LOGIN_SUER_NAME + userName
    query = solrConstants.SOLR_ULR + solrConstants.SOLR_QUERY + login + solrConstants.SOLR_QUERY_RESPONSE_TYPE;
    print(query)
    response = urlRequest.urlopen(query)
    responseRead = response.read()      
    print("login implementation")
    return responseRead
    
def signup(userName, newUserEmail, newUserPhomeNumber, userPassword):
    print("sign up implementation")
    
def subscribeForEvent(eventName, participantName, participantEmail):
    print("subscribeForEvent implementation")
    
def persist(body_to_persist):
    print("persist implementation")
    
def query(query):
    print("query implementation")