# genera_mc_dll.py
with open("mc.dll", "wb") as f:
    f.write(b'\x4D\x5A')              # Header PE (MZ)
    f.write(b'\x00' * (4096 - 2))     # Padding per completare a 4096 byte

print("? mc.dll creato correttamente (4096 byte)")
