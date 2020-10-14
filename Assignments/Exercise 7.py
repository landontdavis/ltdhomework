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
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        floattotal += float(line[19:])
        count += 1
if count > 0:
    final = floattotal/count

print(final)
