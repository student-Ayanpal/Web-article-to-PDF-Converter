import requests
import pdfkit
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from urllib.parse import urljoin

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

pdf_options = {
    'enable-local-file-access': None,
    'no-stop-slow-scripts': None,
    'load-error-handling': 'ignore',
    'load-media-error-handling': 'ignore',
}

def extract_main_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src') or img.get('srcset')
        if src:
            if ',' in src:
                src = src.split(',')[0].split()[0]
            if src.startswith('//'):
                src = 'https:' + src
            elif src.startswith('/'):
                src = urljoin(url, src)
            img['src'] = src

    for noscript in soup.find_all('noscript'):
        sub_soup = BeautifulSoup(noscript.decode_contents(), 'html.parser')
        img = sub_soup.find('img')
        if img and img.get('src'):
            noscript.replace_with(img)

    content = soup.find('div', {'id': 'mw-content-text'}) or soup.body
    return str(content)


def save_pdf_from_html(html_content, filename='output.pdf'):
    try:
        pdfkit.from_string(html_content, filename, configuration=config, options=pdf_options)
    except OSError as e:
        if os.path.exists(filename):
            print("PDF created with minor warnings.")
        else:
            raise e


def start_conversion():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return


    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        html = extract_main_html(url)

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF As"
        )
        if not file_path:
            return

        save_pdf_from_html(html, filename=file_path)
        messagebox.showinfo("Success", f"PDF saved at:\n{file_path}")
        os.startfile(file_path)

    except Exception as e:
        messagebox.showerror("Error", f"Failed: {str(e)}")



root = tk.Tk()
root.title("Web Article to PDF")
tk.Label(root, text="Enter Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

tk.Button(root, text="Convert to PDF", command=start_conversion).pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
