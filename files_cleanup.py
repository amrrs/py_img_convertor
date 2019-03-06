import os
for file in glob.glob("*.jpg"):
    os.remove(file)
