

# date de la care pleci
data_inceput = 2010
data_sfarsit = 2015
# rezultat 2010, 2011...2015 dar unul sub celalalt
ani = []

for an in range(data_inceput, data_sfarsit + 1):
    ani.append(an)
    print(an)

def este_bisect(an):
    return an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)
data_sfarsit = 2025

ani = []
for an in range(data_inceput, data_sfarsit + 1):
    if este_bisect(an):
        ani.append(f"{an} (bisect)")
    else:
        ani.append(an)

# Afișarea anilor specifici
print("Anii specifici:", ani)