# Challenge 5

The task is to decrypt messages like these:

 * 3:1:29 2:9:5 6:10:29 2:13:24 3:9:31 3:8:136 1:2:1 2:9:5 3:2:71 3:1:20 4:6:11 3:1:29 1:1:4 1:2:17 3:8:136
 * 1:3:18 28:9:95 1:1:20 1:2:17 1:3:18 1:1:8 1:1:11 1:3:18 2:3:21 3:11:19 1:2:36 2:2:3 30:27:65
 * 74:43:66 2:6:1 6:1:3 15:11:13 2:12:17 1:2:3 15:36:139 2:6:1 6:39:60 6:40:23

## 1st Clue, The Hard Clue

**English:**
It seems that the attackers have come up with a new code system and this time they have used only digits and colons. Digits are grouped in groups of three, with colons in between. Our investigators have found this link which may or may not be related to the security measure: http://bit.ly/2tA7wGn. If the document that the link points to is the key to solving the cipher then there must be some additional component to it as well since Telnet does not support Swedish characters like å, ä and ö but maybe those characters are simply replaced by similar characters.

**Svenska:**
Det verkar som att attackerarna har hittat på ett nytt kodsystem och den här gången har de bara använd siffror och kolon. Siffror har grupperats tre och tre, med kolon mellan. Våra analytiker har också hittat den här länken som eventuellt är relaterad till säkerhetsmekanismen: http://bit.ly/2tA7wGn. Om dokumentet som länken pekar på är nyckeln till att lösa kryptot så måste det också finnas ytterligare en komponent till lösningen eftersom Telnet inte stödjer svenska tecken som å, ä och ö men de tecknen kanske bara ska ersättas av liknande bokstäver.

## 2nd Clue, The Less Difficult Clue

**English:**
We think that three-number groups represents individual words. It also seems that punctuation characters, like periods and dashes, are skipped. Interestingly, the first number of each number-group is never that large. Also, some number-groups are way more common than other.

**Svenska:**
Vi tror att tre-nummer-grupperna motsvarar enskilda ord. Det verkar också som att punkter, komman och liknande inte stöds av kryptot. Intressant är också att första talet i siffergrupperna ofta är ganska lågt. En del siffergrupper är också vanligare än andra.

## 3rd Clue, The Easy Clue

**English:**
The each number-group correspondes to <chapter>:<paragraph>:<word>. You need to load the XML file (the link) and somehow be able to fetch certain words or letters given a number group.

**Svenska:**
Varje siffergrupp motsvarar <kapitel>:<paragraf>:<ord>. Du måste läsa in XML-filen (länken) och på något sätt översätta varje siffergrupp till ord.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script, book.py, reads the input file (_input.txt_) and encrypts each line "using the book". It then decrypts the encrypted text so that you can see if all input words are present in the book.  
* The Java application, spychallenge.Book, only does decryption.

The Python script and the Java application use two different approaches to solving the problem. Both create a "map or dictionary" to simplify decryption but the Python script processes the book (which is an XHTML document) using an XML library whereas the Java application uses simple string processing (reading the XHTML document line by line and stripping out the XHTML tags). The line-by-line approach is feasible, in this case, because each paragraph is the book happens to be saved without any linefeed characters in the XHTML document.