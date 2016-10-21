import http.client
import urllib.request
import urllib.error
import json

BASE_DIRECTION_URL = 'http://open.mapquestapi.com/directions/v2/route?key=Fmjtd%7Cluu8216t21%2C20%3Do5-94255a&ambiguities=ignore&from='
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'
        
def create_url_address(address:str) -> str:
    '''Formats addresses so they fit in url encoding
    '''
    address = (address.split(','))
    for info in range(len(address)):
        address[info] = address[info].strip()
        address[info] = address[info].replace(" ", "%20")
    address = ','.join(address)
    return(address)

def create_direction_url(address_list:list) -> str:
    '''Creates a url that gives directions based on a list of formatted addresses
    '''
    temp = 1
    beginning_url = BASE_DIRECTION_URL + address_list[0]
    while temp < len(address_list):
        beginning_url = beginning_url + '&to=' + address_list[temp]
        temp+=1
    complete_url = beginning_url + '&callback=renderNarrative'
    return(complete_url)

def get_lat_lng_for_url(json_dict:dict) -> str:
    '''Gets the latitude and longitude of addresses from a dictionary from a direction url and converts it into a str fit for elevation url
    '''
    lat_list = []
    lng_list = []
    lat_lng_str = ''
    for stuff in json_dict['route']['locations']:
        lat_list.append(stuff['displayLatLng']['lat'])
        lng_list.append(stuff['displayLatLng']['lng'])
    for x in range(len(lat_list)):
        lat_lng_str += str(lat_list[x]) + ',' + str(-lng_list[x]) + ','
    if len(lat_list) == 2:
        lat_lng_str = lat_lng_str[:-1] + ',,'
    else:
        lat_lng_str = lat_lng_str[:-1]
    return(lat_lng_str)

##def create_elevation_url() -> str:
##    pass
    
        
def print_directions(json_dict:dict) -> None:
    '''Takes in a dictionary and prints the directions
    '''
    print('DIRECTIONS')
    for stuff in json_dict['route']['legs']:    # goes through the dict 'route' and array 'legs'
        for morestuff in stuff['maneuvers']:    # goes through array 'maneuvers' and prints out the directions
            print(morestuff['narrative'])
    print('\n')






def print_total_distance(json_dict:dict) -> None:
    '''Takes in a dictionary and prints the total distance
    '''
    total_distance = int(json_dict['route']['distance'])
    if total_distance <= 250:
        print('TOTAL DISTANCE: ', '{:.0f}'.format(total_distance) + ' miles\n')
   



def print_total_time(json_dict:dict) -> None:
    '''Takes in a dictionary and prints the total time
    '''
    total_seconds = json_dict['route']['time']
    print('TOTALTIME: '+'{:.0f}'.format(total_seconds/60) + ' minutes\n')

def print_lat_long(json_dict:dict) -> None:
    '''Takes in a dictionary and prints the latitude and longitude of each address
    '''
    lat_list = []
    lng_list = []
    for stuff in json_dict['route']['locations']:
        lat_list.append(stuff['displayLatLng']['lat'])
        lng_list.append(stuff['displayLatLng']['lng'])
    print('LATLONG')
    for x in range(len(lat_list)):
        print('{:.2f}{} {:.2f}{}'.format(lat_list[x], 'N', lng_list[x], 'W'))
    print('\n')

##def print_elevations(json_dict:dict) -> None:
##    '''Takes in a dictionary and prints the height of each address
##    '''
##    for stuff in json_dict['elevationProfile']:
##        print(stuff['height'])

def create_direction_json() -> dict:
    '''Promps user for # of destinations and creates a direction url. The json in the url is then converted to a dict. If an invalid # of destinations is inputted, the function will return None
    '''
    response = None
    try:
        number_of_dest = input('# of destinations: ')
        destinations = int(number_of_dest)
    except:
        print('Error')
    else:
        if destinations <= 1:
            print('You must specify at least 2 locations to run this experiment')
        elif not type(destinations) == int:
            print('The first line must specify a positive integer number of locations')
        else:
            address_list = []
            temp = 0
            while temp < int(number_of_dest):
                address = input('Address: ')
                url_address = create_url_address(address)
                address_list.append(url_address)
                temp+=1
            direction_url = create_direction_url(address_list)
            try:
                response = urllib.request.urlopen(direction_url)
                url_text = response.read().decode(encoding = 'utf-8')
                actual_json = url_text[16:-2]
                json_text = json.loads(actual_json)
                return(json_text)
            except:
                print('Error: could not open url')
            finally:
                response.close()
##            print(address_list) #CHECKING
            print(direction_url) #CHECKING

if __name__ == '__main__':
    response = None
    direction_json = create_direction_json()
##    print(type(direction_json)) #CHECKING
##    print(direction_json) #CHECKING
    if direction_json == None:
        pass
    else:
        elevation_str = get_lat_lng_for_url(direction_json)
        elevation_url = 'http://open.mapquestapi.com/elevation/v1/profile?key=Fmjtd%7Cluu8216t21%2C20%3Do5-94255a&callback=handleHelloWorldResponse&shapeFormat=raw&latLngCollection=' + elevation_str #39.74012,-104.9849,39.7995,-105.7237,39.6404,-106.3736
##        print(elevation_str) #CHECKING
        print(elevation_url) #CHECKING
        try:
            response = urllib.request.urlopen(elevation_url)
            url_text = response.read().decode(encoding = 'utf-8')
            actual_json = url_text[25:-2]
            json_text = json.loads(actual_json)
        except:
            print('Error: could not open url')
        else:
            num_of_requests = input('# of outputs: ')
            temp = 0
            temp1 = 0 #if temp1=1 then there is an invalid output and the code will not print any of the other correct outputs
            output_list = []
            while temp < int(num_of_requests):
                output = input('Output (STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, ELEVATION): ')
                output_list.append(output)
                temp+=1
##                print(output_list) #CHECKING
            print('\n')
            for outputs in output_list:
                if not outputs == 'STEPS' and not outputs == 'TOTALDISTANCE' and not outputs == 'TOTALTIME' and not outputs == 'LATLONG' and not outputs == 'ELEVATION':
                    print('invalid output type: ' + outputs)
                    temp1 = 1
                if temp1 == 0:
                    if outputs == 'STEPS':
                        print_directions(direction_json)
                    elif outputs == 'TOTALDISTANCE':
                        print_total_distance(direction_json)
                    elif outputs == 'LATLONG':
                        print_lat_long(direction_json)
                    elif outputs == 'TOTALTIME':
                        print_total_time(direction_json)
                    elif outputs == 'ELEVATION':
                        print('ELEVATIONS')
                        for stuff in json_text['elevationProfile']:
                            print(stuff['height'])
                        print('\n')
            print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        
##        finally:
##            response.close()
        
     
            
        
              
              
