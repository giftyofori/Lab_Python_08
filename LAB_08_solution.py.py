import re
# Q 03
def isEmail(inp):
  return re.search(r'|R(\w*\s*!$)\.(\w+),inp) !=None
# Q 04
def getTxts(files):
  return re.findall(r'\w*.txt',files)

# Q 05
def percAwesome(inp):
  result = len(re.findall(r"awes[o|\d]me",inp))
  everything =len(inp.split())
  return round((float(result)/float(everything))*100,1)
