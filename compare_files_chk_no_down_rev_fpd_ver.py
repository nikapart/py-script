import re
filename1 = "post_chk_down_rev_fpd.txt"

f1 = open(filename1)
post = f1.read()
post  = post.split("\n")
#print post
upgrade_lst = []
upgrade_dict = {}
for op in post:   
   if re.match(".*Yes|yes", op):         
         if re.match("(\d+/\S+/\S+)\s+(\S+)\s+\d+\.\d+\s+\S+\s+(\S+)\s+\d+\s+(\d+\.\d+)\s+Yes|yes", op):
            (loc, cardType, subType, swVer) = re.match("(\d+/\S+/\S+)\s+(\S+)\s+\d+\.\d+\s+\S+\s+(\S+)\s+\d+\s+(\d+\.\d+)\s+Yes|yes", op).groups()
            upgrade_dict[loc] = {}
            upgrade_dict[loc][cardType] = {}
            upgrade_dict[loc][cardType][subType] = swVer            
         elif re.match("\s*\S+\s+(\S+).*(\d+\.\d+)\s+Yes|yes", op):
            (subType, swVer) = re.match(".*[A-Za-z]+\s+(\S+)\s+\d+\s+(\d+\.\d+)\s+Yes", op).groups()
            upgrade_dict[loc][cardType][subType] = swVer          
            
mnum = 1
snum = 1
if upgrade_dict:
   print "The Following needs uprade:"
   print "-----------------------------\n"
   for loc in upgrade_dict.keys():
      print str(mnum)+". Location: "+loc
      for card in upgrade_dict[loc].keys():
         print "   CardType: "+card
         for sub in upgrade_dict[loc][card].keys():
            print "   "+str(snum)+".Subtype: "+sub
            print "    Sw Version: "+upgrade_dict[loc][card][sub]
            snum +=1
         snum = 1
      print "\n"
      print "---------------------------------------------------"
      mnum+=1
else:
   print "No FPD upgrade needed"
   
         
   
            
"""

sno = 1
if len(upgrade_lst) == 0:
   print "No upgrade needed"
else:
   print "The following needs an upgrade"
   for lst in upgrade_lst:
      print "    "+str(sno)+"."
      print "\tLocation: "+lst['loc']
      print "\tCard Type: "+lst['cardType']
      print "\tSubType: "+lst['subType']
      print "\tSoftware Version: "+lst['swVer']
      print "\n"
      sno+=1
"""

#0/RSP0/CPU0  A9K-RSP440-SE              1.0   lc   cbc     0      16.116    Yes
      

      
"""
neigh_pfx_lst_pre = []
for op in pre:
   neigh_pfx_dict = {}
   if re.match("\d+\.\d+\.\d+\.\d+.*\d+:\d+:\d+\s+\d+",op):
       (bgpNeigh, prefixCnt) = re.match("(\d+\.\d+\.\d+\.\d+).*\d+:\d+:\d+\s+(\d+)",op).groups()
       neigh_pfx_dict['bgpNeigh']=bgpNeigh
       neigh_pfx_dict['pfxCnt']=prefixCnt
       neigh_pfx_lst_pre.append(neigh_pfx_dict)
       
neigh_lst_pre = []
for neig in neigh_pfx_lst_pre:
   neigh_lst_pre.append(neig['bgpNeigh'])

print "pre upgrade list: ",neigh_pfx_lst_pre
print len(neigh_pfx_lst_pre)


neigh_pfx_lst_post = []
for op in post:
   neigh_pfx_dict = {}
   if re.match("\d+\.\d+\.\d+\.\d+.*\d+:\d+:\d+\s+\d+",op):
       (bgpNeigh, prefixCnt) = re.match("(\d+\.\d+\.\d+\.\d+).*\d+:\d+:\d+\s+(\d+)",op).groups()
       neigh_pfx_dict['bgpNeigh']=bgpNeigh
       neigh_pfx_dict['pfxCnt']=prefixCnt
       neigh_pfx_lst_post.append(neigh_pfx_dict)

neigh_lst_post = []
for neig in neigh_pfx_lst_post:
   neigh_lst_post.append(neig['bgpNeigh'])


print "post upgrade list: ",neigh_pfx_lst_post
print len(neigh_pfx_lst_post)

print "Comparing Pre and Post output:"
print "----------------------------------\n"

prelst2 = []
pre_pfx_fail_lst = []
pre_bgpneigh_fail_lst = []
      
for lst in neigh_pfx_lst_pre:
   for poslst in neigh_pfx_lst_post:
      pre_pfx_fail_dict = {}
      if lst['bgpNeigh'] == poslst['bgpNeigh']:
         if int(lst['pfxCnt']) != int(poslst['pfxCnt']):
            pre_pfx_fail_dict['bgpNeigh'] = lst['bgpNeigh']
            pre_pfx_fail_dict['prePfxCnt'] = lst['pfxCnt']
            pre_pfx_fail_dict['posPfxCnt'] = poslst['pfxCnt']
            pre_pfx_fail_lst.append(pre_pfx_fail_dict)      


print "\nBGP Neigbors not in established state post upgrade:"
num = 1
for nei in neigh_lst_pre:
   if nei not in neigh_lst_post:
      print str(num)+". "+nei
      num+=1

print "\nPrefix Count changed for BGP Neighbors post upgrade:"
for pfx in pre_pfx_fail_lst:
   print "Neighbor: ",pfx['bgpNeigh']
   print "Prefix Count before upgrade: ",pfx['prePfxCnt']
   print "Prefix Count post upgrade: ",pfx['posPfxCnt']
   
   
         
            
print "\nAdditional Neighbors found post upgrade:"
num = 1
for nei in neigh_lst_post:
   if nei not in neigh_lst_pre:
      print str(num)+". "+nei
      num+=1
      
"""
      

       
       
       

"""print "Line present in Pre-check but not in Post-check : "
prestep = None
for pr in pre1:
  if pr != "":
    if pr in post1:
      pass
    else:
      prestep = 0
      print pr
      
print "\n\n"
print "Line present in Post-check but not in Pre-check: "
poststep = None
for po in post1:
  if po != "":
    if po in pre1:
      pass
    else:
      poststep = 0
      print po

if prestep is None and poststep is None:
  print "Both the files matched"

"""

"""diffInstance = difflib.Differ()
diffList = list(diffInstance.compare(text1Lines, text2Lines))
print '-'*50
print "Lines different in text1 from text2:"
for line in diffList:
  if line[0] == '-':
    print line,
"""
