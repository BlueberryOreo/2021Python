import re


def urlparse(url):
    protocol = re.compile(r"^\w*")
    ip = re.compile(r"/[\w\d.]*")
    port = re.compile(r"\d{4,}")
    path = re.compile(r"/\w*\.\w*\?")
    parameter = re.compile(r"[a-z]*=[0-9]*$")

    protocol_str = protocol.findall(url)
    ip_str = ip.findall(url)
    port_str = port.findall(url)
    path_str = path.findall(url)
    parameter_str = parameter.findall(url)
    print(parameter_str, protocol_str, port_str, path_str, ip_str)

    return protocol_str[0] if protocol_str else "", ip_str[1][1:] if ip_str else "", port_str[0] if port_str else "", path_str[0][1:-1] if path_str else "", parameter_str[0] if parameter_str else ""


g_url = input()
# g_url = "http://192.168.125.3:8080/index.html?a=1"
url_split = urlparse(g_url)
# print(url_split)
print("协议：", url_split[0])
print("主机域名或IP：", url_split[1])
print("端口：", url_split[2])
print("路径：", url_split[3])
print("参数：", url_split[4])
