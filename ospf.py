import re
preOspfNeig = open("preospfneig.txt","r")
postOspfNeig = open("postospfneig.txt","r")
#preOspfNeig.seek(0)
a = preOspfNeig.read()
b = postOspfNeig.read()
preOspfNeig.seek(0)
c = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(FULL).*(Te.*)\s+',a)
d = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(FULL).*(Te.*)\s+',b)

preupgradeneig = []
for pre in c:
    if pre not in d:
        preupgradeneig.append(pre)

if len(preupgradeneig) == 0:
    print "All Neighbors have formed adjacency after the upgrade"
else:
    print "Following Neighbors have failed to form adjacency after the Upgrade"
    i = 1
    for pre in preupgradeneig:
        print i,". Neighbor "+pre[0]+" on the interface "+pre[2]
        i = i+1
print "\n"
postupgradeneig = []
for post in d:
    if post not in c:
        postupgradeneig.append(post)

if len(postupgradeneig) != 0:
    print "Following Neighbors have formed adjacency only after the upgrade but not before"
    i = 1
    for post in postupgradeneig:
        print i,". Neighbor "+post[0]+" on the interface "+post[2]
        i = i+1





    
        
