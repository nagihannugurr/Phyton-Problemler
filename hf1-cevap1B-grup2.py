yillik_maas = float(input("Yillik maasinizi giriniz: "))
tasarruf_edilen_oran = float(input("Maasinizin tasarruf etmek istediginiz yuzdesini, ondalik olarak giriniz: "))
toplam_maliyet = float(input("Hayalinizdeki evin maaliyetini giriniz: "))
yariyil_maas_zammi_orani = float(input("Yarıyıl maaş zammi oranininizi giriniz: "))
pesinat_orani = 0.25
mevcut_tasarruflar = 0.0
ay_sayisi = 0
pesinat_miktari = toplam_maliyet * pesinat_orani
r = 0.04

while mevcut_tasarruflar < pesinat_miktari:
    mevcut_tasarruflar = mevcut_tasarruflar + (yillik_maas / 12 * tasarruf_edilen_oran) + ((mevcut_tasarruflar * r) / 12)
    ay_sayisi += 1
    if ay_sayisi % 6 == 0:
        yillik_maas = yillik_maas + yillik_maas * yariyil_maas_zammi_orani
print( "\n" + str(ay_sayisi) + " ay")