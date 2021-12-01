    class Suhu:
    
    # fungsi untuk Suhu ke Faranheit
    def CelciusConvertFaranheit(self):
        C = float(input("Masukan suhu Celcius: "))
        F = (C * (9/5)) + 32 #rumus faranhite
        print("Suhu Celcius dari",C, "°C"," adalah ",F,"°F")
        
        self.show_menu()
        
    # fungsi untuk Suhu ke Kelvin
    def CelciusConvertKelvin(self):
        C = float(input("Masukan suhu Celcius: "))
        K = C + 273.15 #rumus kelvin
        print ("Suhu Celcius dari",C,"°C", " adalah ",K,"°K")
        
        self.show_menu()

    # fungsi untuk Suhu ke Reamur
    def CelciusConvertReamur(self):
        C = float(input("Masukan suhu Celcius: "))
        Re = C * (4/5) #rumus reamur
        print ("Suhu Celcius dari",C,"°C", " adalah ",Re,"°Re")
        
        self.show_menu()
    
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

play = Suhu()
play.show_menu()
