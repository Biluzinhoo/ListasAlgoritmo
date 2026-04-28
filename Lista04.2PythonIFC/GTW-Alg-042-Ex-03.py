valores = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Celsius:\t\tFahrenheit:")
for i in range(11):
    fah = (valores[i]* 9/5) + 32
    
    print(f"{valores[i]}°C\t\t\t{fah}°F")
