```cpp
/*server.c*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <unistd.h>
 
#define BUFLEN 10
#define SER_ADDR "127.0.0.1"
#define PORT 8080
#define MAX_CONN 200
 
int main(int argc, char **argv)
{
    int sockfd, newfd;
    struct sockaddr_in s_addr, c_addr;
    char buf[BUFLEN];
    socklen_t len;
    unsigned int port=8080, listnum=200;
 
    /*简历socket*/
    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket");
        exit(errno);
    }
    else
    {
        printf("socket create success!\n");
    }
    /*设置侦听队列的长度*/
    printf("listnum = %d", listnum);
    /*设置服务器ip*/
    bzero(&s_addr, sizeof(s_addr));
    s_addr.sin_family = AF_INET;
    s_addr.sin_port = htons(port);
    printf("port= %d\n", port);
    if(SER_ADDR)
        s_addr.sin_addr.s_addr = inet_addr(SER_ADDR);
    else
        s_addr.sin_addr.s_addr = INADDR_ANY;
    printf("socket_addr.addr = %d", s_addr.sin_addr.s_addr);
    /*把地址和端口绑定到套接字上*/
    if((bind(sockfd, (struct sockaddr*)&s_addr, sizeof(struct sockaddr))) == -1)
    {
        perror("bind");
        exit(errno);
    }
    else
    {
        printf("bind success!\n");
    }
    /*侦听本地端口*/
    if(listen(sockfd, listnum) == -1)
    {
        perror("listen");
        exit(errno);
    }
    else
        printf("the server is listening!\n");
    while(1)
    {
        printf("**********聊天开始********\n");
        len = sizeof(struct sockaddr);
        if((newfd = accept(sockfd, (struct sockaddr*)&c_addr, &len)) == -1)
        {
            printf("a client connected\n");
            perror("accept");
            exit(errno);
        }
        else
            printf("正在与您聊天的客户端是：%s:%d\n", inet_ntoa(c_addr.sin_addr), ntohs(c_addr.sin_port));
        while(1)
        {
_retry:
            /****发送消息****/
            bzero(buf, BUFLEN);
            printf("请输入发送对方的消息:");
            /*fgets函数：从流中读取BUFLEN-1个字符*/
            fgets(buf, BUFLEN, stdin);
            /*打印发送的消息*/
            //fputs(buf, stdout);
            if(!strncasecmp(buf, "quit", 4))
            {
                printf("server请求终止聊天!\n");
                break;
            }
            /*如果输入的字符串只有"\n", 即回车，那么轻重新输入*/
            if(!strncmp(buf, "\n", 1))
            {
                printf("输入的字符只有回车， 这个是不正确的!!!\n");
                goto _retry;
            }
            /*如果buf中含有'\n', 那么要用strlen(buf)-1, 去掉'\n'*/
            if(strchr(buf, '\n'))
                len = send(newfd, buf, strlen(buf)-1, 0);
            /*如果buf中没有'\n',则用buf的真正长度strlen(buf)*/
            else
                len = send(newfd, buf, strlen(buf), 0);
            if(len > 0)
                printf("消息发送成功，本次发送的字节数是：%d\n", len);
            else
            {
                printf("消息发送失败!\n");
                break;
            }
            /*****接受消息******/
            bzero(buf, BUFLEN);
            len = recv(newfd, buf, BUFLEN, 0);
            if(len > 0)
                printf("客户端发来的信息是:%s, 共有字节数是:%d\n", buf, len);
            else
            {
                if(len<0)
                    printf("接受消息失败!\n");
                else
                    printf("客户端退出了，聊天终止!\n");
                break;
            }
        }
        /*关闭聊天的套接字*/
        close(newfd);
        /*是否退出服务器*/
        printf("服务器是否退出程序：y->是;n->否?");
        bzero(buf, BUFLEN);
        fgets(buf, BUFLEN, stdin);
        if(!strncasecmp(buf, "y", 1))
        {
            printf("server退出!\n");
            break;
        }
    }
    /*关闭服务器的套接字*/
    close(sockfd);
    return 0;
}








/*client.c*/
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <unistd.h>
 
#define BUFLEN 100
 
int main(int argc, char **argv)
{
    int sockfd;
    struct sockaddr_in s_addr;
    socklen_t len;
    unsigned int port=8080;
    char buf[BUFLEN];
 
    /*简历socket*/
    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket");
        exit(errno);
    }
    else
        printf("socket create success!\n");
    /*设置服务器ip*/
    bzero(&s_addr, sizeof(s_addr));
    s_addr.sin_family=AF_INET;
    s_addr.sin_port = htons(port);
    char *server_addr = "127.0.0.1";
    if(inet_aton(server_addr, (struct in_addr*)&s_addr.sin_addr.s_addr) == 0)
    {
        perror(server_addr);
        exit(errno);
    }
    printf("s_addr.sin_addr.s_addr = %d", s_addr.sin_addr.s_addr);
    /*开始连接服务器*/
    if(connect(sockfd, (struct sockaddr*)&s_addr, sizeof(struct sockaddr)) != 0)
    {
        printf("connect failed");
        perror("connect");
        exit(errno);
    }
    else
        printf("connect success! %d \n", errno);
    printf("enter the while loop");
    while(1)
    {
        printf("while");
        /**接受消息**/
        bzero(buf, BUFLEN);
        len = recv(sockfd, buf, BUFLEN, 0);
        if(len > 0)
            printf("服务器发送来的消息是:%s,共有字节数是:%d\n", buf, len);
        else
        {
            printf("else");
            if(len < 0)
                printf("接受消息失败!\n");
            else
                printf("服务器退出了，聊天终止!\n");
            break;
        }
_retry:
        /***发送消息***/
        bzero(buf, BUFLEN);
        printf("请输入发送给对方的消息:");
        /*fgets函数：从流中读取BUFLEN-1个字符*/
        fgets(buf, BUFLEN, stdin);
        /*打印发送的消息*/
        //fputs(buf, stdout);
        if(!strncasecmp(buf, "quit", 4))
        {
            printf("client请求终止聊天!\n");
            break;
        }
        /*如果输入的字符串只有'\n',即回车， 那么请重新输入*/
        if(!strncmp(buf, "\n", 1))
        {
            printf("输入的字符只有回车,这个是不正确的!!!\n");
            goto _retry;
        }
        printf("%s", buf);
        /*如果buf中含有'\n', 那么要用strlen(buf)-1,去掉'\n'*/
        if(strchr(buf, '\n'))
        {
            printf("start to send");
            len = send(sockfd, buf, strlen(buf)-1, 0);
        }
        /*如果buf中没有\n,则用buf的真正长度strlen(buf)*/
        else
            len = send(sockfd, buf, strlen(buf), 0);
        printf("len = %d", len);
        if(len > 0)
            printf("消息发送成功，本次共发送的字节数是:%d\n", len);
        else
        {
            printf("消息发送失败!\n");
            break;
        }
    }
    /*关闭连接*/
    close(sockfd);
    return 0;
}

```

PS：发现facebook上的中国人一般都富二代。