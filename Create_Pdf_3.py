import os
import re
from docx2pdf import convert
import shutil
list1 = []

zip_file = re.compile(r'.+\.zip')
for path,folders,files1 in os.walk('./'):
    for files in files1:
        if zip_file.match(files):
            files = zip_file.match(files).group()
            out_file = os.path.splitext(files)[0]
            shutil.unpack_archive(files,os.path.join(path,out_file))
            os.remove(path+files)
            
doc_File = re.compile(r'(.+docx)')

for path,folders,files in os.walk('./'):
	# print("Thisi is "+path)
	for file in os.listdir(path):
		if doc_File.match(file):
			doc_result = doc_File.match(file).group()
			convert(path+'/'+doc_result, path+'/'+doc_result+'.pdf')
			convert(path)
			# print(path+' '+doc_result)
def exec_file():
    
    dcx_pat = re.compile(r'(.+docx.pdf)')
    pdf_file =  re.compile(r'(.+docx)')
    py_file = re.compile(r'(.+py)')
            
    for path,folder,files in os.walk('./'):
        for file in files:
            if dcx_pat.match(file):
                os.remove(path+'/'+file)

    for path,folder,files in os.walk('./'):
        for file in files:                
            if pdf_file.match(file):
                os.remove(path+'/'+file)
                
    for files in os.listdir('./'):
        if not py_file.match(files):
            print(files)
            shutil.make_archive('./'+files,'zip','./'+files)
            # shutil.rmtree('./'+files)
    for path,folders,files in os.walk('./'):
    	for file in folders:
    		shutil.rmtree(path+file)
exec_file()
