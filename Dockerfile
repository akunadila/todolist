# Menggunakan base image Python versi slim untuk ukuran yang lebih kecil
FROM python:3.10-slim 

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file aplikasi Python ke dalam container
COPY todolist.py .

# Perintah yang akan dijalankan saat container dimulai
# Opsi -i (interactive) dan -t (tty) diperlukan agar aplikasi terminal Python dapat berinteraksi
CMD ["python", "todolist.py"]