bill = input("What was the bill? ")
service = input("How was the service? ")#bad,okay,good,great
if service == "bad":
    print (f"0% tip worth $0")
elif service == "okay":
    print (f"5% tip worth ${float(bill)*0.05}")
elif service == "good":
    print (f"10% tip worth ${float(bill)*0.1}")
elif service == "great":
    print (f"15% tip worth ${float(bill)*0.15}")
else:
    print ("invalid answer")