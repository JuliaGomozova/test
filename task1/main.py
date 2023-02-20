n = int(input("Введите трехзначное число:"))
print(n)
sum = 0

while n > 0:
    sum += n % 10
    n //= 10
print(f"сумма цифр введенного числа = {sum}")