def char_count(text):
    char_counts = {}
    lowered = text.lower()
    for char in lowered:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    arr = []
    for k, v in char_counts.items():
        d = {"character": k, "count": v}
        arr.append(d)

    return arr


def sort_on(dict):
    return dict["count"]


def print_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"--- Begin report of {file_path} ---")
        print(f"{len(words)} found in the document\n")

        char_counts = char_count(file_contents)
        char_counts.sort(reverse=True, key=sort_on)
        for c in char_counts:
            if c["character"].isalpha():
                print(f"The '{c['character']}' character was found {c['count']} times")
        print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")


if __name__ == "__main__":
    main()
