import os, sys, time
import pandas as pd
import pycurl
import tabula

'''
# Используем tabula для извлечения данных таблиц из PDF
dfs = tabula.read_pdf(pdf_path, pages='all', lattice=True)

# Объединяем все страницы в один DataFrame (если таблица на нескольких страницах)
combined_df = pd.concat(dfs, ignore_index=True)

# Сохраняем DataFrame в CSV файл
combined_df.to_csv(csv_output_path, index=False)
'''

class Parse:
    def __init__(self) -> None:
        self.PATH_IN = "r.pdf"
        self.PATH_OUT = "data.csv"
    
    def ConvertFile(self):
        pass
    def DownloadFile(self, day):
        #os.system(f'curl -o "{os.getcwd()}\{self.PATH_IN}" "https://www.permaviat.ru/_engine/get_file.php?f={day}&d=_res/fs/&p=file.pdf"')
        url = f"https://www.permaviat.ru/_engine/get_file.php?f={day}&d=_res/fs/&p=file.pdf"

        with open(os.path.join(os.getcwd(), self.PATH_IN), 'wb') as file:
            Curl = pycurl.Curl()
            Curl.setopt(Curl.URL, url)
            Curl.setopt(Curl.WRITEDATA, file)
            Curl.perform()
            Curl.close()

    def Main(self):
        self.DownloadFile(3926)
        time.sleep(1)
        self.ConvertFile()

if __name__ == "__main__":
    Parse().Main()