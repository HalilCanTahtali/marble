# marble
THS 1
---------------
Uygulamanın amacı mermer alıcısınının mermer seçimi için Türkiye'ye gelmesini önlemektir. Bunun için öncelikle mermer alıcısına mermer hakkında bilgileri vermek gerekmektedir.
Mermerin kallitesini belirleyen faktörler arasında; renk, çatlak boyutları, su yolu, damarlanma gibi etkenler vardır. Bu proje de renk ve damar tespiti yapılmayı hedeflenmektedir.
Gerekli olan teknolojiler renk ve damarlanma tespiti yapan algoritmadır. Bu tespit fotoğraf üzernden yapılacaktır.
Sitede alıcı ve satıcı olarak iki farklı giriş bulunmaktadır. Alıcı kişi siteye girip satıcının profilindeki mermerlerin fotorğaflarını, bu mermerlerin içerisinde en çok bulunan üç rengi ve damarlanmalarının testip edildiği çıktıya ulaşabilecektir.
Bu kısımda uzman görüşüne gerek yoktur. Çünkü renkler ve mermerin damarlanma yapısı öznel değildir.

THS 2
---------------
Temel olarak yapılacka iş satıcıların sisteme mermer görselleri vermesi ve bu görsellerin renk ve damarlanma tespiti yapıldıktan sonra satış sitesine sunulmasıdır.

THS 3
---------------
THS 2 de bahsedilen renk tespiti ve damarlanma tespiti üzerine çalışılmıştır. Renk tespiti yapılabilmektedir lakin her pikselin rengini alıp en yakın komşu algoritması ile en yoğun bulunan renk kodunun çıktısı verilmiştir. Algoritma görselde bulunan 3 farklı rengi ekrana vermektedir.
Damarlanma yapısı için yapılan çalışma fotorğafın kontrast değerlerini değiştirip damarlanmaların ortaya çıkartılmasını hedeflemektedir.
Renk tespiti başarı ile çalışmaktadır lakin damarlanma yapısının üzerinde hala çalışılmaktadır.

THS 4
---------------
Prototip olarak ortaya bir web sitesi konmuştur. Sistemde iki farklı giriş mevcutur. Satıcı profilini admin düzenleyeyecektir, gerekli yetkileri admin vermektedir. Admin sisteme fotoğraf ekelyebilir ve de mevcut fotorğafları düzenleyebilir. Fotoğrafların renk kategorilerini, başlığını, açıklamasını değiştirebilir. Kullanıcı girişi yapan bir kişi internet sitesindeki hazır ürünleri inceleyebilir. Ürünlerin renk ve damarlanma tespitini görebilmektedir. Yapılan sistem şu anlık spesifik olarak rosso levanto tipinde mermerler için çalışmaktadır. 