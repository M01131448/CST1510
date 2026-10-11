# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status #returned status to be able to use it outside the function

status = check(87, 100) #called the function inside a variable so print works
print(status)

