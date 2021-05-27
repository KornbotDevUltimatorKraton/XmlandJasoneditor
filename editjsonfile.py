import os, json, uuid

filename = 'data.json'
with open(filename, 'r') as f:
    data = json.load(f)
    data['id'] = 134 # <--- add `id` value.
    # add, remove, modify content
    # Modify the key value
    data['data'] = data.pop('id')
    print(data)
# create randomly named temporary file to avoid 
# interference with other thread/asynchronous request
tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
with open(tempfile, 'w') as f:
    json.dump(data, f, indent=4)

# rename temporary file replacing old file
os.rename(tempfile, filename)
