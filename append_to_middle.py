import re
string="manav"
match=re.search("m|3|e",string)
if not match:
  print("No match found")
else:
  print("Match found")