"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Haidar Ali Tajoo
Lane  :  / Cyber /      
Date  : 17.10.2026

"""

records = [
    {"label" : "10.0.0.5", "value" : 12, "limit" : 400},
    {"label" : "192.168.1.10", "value" : 3, "limit" : 150},
    {"label" : "10.0.0.8", "value" : 75, "limit" : 60}
]

def check_record(record):
    """This function is to return the limit status being OVER-LIMIT or OK"""

    percent = (record["value"]/ record["limit"]) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def print_report(record):
    """This function main job is taking the status from another function to print 1 dictionary per line"""
    status = check_record(record)

    difference = record["limit"] - record["value"]
    percent = (record["value"] / record["limit"]) * 100
#(The function's main role is also to print the record properly.)
    print("="  * 34)
    print(f" Source IP - {record["label"]:>10}")
    print("=" * 34)
    print(f"Failed Logins : {record["value"]:>10}")
    print(f"Total Attempts: {record["limit"]:>10}")
    print(f"Attempts left : {difference:>10}")
    print(f"Percent       : {percent:>10.2f} %")
    print(f"Status        : {status:>10}")
    print("=" * 34)

def fulldictionary(records):
    """This function is TO print. The entire dictionary lists AND IP's limit Status"""
    count = 0
    for r in records: #where r represents records[0]- records[2]
        if check_record(r) == "OVER LIMIT":
            count = count + 1

        print_report(r)  
        print (f"Amounts of Over Limit Status: {count}")

fulldictionary(records)

