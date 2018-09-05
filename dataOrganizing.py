import os
import sys


def clean(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename[0] == '.':
                os.system('rm -f %s' % (os.sep.join([dirpath, filename])))


def report(path):
    num_dir = {}
    need_dir = {}
    numbers = []
    for dirpath, dirnames, filenames in os.walk(path):
        if len(filenames) != 0:
            try:
                num_dir[len(filenames)].append(dirpath)
            except:
                num_dir[len(filenames)] = [dirpath, ]

    print("If you don't want to keep it, please type N/n. ")
    for num in num_dir:
        print(num, end='\t')
        print(len(num_dir[num]), end='')
        answer = input(':')
        if answer != 'N' and answer != 'n':
            numbers.append(num)

    print("\n\nIf you don't want to keep it, please type N/n. ")
    for num in num_dir:
        if num in numbers:
            need_dir[num] = []
            for dirpath in num_dir[num]:
                print(num, end='\t')
                print(dirpath, end='')
                answer = input(':')
                if answer != 'N' and answer != 'n':
                    need_dir[num].append(dirpath)
    print('\n\n')
    try:
        os.mkdir('Analysis')
    except:
        pass
    for num in need_dir:
        for dirpath in need_dir[num]:
            print(dirpath)
            try:
                os.system('mkdir Analysis%s%d%s%s' %
                          (os.sep, num, os.sep, '_'.join(dirpath.split(os.sep)[1:])))
                os.system('xcopy /Y %s Analysis%s%d%s%s > log.txt' %
                          (dirpath, os.sep, num, os.sep, '_'.join(dirpath.split(os.sep)[1:])))
            except:
                pass

clean('.')
report('unzip')
