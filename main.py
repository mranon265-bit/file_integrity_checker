import sys

from integrity.scanner import get_current_state, compare
from integrity.storage import save_mapping, load_mapping


def main():
    if len(sys.argv) !=2:
        print(f"usage: python scanner.py init/check ")
        exit(1)
    current_state=get_current_state()
    if sys.argv[1]=="init":
        save_mapping(mapping=current_state, filepath="data.json")
    elif sys.argv[1]=="check":
        old_state=load_mapping("data.json")
        compare(current_state=current_state, old_state=old_state)

if __name__=="__main__":
    main()

