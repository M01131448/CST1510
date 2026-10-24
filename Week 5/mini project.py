"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Haidar Ali TAJOO
Lane  :   / Cyber /      (delete two)
Date  : 23.10.2026

"""

class Record:
    def __init__(self, source_ip, failed_logins, total_attempts):
        """Initialise record with IP, Failed Logins and Total Attempts"""
        self.source_ip = source_ip  
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts


    def status(self):
        """Return OVER LIMIT, WARNING or OK"""
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"
                
    def percent(self):
        """Return Percentage"""
        return (self.failed_logins / self.total_attempts) * 100 

    def attempts_left(self):
        """Return how many attempts are left"""
        return self.total_attempts - self.failed_logins



def load_records(path):
    """Read IP,failed Login Attempts and Total Attempts lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            source_ip, failed_logins, total_attempts = line.strip().split(",")
            records.append(Record(source_ip, float(failed_logins), float(total_attempts)))
    return records


recordlist = load_records("data.txt")

over_limit_count = 0 #counter which counts how many records are "OVER LIMIT"
total_records = 0 #Counter to count the total number of records in the loop



for r in recordlist:
    status = r.status()
    total_records = total_records + 1

    
    if status == "OVER LIMIT": #This line is to count over limit status
        over_limit_count = over_limit_count + 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {r.source_ip}")  
    print("=" * 34)
    print(f"Failed Logins  : {r.failed_logins}")
    print(f"Total Attempts : {r.total_attempts}")
    print(f"Attempts Left  : {r.attempts_left()}")
    print(f"Percentage     : {r.percent():.2f}%")
    print(f"Status         : {status}")
    print("=" * 34)

print(f"\nTotal OVER LIMIT records: {over_limit_count} out of {total_records}")



