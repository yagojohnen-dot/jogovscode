import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000

# Força o Python a rodar na pasta correta onde estão seus arquivos
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se tentar acessar a raiz ou o index.html direto
        if self.path == '/' or self.path == '/index.html':
            # Procura o index dentro da pasta templates se ele não estiver na raiz
            if os.path.exists('templates/index.html'):
                self.path = 'templates/index.html'
        return super().do_GET()

def iniciar_servidor():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), MyHandler) as httpd:
            print(f"\n[OK] Servidor ativo em http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        print(f"[ERRO] Não foi possível iniciar o servidor: {e}")

if __name__ == "__main__":
    print("=== INICIANDO BINDING OF PYTHON ===")
    
    # Inicia o servidor
    thread = threading.Thread(target=iniciar_servidor, daemon=True)
    thread.start()
    
    # Dá um tempo maior para o Windows abrir a porta
    time.sleep(1.5)
    
    # Abre no navegador usando localhost (evita bloqueios de firewall do 127.0.0.1)
    url = f"http://localhost:{PORT}/"
    print(f"Abrindo o jogo em: {url}")
    webbrowser.open(url)
    
    # Mantém o terminal aberto
    print("\n>>> MANTENHA ESTA JANELA DO TERMINAL ABERTA ENQUANTO JOGA <<<")
    print("Pressione Ctrl+C aqui no terminal para fechar o jogo.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServidor encerrado.").
        
