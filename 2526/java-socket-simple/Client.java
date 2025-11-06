import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws IOException {
        String host = args.length > 0 ? args[0] : "localhost";
        int port = args.length > 1 ? Integer.parseInt(args[1]) : 5000;
        String oneshot = args.length > 2 ? args[2] : null;
        if (oneshot != null) {
            sendOne(host, port, oneshot);
        } else {
            interactive(host, port);
        }
    }
    private static void interactive(String host, int port) throws IOException {
        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true);
             Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8)) {
            System.out.println(in.readLine());
            while (true) {
                System.out.print("> ");
                String line = scanner.nextLine();
                if (line == null) break;
                out.println(line);
                String resp = in.readLine();
                if (resp == null) { System.out.println("(connessione chiusa)"); break; }
                System.out.println(resp);
                if ("EXIT".equalsIgnoreCase(line.trim())) break;
            }
        }
    }
    private static void sendOne(String host, int port, String cmd) throws IOException {
        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true)) {
            in.readLine(); // greeting
            out.println(cmd);
            String resp = in.readLine();
            if (resp != null) System.out.println(resp);
        }
    }
}
