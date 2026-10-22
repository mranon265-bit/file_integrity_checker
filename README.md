# File Integrity Checker

A Python-based CLI utility that monitors file changes in the current directory. It uses SHA-256 hashing to create a baseline snapshot and detect added, modified, or deleted files.

## Features
- Scans the current directory and calculates SHA-256 hashes.
- Saves a baseline snapshot to `.integrity.json`.
- Compares the current state against the baseline.
- Reports which files were Added, Modified, or Deleted.

## Clone the repo 
```bash 
git clone https://github.com/mranon265-bit/file_integrity_checker.git
```

## Usage

**1. Create a baseline:**
Run this once to snapshot the current directory.
```bash
python main.py init
```

**2. Check for changes:**
Run this whenever you want to see what has changed since the baseline.
```bash
python main.py check
```

### Example Output
```text
./test.txt was modified
./secret.env was added
./old_script.py was deleted
```

## Project Structure
- `main.py` - The CLI entry point.
- `integrity/scanner.py` - Walks the directory and finds files.
- `integrity/crypto.py` - Handles SHA-256 hashing.
- `integrity/storage.py` - Handles saving/loading to `data.json`.

## Requirements
- Python 3.8+
- No external dependencies (uses only the standard library).