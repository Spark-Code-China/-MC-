import socket
import time
 
def remove_mc_formatting(text):
   for code in range(0, 10):
       text = text.replace(f'§{code}', '')
   for code in 'abcdefklmnor':
       text = text.replace(f'§{code}', '')
   return text
 
def get_java_server_info(address, port):
   start_time = time.time()
   temp_ip = address
   temp_text = ""
   tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       tcp_client.connect((temp_ip, port))
       tcp_client.sendall(b'\xfe\x01')
       data = tcp_client.recv(1024)
       if data:
           temp_text = "\n服务器延迟：" + str(int((time.time() - start_time) * 1000)) + "ms"
           if data[:2] == b'\xff\x00':
               data_parts = data.split(b'\x00\x00\x00')
               if len(data_parts) >= 6:
                   temp_text += "\n服务器类型：MCJE" + \
                               "\n服务器版本：" + data_parts[2].decode('latin1').replace('\x00', '') + \
                               "\n服务器提示文本：" + remove_mc_formatting(data_parts[3].decode('latin1').replace('\x00', '')) + \
                               "\n服务器在线人数：" + data_parts[4].decode('latin1').replace('\x00', '') + \
                               "\n服务器人数上限：" + data_parts[5].decode('latin1').replace('\x00', '')
               else:
                   temp_text += "\n数据格式不正确，部分信息无法解析"
               return temp_text
           else:
               return "不支持读取该服务器信息，版本不兼容"
       else:
           return "服务器离线"
   except socket.error as e:
       return f"连接错误: {e}"
   finally:
       tcp_client.close()
 
server_info = get_java_server_info("127.0.0.1", 25565)
print("服务器信息:", server_info)
