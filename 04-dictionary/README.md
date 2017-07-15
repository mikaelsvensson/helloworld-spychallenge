# Challenge 4

The task is to decrypt messages like these:

 * 1 159 1204 39 4005 201 1031
 * 1 228 9447 4 40 786 9 8 1031 9 586
 * 16 17 7525 23 1031 110 72 16 333 148 9 132 11670 8 1779

## 1st Clue, The Hard Clue

**English:**
The prompt when connecting to this Telnet port only shows a bunch of numbers but we have intercepted two interesting text messages from one of the suspects. The first contained numbers similar to the prompts but the second contained this link: http://s3-us-east-2.amazonaws.com/sibuna/stats_EUROPARL-EN.txt. The link is presumably the key to decrypting the messages.

**Svenska:**
Prompten när du kopplar upp dig mot Telnet-porten visar bara en massa nummer men vi har snappat upp två intressanta SMS från en av de misstänkta. Det första innehöll nummer precis som i Telnet-prompten men det andra innehåll den här länken: http://s3-us-east-2.amazonaws.com/sibuna/stats_EUROPARL-EN.txt. Länken är förmodligen nyckeln till att dekryptera meddelandena, och därmed förhoppningsvis även Telnet-prompten.

## 2nd Clue, The Less Difficult Clue

**English:**
It seems low numbers appear more often than high numbers.

**Svenska:**
Det verkar som att låga nummer dyker upp oftare än höga nummer.

## 3rd Clue, The Easy Clue

**English:**
The highest number is never larger than the number of lines in the big text file.

**Svenska:**
Det högsta numret är inte större än antalet rader i den stora textfilen.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script, dictionary_compression.py, reads the input file (_input.txt_) and encrypts each line using the wordlist. It then decrypts the encrypted text so that you can see if all input words are present in the book.  
* The Java application, spychallenge.Dictionary, only does decryption.