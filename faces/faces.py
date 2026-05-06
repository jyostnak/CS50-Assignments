statement = input("Enter your statement:")
def convert(sentance):
    sentance = sentance.replace(":)", "🙂")
    sentance = sentance.replace(":(","🙁")
    return sentance
print(convert(statement))



