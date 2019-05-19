P = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
H = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

sum_x = sum(P)
sum_y = sum(H)
sum_xx = sum([p*p for p in P])
sum_yy = sum([h*h for h in H])
sum_xy = sum([p*h for p,h in zip(P,H)])

a = (sum_y*sum_xx - sum_x*sum_xy)/((len(P)*(sum_xx)) - sum_x**2)
b = ((len(P)* sum_xy) - (sum_x*sum_y))/((len(P)*sum_xx) - sum_x**2)

y = a + b*10
print(y)