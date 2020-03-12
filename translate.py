import xlrd, xlwt
import os
from googletrans import Translator
import sys

def main(DEST_LANG='ja', IN_FILE_NAME='in.xlsx', OUT_FILE_NAME = 'out.xls'):
    
    translator = Translator()
    # Set file path
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    workbook_r = xlrd.open_workbook(IN_FILE_NAME, encoding_override="utf-8")
    worksheet_r = workbook_r.sheet_by_index(0)

    workbook_w = xlwt.Workbook()
    worksheet_w = workbook_w.add_sheet('Sheet 1')

    for row in range(0, worksheet_r.nrows):
        cont = worksheet_r.cell_value(row,0)
        translated = translator.translate(cont, dest=DEST_LANG)
        try:
            worksheet_w.write(row, 0, translated.text)
        except:
            print(translated)
            print(sys.exc_info()[0])
            raise
    workbook_w.save(OUT_FILE_NAME)

if __name__ == '__main__':
    main()