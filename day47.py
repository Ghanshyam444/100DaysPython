import random
import string
st = input("Enter a string: ")
coding = input("Enter 1 for coding and 0 for decoding: ")
coding = True if coding == "1" else False
words = st.split(" ")
if(coding):
  nwords = []
  for word in words: 
    if(len(word) >= 3):
      word = word[1:] + word[0]
      r2 = ''.join(random.choices(string.ascii_lowercase, k=3))
      r1 = ''.join(random.choices(string.ascii_lowercase, k=3))
      stnew = r1 + word + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
else:
  nwords = []
  for word in words:
    if(len(word) >= 3):
      word = word[3:-3] 
      stnew = word[-1] + word[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
print(" ".join(nwords))