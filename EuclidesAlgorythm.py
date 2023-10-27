#przyjecie dwoch liczb
a = int(input('Większa liczba: '))
b = int(input('Mniejsza liczba: '))
#dzielenie w petli

#Aby obliczyć NWD(a,b), wykonujemy kolejno następujące kroki:
#Dzielimy z resztą liczbę a przez liczbę b
#jeżeli reszta jest równa 0, to NWD(a,b)=b
#jeżeli reszta jest różna od 0, to przypisujemy liczbie a wartość liczby b, liczbie b wartość otrzymanej reszty, a następnie wykonujemy ponownie punkt 1.
while True:
    c = a % b
    if c == 0:
        print(b)
        break
    else:
        a = b
        b = c
