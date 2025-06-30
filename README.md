# 🧠 Web Article to PDF Converter 📰➡️📄

This is one of the first practice projects I built as part of my **big learning journey** into real-world Python projects. I am currently sharpening my skills in **HTML Web Scraping**, **PDF generation**, and **GUI development using Tkinter**.

---

## 🚀 About the Project

This Python application lets users:

- Enter a website URL (especially articles like Wikipedia pages).
- Automatically extract the main readable content (excluding ads, headers, sidebars, etc.).
- Download and save the cleaned content as a **PDF file**.

It uses a simple **Tkinter-based GUI** for user interaction.

---

## 🧠 What I Practiced and Learned

This project helped me understand and get hands-on experience with:

- ✅ `requests` – to load webpage content
- ✅ `BeautifulSoup` – to extract and clean HTML content
- ✅ `pdfkit` – to convert HTML to PDF
- ✅ `tkinter.filedialog` – to choose where to save the file
- ✅ `os.startfile()` – to automatically open the PDF after creation
- ✅ Cleaning and fixing image links for proper PDF rendering

> I mainly focused on **HTML Web Scraping**, using **file dialogs**, and mastering **pdfkit**. Other parts I more or less already knew.

---

## 🛠 How It Works

1. You run the app.
2. Enter any valid article-like URL (e.g., from Wikipedia).
3. Choose where to save the PDF file.
4. The app extracts the core content and saves it as a clean PDF with images.

---

## 📁 Project Structure
web-to-pdf-converter/
├── main.py # Main Python script
├── README.md # Project overview and instructions

## 📌 Dependencies

Make sure you install the following before running the app:

```bash
pip install requests beautifulsoup4 pdfkit
Also, install wkhtmltopdf and configure the path:

Download wkhtmltopdf

Update the path in the code:

python
Copy
Edit
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
