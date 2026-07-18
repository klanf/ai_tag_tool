import http.server
import socketserver
import webbrowser
import os

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8080
    Handler = MyHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        webbrowser.open(url)
        print("=" * 50)
        print("  AI 绘图标签分类工具")
        print("=" * 50)
        print(f"  服务器已启动: {url}")
        print("=" * 50)
        print("  按 Ctrl+C 停止服务器")
        print("=" * 50)
        httpd.serve_forever()
