import re
filename1 = "pre_out_SMU_check.txt"
filename2 = "post_out_SMU_check.txt"

f1 = open(filename1,'r')
f2 = open(filename2,'r')

pre = f1.read()
prelst  = pre.split("\n")

post = f2.read()
post  = re.split("\S+\s+Packages",post)
post1 = post[1].split("\n")

postlst = []
for pos in post1:
  pos = pos.strip()
  if pos == ':' or pos == "":
    continue
  else:
    postlst.append(pos[6:])

postfail = []
for pre in prelst:
  if pre in postlst:
    pass
  else:
    postfail.append(pre)

sno = 1
if len(postfail) != 0:
  print "SMUs not found post upgrade: "
  for pos in postfail:
    print str(sno)+". "+pos
    sno+=1
else:
  print "All SMU packages found post upgrade"
   
print "\n------------------------------------------------------------------\n"
postaddn = []
for pos in postlst:
  if pos not in prelst:
    postaddn.append(pos)
sno=1
if len(postaddn) != 0:
  print "Additional SMUs found post upgrade: "
  for pos in postaddn:
    print str(sno)+". "+pos
    sno+=1
    


