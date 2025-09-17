x = float(input("whats x: "))
y = float(input("whats y:"))
z = float(input("whats z: "))

maximum = max(x , y , z)
minimum = min(x , y , z)

result = round(x) + abs(y) + pow(z, 3)
print(result)
print(f"the maximum is {maximum}.")
print(f"the minimum is {minimum}.")