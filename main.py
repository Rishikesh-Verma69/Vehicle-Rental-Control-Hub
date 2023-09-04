import mysql.connector as a
import tabulate as t

print("\033[95m\033[92m\033[1m\033[4mCAR RENTAL MANAGEMENTSYSTEM\033[0m")
x = a.connect(host="localhost",user = "root",passwd='',database='car')
def der():
    for i in range(70):
        print("\033[4m\033[96m=\033[0m", end="")
    print("\n")
def show(x):
    print("\x1b[60;30;42mPython Successfully connected to the database\x1b[0m")
    c = x.cursor()
    c.execute('select * from rental')
    f = [(' customer name ',' Car company ',' Model name ',' price as per day',' Date of Booking ',' Number of Days ',' Total Bill ')]
    for i in c:
        f.append(i)
    print(t.tabulate(f, headers="firstrow",tablefmt="pretty"))
    der()
def ins(x):
    der()
    print("\x1b[60;30;42mPython Successfully connected to the database\x1b[0m")
    c = x.cursor()
    ch = 1
    na = input("Enter your Name: ")
    print('''Select Your Car Company:
    1. Hyundai.
    2. Toyota.
    3. Mahindra.
    4. Tata Motors.
    5. Maruti Suzuki.
    6. Tesla.
    7. BMW.
    8. Ford
    9. Ferrari
    10. Audi''')
    se = int(input("Enter Your Choice: "))
    if se == 1:
        cm = "Hyundai"
        print('''Select Model from Hyundai: price:
        1. Tucson 6,000
        2. Kona 8,000
        3. i20 5,500
        4. Elantra 8,800
        5. Creta 7,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Tuscson"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 : "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 2:
            mm = "Kona"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 3:
            mm = "i20"
            pri = 5500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 4:
            mm = "Elantra"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 5:
            mm = "Creta"
            pri = 7000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!! selection will re start!!!!!""")
            ins(x)
    elif se == 2:
        cm = 'Toyota'
        print('''Select Model from Toyota: price:
            1. Yaris 5,000
            2. Camry 5,400
            3. Fortuner 8,500
            4. Vellfire 9,800
            5. Glanza 4,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Yaris"
            pri = 5000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 2:
            mm = "Camry"
            pri = 5400
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 3:
            mm = "Fortuner"
            pri = 8500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 4:
            mm = "VellFire"
            pri = 9800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        elif cmod == 5:
            mm = "Glanza"
            pri = 4000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!! selection will re start!!!!!""")
            ins(x)
    if se == 3:
        cm = 'Mahindra'
        print('''Select Model from Mahindra: price:
        1. Thar 6,000
        2. Scorpio 4,000
        3. XUV300 5,500
        4. Bolero 7,800
        5. XUV500 5,800''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Thar"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Scorpio"
            pri = 4000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "XUV300"
            pri = 5500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Bolero"
            pri = 7800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "XUV500"
            pri = 5800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 4:
        cm = 'Tata Motors'
        print('''Select Model from Tata Motors: price:
        1. Safari 6,000
        2. Nexon 8,000
        3. Altroz 6,500
        4. Tiago 4,800
        5. Harrier 7,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Safari"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Nexon"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "Altroz"
            pri = 6500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Tiago"
            pri = 4800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "Harrier"
            pri = 7000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 5:
        cm = 'Maruti Suzuki'
        print('''Select Model from Maruti Suzuki: price:
        1. Swift 4,000
        2. Baleno 8,000
        3. Ertiga 5,500
        4. Vitara Brezza 8,800
        5. Alto 3,500''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Swift"
            pri = 4000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Baleno"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "Ertiga"
            pri = 5500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Vitara Brezza"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "Alto"
            pri = 3500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 6:
        cm = 'Tesla'
        print('''Select Model from Tesla: price:
        1. Model 3 6,900
        2. Model S 8,000
        3. Model X 7,500
        4. Model Y 8,800''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Model 3"
            pri = 6900
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Model S"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "Model X"
            pri = 7500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Model Y"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 7:
        cm = 'BMW'
        print('''Select Model from BMW: price:
        1. X5 6,000
        2. X1 8,000
        3. X3 5,500
        4. Z4 8,800
        5. X7 7,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "X5"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "X1"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "X3"
            pri = 5500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Z4"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "X7"
            pri = 7000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 8:
        cm = 'Ford'
        print('''Select Model from Ford: price:
            1. Mustang 6,000
            2. Figo 6,000
            3. EcoSport 7,500
            4. Aspire 4,800
            5. Freestyle 5,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Mustang"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Figo"
            pri = 6000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "EcoSports"
            pri = 7500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Aspire"
            pri = 4800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "Freestyle"
            pri = 5000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
                selection will re start!!!!!""")
            ins(x)
    if se == 9:
        cm = 'Dodge'
        print('''Select Model from Ferrari: price:
            1. Challenger 9,000
            2. Demon 9,999
            3. Charger 9,900
            4. SRT Hell Cat 8,800
            5. Durango 8,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "Challenger"
            pri = 9000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "Demon"
            pri = 9999
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "Charger"
            pri = 9900
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "STR Hell Cat"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "Durango"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
            selection will re start!!!!!""")
            ins(x)
    if se == 10:
        cm = 'Audi'
        print('''Select Model from Audi: price:
            1. A4 7,000
            2. A6 8,000
            3. Q2 6,500
            4. Q8 8,800
            5. RS Q8 7,000''')
        cmod = int(input("Enter your choice(1,2,3...) : "))
        if cmod == 1:
            mm = "A4"
            pri = 7000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 2:
            mm = "A6"
            pri = 8000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 3:
            mm = "Q2"
            pri = 6500
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 4:
            mm = "Q8"
            pri = 8800
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 "))
            if ch == 1:
                ins(x)
            else:
                menu()
        if cmod == 5:
            mm = "RS Q8"
            pri = 7000
            tim = input("Enter todays date(YYYY-MM-DD): ")
            nd = int(input("Enter the no of days for rent: "))
            tot = (nd * pri)
            sql = "INSERT INTO rental VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (na, cm, mm, pri, tim, nd, tot)
            c.execute(sql, val)
            x.commit()
            show(x)
            ch = int(input("To Enter More Recode Press 1 : "))
            if ch == 1:
                ins(x)
            else:
                menu()
        else:
            print("""You have entered the wrong number !!!!
            selection will re start!!!!!""")
            menu()
    else:
        print("Please select carefully!!")
        ins(x)
def menu():
    print("""Select your Operation:
    1. Insert new data.
    2. show existing data.
    3. Show Car Companies.
    4. exit. """)
    q = int(input("Enter your Choice: "))
    if q==1:
        ins(x)
    if q==2:
        show(x)
    menu()
    if q==3:
        print("""Select Your Car Company:
            1. Hyundai.
            2. Toyota.
            3. Mahindra.
            4. Tata Motors.
            5. Maruti Suzuki.
            6. Tesla.
            7. BMW.
            8. Ford
            9. Ferrari
            10. Audi""")
    der()
    menu()
    if q==4:
        exit()
    else:
        print("Please select carefully!! ")
        der()
        menu()
menu() 
