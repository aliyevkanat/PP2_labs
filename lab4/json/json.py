import json

inter = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(inter)

with open('sample-data.json', 'r') as f:
    data = json.load(f)

    for i in data['imdata']:
        key = next(iter(i))
        attributes = i[key]['attributes']

        print(f"{attributes["dn"]: < 45} {attributes["dot1qEtherType"]: < 13}{attributes["speed"]: < 10}{attributes["mtu"]: < 11}")