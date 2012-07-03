import re
# Q 03
def isEmail(inp):
  return re.search(r"[\w$]@*\w+(\.\w)",inp) !=None
# Q 04
def getTxts(files):
  return re.findall(r'[a-z]*.txt',files)

# Q 05
def percAwesome(inp):
  search = re.findall(r"awes[o|\d]me",inp)
  sentence =len(inp.split())
  return round((len(search)/float(sentence))*100,1)
