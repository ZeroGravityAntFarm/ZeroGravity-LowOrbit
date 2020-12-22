import os
import json

valid = ['sandbox.map', 'variant.zombiez', 'variant.ctf', 'variant.koth', 'variant.slayer', 'variant.assault', 'variant.vip', 'variant.jugg', 'variant.terries']
directory = "maps"
voting = 'voting.json'
clean = 0

def get_folders(folder):
    try:
        return os.listdir(folder)
    except:
        clean = 1
        return -1

for folder in get_folders(directory):
    for file in get_folders(directory + '\\' + folder):
        if file not in valid:
            clean = 1
            print('[ERROR] - "' + directory + '\\' + folder + '" contains invalid game file ' + file)

with open(voting, 'r') as f:
    try:
        json_data = json.load(f)
    except Exception as e:
        clean = 1
        print('[JSON ERROR] - Voting.json is invalid json.')
        print(e)
        exit()

for gameType in json_data['Types']:
    if gameType['typeName'] != gameType['SpecificMaps'][0]['mapName']:
        clean = 1
        print('[JSON ERROR] - gameType ' + gameType['SpecificMaps'][0]['mapName'] + ' does not match ' + gameType['typeName'] + ' typeName.' )

maps = get_folders(directory)

for gameType in json_data['Types']:
    if gameType['typeName'] not in maps:
        clean = 1
        print('[JSON ERROR] - ' + gameType['typeName'] + ' typeName does not match any of the map folder names.')
    
    elif gameType['SpecificMaps'][0]['mapName'] not in maps:
        clean = 1
        print('[JSON ERROR] - ' + gameType['SpecificMaps'][0]['mapName'] + 'mapName does not match any of the map folder names.')

if clean == 0:
    print('[PASS] - Looks good!')
