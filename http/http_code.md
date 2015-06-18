今天去又拍云玩了一下。真是丢脸丢到家了。不过收获还是不小的。发现自己http协议和数据库这一块还是又很多东西不清晰。今天连http_code都没回答出来，真是不应该啊。不过还是十分感谢死月给我这次机会的。下次还是要请死月帮忙，但是不能再这么丢脸了。

http常用状态码。明天把我写的服务的状态码都该正确。
<pre>
* 1xx消息
** 100 Continue
** 101 Switching Protocols
** 102 Processing
* 2xx成功
** 200 OK
** 201 Created
** 202 Accepted
** 203 Non-Authoritative Information
** 204 No Content
** 205 Reset Content
** 206 Partial Content
** 207 Multi-Status
* 3xx重定向
** 300 Multiple Choices
** 301 Moved Permanently
** 302 Move temporarily
** 303 See Other
** 304 Not Modified 表示没有变化，不用传输完成的内容，直接用浏览器之前请求的内容就可以了。
** 305 Use Proxy
** 306 Switch Proxy
** 307 Temporary Redirect
* 4xx请求错误
** 400 Bad Request
** 401 Unauthorized
** 402 Payment Required
** 403 Forbidden
** 404 Not Found
** 405 Method Not Allowed
** 406 Not Acceptable
** 407 Proxy Authentication Required
** 408 Request Timeout
** 409 Conflict
** 410 Gone
** 411 Length Required
** 412 Precondition Failed
** 413 Request Entity Too Large
** 414 Request-URI Too Long
** 415 Unsupported Media Type
** 416 Requested Range Not Satisfiable
** 417 Expectation Failed
** 421There are too many connections from your internet address
** 422 Unprocessable Entity
** 423 Locked
** 424 Failed Dependency
** 425 Unordered Collection
** 426 Upgrade Required
** 449 Retry With
* 5xx服务器错误
** 500 Internal Server Error
** 501 Not Implemented
** 502 Bad Gateway
** 503 Service Unavailable
** 504 Gateway Timeout
** 505 HTTP Version Not Supported
** 506 Variant Also Negotiates
** 507 Insufficient Storage
** 509 Bandwidth Limit Exceeded
** 510 Not Extended
** 600 Unparseable Response Headers
</pre>