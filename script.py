import json

# Opening JSON file
f = open('keys.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
datakeys = []
for i in data:
    # datakeys.append(i)
    datakeys.append(i)
  
# Closing file
f.close()

print(datakeys[0]['email_address'])
