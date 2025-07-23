with open("metin2.exe", "wb") as f:
    f.write(b'\x4D\x5A')              # Header "MZ" di un file .exe valido
    f.write(b'\x00' * (1024 * 32))    # 32 KB di spazio (dummy content)

print("? File metin2.exe generato con successo (32KB segnaposto)")
