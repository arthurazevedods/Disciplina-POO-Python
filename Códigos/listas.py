series = [
    ("The Wire", 25),       #nome e valor
    ("The Office", 20),     #tupla
    ("Breaking Bad", 20), 
    ("The Sopranos", 30),
    ("Mr. Robot", 35), 
    ("Game Of Thrones", 20), 
    ("Fullmetal Alchmist", 25), 
    ("Jujutsu Kaisen", 30), 
    ("Frieren", 28),
    ("Attack On Titan", 28),
    ("Pluto", 20), 
]
print(series[7]) #mostra o valor da série no índice 10
print(series[0:3]) #mostra os valores da série do índice 0 ao 2
print(series[3:]) #mostra os valores da série do índice 3 ao final
print(series[3][0]) #mostra o valor da série no índice 10
print(series[3][1]) #mostra o valor da série no índice 10

print(series[-1][0]) #mostra o valor da série no índice 10

print(f'{series[2][0]} - {series[2][1]}') #mostra o valor da série no índice 10
