import json
import os 

def save_mapping(mapping,filepath):
    with open(filepath,"w") as f:
        json.dump(mapping,f)

def load_mapping(filepath):
    with open(filepath,"r") as f :
        return json.load(f)
    
