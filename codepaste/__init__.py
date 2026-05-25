from pathlib import Path
import sys
 
_dir = Path(__file__).parent / "files"
 
def main():
    args = sys.argv[1:]

    if not args:
        print("usage: codepaste ls | codepaste cat <name>")

    elif args[0] == "ls":
        print([f.name for f in _dir.iterdir() if f.is_file()])

    elif args[0] == "cat" and len(args) > 1:
        matches = list(_dir.glob(f"{args[1]}.*"))
        if not matches:
            print(f"'{args[1]}' not found. available: {[f.name for f in _dir.iterdir() if f.is_file()]}")
        else:
            print(matches[0].read_text(encoding="utf-8"))
            
    else:
        print("usage: codepaste ls | codepaste cat <name>")
 