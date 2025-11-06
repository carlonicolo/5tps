import java.io.*;
import java.net.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Server {
    private final int port;

    public Server(int port) {
      this.port = port;
    }

    public void start() throws IOException {
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("[server] Listening on port " + port);
            while (true) {
                Socket client = serverSocket.accept();
                new Thread(new ClientHandler(client)).start();
            }
        }
    }


    private static class ClientHandler implements Runnable {
        private final Socket socket;

        ClientHandler(Socket socket) {
          this.socket = socket;
        }

        @Override public void run() {
            String who = socket.getRemoteSocketAddress().toString();
            System.out.println("[server] Connected: " + who);
            try (
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
                PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true)
            ) {
                out.println("OK SimpleJavaServer v1");
                String line;
                while ((line = in.readLine()) != null) {
                    line = line.trim();
                    if (line.isEmpty()) continue;
                    String upper = line.toUpperCase();
                    if (upper.equals("TIME")) {
                        String now = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
                        out.println(now);
                    } else if (upper.equals("EXIT")) {
                        out.println("OK bye");
                        break;
                    } else if (upper.startsWith("ECHO ")) {
                        out.println(line.substring(5));
                    } else {
                        out.println("ERROR");
                    }
                }
            } catch (IOException e) {
                System.err.println("[server] I/O error: " + e.getMessage());
            } finally {
                try { socket.close(); } catch (IOException ignored) {}
                System.out.println("[server] Disconnected: " + who);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        int port = 5000;
        if (args.length > 0) port = Integer.parseInt(args[0]);
        new Server(port).start();
    }
}
