#!/bin/bash
import os
import sys

clear

figlet TOOL SPAM | lolcat
echo '
[+] Pilih Menu Spam :
[1]. Spam Call Beta
[2]. Spam Sms 3×
[3]. Keluar
'
echo
read -p "Masukan Pilihan Anda : " pil
if [[ $pil == 1 ]]; then
os.system('clear')
os.system('git clone https://github.com/candranovanmahendra/Codot-Spam')
os.system('cd Codot-Spam')
os.system('sh Codot-Spam')
exit
fi
;
if [[ $pil == 2 ]]; then
os.system('clear')
os.system('pkg install python2')
os.system('git clone https://github.com/candranovanmahendra/sms.py')
os.system('cd sms.py')
os.system('python2 sms.py')
exit
fi
;
if [[ $pil == 3 ]]; then
exit
fi
;
