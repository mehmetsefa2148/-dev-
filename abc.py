import math


g = 10
hedef_mesafe = 20000
hedef_genislik = 1000
top_yukseklik = 8
aci_rad = math.radians(30)

def hedefi_vurabilme_hizi():
    """Hedefi vurabilmek için gereken hızı bulma fonksiyonu."""
    h_min = 330
    h_max = 1800
    atis_sayisi = 1

    while True:
        hiz = (h_min + h_max) / 2


        V0x = hiz * math.cos(aci_rad)
        V0y = hiz * math.sin(aci_rad)


        Tu = (2 * V0y) / g
        X_menzil = V0x * Tu


        if X_menzil < hedef_mesafe - hedef_genislik / 2:
            print("Uzağına düştü")
            h_min = hiz
        elif X_menzil > hedef_mesafe + hedef_genislik / 2:
            print("Önüne düştü")
            h_max = hiz
        else:
            print(f"Hedefi vurdun")
            break

        atis_sayisi += 1

    return hiz, atis_sayisi


def vurus_koordinati(hiz):
    """Hedefi vurduğumuzda topun iniş koordinatlarını hesapla."""
    V0x = hiz * math.cos(aci_rad)
    V0y = hiz * math.sin(aci_rad)


    Tu = (2 * V0y) / g


    X_inis = V0x * Tu
    Y_inis = top_yukseklik + (V0y * Tu) - (0.5 * g * Tu**2)

    return X_inis, Y_inis


gereken_hiz, atis_sayisi = hedefi_vurabilme_hizi()
print(f"{atis_sayisi}. seferde vuruş gerçekleşmiştir. Hedefi vurmak için gereken hız: {gereken_hiz} m/s")


X, Y = vurus_koordinati(gereken_hiz)
print(f"Vuruş koordinatı: ({X:.2f} m, {Y:.2f} m)")
