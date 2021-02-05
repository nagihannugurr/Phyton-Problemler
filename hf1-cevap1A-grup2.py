yillik_maas = float(input("Yillik maasinizi giriniz: "))
tasarruf_edilen_oran = float(input("Maasinizin tasarruf etmek istediginiz yuzdesini, ondalik olarak giriniz: "))
toplam_maliyet = float(input("Hayalinizdeki evin maaliyetini giriniz: "))
pesinat_orani = 0.25
mevcut_tasarruflar = 0.0
ay_sayisi = 0
r = 0.04
pesinat_miktari = toplam_maliyet * pesinat_orani

while mevcut_tasarruflar < pesinat_miktari:
    mevcut_tasarruflar = mevcut_tasarruflar + (yillik_maas / 12 * tasarruf_edilen_oran) + ((mevcut_tasarruflar * r) /12)
    ay_sayisi += 1
print( "\n" + str(ay_sayisi) + " ay")