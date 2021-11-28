# fungsi untuk Suhu ke Faranheit
def suhuConvertFaranheit(C):
    F = (C * (9/5)) + 32 #rumus faranhite
    print("Suhu dari",C, " adalah ",F,"°F")
suhuConvertFaranheit(30)
# fungsi untuk Suhu ke Kelvin
def suhuConvertKelvin(C):
    K = C + 273.15 #rumus kelvin
    print ("Suhu dari",C, " adalah ",K,"°K")
suhuConvertKelvin(30)
# fungsi untuk Suhu ke Reamur
def suhuConvertReamur(C):
    Re = C * (4/5) #rumus reamur
    print ("Suhu dari",C, " adalah ",Re,"°Re")
suhuConvertReamur(30)
