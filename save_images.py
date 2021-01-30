import re
import requests

with open("Hashmasks Provenance Record") as hash:
    while(hash):
        t = hash.readline()
        t0 = t.split("|")
        if len(t0)==3:
            t2 = t0[2]
            t3 = re.search("[a-zA-Z0-9]+", t2)
            if t3:
                t4 = t3.group(0)
                print(f"{t4}")
                r = requests.get(f"https://ipfs.io/ipfs/{t4}")
                img = r.content
                with open(f"{t4}.png", "wb") as t5:
                    t5.write(img)
