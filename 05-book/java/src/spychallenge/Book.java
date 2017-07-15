package spychallenge;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Book {

    private static final String PARAGRAPH_PREFIX = "<p class=\"br-dtext-pfa br-dtext-pfa-override-1\" xml:lang=\"sv\"><span class=\"no-style-override-2\">";
    private static final String PARAGRAPH_SUFFIC = "</span></p>";
    private static final Pattern SWEDISH_WORD_PATTERN = Pattern.compile("[a-zA-ZåäöÅÄÖ][a-zA-ZåäöÅÄÖ-]*");

    public static void main(String[] args) throws IOException {
        List<List<List<String>>> book = new ArrayList<>();
        List<List<String>> currentChapterParagraphs = null;

        final Path bookPath = new File("../selma-lagerlof-nils-holgerssons-underbara-resa-genom-sverige.xml").toPath();
        final List<String> lines = Files.lines(bookPath)
                .map(String::trim)
                .map(String::toLowerCase)
                .map(s -> s.replace("<br/>", " "))
                .map(s -> s.replace("</span><span class=\"no-style-override-2\">", " "))
                .collect(Collectors.toList());
        boolean newChapterFound = false;
        for (String line : lines) {
            if (line.startsWith(PARAGRAPH_PREFIX)) {
                if (newChapterFound) {
                    newChapterFound = false;
                    currentChapterParagraphs = new ArrayList<>();
                    book.add(currentChapterParagraphs);
                }
                final ArrayList<String> words = new ArrayList<>();
                final String xmlElementContent = line.substring(PARAGRAPH_PREFIX.length(), line.length() - PARAGRAPH_SUFFIC.length());
                final Matcher matcher = SWEDISH_WORD_PATTERN.matcher(xmlElementContent);
                while (matcher.find()) {
                    final String word = matcher.group(0);
                    words.add(word);
                }
                currentChapterParagraphs.add(words);
            } else if (line.startsWith("<h1") || line.startsWith("<h2")) {
                newChapterFound = true;
            }
        }
        for (String sentenceCode : new String[]{
                "39:10:1 1:1:1 1:1:4 91:6:177 15:26:6 2:12:17 22:12:45 1:3:18 16:21:38 1:1:36",
                "1:1:34 1:1:3 1:2:17 1:3:38 2:9:5 60:2:76 3:5:74 1:1:36 1:1:34 3:5:69 4:29:3 3:5:74 2:14:28 3:1:39 2:2:3 2:4:5 7:28:26 2:2:3",
                "4:41:22 20:1:148 32:27:155 1:2:27 54:8:81 1:1:4 3:26:44 1:2:1 3:1:20 46:51:11",
                "3:29:18 3:3:81 2:3:21 2:4:2 3:29:18 3:3:81 4:10:44 2:3:21 1:3:18 2:2:3 3:1:20 4:27:12 3:5:67 54:8:81 5:14:89"
        }) {
            final String translation = Stream.of(sentenceCode.split(" "))
                    .map(wordCode -> wordCode.split(":"))
                    .map(positionTriple -> book
                            .get(Integer.parseInt(positionTriple[0]) - 1)
                            .get(Integer.parseInt(positionTriple[1]) - 1)
                            .get(Integer.parseInt(positionTriple[2]) - 1))
                    .collect(Collectors.joining(" "));
            System.out.println(translation);
        }
    }
}
