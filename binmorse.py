#!/usr/bin/env python
import click
from utilities import *


@click.command()
@click.argument('input_string', required=True, metavar='<input>', type=click.STRING)
@click.option('-o', '--output_file', help='Output filename. Will overwrite existing files.')
@click.option('-tb', '--text_to_binary', help='Changes input_string text to binary.', is_flag=True)
@click.option('-tm', '--text_to_morse', help="Changes input_string text to morse code.", is_flag=True)
@click.option('-mt', '--morse_to_text', help="Changes input_string morse code to text.", is_flag=True)
@click.option('-mb', '--morse_to_binary', help="Changes input_string morse code to binary.", is_flag=True)
@click.option('-bt', '--binary_to_text', help="Changes input_string binary to text.", is_flag=True)
@click.option('-bm', '--binary_to_morse', help="Changes input_string binary to morse code.", is_flag=True)
def main(input_string, output_file, text_to_binary, text_to_morse, morse_to_text,
         morse_to_binary, binary_to_text, binary_to_morse):
    """Converts text, binary morse, and ascii morse code to each other. Use base64 encoding for binary input.

    \b
    examples:
    binmorse.py -tb "Hello World"
    binmorse.py -mb ".... . .-.. .-.. --- /.-- --- .-. .-.. -.."
    binmorse.py -bt qiLqLqO7gLuO7i6LqOoA
    """
    printable_output = ""

    if text_to_binary and input_string:
        printable_output = text_to_base64(input_string)
    if text_to_morse and input_string:
        printable_output = text_to_morse_str(input_string)
    if binary_to_text and is_valid_base64(input_string):
        printable_output = base64_to_text(input_string)
    if binary_to_morse and is_valid_base64(input_string):
        printable_output = base64_to_morse(input_string)
    if morse_to_text and is_valid_morse(input_string):
        printable_output = morse_str_to_text(input_string)
    if morse_to_binary and is_valid_morse(input_string):
        printable_output = morse_str_to_base64(input_string)
    if (text_to_binary or text_to_morse) and not input_string:
        print("Text is required for text conversion.")
    if (binary_to_text or binary_to_morse) and not is_valid_base64(input_string):
        print("Binary is required for binary conversion.")
    if (morse_to_text or morse_to_binary) and not is_valid_morse(input_string):
        print("Morse is required for morse conversion.")
    if output_file:
        if text_to_binary and input_string:
            write_file(output_file, text_to_binary_morse(input_string))
        elif morse_to_binary and is_valid_morse(input_string):
            write_file(output_file, morse_str_to_bytearray(input_string))
        elif printable_output != "":
            write_file(output_file, printable_output)
        else:
            print("No output to write to file.")

    print(printable_output)


if __name__ == "__main__":
    main()
