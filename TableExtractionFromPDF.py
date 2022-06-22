import camelot


tables = camelot.read_pdf('/Users/raulgiron/Downloads/automation-main/1.Table Extraction/foo.pdf', pages='1')
print(tables)

# tables.export('/Users/raulgiron/Desktop/AutomateWithPython/foo.csv', f='csv', compress=False)
tables[0].to_csv('/Users/raulgiron/Desktop/AutomateWithPython/foo.csv')
