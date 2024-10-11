import socket

def start_tcp_server(port):
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定到所有可用的接口上的指定端口
    host = '0.0.0.0'  # 允许所有IP地址连接
    server_socket.bind((host, port))
    
    # 设置最大连接数，超过后排队
    server_socket.listen(5)
    
    print(f"服务器启动成功，监听端口：{port}")
    
    while True:
        # 建立客户端连接
        client_socket, addr = server_socket.accept()
        
        print(f"客户端 {addr} 已连接")
        
        try:
            while True:
                # 接收小于 1024 字节的数据
                data = client_socket.recv(1024).decode()
                if not data:
                    # 如果没有数据，跳出循环
                    break
                print(f"从 {addr} 收到消息：{data}")
                # 发送数据
                client_socket.send(data.encode())
        except ConnectionResetError:
            print(f"客户端 {addr} 断开连接")
        finally:
            # 关闭连接
            client_socket.close()

if __name__ == '__main__':
    port = 9999
    start_tcp_server(port)
