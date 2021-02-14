
import urllib
import os

def fr(cloudfilename, storage):
    url=storage.child(cloudfilename).get_url(None)
    f=urllib.request.urlopen(url).read()

    f = str(f)

    a, f, b = f.split("'")

    return f

def fw(text, cloudfilename, storage):
    #upload a file to storage

    try:
        fw = open(cloudfilename, "w")
        loc = cloudfilename
    except:
        fw = open("testfile.txt", "w")
        loc = "testfile.txt"

    fw.write(text)
    fw.close()

    storage.child(cloudfilename).put(loc)

    os.remove(loc)

