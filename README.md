# Binary Morse Code Converter
This is a simple script that converts text to ascii morse code, or binary morse code. You can swap between those 3 different mode using options on the command line.
    
Here are three examples using the script:
```bash
    binmorse.py -tb "Hello World"
    binmorse.py -mb ".... . .-.. .-.. --- /.-- --- .-. .-.. -.."
    binmorse.py -bt qiLqLqO7gLuO7i6LqOoA
```
They will produce the following output:

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