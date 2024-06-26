from hebill_html import Document
from http.server import BaseHTTPRequestHandler, HTTPServer

doc = Document()

alert = doc.html.body.middle.create.component.alert('你好！')
alert.color.set_danger()

table = doc.html.body.middle.create.component.table()
table.set_bordered()

table.head.add_row(['ID', '姓名', '年龄', '职位'])

table.body.add_row(['1', '张三', '18', '总监'])
table.body.add_row(['2', '李四', '18', '总监'])
table.body.add_row(['3', '王二', '18', '总监'])

table.body.add_row(['4', '麻一', '18', '总监'])


# 定义一个处理HTTP请求的处理程序
class MyHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    # noinspection PyPep8Naming
    def do_GET(self):
        self.send_response(200)  # 发送HTTP响应码200，表示成功
        self.send_header('Content-type', 'text/html')  # 发送响应头，指定内容类型为HTML
        self.end_headers()  # 结束响应头的发送
        # 发送响应内容
        self.wfile.write(doc.output().encode('utf-8'))


# 主函数，用于启动服务器
def main():
    host = 'localhost'  # 主机名
    port = 1080  # 端口号

    # 创建HTTP服务器对象，并指定请求处理程序
    server = HTTPServer((host, port), MyHandler)
    print(f"Server started on http://{host}:{port}")

    try:
        # 启动服务器，一直运行直到手动停止或程序异常退出
        server.serve_forever()
    except KeyboardInterrupt:
        # 捕获键盘中断信号（Ctrl+C），停止服务器
        print("\n Server stopped.")
        server.shutdown()
    except ConnectionAbortedError as e:
        print("\n Client interrupted.")


if __name__ == "__main__":
    main()
