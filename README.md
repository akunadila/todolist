# todolist
# Proyek Ujian Cloud Services: Aplikasi To-Do List Lintas Platform

**Oleh:** Nadila Zindi Aulia Putri
**Mata Kuliah:** Cloud Services

---

## 1. Deskripsi Proyek

Aplikasi ini adalah To-Do List sederhana berbasis Command Line Interface (CLI) yang dibangun menggunakan Python. Project ini bertujuan untuk mendemonstrasikan implementasi penuh Containerization dan Cross-Platform Deployment menggunakan Docker dan diuji konsistensinya di lingkungan Linux (WSL) dan Windows.

### Fitur Aplikasi:
* Menambah Tugas
* Melihat Daftar Tugas
* Menghapus Tugas
* Keluar dari Aplikasi

## 2. Konfigurasi Proyek & Workflow

### Version Control (LO 2.a)
Proyek ini dikembangkan menggunakan Git Flow sederhana, melibatkan branching fitur dan merge ke cabang `main`.

**CI/CD:** Menggunakan GitHub Actions untuk menjalankan linting atau build check otomatis setiap kali terjadi push, menjamin kode di `main` selalu stabil.

### Container (LO 2.b)
Aplikasi di containerize menggunakan Dockerfile berbasis image `python:3.10-slim`.

