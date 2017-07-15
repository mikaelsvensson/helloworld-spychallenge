package spychallenge;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;

public class HiddenBits {
    enum Channel {
        red(16),
        green(8),
        blue(0);
        private int leastSignificantBitPositionInByte;

        Channel(int leastSignificantBitPositionInByte) {
            this.leastSignificantBitPositionInByte = leastSignificantBitPositionInByte;
        }
    }

    public static void main(String[] args) throws IOException {
        Channel channel = Channel.valueOf(args[0]);
        for (int i = 1; i < args.length; i++) {
            final String imagePath = args[i];

            final String message = decrypt(imagePath, channel);

            System.out.format("Text i fil %s:%n", imagePath);
            System.out.println(message);
            System.out.println();
        }
    }

    private static String decrypt(String imagePath, Channel channel) throws IOException {
        final BufferedImage image = ImageIO.read(new File(imagePath));
        final int width = image.getWidth();
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        while (true) {
            byte currentByte = 0;
            for (int pixelOffset = 0; pixelOffset < 8; pixelOffset++) {
                final int pixel = bytes.size() * 8 + pixelOffset;
                final int rgb = image.getRGB(pixel % width, pixel / width);

                final int bitInByte = 7 - pixelOffset;

                final int channelValue = (rgb >> channel.leastSignificantBitPositionInByte) & 0xFF;
                final int bit = channelValue & 0x1;

                currentByte += bit << bitInByte;
            }
            if (currentByte == '\0') {
                break;
            } else {
                bytes.write(currentByte);
            }
        }
        return new String(bytes.toByteArray(), Charset.forName("utf-8"));
    }
}
