print("✈️ Aircraft Range Calculator")

fuel = float(input("Fuel Capacity (Liters): "))
consumption = float(input("Fuel Consumption (L/100 km): "))
passengers = int(input("Number of Passengers: "))

range_km = (fuel / consumption) * 100

print("\n------ FLIGHT REPORT ------")
print(f"Maximum Range: {range_km:.1f} km")

if passengers <= 2:
    print("Aircraft Load: Light")
elif passengers <= 5:
    print("Aircraft Load: Medium")
else:
    print("Aircraft Load: Heavy")

if range_km >= 2500:
    print("Mission Status: LONG RANGE ✅")
elif range_km >= 1000:
    print("Mission Status: MEDIUM RANGE ✅")
else:
    print("Mission Status: SHORT RANGE ⚠️")