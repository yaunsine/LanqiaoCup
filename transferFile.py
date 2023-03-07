import pdfkit
from markdown import markdown
import requests
import re


def transfer(pdf_file_to=None) -> None:
    content = requests.get("http://localhost:6419/").text

    # 加上启动参数
    wkhtmltopdf_options = {
        'enable-local-file-access': None,
        'encoding': 'utf-8'
    }
    content = re.sub('<h2 class="Box-title">([\s\S]*?)</h2>', '', content)
    html = markdown(content, output_format='html')  # MarkDown转HTML

    htmltopdf_file = "bin/wkhtmltopdf.exe"
    configuration = pdfkit.configuration(wkhtmltopdf=htmltopdf_file)
    pdfkit.from_string(html, output_path=pdf_file_to, configuration=configuration,
                       options=wkhtmltopdf_options)  # HTML转PDF
    print("转换成功...")
