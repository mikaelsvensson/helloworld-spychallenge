package spychallenge;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Dictionary {
    public static void main(String[] args) throws IOException {
        final List<String> words = Files.lines(new File("./dictionary.txt").toPath())
                .map(s -> s.substring(0, s.indexOf('\t')))
                .collect(Collectors.toList());

        final String message = Stream.of(args)
                .map(s -> words.get(Integer.parseInt(s) - 1))
                .collect(Collectors.joining(" "));

        System.out.println(message);
    }
}
