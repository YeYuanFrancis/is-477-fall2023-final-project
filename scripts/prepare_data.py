import requests
import os
import zipfile

wine_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'

path = "data/wine"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
    
url= 'https://archive.ics.uci.edu/static/public/109/wine.zip'
response = requests.get(url)

with open ('data/wine/wine.zip', mode='wb') as f: 
    f.write(response.content)

import hashlib
filename = 'data/wine/wine.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    
if wine_sha256 != sha256hash:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")

if wine_sha256 == sha256hash:
    with zipfile.ZipFile('data/wine/wine.zip', 'r') as zip_ref:
        zip_ref.extractall('data/wine')
    print("Extraction complete.")
else:
    print("Computed hash does not match expected hash. Halting extraction.")
