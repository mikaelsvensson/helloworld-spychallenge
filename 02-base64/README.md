# Challenge 2

The task is to decode messages like these:

 * VGhlcmUncyBubyBuZWVkIHRvIGltYWdpbmUgdGhhdCB5b3UncmUgYSB3b25kcm91cyBiZWF1dHksIGJlY2F1c2UgdGhhdCdzIHdoYXQgeW91IGFyZS4=
 * SSBkbyBub3QgdW5kZXJzdGFuZCB3aHkgdGhlIGhlcm9pbmUgaW4gdGhlIGJvb2sgaXMgYWx3YXlzIHByZXR0aWVyIHRoYW4gdGhlIG9uZSBhdCBob21lLg==
 * VGhhdCdzIG1vc3QgZXh0cmFvcmRpbmFyeSwgYnV0IEknbSBzbyB1c2VkIHRvIHlvdXIgZG9pbmcgZXh0cmFvcmRpbmFyeSB0aGluZ3MgdGhhdCBub3RoaW5nIHN1cnByaXNlcyBtZS4gQmVzaWRlcyBJJ20gZmVlbGluZyBtZWxhbmNob2x5IGp1c3Qgbm93Lg==

## 1st Clue, The Hard Clue

**English:**
The attackers’ code is made with only lowercase letter, uppercase letters, numbers and some = signs. There are no spaces between words or anything that looks obviously like a word, so it doesn’t seem that we would be able to replace letters and find the solution. But we’ve seen this encoding before, around the web.

**Svenska:**
Attackerarnas kod består bara av små bokstäver, stora bokstäver, siffror och några likhetstecken. Det finns inga mellanrum mellan ord, eller något som liknar ord, så det verkar inte som att vi kan byta ut bokstäver för att hitta lösningen. Men vi har sett den här sortens kodning förut, på webben.

## 2nd Clue, The Less Difficult Clue

**English:**
A closer look reveals that this encoding looks really similar to something that appears in a lot of long URLs. Our analyst says that the encoding is something called base64, and that it is used to convert any text (or information of any kind) into just letters and numbers.

**Svenska:**
En närmare granskning visar att den här kodningen är väldigt lik något som syns i långa URL:er på nätet. Vår analytiker menar att kodningen kallas base64, och att den används för att konvertera text (eller vilken information som helst) till bara bokstäver och siffror.

## 3rd Clue, The Easy Clue

**English:**
Many programming languages have functions to decode base64. You can probably also find something to do it online.

**Svenska:**
Många programmeringsspråk har funktioner för att avkoda base64. Du kan säkert också hitta något på webben för att göra det åt dig.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script base64_encoding.py can both encode and decode messages (we use the words encode/decode instead of encrypt/decrypt since Base64 was never intended as a way of sending secret information).  