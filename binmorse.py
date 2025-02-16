#!/usr/bin/env python
import click
import utilities


@click.command()
@click.option('-t', '--text', help='Text enclosed in quotes.')
@click.option('-b', '--binary', help='Base64 encoded binary.')
@click.option('-m', '--morse', help='Morse code. dot=., dash=-, Words separated by /.')
@click.option('-o', '--output_file', help='Output to file with this name. Will overwrite existing files.')
@click.option('-tb', '--text_to_binary', help='Changes input text to binary.', is_flag=True)
@click.option('-tm', '--text_to_morse', help="Changes input text to morse code.", is_flag=True)
@click.option('-mt', '--morse_to_text', help="Changes input morse code to text.", is_flag=True)
@click.option('-mb', '--morse_to_binary', help="Changes input morse code to binary.", is_flag=True)
@click.option('-bt', '--binary_to_text', help="Changes input binary to text.", is_flag=True)
@click.option('-bm', '--binary_to_morse', help="Changes input binary to morse code.", is_flag=True)
def main(text, binary, morse, output_file, text_to_binary, text_to_morse, morse_to_text,
         morse_to_binary, binary_to_text, binary_to_morse):
    printable_output = ""

    if text_to_binary and text:
        printable_output = utilities.text_to_base64(text)
    if text_to_morse and text:
        printable_output = utilities.text_to_morse(text)
    if binary_to_text and binary:
        printable_output = utilities.base64_to_text(binary)
    if binary_to_morse and binary:
        printable_output = utilities.base64_to_morse(binary)
    if morse_to_text and morse:
        printable_output = utilities.morse_to_text(morse)
    if morse_to_binary and morse:
        printable_output = utilities.morse_str_to_base64(morse)
    if (text_to_binary or text_to_morse) and not text:
        print("Text is required for text conversion.")
    if (binary_to_text or binary_to_morse) and not binary:
        print("Binary is required for binary conversion.")
    if (morse_to_text or morse_to_binary) and not morse:
        print("Morse is required for morse conversion.")
    if output_file:
        if text_to_binary and text:
            utilities.write_file(output_file, utilities.text_to_binary_morse(text))
        elif text_to_morse and text:
            utilities.write_file(output_file, utilities.text_to_morse(text))
        elif printable_output != "":
            utilities.write_file(output_file, printable_output)
        else:
            print("No output to write to file.")

    print(printable_output)


if __name__ == "__main__":
    main()
