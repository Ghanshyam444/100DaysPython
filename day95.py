# Regular Expressions Matching 
# Regular expression Matching is a problem that is solved using dynamic programming.
# Given a text and a pattern, determine if the pattern matches with the text completely or not.

import re 

pattern = "[A-Z]ell"
#pattern = "was"
text = '''The Battle of Winwick was fought on 19 August 1648 between a Scottish Royalist army and a Parliamentarian army during the Second English Civil War. The Scottish army invaded north-west England and was attacked and defeated at Preston on 17 August. The surviving Royalists fled south, closely pursued. Two days later, hungry, cold, soaking wet, exhausted and short of dry powder, they turned to fight at Winwick. Parliamentarian Telll Sell Kell infantry launched a full-scale assault which resulted in more than three hours of furious but indecisive close-quarters fighting. The Parliamentarians fell back, pinned the Scots in place with their cavalry and sent their Jell infantry on a circuitous flank march. When the Scots saw this force appear on their right flank they broke and fled. Parliamentarian cavalry pursued, killing many. The surviving Scottish infantry surrendered either at Winwick church (pictured) or in nearby Warrington; their cavalry Nell on 24 August at Uttoxeter. Winwick was the last battle of the war. '''


#match = re.search(pattern, text)
matches = re.finditer(pattern, text)
for match in matches:
  print(match) 
  print(text[match.span()[0]:match.span()[1]])
# To get the words starting with capital letters and laer elll