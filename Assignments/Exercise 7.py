fname=input("Enter file name: ")
try:
    fh=open(fname)
except:
    print('File cannot be opened:',fname)
    exit()

fh=open(fname)
count=0
floattotal = 0
for line in fh:
    count += 1
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        floattotal += float(line[:19])
if count > 0:
    final = floattotal/count
