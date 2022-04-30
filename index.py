import re
import os
from shutil import move

def help():
    print("Ceci est un trieur de fichiers pour les cours.")

def svt():
    files = os.listdir()
    #get all files with _svt in the name
    svt_files = [f for f in files if re.search(r'_svt', f)]
    #if SVT folder doesn't exist, create it
    if not os.path.exists('SVT'):
        os.makedirs('SVT')
    #move all files with _svt in the directory called SVT
    for f in svt_files:
        move(f, 'SVT')

def pc():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('PC'):
        os.makedirs('PC')
    #move all files with _svt in the directory called SVT
    for f in pc_files:
        move(f, 'PC')

def snt():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('SNT'):
        os.makedirs('SNT')
    #move all files with _svt in the directory called SVT
    for f in snt_files:
        move(f, 'SNT')

def maths():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('Maths'):
        os.makedirs('Maths')
    #move all files with _svt in the directory called SVT
    for f in maths_files:
        move(f, 'Maths')

def espa():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('Espagnol'):
        os.makedirs('Espagnol')
    #move all files with _svt in the directory called SVT
    for f in espa_files:
        move(f, 'Espagnol')

def en():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('Anglais'):
        os.makedirs('Anglais')
    #move all files with _svt in the directory called SVT
    for f in en_files:
        move(f, 'Anglais')

def fr():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('Français'):
        os.makedirs('Français')
    #move all files with _svt in the directory called SVT
    for f in fr_files:
        move(f, 'Français')

def ses():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('SES'):
        os.makedirs('SES')
    #move all files with _svt in the directory called SVT
    for f in ses_files:
        move(f, 'SES')


def hg():
    files = os.listdir()
    #if SVT folder doesn't exist, create it
    if not os.path.exists('Histoire-Géo'):
        os.makedirs('Histoire-Géo')
    #move all files with _svt in the directory called SVT
    for f in hg_files:
        move(f, 'Histoire-Géo')


files = os.listdir()
hg_files = [f for f in files if re.search(r'_hg', f)]
ses_files = [f for f in files if re.search(r'_ses', f)]
fr_files = [f for f in files if re.search(r'_fr', f)]
en_files = [f for f in files if re.search(r'_en', f)]
espa_files = [f for f in files if re.search(r'_espa', f)]
maths_files = [f for f in files if re.search(r'_maths', f)]
snt_files = [f for f in files if re.search(r'_snt', f)]
pc_files = [f for f in files if re.search(r'_pc', f)]
svt_files = [f for f in files if re.search(r'_svt', f)]

if svt_files:
    print(svt_files)
    svt()

if pc_files:
    print(pc_files)
    pc()

if snt_files:
    print(snt_files)
    snt()

if maths_files:
    print(maths_files)
    maths()

if espa_files:
    print(espa_files)
    espa()

if en_files:
    print(en_files)
    en()

if fr_files:
    print(fr_files)
    fr()

if ses_files:
    print(ses_files)
    ses()

if hg_files:
    print(hg_files)
    hg()