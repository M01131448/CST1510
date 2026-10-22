"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Haidar Ali Tajoo
Lane  :   / Cyber /      
Date  : 10.10.2026

Run it:   python template.py
"""

def status_of(percent):
    """This function displays the status of percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING" 
    else:
        return "OK"

def check(value, limit):
    """This function calculates the difference and percentage and returns it to difference and percent"""
    difference = limit - value
    percentage = (value / limit) * 100
    return difference, percentage

def print_report(label, value, limit, difference, percent, status):
    """This Function is the main printing output to display the record"""
    print("=" * 34)
    print(f"  SOURCE IP  -  {label:>10}")
    print("=" * 34)
    print(f"Failed Logins : {value:>10}")
    print(f"Total Attempts: {limit:>10}")
    print(f"Attempts Left : {difference:>10}")
    print(f"Percent       : {percent:>10.2f}")
    print(f"Status        : {status:>10}")

    print("=" * 34)

count = 0
while True:
    
    label = (input("Input Source IP: (press quit to exit.) "))
    if label == "quit":
        break

    value = float(input("Input Failed logins: "))
    limit = float(input("Input Total Attempts: "))

    difference, percent = check(value,limit) #value and limit here is returned after calling the check(value,limit) function and difference and percent gets the value.

    status = status_of(percent) #status gets the returned value after calling the function status_of(percent)
    if status == "OVER LIMIT":
        count = count + 1

    
    print_report(label, value, limit, difference, percent, status) #this function when it is called it displays the record report

    print(f"Amount of Over Limit Status : {count}")


