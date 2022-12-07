# marble
THS 1
---------------
Uygulamanın amacı mermer alıcısınının mermer seçimi için Türkiye'ye gelmesini önlemektir. Bunun için öncelikle mermer alıcısına mermer hakkında bilgileri vermek gerekmektedir.
Mermerin kallitesini belirleyen faktörler arasında; renk, çatlak boyutları, su yolu, damarlanma gibi etkenler vardır. Bu proje de mermerin rengi, mermerdeki damar tespiti ve mermerin türünü tanımlamayı yapabilmeyi hedeflenmektedir.
Gerekli olan teknolojiler renk ve damarlanma tespiti yapan algoritmadır. Mermerin türünü belirlemek için ise yapay zeka kullanılacaktır. Bu tespit fotoğraf üzerinden yapılacaktır.
Sitede alıcı ve satıcı olarak iki farklı giriş bulunmaktadır. Alıcı kişi siteye girip satıcının profilindeki mermerlerin fotorğaflarını, bu mermerlerin içerisinde en çok bulunan üç rengi, damarlanmalarının testip edildiği çıktıya ve mermerin türüne ulaşabilecektir. 
Bu kısımda uzman görüşüne gerek yoktur. Çünkü renkler, mermerin damarlanma yapısı ve mermer türü öznel değildir.

THS 2
---------------
Temel olarak yapılacak iş satıcıların sisteme mermer görselleri vermesi ve bu görsellerin renk ve damarlanma tespiti yapıldıktan sonra satış sitesine sunulmasıdır.

THS 3
---------------
THS 2 de bahsedilen renk tespiti ve damarlanma tespiti üzerine çalışılmıştır. Renk tespiti yapılabilmektedir lakin her pikselin rengini alıp en yakın komşu algoritması ile en yoğun bulunan renk kodunun çıktısı verilmiştir. Algoritma görselde bulunan 3 farklı rengi ekrana vermektedir.
Damarlanma yapısı için yapılan çalışma fotorğafın kontrast değerlerini değiştirip damarlanmaların ortaya çıkartılmasını hedeflemektedir.
Renk tespiti başarı ile çalışmaktadır lakin damarlanma yapısının üzerinde hala çalışılmaktadır.
Mermer türünü tespit etme başarılı şekilde çalışmaktadır. Roboflow üzerinden model eğitimi gerçekleştirilmiş ve aktif olarak prototipte kullanılmaktadır.

THS 4
---------------
Prototip olarak ortaya bir web sitesi konmuştur. Sistemde iki farklı giriş mevcutur. Satıcı profilini admin düzenleyeyecektir, gerekli yetkileri admin vermektedir. Admin sisteme fotoğraf ekelyebilir ve de mevcut fotorğafları düzenleyebilir. Fotoğrafların renk kategorilerini, başlığını, açıklamasını değiştirebilir. Kullanıcı girişi yapan bir kişi internet sitesindeki hazır ürünleri inceleyebilir. Görsellerin barındırdığı renkleri ve mermerin türünü görüntüleyebilmektedir. Yapılan sistemde şu anlık damarlanma testipi spesifik olarak rosso levanto tipinde mermerler için çalışmaktadır ve yapım aşmsındadır. 