import random

def getAnswer(answerNumber):
    return_value = ""
    if answerNumber == 1:
       return_value = 'It is certain'
    elif answerNumber == 2:
        return_value =  'It is decidely decidedly so'
    elif answerNumber == 3:
        return_value =  'Yes'
    elif answerNumber == 4:
        return_value =  'Reply hazy try again'
    elif answerNumber == 5:
        return_value =  'Ask again later'
    elif answerNumber == 6:
        return_value =  'Concentrate and ask again'
    elif answerNumber == 7:
        return_value =  'My reply is no'
    elif answerNumber == 8:
        return_value =  'Outlook not so good'
    elif answerNumber == 9:
        return_value =  'Very doubtful'
    return return_value

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
print (r)
