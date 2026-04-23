from datetime import datetime

today = datetime.now()

print(f"Year: {today:%Y}")

print(f"Month: {today:%B}")

print(f"Day: {today:%d}")

print(f"Full Date: {today:%Y-%B-%d}")

print(f"Current time is {today:%H:%M:%S %p}")