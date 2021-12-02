    
class Suhuu:
    
    # fungsi untuk Suhu ke Faranheit
    def CelciusConvertFaranheit(C):
        F = (C * (9/5)) + 32 #rumus faranhite
        return F
    faranheit = CelciusConvertFaranheit(30)
    print(faranheit)
    # fungsi untuk Suhu ke Kelvin
    def CelciusConvertKelvin(C):
        K = C + 273.15 #rumus kelvin
        return K
        
    kelvin = CelciusConvertKelvin(30)
    print(kelvin)

    # fungsi untuk Suhu ke Reamur
    def CelciusConvertReamur(C):
        Re = C * (4/5) #rumus reamur
        return Re
    reamur = CelciusConvertReamur(30)
    print(reamur)    
