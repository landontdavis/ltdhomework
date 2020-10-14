fname=input("Enter file name: ")
try:
    fh=open(fname)
except:
    print('File cannot be opened:',fname)
    exit()

fh=open(fname)
count=0
for line in fh:
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        print(line)
