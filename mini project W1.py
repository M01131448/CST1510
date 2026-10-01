"""
RECORD CHECK  -  10.0.0.5
===========================

Name  : Mohammad Haidar Ali Tajoo
Lane  : / Cyber /     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


print()
label = input("Input Source IP: ")
first = float(input("Input failed logins: "))
second = float(input("Input total attempts: "))
difference = second - first
percent = first / second * 100

print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)


print(f"Failed logins     :     {first:>10.2f}")
print(f"Total attempts    :     {second:>10.2f}")
print(f"Free Attempts     :     {difference:>+10.2f}")
print(f"percent           :     {percent:>10.2f}%")




print("=" * 34)



