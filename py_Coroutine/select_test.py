# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 6:22 PM
describe:

本节 文字相关资料 在 印象笔记中 https://app.yinxiang.com/shard/s65/nl/14802286/4176dc9f-b4f2-41de-a44d-a5fcca098b87/
 印象笔记不能公开链接,如需要访问 请申请 文字内容 关于 uninx 的五种IO模型
  阻塞 、 非阻塞 、I/O复用 、信号驱动 、异步IO
  I/O复用 分成三种 select poll epoll 
  
  select

select函数监视的文件描述符分3类,分别是writefds、readfds、和 exceptfds。调用后select函数会阻塞，直到有描述副就绪(有数据可读、 
可写、或者有except) , 或 者 超 时 ( timeout指定等待时间，如果立即返回 设为nuH即可)，函数返回。当select函数返回后，可以通过遍历fdset,来 
找到就绪的描述符。 select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个 
优点  selec啲一个缺点在于单个进程能够监视的文件描述符的数量存在最 大限制，在Linux上一般为1024 ,可以通过修改宏定义甚至重新编译内核的 
方式提升这一限制，但是这样也会造成效率的降低。
Poll

不同与select使用三个位图来表示三个fdset的方式， pol肢用一个 pollfd的指针实现。 
pollfd结构包含了要监视的event和发生的event,不再使用select “参 数-值〃 传 递 的方式。同时， pollfd并没有最大数量限制(但是数量过大后 性能也是会下降)。和select函数一样，poll返回后，需要轮询pollfd来获 
取就绪的描述符。 从上面看，select和pol嘟需要在返回后，通过遍历文件描述符来获取 
已经就绪的socket。事实上，同时连接的大量客户端在一时刻可能只有很少 的处于就绪状态，因此随着监视的描述符数量的增长，其效率也会线性下降
epoll 只支持Linux 。windos不支持

epoll是在2.6内核中提出的，是之前的select和poll的增强版本。相对 于select和poll来说，epoll更加灵活，没有描述符限制。epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的_ 个事件表中，这样在用户空间和内核空间的copy只需一次。 
  
 epoll并不代表一定比select 好
* 在并发高的情况下, 连接活跃度不是很高 ，epoll比select好 (网站)
* 在并发不高，同时连接后很活跃，select比epoll好（游戏中，常连接） 
"""

import socket
from urllib.parse import urlparse
#使用非阻塞io完成http请求

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  #设置非阻塞
    try:
        client.connect((host, 80)) #阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    #不停的询问连接是否建立好， 需要while循环不停的去检查状态
    #做计算任务或者再次发起其他的连接请求

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass


    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")

