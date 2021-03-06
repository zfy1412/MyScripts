import os
import uuid
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')

screen = '脚本开始工作！'
file_path = '.\\'
print('确认目录为'+str(os.path.abspath('.')))
print(screen)

filename = str(uuid.uuid4())
filename.replace('-','')
filename = filename[0:8]+'.txt'
outfile = open(filename,'w',encoding='utf-8')

num1 = 0
num2 = 0

for root,dirs,files in os.walk(file_path):
    outfile.write(str(root)+'?')    #间隔符'?'
    print('目录：'+str(root))
    num2+=1
    for f in files:
        if f==filename or f==__name__:#不包括文件清单
            continue
        outfile.write(f+'?')
        print(f,end='  ') 
        num1+=1
    outfile.write('\n')
    print('\n---------------------')

outfile.close()
print('扫描完毕，共扫描%d个目录，有%d个文件'%(num2,num1))
