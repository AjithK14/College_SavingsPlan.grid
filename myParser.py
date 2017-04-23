def function():
 file = open("bigParse.txt", 'r')
 out = open("output.txt", 'w')
 list = []
 temp = ""
 for line in file:
  if line.replace(" ","") == "":
   pass
  elif line == line.upper():
   temp = line
  else:
   list.append(temp)
   out.write(line)
 for string in list:
  out.write(str(string))
 file.close()
 out.close()
function()