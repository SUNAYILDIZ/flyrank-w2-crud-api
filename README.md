# CRUD API
CRUD'un açılımı nedir ? 
Create Read Update Delete yani bizim bildiğim to do list yeni bir görev yarat görevleri listele görevi güncelle ve görevi sil mantığımız budur.
## Veriler Nerde Tutuluyor ?
Veriler ramde tutuluyor bu yüzden sunucuyu yeniden çalıştırmada sadece orjinal listeyi görebiliriz.Yani yaptığımız değişiklikler gitmiş olacak.
## Teknolojiler
- Python 3.12.10
- FastAPI
- Uvicorn

## Endpoint'ler
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | / | API bilgisi |
| GET | /health | Sağlık kontrolü |
| GET | /tasks | Tüm görevleri listele |
| POST | /tasks | Yeni görev yarat |
| GET | /tasks/{id} | Aranılan görevi getir |
| PUT | /tasks/{id} | Görevin istenilen alanını güncellemek |
| DELETE | /tasks/{id} | İstenilen görevi silme |
 
## Örnek Kullanım

```bash
curl -i -X DELETE http://localhost:8000/tasks/99
```

**Yanıt:**

```
HTTP/1.1 404 Not Found
date: Sun, 16 Aug 2026 12:18:46 GMT
server: uvicorn
content-length: 29
content-type: application/json
{"error":"Task 99 not found"}
```
## Swagger UI
![Swagger UI] (swagger-screenshot.png)
## Kurulum ve Çalıştırma

1. Depoyu Klonla:
```bash
git clone https://github.com/SUNAYILDIZ/flyrank-w2-crud-api.git 
cd flyrank-w2-crud-api
```

2. Sanal Ortam Oluştur ve aktive et:
```bash
python -m venv venv
# Windows:
venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate
```

3. Bağımlılıkları kur:
```bash
pip install -r requirements.txt
```

4. Sunucuyu başlat:
```bash
uvicorn main:app --reload
```

5. Tarayıcıda aç:  `http://localhost:8000`







