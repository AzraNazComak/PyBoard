
from gorevler import Gorev, GorevPanosu




pano = GorevPanosu()
gorev1 = Gorev("raporu hazırla", "azra naz comak", "bu haftanın raporunu hazırla", " yüksek", "2026-10-25")
gorev2 = Gorev("Sunum hazırla", "mehmet yılmaz", "bu haftanın sunumunu hazırla", "orta", "2026-10-26")
gorev3 = Gorev("Toplantı düzenle", "ayşe demir", "bu haftanın toplantısını düzenle", "düşük", "2026-10-27")

pano.gorev_ekle(gorev1)
pano.gorev_ekle(gorev2)
pano.gorev_ekle(gorev3)

print("\n TÜM GÖREVLER:")
pano.tumunu_goruntule()


pano.gorevlerini_goruntule("azra naz comak")