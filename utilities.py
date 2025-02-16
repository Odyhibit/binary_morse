import base64

text_to_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    ",": "--..--",
    "1": ".----",
    ".": ".-.-.-",
    "2": "..---",
    "?": "..--..",
    "3": "...--",
    ";": "-.-.-.",
    "4": "....-",
    ":": "---...",
    "5": ".....",
    "'": ".----.",
    "6": "-....",
    "-": "-....-",
    "7": "--...",
    "/": "-..-.",
    "8": "---..",
    "(": "-.--.",
    "9": "----.",
    ")": "-.--.-",
    " ": "/",
    "_": "..--.-",
    "=": "-...-",
}

morse_to_binary_string_dict = {".": "10", "-": "1110", "_": "1110", " ": "00", "/": "0000"}


def text_to_morse_str(ascii_text: str) -> str:
    """Letters separated by a space, words separated by '/'."""
    morse = ""
    for character in ascii_text.upper():
        if character in text_to_morse_dict:
            morse += text_to_morse_dict[character]
            if character != " ":
                morse += " "
    return morse


def morse_str_to_text(morse: str) -> str:
    """Expects '/' as word separator."""
    text = ""
    words = morse.split("/")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            if letter:
                text += list(text_to_morse_dict.keys())[list(text_to_morse_dict.values()).index(letter)]
        text += " "
    return text


def morse_str_to_bin_str(morse_str: str) -> str:
    """Changes a morse code string into a matching binary string.
        Output string will be padded to full bytes. (length: multiple of 8)"""
    binary_str = ""
    for char in morse_str:
        binary_str += morse_to_binary_string_dict[char]
    binary_str += "0" * (8 - (len(binary_str) % 8))
    return binary_str


def bin_str_to_bytearray(binary_str: str) -> []:
    """Changes a binary sting into a byte array.
        input_string needs to contain full bytes. (length: multiple of 8)"""
    byte_array = bytearray()
    for byte_index in range(0, len(binary_str), 8):
        start = byte_index
        byte_array.append(int(binary_str[start: start + 8], 2))
    return byte_array


def morse_str_to_bytearray(morse_str: str) -> []:
    """Changes a morse code string into a byte array."""
    return bin_str_to_bytearray(morse_str_to_bin_str(morse_str))


def morse_str_to_base64(morse_str: str) -> str:
    """Changes a morse code string into a base64 string."""
    return base64.b64encode(morse_str_to_bytearray(morse_str)).decode('utf-8')


def base64_to_binary_string(base64_str: str) -> []:
    """Changes a base64 string into a byte array."""
    return "".join([bin(i)[2:].zfill(8) for i in base64.b64decode(base64_str)])


def base64_to_text(base64_str: str) -> str:
    return morse_str_to_text(binary_string_to_morse(base64_to_binary_string(base64_str)))


def base64_to_morse(base64_str: str) -> str:
    return binary_string_to_morse(base64_to_binary_string(base64_str))


def binary_string_to_morse(binary_str: str) -> str:
    """Changes binary in a string to a morse code string.
       Extra trailing '0,/' may exist from padding to full bytes.
       They will be removed.
    """
    morse_str = binary_str
    morse_str = morse_str.replace("1110", "-")
    morse_str = morse_str.replace("10", ".")
    morse_str = morse_str.replace("0000", "/")
    morse_str = morse_str.replace("00", " ")
    return morse_str.rstrip("0/")


def write_file(filename: str, bin_out: bytearray | str):
    """Will overwrite existing files."""
    with open(filename, "wb") as output:
        output.write(bin_out)
        print()
        print(f"File {filename} written to disc.")


def text_to_binary_morse(text: str) -> []:
    return bin_str_to_bytearray(morse_str_to_bin_str(text_to_morse_str(text)))


def text_to_base64(text: str) -> str:
    return base64.b64encode(text_to_binary_morse(text)).decode('utf-8')


def is_valid_morse(morse: str) -> bool:
    for char in morse:
        if char not in ".-/ ":  # space is allowed for letter separation
            return False
    return True


def is_valid_base64(base64_str: str) -> bool:
    for char in base64_str:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=":
            return False
    return True


def main():
    test_string = "NCL ABCD 1234"
    print(text_to_morse_str(test_string))
    print(morse_str_to_text(text_to_morse_str(test_string)))
    print(base64.b64encode(text_to_binary_morse(test_string)).decode('utf-8'))
    # write_file("morse_bin_output", text_to_binary_morse(test_string))
    # write_file("Ascii_bin_output", bytearray(test_string.encode("ascii")))
    print(base64_to_binary_string("6Oui6jqri46o66Oo6q4u7uK7uKu4quA="))
    print(binary_string_to_morse(base64_to_binary_string("6Oui6gLjqjro6gLu7iu7iruKrgA=")))


if __name__ == "__main__":
    main()
