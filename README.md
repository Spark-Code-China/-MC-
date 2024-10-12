# Minecraft 服务器信息查询工具
 
## 简介
 
本项目是一个基于Python的Minecraft Java版服务器信息查询工具，能够获取服务器的延迟、版本、在线人数等信息。
 
## 功能
 
- 获取服务器延迟
- 获取服务器类型（仅支持Minecraft Java版）
- 获取服务器版本
- 获取服务器提示文本
- 获取服务器在线人数及人数上限

## 参数说明
address: 服务器的IP地址
port: 服务器的端口号（默认为25565）

## 使用方法
```bash
server_info = get_java_server_info("127.0.0.1", 25565)
```
### 注意事项
本工具仅支持Minecraft Java版服务器。
 

