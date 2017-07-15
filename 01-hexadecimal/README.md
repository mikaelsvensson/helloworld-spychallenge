# Challenge 1

The task is to decode messages like these:

* 75088FF08
* 65438E3ED
* 20ED5EA4CD

## 1st Clue, The Hard Clue

**English:**
What is this that the attackers have used this time? It almost looks like numbers, but there are letters in them! It seems not all letters are present though. Could this be a different type of numbers? How can we convert them to normal ones?

**Svenska:**
Vad är det som attackerarna har använt den här gången? Det ser ut som nummer men med bokstäver inuti! Det verkar dock inte som att alla bokstäver är representerade. Kan det här vara en annan typ av nummer? Hur kan de konverteras till vanliga nummer?

## 2nd Clue, The Less Difficult Clue

**English:**
The attackers like to use Hexadecimal to hide the tracks we might find. We found in previous attacks that internet pin codes were hidden like this.

**Svenska:**
Attackerarna verkar gilla att använda hexadecimala värden för att dölja sina spår. Vi vet sedan tidigare attacker att pin-koder ibland döljs så här.

## 3rd Clue, The Easy Clue

**English:**
Hexadecimal uses sixteen distinct symbols, most often the symbols 0–9 to represent values zero to nine, and A, B, C, D, E, F (or alternatively a, b, c, d, e, f) to represent values ten to fifteen. Convert hexadecimal values to plain decimal numbers.

**Svenska:**
Hexadecimala tal använder sexton symboler, oftast används 0-9 för att representera värdena noll till nio och sedan A-F (eller a-f) för att representera tio till femton. Konvertera hexadecimala värden till vanliga decimala tal.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script hex_encoding.py can both encode and decode messages (we use the words encode/decode instead of encrypt/decrypt since hexadecimal notation was never intended as a way of sending secret information).  