
import urllib.request
import requests
import os
import json
from PIL import Image

data = requests.get("https://produce-codes-library.github.io/plu-data/data/plu_data.json").json()

failed = []
passed = []

for plu in data:
	
	try:
		'''
		extension = plu["image"].split(".")[-1]
		output = f"{plu['plu']}.{extension}"
		urllib.request.urlretrieve(plu["image"], output)

		basewidth = 600
		img = Image.open(output)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		os.remove(output)
		img.save(plu['plu'] + ".jpg")

		'''

		files = os.listdir()
		plu["image"] = "https://produce-codes-library.github.io/plu-data/images/" + list(filter(lambda x:x[:4] == plu["plu"], files))[0]
		passed.append(plu["plu"])


	except:
		failed.append(plu["plu"])

	

with open("plu_data.json", "w") as f:
	f.write(json.dumps(data, indent=2))

print(failed)