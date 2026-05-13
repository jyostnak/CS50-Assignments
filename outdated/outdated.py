months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
] #12-23-2007
def convert():
    n = input('Date: ')
    if 11<=len(n)<=20:
        lst = n.split()
        if lst[0] in months:
            date = str(lst[1])
            date = date.replace(',','')
            if int(date)<1 or int(date)>31:
                raise ValueError
            year = lst[2]
            if len(year) != 4:
                raise ValueError
            month = str(months.index(lst[0]) + 1)
            if int(month)<1 or int(month)>12:
                raise ValueError
            if len(date) == 1:
                date = '0'+date
            if len(month) == 1:
                month = '0'+month
            print(f'{year}-{month}-{date}')
        else:
            raise KeyError
    if len(n)<=10:
        lst1 = n.split('/')
        month1 = lst1[0]
        date1 = lst1[1]
        year1 = lst1[2]
        if len(year1) != 4:
            raise ValueError
        if int(date1)>31 or int(date1)<1:
            raise ValueError
        if int(month1)>12 or int(month1)<1:
            raise ValueError
        if len(date1) == 1:
            date1 = '0'+date1
        if len(month1) == 1:
            month1 = '0'+month1
        print(f'{year1}-{month1}-{date1}')
while True:
    try:
        convert()
        break
    except KeyError:
        pass
    except ValueError:
        pass
