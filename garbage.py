import binascii


def ascii_to_hex(ascii_str):
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str


ascii_input = 'JIJIDOUMlol'
hex_output = ascii_to_hex(ascii_input)
print('hex result is', hex_output.upper())
life = hex_output.upper().decode("utf-8")
print(life)

print(len(ascii_input),len(ascii_input)%8)
add=8-len(ascii_input)%8
print(add)
if (add!=8):
    for i in range(add):
        ascii_input+="#"

print(ascii_input)

blocks=len(life)/16
print(life[:16])
if(len(life)%8):
    pass