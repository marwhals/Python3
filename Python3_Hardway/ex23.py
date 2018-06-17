imports sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = languages_file.readlines()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encodings="utf-8")

main(languages, encodings, errors)
