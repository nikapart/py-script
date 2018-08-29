import re
filename1 = "pre_out_bgp_neigh.txt"
filename2 = "post_out_bgp_neigh.txt"

f1 = open(filename1,"r")
f2 = open(filename2,"r")

pre = f1.read()
pre  = pre.split("\n")

pre2 = f1.readlines(0)
print pre2


post = f2.read()
post  = post.split("\n")

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
num=1
for pfx in pre_pfx_fail_lst:
   print str(num)+"."
   print " Neighbor: ",pfx['bgpNeigh']
   print " Prefix Count before upgrade: ",pfx['prePfxCnt']
   print " Prefix Count post upgrade: ",pfx['posPfxCnt']
   print "\n"
   num+=1

print "\nAdditional Neighbors found post upgrade:"
num = 1
for nei in neigh_lst_post:
   if nei not in neigh_lst_pre:
         print str(num)+". "+nei
         num+=1

      

       
       
       

