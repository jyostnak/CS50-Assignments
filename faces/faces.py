statement = input("Enter your statement:")
def convert(sentance):
    smile_converted = sentance.replace(":)", "🙂")
    frown_converted = sentance.replace(":(","🙁")
    return sentance
print(convert(statement))



