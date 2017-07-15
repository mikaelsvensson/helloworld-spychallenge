# Challenge 3

The task is to decrypt messages like these:

 * knk vyfovkmo fkb odd wkdowkdscu qoxs ymr exnob pybcdk rkvfkx kf kbdyxrexnbkdkvod cukzkno ryx fkn cyw cuevvo fsck csq fkbk nox pybcdk nkdybkvqybsdwox.
 * pybcukbox crsbvoi tkmucyx qtybno nod wytvsqd pyb kxnbk kdd ezzpsxxk dovopkhox, uxkzzdovopyxox, cyvmovvob ymr yzdscuk uklvkb lvkxn wimuod kxxkd.
 * exnob kxnbk fkbvncubsqod ezzpkxx cuknoczovobcukx ymr ezzpsxxkbox roni vkwkbb ox wodyn pyb kdd bknsycdibk dybzonob ymr cyw coxkbo vkno qbexnox pyb lvkxnkd qzc.

## 1st Clue, The Hard Clue

**English:**
It’s clear that the attackers are using some kind of letter substitution encryption. We found this ‘word wheel’ laying around in one suspect’s apartment and we’re working under the assumption that we are dealing with a so called ‘Caesar cipher’, but we don’t know how many steps to turn it. Side note: We get a new crypto to solve every time we connect to the machine but presumably all can be solved in the same way.

**Svenska:**
Det är tydligt att attackerarna använder någon sorts kryptering där varje bokstav i alfabetet byts ut mot en annan. Vi hittade det här ‘ordhjulet’ i en misstänkts lägenhet och vi arbetar utifrån tesen att vi har att göra med ett s.k. Caesar-chiffer, men vi vet inte hur många steg som varje bokstav har förskjutits. Notering: Vi får inte alltid samma krypto när vi ansluter till attackerarnas Telnet-server men vi utgår ifrån att alla kan lösas på samma sätt.

## 2nd Clue, The Less Difficult Clue

**English:**
If you don’t want to write a program that generates 20-something different possible solutions, one per offset, you could automate it by using a list of the most common Swedish words and see which offset produces the most Swedish words in the output.

**Svenska:**
Om du inte vill skriva ett program som genererar 20-någonting olika lösningsförslag, ett per förskjutningssteg, så kan du automatisera det genom att använda en lista över de vanligaste orden i svenska språket och räkna vilket lösningsförslag som resulterar i flest svenska ord.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script ceasar_basic.py can both encrypt and decrypt messages.  