# fungsi untuk Suhu ke Faranheit
def suhuConvertFaranheit(C):
    F = (C * (9/5)) + 32 #rumus faranhite
    return F
suhuConvertFaranheit(30)
# fungsi untuk Suhu ke Kelvin
def suhuConvertKelvin(C):
    K = C + 273.15 #rumus kelvin
    return K
suhuConvertKelvin(30)
# fungsi untuk Suhu ke Reamur
def suhuConvertReamur(C):
    Re = C * (4/5) #rumus reamur
    return Re
suhuConvertReamur(30)
# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Mengubah Suhu ke Faranheit")
    print ("[2] Mengubah Suhu ke Reamur")
    print ("[3] Mengubah Suhu ke Kelvin")
    print ("[4] Exit")
    
    menu = int(input("PILIH MENU> "))
    print ("\n")

    if menu == 1:
        suhuConvertFaranheit()
    elif menu == 2:
        suhuConvertReamur()
    elif menu == 3:
        suhuConvertKelvin()
    elif menu == 4:
        exit()
    else:
        print ("Salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu()