#must be called from the directory with corpus files

file= open("SB_words.txt", "w")

import re
import os
def get_words(file):
     with open(file) as fp:
         for result in re.findall('<w>(.*?)<', fp.read(), re.S):
		with open("SB_words.txt", "a") as myfile:
    			myfile.write(bytes.lower(result))
    			myfile.write(" ")
for f in os.listdir('/Users/callab/Downloads/valian_sbcsae/SBCSAE-xml/'):
	get_words(f)






#def remove_char(text):
#   return ''.join(i for i in text if ord(i)<128)
#with open("SB_words.txt", "a") as myfile:
#	remove_char("SB_words.txt")


#need a way to drop the special cases
#  <p type= " "/>t
#  things<overlap-point start-end="start" top-bottom="top"/><p type="drawl"/>
# even this 
#  S<overlap-point start-end="end" top-bottom="bottom"/>outh



# old attempt
#with open("/Users/callab/Downloads/SBCSAE-xml/SBC001.xml") as input_data:
    # Skips text before the beginning of the interesting block:
 #   for line in input_data:
  #      if line.strip() == '<w>':  # Or whatever test is needed
   #         break
    # Reads text until the end of the block:
    #for line in input_data:  # This keeps reading the file
     #   if line.strip() == '</w>':
      #      break
        # print line  # Line is extracted (or block_of_lines.append(line), etc.)