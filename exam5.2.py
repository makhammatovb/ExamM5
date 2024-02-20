import pdfkit
from time import perf_counter
import threading


def main(a):
    pdfkit.from_url(
        'https://tilshunos.com/omonims/' + str(a),
        'out' + str(a) + '.pdf', configuration=config)
    print(f'{a} Saved')


path_to_wkhtmltopdf = r"C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
base_url = 'https://tilshunos.com/omonims/'

start = perf_counter()
threads = []

for i in range(1, 15):
    thread = threading.Thread(target=main, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
finish = perf_counter()
print(f'{finish - start} sec')



