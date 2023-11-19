# Automatic Monitoring System (automons) ve Demo

Bu adımda sizlere, henüz geliştirme aşamasında olan ve tamamlanmamış bir projemden bahsedeceğim sonra da basit birkaç komutla kendi sistemimizi izleyeceğiz.

 -**Automons**- Bu proje, Grafana panellerinin uzaktaki makineler üzerine sorunsuz bir şekilde yerleştirilmesini ve yönetilmesini kolaylaştırmak için tasarlanmış bir sistemdir.

🔗 Proje GitHub'da yer alıyor ve bu adresten inceleyebilirsiniz: [github.com/nesiler/automons](https://github.com/nesiler/automons)

## Automons'un Amacı

Automons, Docker, Python, Jinja2 ve Ansible kullanarak Grafana panellerini ve data sourcelari uzaktaki makineler üzerine yerleştirmenize ve yönetmenize olanak tanıyan bir sistemdir. Komut satırı arayüzü üzerinden kullanıcılar, çeşitli parametreleri yapılandırarak Grafana panellerini zahmetsizce oluşturabilir ve yönetebilir.

Daha fazla bilgi için: [Automons Plan](https://github.com/nesiler/automons/blob/main/plan_en.md)

## Demo Adımı: Docker-Compose ile Grafana Provisioning

Bu demo, Grafana'nın provisioning özelliğini kullanarak, Prometheus ve Grafana'yı içeren bir monitoring çözümünü tek bir `docker-compose.yaml` dosyası ile nasıl kurabileceğinizi gösterir.

### Gereksinimler:
Öncelikle projeyi github'dan indirelim:

```sh
git clone https://github.com/nesiler/automons.git
```

Daha sonra, demo dosyalarınızın bulunduğu dizine gidin:

```sh
cd automons/demo
```

### Dosya Yapısı ve İşlevleri:

- **docker-compose.yaml:** Docker container'larınızı yönetmek ve birden çok servisi tek bir komutla başlatmak için kullanılan YAML dosyasıdır. Bu dosyada Prometheus ve Grafana servisleri ve bazı konfigürasyonlar yer alır.

- **prometheus.yml:** Prometheus'un yapılandırma dosyasıdır ve izlenecek hedefleri, kuralları ve alertleri tanımlar.

- **templates/conf/grafana.ini:** Grafana'nın ana yapılandırma dosyasıdır ve Grafana sunucusunun çalışma parametrelerini belirler.

- **templates/datasources/datasource_test.yaml:** Grafana için veri kaynaklarının (datasources) otomatik olarak yapılandırılmasını sağlayan YAML dosyasıdır. Bu dosya, Prometheus gibi veri kaynaklarının Grafana'ya nasıl bağlanacağını tanımlar.

- **templates/models/fullnode.json:** Grafana için kullanılacak olan dashboard modelidir. Bu JSON dosyası, panonun görsel yapısını ve sorgularını içerir.

- **templates/dashboards/fullnode.yaml:** Grafana'nın dashboard yapılandırmasını içeren YAML dosyasıdır. Bu dosya, Grafana'nın hangi dashboard modellerini yükleyeceğini tanımlar.

### Docker-Compose Dosyasını Çalıştırma Rehberi:

1. Eğer repoyu indirip demo dizinine gittiyseniz, `docker-compose.yaml` dosyasını çalıştırmak için aşağıdaki Docker-Compose komutunu kullanın:

   ```sh
   docker-compose -f /demo/docker-compose.yaml up -d
   ```

2. Komut başarılı bir şekilde çalıştırıldıktan sonra, tarayıcınızda port yönlendirme kısmından "3000" portuna giderek Grafana'nın kullanıcı arayüzüne erişebilirsiniz.

3. Grafana'ya varsayılan kullanıcı adı (`admin`) ve şifre (`admin`) ile giriş yapın.

4. Giriş yaptıktan sonra, Prometheus veri kaynağının ve `fullnode` dashboard'unun otomatik olarak yapılandırıldığını görmelisiniz.

5. Artık Grafana üzerinden sistem izleme ve veri analizi yapmaya başlayabilirsiniz.