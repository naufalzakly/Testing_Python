    
class Suhuu:
    
    # fungsi untuk Suhu ke Faranheit
    def CelciusConvertFaranheit(self):
        C = float(input("Masukan suhu Celcius untuk diconvert ke Faranheit: "))
        F = (C * (9/5)) + 32 #rumus faranhite
        print("Suhu Celcius dari",C, "°C"," adalah ",F,"°F")
        
        
        
    # fungsi untuk Suhu ke Kelvin
    def CelciusConvertKelvin(self):
        C = float(input("Masukan suhu Celcius untuk diconvert ke Kelvin: "))
        K = C + 273.15 #rumus kelvin
        print ("Suhu Celcius dari",C,"°C", " adalah ",K,"°K")
        
        

    # fungsi untuk Suhu ke Reamur
    def CelciusConvertReamur(self):
        C = float(input("Masukan suhu Celcius untuk diconvert ke Reamur: "))
        Re = C * (4/5) #rumus reamur
        print ("Suhu Celcius dari",C,"°C", " adalah ",Re,"°Re")
        
        
    
    def show_menu(self):
        print ("\n")
        print ("----------- MENU ----------")
        print ("[1] Celcius Convert Faranheit")
        print ("[2] Celcius Convert Kelvin")
        print ("[3] Celcius Convert Reamur")
        print ("[4] Exit")
        
        menu = int(input("PILIH MENU: "))
        print ("\n")

        if menu == 1:
            self.CelciusConvertFaranheit()
        elif menu == 2:
            self.CelciusConvertKelvin()
        elif menu == 3:
            self.CelciusConvertReamur()
        elif menu == 4:
            exit()
        else:
            print ("Salah pilih!")
play = Suhuu()
play.show_menu()
