import hashlib
import sys

def get_hash(file):
    BUFFER_SIZE = 1024

    sha256 = hashlib.sha256()
    try:
        with open(file, "rb") as f:

            while True:
                data = f.read(BUFFER_SIZE)

                if not data:
                    break
                sha256.update(data)
    except Exception as e:
        print(e, file=sys.stderr)
    return sha256.hexdigest()

