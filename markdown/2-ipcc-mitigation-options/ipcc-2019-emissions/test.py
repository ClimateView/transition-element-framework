
with open("ipcc.csv") as f:
  lines = f.read().split("\n")
  for line in lines:
    md = line.replace("\"","").replace("/","_")
    parts = md.split(".")
    if len(parts)>0:
      depth = len(parts[0])
      print("\t"*2*(depth-1) + "- [[IPCC Hierarchy/"+md+".md|"+md+"]]")
    #with open(md, "w") as w:
    #  w.write("\n")





