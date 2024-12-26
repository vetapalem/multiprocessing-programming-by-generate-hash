import os ,secrets as ss ,concurrent.futures as c

tracker = []




def  hash_generte(a):
  return ss.token_hex(25)



with c.ProcessPoolExecutor() as execute:

  result = execute.map(hash_generte,[a for a in range(100000)])

  for (a,b) in enumerate(result,start=1):
    if a not in tracker:
      tracker.append(a)
      print(a,True)
    else:
      print(a,False,sep="------")
