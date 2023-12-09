def weather_data(temperature):
    if not temperature:
        return None

    avg_temp = sum(temperature) / len(temperature)

    highest = max(temperature)
    lowest = min(temperature)

    return {
        'avg_temp': avg_temp,
        'highest': highest,
        'lowest': lowest
    }

temperature = [25.0, 28.0, 21, 24, 27]
result = weather_data(temperature)

print("Average Temperature:", result['avg_temp'])
print("Highest Temperature:", result['highest'])
print("Lowest Temperature:", result['lowest'])