# Webserver_demo
Multithreaded HTTP Web Server demonstration.

When server is running, files can be requested in two ways.

by a client via a client GET request:
>GET / HTTP/1.1\r\n
>Host: 127.0.0.1\r\n
>User-Agent: PythonClient/1.0\r\n
>Accept: text/html\r\n
>\r\n

via browser:
>http://127.0.0.1:5001/HelloWorld.html

>http://127.0.0.1:5001/ANI_HelloWorld.html  

>http://127.0.0.1:5001/index.html
