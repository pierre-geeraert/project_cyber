# Xor decoder
this programm help you to decrypt a file encoded in XOR 

## Prerequisites
clone the repo
```
git clone git@github.com:pierre-geeraert/project_cyber.git
```
navigate into this folder
```
cd projet_cyber
```
Install the virtual env
```
python3.7 -m venv .env
```
Activate this environment
```
source .env/bin/activate
```
Install all the dependencies
```
pip install -r requirements.txt```
```
## generate a wordlist
In this example, this programm generate a wordlist with every letter in lower case , from 1 letter to 15 letter
```
python wgen.py  -chr=abcdefghijklmnopqrstuvwxyz -min=1 -max=15 -out=wordlist.txt
```

## test a password for a specific file
```
python xor_converter.py "12345" "PA.txt" "PA_decrypted.txt"
```
Where 12345 is the password <br/> 
PA.txt is the encrypted file <br/> 
PA_decrypted.txt will be the decrypted file

## compare the percentage of word with a dictionnary
```
python word_checker.py "liste_francais.txt" "ISO-8859-1" "FICHIERS/PA_decrypted.txt" "ISO-8859-1"
```
where liste_francais.txt is the list wit some french words <br/>
where the first "ISO-8859-1" is the encoding of the list with some words<br/>
where "FICHIERS/PA_decrypted.txt" is the decrypted file<br/>
where  the second "ISO-8859-1"  is the encoding of the decrypted file<br/>
 