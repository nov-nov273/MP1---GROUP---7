total = int(input())

days = total // 86400
total %= 86400
hours = total // 3600
total %= 3600
minutes = total // 60
seconds = total % 60

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")