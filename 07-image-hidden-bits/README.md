# Challenge 7

The task is to decrypt messages like these:

 * encrypted-image.png

## 1st Clue, The Hard Clue

**English:**
This seems to be an improvement on the previous ‘bytes in images’ messages. However, this time we cannot see any visible changes to the image at all. It seems they have managed to hide a message in the images without it being visible to the naked eye. How? Well, modern file formats allow users to embed metadata, like GPS coordinates or camera model, into images files but we have not seen any weird messages in any of the metadata fields. The leads us to believe that the secret message is somehow still hidden in the image data itself, but more cleverly hidden than before. Our best idea on how to crack this comes from the image names: All files seemed to be named ‘some random characters, an underscore, the letter R, G or B and then a number between 0 and 7’. We think that the last part of the name is the key to cracking this problem.

**Svenska:**
Det verkar som att vi den här gången har att göra med en förbättrad version av ‘bildkryptot’. Den här gången ser vi inga konstiga färger över huvud taget. Det verkar som att de lyckats dölja meddelandet på ett sätt som inte är synligt för ögat. Hur? Inte heller dessa bilder verkar ha någon dold information i några metadatafält. Det får oss att dra slutsatsen att de dolda meddelandena fortfarande är dolda i bilderna, men smartare dolt än tidigare. En av våra mer rutinerade analytiker har noterat att den här Telnet-prompten länkar till bilder vars namn börjar med lilla ‘b’ medan den tidigare prompten länkar till bilder med namn som börjar med stora ‘B’. Stora B kan tolkas som 'byte' medan lilla 'b' kan indikera 'bit', som i 10 MB/s eller 80 Mb/s.

## 2nd Clue, The Less Difficult Clue

**English:**
The human eye is not particularly good at noticing small hue differences between different pixels in an image. If the attackers changed a black pixel, which correspond to colour {0, 0, 0} (pure black in RGB colour), to {0, 0, 1} (ridiculously close to pure black but with a hint of blue not noticeable by the human eye) they would be able to add one bit of information into the image without anyone noticing it when looking at the image. If they change the right-most bit of the first 8 pixels in the image they would be able to encode 1 byte of data, and 1 byte of data corresponds to one letter (or digit). Could they have embedded a secret message into the images by changing the colours of the image in such a way? You can read more about this type of hiding a message on ____ and you can read more about computer colours on ____.

**Svenska:**
Det mänskliga ögat är inte speciellt bra på att märka små nyansskillnader mellan pixlar i en bild. Om attackerarna förändrar en svart pixel, som motsvarar färg (0,0,0) till (0,0,1) så kommer det inte gå att upptäcka, genom att bara titta på bilden, att pixeln inte är totalt svart utan egentligen svart med en löjligt svag blå nyans. På detta sätt skulle det gå att dölja en bit (en åttondels byte) i varje pixel. Om de ändrat den 'högra biten', även kallat LSB-biten, i de åtta första pixlarna i bilderna så skulle de kunna koda 1 byte av data, och 1 byte av data motsvarar en bokstav (eller siffra). Kan de ha sparat ett hemligt meddelande i bilderna genom att förändra färgerna på detta sätt? Du kan läsa mer om detta sätt att dölja information på https://stackoverflow.com/questions/1216156/how-can-you-hide-information-inside-a-jpg-or-gif-photo och du kan läsa mer om hur färger fungerar på datorer på http://www.rit-mcsl.org/fairchild/WhyIsColor/Questions/4-5.html.

## Code Samples

Not enough time to come up with full solution on your own? Get inspiration from the available solutions:

* The Python script, image_bits.py, contains one method for embedding a message into an image and for extracting a message from an image. This solution supports embedding the information into any of the three colour channels and can also write "horizontally or vertically".
* The Java application, spychallenge.HiddenBits, only does message extraction. It supports embedded messages in all three channels but does not support "vertical" messages (only "horizontal").