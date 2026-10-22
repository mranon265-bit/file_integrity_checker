import os 
from integrity.storage import load_mapping, save_mapping
from integrity.crypto import get_hash




def get_current_state(dirpath="."):
    state = {}
    # os.listdir() gives just filenames. os.path.join makes the full path.
    for filename in os.listdir(dirpath):
        full_path = os.path.join(dirpath, filename) 
        if full_path == "./data.json":
            continue
        if os.path.isfile(full_path):
            state[full_path] = get_hash(full_path)
            
    return state

def compare(current_state,old_state):
    file_set=set(current_state.keys()) | set(old_state.keys())

    for file in file_set:
        if file not in current_state:
            print(f"{file} was deleted!")
        elif file not in old_state:
            print(f"{file} was added")
        elif current_state[file] != old_state[file]:
            print(f"{file} was modified")



