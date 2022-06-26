from openpyxl import load_workbook
from openpyxl.styles import Font


# Read workbook and select sheet
wb = load_workbook('/Users/raulgiron/Desktop/AutomateWithPython/pivot_table_barchart.xlsx')
sheet = wb['Report']

sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save('/Users/raulgiron/Desktop/AutomateWithPython/formatted-cells_pivot_table_barchart.xlsx')
