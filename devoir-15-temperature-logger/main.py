temps = []
while True:
    entry = input("Enter temperature (or 'q' to quit): ")
    if entry.lower() == 'q':
        break
    try:
        temp = float(entry)
        temps.append(temp)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")

if temps:
    print("Number of readings:", len(temps))
    print("Highest temperature:", max(temps))
    print("Lowest temperature:", min(temps))
    print("Average temperature:", round(sum(temps) / len(temps), 1))
else:
    print("No temperatures were entered")
