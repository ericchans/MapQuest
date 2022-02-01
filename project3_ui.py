#Eric Chan 28343278
import mapquestapi
import outputclass

def find_output(output:str,path:dict)->str:
    '''Runs through a user input and creates objects from classes to print a desired response'''
    if output.upper().strip()=='STEPS':
        step=outputclass.steps()
        return 'DIRECTIONS\n'+step.elements(path)
        
    elif output.upper().strip()=='TOTALDISTANCE':
        dist = outputclass.totaldistance()
        return 'TOTAL DISTANCE: '+dist.elements(path)+'\n'
        
    elif output.upper().strip()=='TOTALTIME':
        time=outputclass.totaltime()
        return 'TOTAL TIME: '+time.elements(path)+'\n'
        
    elif output.upper().strip()=='LATLONG':
        coord=outputclass.latlong()
        return 'LATLONGS\n'+coord.elements(path)
        
    elif output.upper().strip()=='ELEVATION':
        height=outputclass.elevation()
        return 'ELEVATIONS\n'+height.elements(path)
    
def route(locations:list)->dict:
    '''This function receives the dictionary of the route given the locations'''
    return mapquestapi.get_route(locations)
    

def get_locations()->list:
    '''Asks the user for number of locations and the location names. Returns a list of locations'''
    location_names=[]
    num_locations=int(input())
    for loc_num in range(num_locations):
        location_names.append(input())
    return location_names

def get_outputs()->list:
    '''Asks the user for a number of outputs and to specify the output names.
    Returns a list of outputs'''
    output_names=[]
    num_outputs=int(input())
    for out_num in range(num_outputs):
        output_names.append(input())
    return output_names

def run_outputs(path:dict,outputs:list)->str:
    '''Runs through all the outputs in the list individually to be called by find_output'''
    result=''
    for output in range(len(outputs)):
        result+=find_output(outputs[output],path)+'\n'
    return result.strip('\n')

def print_all(text:str)->None:
    '''Displays all the specified outputs'''
    print(text)

def main():
    '''Main function that prompts the functions to ask for user inputs.'''
    locations=get_locations()
    outputs=get_outputs()
    print()
    final_output=[]
    try:
        path=route(locations)
        all_strings=run_outputs(path,outputs)
        print_all(all_strings)
        
    except mapquestapi.MAPQUEST_ERROR:
         print('MAPQUEST ERROR')
    except:
        print('NO ROUTE FOUND')
    else:
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
if __name__ == '__main__':
    main()
