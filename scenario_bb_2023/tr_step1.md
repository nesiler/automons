# Grafana ve Prometheus ile Sistem İzleme

Sistem izleme, sağlıklı bir altyapının sürdürülebilirliği için kritik öneme sahiptir. Bu dokümanda, Grafana ve Prometheus kullanarak nasıl etkili bir izleme sistemi kurulabileceğini ve Node Exporter'ın bu yapı içindeki rolünü ele alacağız.

## Grafana

### Grafana Nedir?
Grafana, çeşitli veri kaynaklarından topladığı verileri görselleştiren açık kaynak kodlu bir web uygulamasıdır. Grafikler ve çizelgeler aracılığıyla verilerinizi daha anlaşılır ve yorumlanabilir hale getirir. Karmaşık veri setlerini basit ve etkili görsellerle ifade edebilir, böylece izleme süreçlerini optimize edebilirsiniz.

### Grafana Kurulumu
Grafana'yı [resmi internet sitesi](https://grafana.com/) üzerinden indirip kurabilirsiniz. Kurulum tamamlandıktan sonra, varsayılan olarak `http://localhost:3000/` adresinde çalışır. İlk girişte karşınıza çıkan ekranda, kullanıcı adı ve şifre olarak "admin" girerek sisteme erişebilirsiniz. Ayrıca bir bir sonraki adımlarda Docker ile nasıl kolay bir şekilde kurabileceğimizi göstereceğim.

## Prometheus

### Prometheus'un İşlevi
Prometheus, sistem ve uygulama performans verilerini toplayan, depolayan ve işleyen açık kaynak kodlu bir izleme çözümüdür. Prometheus, izleme sürecinde pull temelli bir yaklaşım benimser; yani belirli aralıklarla yapılandırılmış hedeflerden veri çeker. Bu yaklaşım, izleme sürecinin daha az kaynak tüketmesini ve daha ölçeklenebilir olmasını sağlar.

### Prometheus ve Node Exporter İlişkisi
Node Exporter, Prometheus ile doğrudan çalışan bir araçtır. Sunucu veya bilgisayarınızın donanım ve işletim sistemi metriklerini toplayıp Prometheus'un bu verileri çekebileceği bir formatta sunar. Node Exporter, sistem metriklerini bir HTTP portu üzerinden dışa aktarır, böylece Prometheus bu verileri kolaylıkla toplayabilir.


### Sistem Kaynaklarının İzlenmesi
İşletim sistemleri ve uygulamalar, işlevlerini yerine getirmek için çeşitli kaynakları kullanır. Kaynaklar yetersiz olduğunda veya sorun yaşandığında sistem performansı etkilenebilir. Prometheus, bu kaynakların durumunu izleyerek sistemlerin sorunsuz çalışmasını sağlamak için gerekli bilgileri toplar.

### Prometheus'un İzleme Yaklaşımı
Prometheus, diğer izleme araçlarından farklı olarak, pull temelli bir izleme yaklaşımı benimser. Bu, hedef sistemlerin izleme verilerini bir adres üzerinden sunmasını ve Prometheus'un bu verileri belirli aralıklarla çekmesini ifade eder. Pushgateway bileşeni sayesinde, push temelli izleme sistemleri de Prometheus ile uyumlu hale getirilebilir.


---
