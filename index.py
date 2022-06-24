import re
import os
from shutil import move

def help():
    print("Ceci est un trieur de fichiers pour les cours.")

def svt():
    files = os.listdir()
    if not os.path.exists('SVT'):
        os.makedirs('SVT')
    for f in svt_files:
        move(f, 'SVT')

def pc():
    files = os.listdir()
    if not os.path.exists('PC'):
        os.makedirs('PC')
    for f in pc_files:
        move(f, 'PC')

def snt():
    files = os.listdir()
    if not os.path.exists('SNT'):
        os.makedirs('SNT')
    for f in snt_files:
        move(f, 'SNT')

def maths():
    files = os.listdir()
    if not os.path.exists('Maths'):
        os.makedirs('Maths')
    for f in maths_files:
        move(f, 'Maths')

def espa():
    files = os.listdir()
    if not os.path.exists('Espagnol'):
        os.makedirs('Espagnol')
    for f in espa_files:
        move(f, 'Espagnol')

def en():
    files = os.listdir()
    if not os.path.exists('Anglais'):
        os.makedirs('Anglais')
    for f in en_files:
        move(f, 'Anglais')

def fr():
    files = os.listdir()
    if not os.path.exists('Français'):
        os.makedirs('Français')
    for f in fr_files:
        move(f, 'Français')

def ses():
    files = os.listdir()
    if not os.path.exists('SES'):
        os.makedirs('SES')
    for f in ses_files:
        move(f, 'SES')


def hg():
    files = os.listdir()
    if not os.path.exists('Histoire-Géo'):
        os.makedirs('Histoire-Géo')
    for f in hg_files:
        move(f, 'Histoire-Géo')

def nsi():
    files = os.listdir()
    if not os.path.exists('NSI'):
        os.makedirs('NSI')
    for f in nsi_files:
        move(f, 'NSI')

def inge():
    files = os.listdir()
    if not os.path.exists('Sc. Ingénieur'):
        os.makedirs('Sc. Ingénieur')
    for f in inge_files:
        move(f, 'Sc. Ingénieur')

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
nsi_files = [f for f in files if re.search(r'_nsi', f)]
inge_files = [f for f in files if re.search(r'_inge', f)]

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

if nsi_files:
    print(nsi_files)
    nsi()

if inge_files:
    print(inge_files)
    inge()