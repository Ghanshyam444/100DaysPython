#KBC
questions = [
  ["Which language was used to create FB?","Python","French","JavaScript","PHP","None",4],
  ["What is the capital of Australia?","Sydney","Melbourne","Canberra","Perth","None",3],
  ["Which of the following is a programming language?","HTML","CSS","Java","XML","None",3],
  ["What is the currency of Japan?","Yen","Dollar","Rupee","Euro","None",1],
  ["Which of the following is a mammal?","Whale","Shark","Tuna","Dolphin","None",1],
  ["Which of the following is a reptile?","Whale","Shark","Tuna","Crocodile","None",4],
  ["Which of the following is a bird?","Whale","Shark","Tuna","Sparrow","None",4],
  ["Which of the following is a fish?","Whale","Shark","Tuna","Sparrow","None",3],
  ["Which of the following is a fruit?","Whale","Shark","Tuna","Apple","None",4],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range(0,len(questions)):
  question = questions[i]
  print(f"Question for Rs. {levels[i]}")
  print(f"Q{i+1}. {question[0]}")
  print(f"a. {question[1]}                      b. {question[2]} ")
  print(f"c. {question[3]}                      d. {question[4]} ") 
  reply = int(input("Enter your choice (1-4) : "))
  if(reply == question[6]):
    print(f"Correct answer! You have won Rs. {levels[i]}")
    if(i==4):
      money = 10000
    elif(i==9):
      money = 320000
    elif(i==14):
      money = 10000000
  else:
    print("Wrong answer! Game Over")
    break
  
print(f"Congratulations! You have won Rs. {money}")