#Eric Chan 28343278

import urllib.parse
import json
import urllib.request


API_key = 'g4lu91EojWruGokVERM8FkT3BXARZu8C'

API_dir_base = 'https://open.mapquestapi.com/directions/v2'

API_ele_base='https://open.mapquestapi.com/elevation/v1'

class MAPQUEST_ERROR(Exception):
    '''Raised when the MapQuest API cannot be reached
    (no network,wrong API key,etc.)'''
    pass

def get_route(locations:list)->dict:
    '''This takes the location list and creates a url that calls the function _get_result and will receive
    information from MapQuest's API in dictionary format and will also return it.'''
    try:
        parameters=[('key',API_key),('from',locations[0])]
        for index in range(1,len(locations)):
            parameters.append(('to',locations[index]))
        url=API_dir_base + '/route?' + urllib.parse.urlencode(parameters)
        return _get_result(url)
    except:
        raise MAPQUEST_ERROR
    
def get_elevation(coordinates:str)->dict:
    '''This function will take a string of latitude and longitude coordinates that creates a url and
    calls _get_result to receive information from MapQuest's API in dictionary format and will also
    return it'''
    try:
        parameters=[('key',API_key),('latLngCollection',coordinates),('unit','f')]
        url=API_ele_base+'/profile?'+urllib.parse.urlencode(parameters)
        return _get_result(url)
    except:
        raise MAPQUEST_ERROR

def _get_result(url:str)->dict:
    '''This takes the url as a parameter and opens it. After it opens it, it reads the JSON response and
    returns it as a dictionary'''
    try:
        response = urllib.request.urlopen(url)
        text=response.read().decode(encoding='utf-8')
        return json.loads(text)
    finally:
        if response!=None:
            response.close()
