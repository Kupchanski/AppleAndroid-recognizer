from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords": "xiaomi redmi pro", "limit":90}
paths = response.download(arguments)
print(paths)