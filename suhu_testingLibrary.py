# fungsi untuk Suhu ke Faranheit
def suhuConvertFaranheit(C):
    F = (C * (9/5)) + 32 #rumus faranhite
    return F
faranheit = suhuConvertFaranheit(30)
print ("Suhu Faranheit {}".format(faranheit))
# fungsi untuk Suhu ke Kelvin
def suhuConvertKelvin(C):
    K = C + 273.15 #rumus kelvin
    return K
kelvin = suhuConvertKelvin(30)
print ("Suhu Kelvin {}".format(kelvin))
# fungsi untuk Suhu ke Reamur
def suhuConvertReamur(C):
    Re = C * (4/5) #rumus reamur
    return Re
reamur = suhuConvertReamur(30)
print ("Suhu Reamur {}".format(reamur))
