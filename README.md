# Base_EN_DE_Coder
You can encode and decode b85, a85, b64, b32, and b16 with this tool.
--------------- Encoding ---------------
Step 1: Run the program.
Step 2: Enter '1'.
Step 3: write your text.
Step 4: write map for encoding like: 'b64, b32, b16, b85, r, a85'. (r: reverse, b64: Base64, a85: Ascii85)
Step 5: copy your encoded text and enter 'q' to exit from program.
--------------- Decoding ---------------
Step 1: Run the program.
Step 2: Enter '2'.
Step 3: Enter encoded text.
Step 4: Enter number of steps, for example if your encoded text twice encoded, enter 2.
Step 5: Verify that it has been decoded correctly.(if it is True write 'y' and if it is False write 'n')
Step 6: Copy your decoded text and enter 'q' to exit from program.
--------------- Decode with map ---------------
Step 1: Run the program.
Step 2: Enter '3'.
Step 3: Enter encoded text.
Step 4: Enter a map to decode your code like: b32, b16, r, b64, b85, r, a85. (r: reverse, b64: Base64, a85: Ascii85)
< Reverse the build map to made the map for decoding. >
Step 6: Copy your decoded text and enter 'q' to exit from program.
--------------- HINT ---------------
When you enter 'n' to verify the decoder, the program removes the last decoder.(If you enter None it's True for program.)
You can enter None for number of step(s).(Default steps = 10)
