import os
import datetime

def rec(dir, mdir):
    for (dirpath, dirnames, files) in os.walk(dir):
        try:
            if mdir != dirpath.split('\\')[4]:
                mdir = dirpath.split('\\')[4]
                print(mdir)
        except:
            pass
        for file in files:
            if file.endswith('.py'):
                print('   ' + file)
                print('   DataMod: ' + str(datetime.datetime.fromtimestamp(os.path.getmtime(dir + '\\' + file))))
        if len(dirnames) != 0:
            for i in range(len(dirnames)):
                rec(dir + '\\' + dirnames[i], mdir)
        return 0
rec("C:\\Users\\79101\\Desktop", '')
#рекурсивная функция для вывода всех *.py файлов в заданном каталоге и подкаталогах с выводом даты изменения