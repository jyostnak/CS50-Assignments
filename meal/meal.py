def main():
    time = input("What time is it?")
    converted_time = convert(time)
    if converted_time>=7 and converted_time<=8:
        print("Breakfast Time")
    if converted_time>=12 and converted_time<=13:
        print('Lunch Time')
    if converted_time>=18 and converted_time<=19:
        print('Dinner Time')


def convert(time):
    time = time.replace(':',"")
    if len(str(time))==3:
        time = str(time)
        a = int(time[0])
        b = int(time[1:])/60
        return a+b

    if len(str(time))==4:
        time = str(time)
        a = int(time[:2])
        b = int(time[2:])/60
        return a+b


if __name__ == "__main__":
    main()
