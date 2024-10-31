

xilk=float(input("\nX₀ Değerini Girin(m)\n"))
Vilk=float(input("\nV₀ Değerini Girin(m/s)\n"))
a=float(input("\na Değerini Girin(m/s²)\n"))
t=float(input("\nt Değerini Girin(s)\n"))

x=xilk+Vilk*t+a*0.5*(t**2)
print("\nKonum: {}m dir\n".format(x))
