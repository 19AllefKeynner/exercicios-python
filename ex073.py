times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo',
         'Athletico-PR','Atlético-MG','Fortaleza','São Paulo',
         'América-MG','Bota Fogo','Santos','Goías','Bragantino',
         'Curitiba','Cuiabá','Ceará-SC','Atlético-GO','Avaí','Juventude')
print(f'\033[1;33mLista de times do Brasileirão:\033[m {times[:21]}')
print(f'\033[1;33mOs cinco primeiros colocados são:\033[m {times[:5]}')
print(f'\033[1;33mOs quatro ultimos colocados são: \033[m {times[-4:]}')
print(f'\033[;33mTimes em órdem alfabética:\033[m {sorted(times)}')
print(f'\033[1;33mO Flamengo está na {times.index("Flamengo")+1}ª posição!\033[m')