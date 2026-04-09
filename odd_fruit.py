num = int(input("enter a number: "))
odd = [x for x in range(num) if x %2 != 0]
odd1 = [x for x in range(1,20) if x %2 !=0]
print(f"odd numbers under {num}: {odd}")
print(f"another odd number list: {odd1}")

fruits = ["apple","mango","banana","cherry"]
capitalized_fruit = [fruits.capitalize() for fruit in fruits]
print(f"uptated list: {capitalized_fruit}")