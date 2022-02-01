#Eric Chan 28343278

import mapquestapi

    
class steps:
    def elements(self,path:dict):
        '''Returns directions with each step being its own line.'''
        result=''
        for objects in path['route']['legs']:
            for i in objects['maneuvers']:
                result+=i['narrative']+'\n'
        return result

class totaldistance:
    def elements(self,path:dict):
        '''Returns the total distance that will be traveled'''
        distance=path['route']['distance']
        return str(round(distance))+' miles'
    
class totaltime:
    def elements(self,path:dict):
        '''Returns the total time that the trip will take'''
        TimeS=path['route']['time']
        return str(round(TimeS/60))+' minutes'

class latlong:
    def elements(self,path:dict):
        '''Returns latitude and longitude of each location with each location having its own line.
        Anything negative will be South for lat and West for long. '''
        result=""
        for objects in path['route']['locations']:
            lat=objects['latLng']['lat']
            long=objects['latLng']['lng']
            if lat>=0:
                lat=str(round(lat,2))+'N'
            elif lat<0:
                lat=lat*-1    
                lat=str(round(lat,2))+'S'
            if long >=0:
                long=str(round(long,2))+'E'
            elif long<0:
                long=long*-1
                long=str(round(long,2))+'W'
            result+= lat + " "+ long + '\n'
        return result
    
class elevation:
    def elements(self,path:dict):
        '''Returns the elevation (height) of the location. Does this by calling get_elevation with the
        parameter being a string of all the location's lat and long separated by commas.'''
        parameter=''
        for objects in path['route']['locations']:
            parameter+=str(objects['latLng']['lat'])+','
            parameter+=str(objects['latLng']['lng'])+','
        
        elevation_path=mapquestapi.get_elevation(parameter.strip(','))
        result=''
        for objects in elevation_path['elevationProfile']:
            result+=str(round(objects['height']))+'\n'
        return result
