inp = input("File name: ")

if ".gif" in inp:
    print("image/gif")
elif ".jpg" in inp:
    print("image/jpeg")
elif ".jpeg" in inp:
    print("image/jpeg")
elif ".png" in inp:
    print("image/png")
elif ".pdf" in inp:
    print("application/pdf")
elif ".txt" in inp:
    print("text/plain")
elif ".zip" in inp:
    print("application/zip")
else:
    print("application/octet-stream")
