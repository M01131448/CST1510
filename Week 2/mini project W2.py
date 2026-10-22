"""
RECORD CHECK  -  10.0.0.5
===========================

Name  : Mohammad Haidar Ali TAJOO
Lane  :   / Cyber /      (delete two)
Date  : 02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""






count = 0
while True:
 label = input("Please enter IP Address: (OR TYPE QUIT TO END THE SESSION) ")
 if label == "quit":
    break
 
 failed_logins = float(input("Enter failed log-in amounts: "))
 total_amounts = float(input("Enter the total amounts of Log-in amounts sessions: "))
 difference = total_amounts - failed_logins
 percent = (failed_logins / total_amounts) * 100

 if percent >= 100:
    count += 1

 if percent >= 100:
    status = "OVER LIMIT"
 elif percent >= 90:
    status = "WARNING"
 else:
    status = "OK"



 print()

 print("=" * 34)
 print(f"  RECORD CHECK  -  {label}")
 print("=" * 34)

 print(f"Failed logins(USED)    :     {failed_logins:>10.2f}")
 print(f"Total attempts(TOTAL)  :     {total_amounts:>10.2f}")
 print(f"Free Attempts(FREE)    :     {difference:>+10.2f}")
 print(f"Percent                :     {percent:>10.2f}%")
 print(f"Status                 :     {status:>10}")
 print("=" * 34)

print(f"OVER LIMIT Status      :     {count:>10}")
