from pathlib import Path
 
_dir = Path(__file__).parent / "files"
 
print("codepaste: use ls() to list files, cat('name') to print contents")
 
def cat(name: str):
    matches = list(_dir.glob(f"{name}.*"))
    if not matches:
        print(f"'{name}' not found. available: {ls()}")
        return
    print(matches[0].read_text(encoding="utf-8"))
 
def ls():
    return [f.stem for f in _dir.iterdir()]