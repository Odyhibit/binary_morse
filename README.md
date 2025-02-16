# Binary Morse Code Converter
This is a simple script that converts text to ascii morse code, or binary morse code. You can swap between those 3 different mode using options on the command line.

```bash
Usage: binmorse.py [OPTIONS] <input>

  "Converts text, binary morse, and ascii morse code to each other. Use base64
  encoding for binary input."

  examples:
  binmorse.py -tb "Hello World"
  binmorse.py -mb ".... . .-.. .-.. --- /.-- --- .-. .-.. -.."
  binmorse.py -bt qiLqLqO7gLuO7i6LqOoA

Options:
  -o, --output_file TEXT  Output filename. Will overwrite existing files.
  -tb, --text_to_binary   Changes input_string text to binary.
  -tm, --text_to_morse    Changes input_string text to morse code.
  -mt, --morse_to_text    Changes input_string morse code to text.
  -mb, --morse_to_binary  Changes input_string morse code to binary.
  -bt, --binary_to_text   Changes input_string binary to text.
  -bm, --binary_to_morse  Changes input_string binary to morse code.
  --help                  Show this message and exit.

```
They examples above will produce the following output:

```bash
    qiLqLqO7gLuO7i6LqOoA
    qiLqLqO7gLuO7i6LqOoA
    Hello World
 ```
The binary format is in base64, so it can be easily copied and pasted.

If you decode the base64 into binary you will see the following:
```bash
    101010100010001011101010001011101010001110111011100000001011101110001110111011100010111010001011101010001110101000000000
```
Each dot is 10, and each dash is 1110. The space between each letter is 00, and the space between each word is 0000.

You could recover the original text using a simple find and replace operation (longest to shortest), or use this script.

If you wish to save binary content, and not have it converted to base64, you can use the -o option to specify a filename.

```bash
    binmorse.py -tb "Hello World" -o output.dat
```
This will produce a binary file with the contents:
```
AA 22 EA 2E A3 BB 80 BB 8E EE 2E 8B A8 EA 00
```
Which matches the binary content of the base64 encoded binary morse above.