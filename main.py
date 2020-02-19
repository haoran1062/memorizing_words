# encoding:utf-8
import os, sys, shutil, random, time, datetime, pyttsx3
from glob import glob

from random import shuffle

def get_word_list(in_path):
    l = []
    with open(in_path, 'r', encoding='utf-8') as f:
        for line in f:
            lt = line.strip().split(',')
            if len(lt) != 2:
                print(line + ' fucked!!!')
                exit()
            [a, b] = lt
            b_list = b.split(';')
            l.append([a, b_list])
        shuffle(l)
    return l

def save_state(out_bpath, word_list):
    out_file = out_bpath + '%s.txt'%(datetime.datetime.now().strftime('%Y-%m-%d'))
    with open(out_file, 'w', encoding='utf-8') as f:
        for [a, b, c] in word_list:
            s = a + ',' + ';'.join([i for i in b]) + '|%d\n'%(c)
            f.write(s)
        
def load_state(in_file):
    if not os.path.exists(in_file):
        return []
    else:
        l = []
        with open(in_file, 'r', encoding='utf-8') as f:
            for line in f:
                lt = line.strip().split(',')
                [a, b] = lt
                [b, c] = b.split('|')
                c = int(c)
                b = [i for i in b.split(';')]
                print(a, b, c)
                l.append([a, b, c])
        return l

def memorizing(word_list, out_bpath = 'datasets/memorizing_history/', correct_num=2):
    tts = pyttsx3.init()

    
    history_file = out_bpath + '%s.txt'%(datetime.datetime.now().strftime('%Y-%m-%d'))
    history_word_list = load_state(history_file)
    if history_word_list:
        word_list = history_word_list
    else:
        word_list = [[a, b, correct_num] for [a, b] in word_list]

    st = input(u'开始背单词 [Y/n]: ')
    if st.lower() == 'n':
        return
    else:
        while word_list:
            
            [a, b, c] = word_list[0]
            sb = ';'.join([i for i in b])
            print_ch = random.choice([True, True, False])
            if print_ch:
                print(sb + u' 的英文拼写:\n\t')
                s = input('')
                if s == a:
                    print('牛逼！ correct!')
                    c -= 1
                    word_list[0][-1] = c
                    if c == 0:
                        word_list.pop(0)
                else:
                    print(u'wrong! correct spell is :' + a)
                    word_list[0][-1] += 1
            else:
                print(a + u' 的中文含义:\n\t')
                s = input('')
                if s in b:
                    print('牛逼！ correct!')
                    c -= 1
                    word_list[0][-1] = c
                    if c == 0:
                        word_list.pop(0)
                else:
                    print(u'wrong! %s 的中文含义为 :'%(a))
                    print('\t' + ';'.join([i for i in b]))
                    word_list[0][-1] += 1
            
            save_state(out_bpath, word_list)
            shuffle(word_list)
            tts.say(a + sb)
            tts.runAndWait()
            # time.sleep(1)
            os.system('clear')
        
        print(u'今天单词背完了！又是牛逼的一天~')
        tts.say(u'今天单词背完了！又是牛逼的一天 哈哈哈~')
        tts.runAndWait()

if __name__ == "__main__":
    base_path = 'datasets/word_lists/'
    memorize_base_path = 'datasets/memorizing_history/'
    correct_number = 2

    unit = input(u'单词表ID:')
    word_path = base_path + 'unit' + unit + '.txt'
    word_list = get_word_list(word_path)
    memorizing(word_list, out_bpath=memorize_base_path, correct_num=correct_number)
