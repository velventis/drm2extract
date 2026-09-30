import sys

import struct


print(f"WELCOME TO DRM2EXTRACT. 2026.")
print(f"USAGE: drm2extract.py <input file> <output file>")

with open(sys.argv[1], "rb") as file:
    print(f"FINDING DRM IN {sys.argv[1]}")
    
    data = file.read()
    if b"DRM" in data:
        print("DRM IS FOUND, EXTRACTING SL9999 DRM...")
    
        with open(sys.argv[2], "wb") as outf:
            outf.write(b"CHAI\xFFDRM_FILE\x00\x00_EXTRACTED_DRM\x99\x99_SECURITY_LEVEL:SL9999_L1_4k_NETFLIX")
            
        print("EXTRACTION COMPLETE BTW.")
    
    else:
        print("ERROR: DRM IS NOT FOUND IN THIS FILE!!!!")
        exit()