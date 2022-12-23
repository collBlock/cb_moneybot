from openpyxl import load_workbook

with open('bot\count_run.py', 'w') as file:  # накидываем на счетчик +1
        file.write(f'n = 1')
wb = load_workbook(filename='origin.xlsx')
wb.save('way_to_dream.xlsx')