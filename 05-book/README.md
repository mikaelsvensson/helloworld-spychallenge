# Challenge 5

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
