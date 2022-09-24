# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]

# На конзолата се отпечатва:
# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

vacation_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

total_price_for_all_the_toys = (num_puzzles * 2.60) + (num_dolls * 3) + (num_bears * 4.10) + \
                               (num_minions * 8.20) + (num_trucks * 2)


num_of_all_toys = num_trucks + num_minions + num_bears + num_dolls + num_puzzles

if num_of_all_toys >= 50:
    total_price_for_all_the_toys -= total_price_for_all_the_toys * 0.25
rent = total_price_for_all_the_toys * 0.10
profit = total_price_for_all_the_toys - rent
diff = abs(profit - vacation_price)

if profit >= vacation_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
