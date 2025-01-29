from pathlib import Path
def main():
    with open(Path(__file__).parent.joinpath("books","frankenstein.txt")) as f:
        res = {}
        text = f.read()
        for c in text[:]:
            res[c.lower()] = res.get(c.lower(),0) + 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(text[:])} words found in the document")
    print()
    for key in res:
        if ord('a') > ord(key) or ord('z') < ord(key):
            continue
        print(f"The '{key}' character was found {res[key]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
