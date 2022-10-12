import openpyxl         
deez=openpyxl.load_workbook("C:\\Users\\Lopez\\test\\Actual Amazon.xlsx")
print(type(deez))

sheets=deez.sheetnames
print(sheets)
sh1=deez['Sheet1']  
info=sh1['E2'].value 
print(info)