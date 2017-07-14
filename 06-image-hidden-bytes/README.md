# Challenge 6

## 1st Clue, The Hard Clue

English:
This one is really different from the other self-destruct mechanisms. The server still gives you a prompt when you connect to it but instead of a question it only shows a link to an image. The images are clearly not encrypted since they can be opened and viewed in any decent image viewer or web browser. Presumably the image is either the key to figuring out the password or the password is somehow hidden in the image. We are leaning towards the latter, that there is a message hidden inside the image file somehow. Now, modern file formats allow users to embed metadata, like GPS coordinates or camera model, into images files but we have not seen any weird messages in any of the metadata fields. We noticed that the pixels (colours) in the upper left corner of each image seem a bit ‘off’. This leads us to believe that the secret message is somehow hidden in the image data itself, maybe by changing the colors somehow. We suggest to you process the images using some kind of library which allows you to look at the colours of every pixel in the images.

Svenska:
Den här är rejält annorlunda från de andra säkerhetsmekanismerna. Servern ger dig fortfarande en prompt när du ansluter men istället för bokstäver, siffror eller något som kan påminna om ord så visas bara en länk till en bild. Bilden är definitivt inte krypterad eftersom den kan öppnas och visas i vilket dugligt bildvisarprogram som helst. Förmodligen är bilden antingen nyckeln till att få ett lösenord eller så är lösenordet på något sätt dolt i bilden. Vi anar att det är det senare, att lösenordet på något sätt är dolt i bilden. Moderna filformat kan innehålla metadata, såsom information om GPS-koordinater eller kameramodell, men våra analytiker har inte funnit någon dold data i bildernas metadatafält. Vi har också noterat att pixlarna (färgerna) i övre vänstra hörnen på bilderna är ‘en smula konstiga’. Detta får oss att tro att det hemliga meddelandet på något sätt är dolt i själva bilddatat, kanske genom att förändra färgerna på något sätt. Vi föreslår att du undersöker bilderna med något sorts funktionsbibliotek som ger dig möjlighet att undersöka färgerna i varje pixel.

## 2nd Clue, The Less Difficult Clue

English:
Colours on computer screens are always composed of some amount of red, green and blue light (sometimes referred to as the three ‘colour channels’). No red, no green and no blue means black and maximum of each means white. All other colours can be made by setting the values for red, green and blue to values between 0 (no colour) to 255 (maximum colour). This range, 0-255, is also the range for a ‘byte’, meaning that each colour channel value of a pixel holds data equivalent to a character on the keyboard (letters, digits, punctuation and so on). In the images the attackers use we see that the first pixels in the image have sort of a ‘blue tint’. It would be interesting to see if the blue channel holds some interesting data...

Svenska:
Färger på datorskärmar består alltid av någon mängd rött, grönt och blått ljus (vilket ibland kallas för de tre ‘färgkanalerna’). Inget rött, grönt och blått ljus betyder svart och maximalt av varje betyder vitt. Alla andra färger kan skapas genom att sätta värdena för rött, blått och grönt till värden mellan 0 (ingen färg) och 255 (maximalt med färg). Detta intervall, 0-255, är också intervallet för värden som kan lagras i en ‘byte’, vilket betyder att värdet för en pixel i en färgkanal använder lika mycket data som en bokstav, siffra, punkt osv. från tangentbordet. I bilderna som attackerarna länkar till så ser vi att de första pixlarna har en sorts ‘färgtoning’ mot antingen rött, grönt eller blått. Det vore intressant att undersöka om motsvarande färgkanal innehåller någon intressant data... 

## 3rd Clue, The Easy Clue

English:
We have gather enough sample data to conclusively state that the hidden message is encoded into the images by first transforming the message into a series of bytes (a byte array) and then replacing the ‘blue channel values’, starting at the upper left pixel and moving downwards, with the bytes of the message. In order to know where the message ends, it seems the attackers set the ‘blue channel value’ to 0.

Svenska:
Vi har samlat in tillräckligt med information för att vara säkra på att det dolda meddelandet är kodat i varje bild genom att först göra om meddelandet, textsträngen, till en serie av bytes (en ‘byte array’) och sedan ersätta ‘det blå värdet’, med början i övre vänstra hörnet, med dessa bytes. För att avsluta meddelandet så verkar attackerarna avsluta ‘byte-arrayen’ med värdet 0.
