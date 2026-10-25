

class Gorev:
    def __init__(self, baslik, sorumlu, aciklama, oncelik, tarih, durum="yapilacak"):
        self.baslik = baslik
        self.sorumlu = sorumlu
        self.aciklama = aciklama
        self.oncelik = oncelik
        self.durum = durum
        self.tarih = tarih

    def durum_degistir(self, yeni_durum):
        self.durum = yeni_durum

    def bilgi_goster(self):
        return f"[{self.durum}] {self.baslik} - Sorumlu: {self.sorumlu} Aciklama: {self.aciklama}(Oncelik: {self.oncelik}) (Tarih: {self.tarih})"


class GorevPanosu:
    def __init__(self):
        self.Liste = []

    def gorev_ekle(self, gorev_nesnesi):
        self.Liste.append(gorev_nesnesi)
        print(f"{gorev_nesnesi.baslik} eklendi")

    def tumunu_goruntule(self):
        for gorev in self.Liste:
            print(gorev.bilgi_goster())

    def gorevlerini_goruntule(self, isim):
        print(f"----- {isim} -> gorevleri:")
        for gorev in self.Liste:
            if gorev.sorumlu.lower() == isim.lower():
                print(gorev.bilgi_goster())
