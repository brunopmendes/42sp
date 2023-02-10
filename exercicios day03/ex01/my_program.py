#!/usr/bin/env python3

from path import Path

def main():
    p = Path('./new_folder')
    if not p.isdir():
        p.mkdir()
    
    f = p/"new_file.txt"
    f.write_text('Hello, path.py!')
    print(f.text())

if __name__ == '__main__':
    main()