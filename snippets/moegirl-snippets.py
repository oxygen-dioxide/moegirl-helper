import yaml
from openpyxl import load_workbook
wb = load_workbook("moegirl-snippets.xlsx")
ws=wb[wb.sheetnames[0]]
snippet_dict={}
for i in range(2,ws.max_row):
    keys=ws.cell(row=i,column=1).value.split(";")
    #print(keys)
    if(keys[0][0]!="\\"):#以反斜杠开头的行视为注释
        for key in keys:
            body="{{"+ws.cell(row=i,column=2).value
            if("\n" in body):
                body=body.split("\n")
            description=ws.cell(row=i,column=3).value
            snippet_dict[key]={"prefix":"{{"+key,"body":body,"description":description}
outstr=""
line=""
with open("snippets.yaml",encoding="utf8") as infile:
    while(not(line.startswith("#="))):
        line=infile.readline()
        outstr+=line
outstr+=yaml.dump(snippet_dict,allow_unicode=True)
with open("snippets.yaml","w",encoding="utf8") as outfile:
    outfile.write(outstr)
    