
````markdown
# 🖼️ Smart Image to WebP Converter (CLI)

A smart and lightweight **Python CLI tool** for converting **JPG / PNG images or folders** into optimized **WebP** format, suitable for modern web performance, SEO, and Core Web Vitals.

This tool automatically:
- Converts single images or entire folders
- Optimizes large images for web usage
- Preserves PNG transparency (alpha channel)
- Produces clean and predictable output folders

---

## ✨ Features

- Supports **JPG, JPEG, PNG**
- Converts images to **WebP**
- Smart resize for large images (max 1920px)
- Preserves transparency for PNG files
- Optimized output size with high visual quality
- Simple CLI usage via `-c` flag
- Clean output folder structure
- Cross-platform (Windows / Linux / macOS)

---

## 📦 Requirements

- Python **3.8+**
- Pillow library

Install dependency:

```bash
pip install pillow
````

---

## 🚀 Usage

All commands below are inside a single code block to ensure GitHub copy buttons work correctly.

```bash
# Convert a single image
python webp_converter.py -c path/to/image.png
# Output:
# image_webp/
# └── image.webp

# Convert an entire folder
python webp_converter.py -c path/to/images_folder
# Output:
# images_folder_webp/
# ├── image1.webp
# ├── image2.webp
# └── image3.webp
```

---

## ⚙️ How It Works

* If the input is a **file**:

  * A new folder named `<filename>_webp` is created
* If the input is a **directory**:

  * A new folder named `<foldername>_webp` is created
* Images larger than 1920px are resized proportionally
* JPG images are converted using lossy WebP optimization
* PNG images retain transparency using alpha-safe WebP encoding

---

## 🧠 Why WebP?

* Smaller file sizes
* Faster page load times
* Better SEO & Core Web Vitals
* Supported by all modern browsers

---

## 📄 License

MIT License
Free to use, modify, and distribute

---

# 🖼️ مبدل هوشمند تصویر به WebP (خط فرمان)

این پروژه یک ابزار **CLI سبک و هوشمند با پایتون** است برای تبدیل تصاویر **JPG / PNG** (تکی یا پوشه‌ای) به فرمت **WebP**، مناسب برای بهینه‌سازی سایت، سئو و افزایش سرعت لود.

این ابزار به‌طور خودکار:

* تبدیل تصویر تکی یا کل پوشه
* بهینه‌سازی تصاویر بزرگ برای وب
* حفظ شفافیت PNG
* ایجاد پوشه خروجی مرتب و پیش‌بینی‌شده

---

## ✨ امکانات

* پشتیبانی از **JPG, JPEG, PNG**
* تبدیل تصاویر به **WebP**
* تغییر اندازه هوشمند تصاویر بزرگ (حداکثر 1920px)
* حفظ شفافیت برای فایل‌های PNG
* خروجی بهینه و حجم کم با کیفیت بالا
* استفاده ساده از طریق دستور `-c`
* ساختار پوشه خروجی تمیز
* قابل اجرا در ویندوز، لینوکس و مک

---

## 📦 پیش‌نیازها

* Python **3.8+**
* کتابخانه Pillow

نصب کتابخانه:

```bash
pip install pillow
```

---

## 🚀 نحوه استفاده

تمام دستورات زیر داخل یک بلاک کد هستند تا دکمه‌ی کپی GitHub درست کار کند.

```bash
# تبدیل یک تصویر تکی
python webp_converter.py -c path/to/image.png
# خروجی:
# image_webp/
# └── image.webp

# تبدیل یک پوشه کامل
python webp_converter.py -c path/to/images_folder
# خروجی:
# images_folder_webp/
# ├── image1.webp
# ├── image2.webp
# └── image3.webp
```

---

## ⚙️ چطور کار می‌کند

* اگر مسیر ورودی **یک فایل** باشد:

  * یک پوشه به نام `<filename>_webp` ساخته می‌شود
* اگر مسیر ورودی **یک پوشه** باشد:

  * یک پوشه به نام `<foldername>_webp` ساخته می‌شود
* تصاویر بزرگ‌تر از 1920px به صورت هوشمند تغییر اندازه می‌دهند
* تصاویر JPG با بهینه‌سازی lossy تبدیل می‌شوند
* تصاویر PNG شفافیت خود را حفظ می‌کنند

---

## 🧠 چرا WebP؟

* کاهش حجم فایل‌ها
* افزایش سرعت بارگذاری صفحات
* بهبود SEO و Core Web Vitals
* پشتیبانی توسط مرورگرهای مدرن

---

## 📄 مجوز

MIT License
استفاده، تغییر و توزیع رایگان

```

این نسخه:  
- زبان‌ها کاملاً جدا هستند  
- همه‌ی دستورات CMD داخل یک بلاک واحد `bash` هستند → دکمه‌های کپی GitHub درست کار می‌کنند  
- کامل و مناسب README پروژه است  

اگر بخوای، می‌تونم یه نسخه‌ی **فوق کوتاه برای Description** هم آماده کنم تا وقتی repo آپلود شد، جلو اسمش جذاب و حرفه‌ای دیده بشه.
```
