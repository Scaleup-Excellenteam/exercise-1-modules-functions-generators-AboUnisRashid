import re


def find_matches(file_obj):
    # Search for any text that matches the pattern of 5 or more lowercase letters followed by an exclamation mark
    pattern = re.compile(b'[a-z]{5,}!')
    matches = []
    for line in file_obj:
        # Search for matches of the pattern in the line
        matches.extend(pattern.findall(line))
    # Convert all matches from bytes to strings and return as a list
    return [match.decode('utf-8') for match in matches]


def process_file():
    try:
        with open("resources/logo.jpg", "rb") as f:
            all_matches = find_matches(f)
            for match in all_matches:
                print(f"Found match: {match}")
    except IOError:
        print('Error while opening the file!')


process_file()
