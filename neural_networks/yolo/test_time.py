import time
start = time.time()
f = open("time.txt", "a")

end = time.time()
f.write("\n")
f.write(f"{end - start}")
f.close()