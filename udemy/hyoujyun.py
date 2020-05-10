from pathlib import Path

current = Path()
for path in current.iterdir():
    if path.is_dir():
        for p in path.iterdir():
            print(p)
#    print(path.resolve())
