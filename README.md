# security-scripts

<div align="center">

[![中文](https://img.shields.io/badge/语言-中文-red.svg)](README.md)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](README_EN.md)

</div>

## 项目简介 (Description)

本项目主要用于**Vulhub 漏洞环境自动化验证**。

包含针对常见Web漏洞（RCE, SQLi, SSRF, 反序列化）的Python利用脚本，旨在**仅用于本地学习研究**。

## 免责声明 (Disclaimer)

**重要提示：**

1. 本仓库所有脚本仅用于**本地漏洞复现**。
2. 未经授权的系统攻击属于违法行为，使用者需自行承担一切法律后果。
3. 作者保留所有权利。

---

##  目录结构 (Directory Structure)

```bash
security-scripts/
├── README.md                 # 项目说明
├── requirements.txt          # 依赖清单 (requests等)
├── rce/                      # 远程代码执行
│   ├── thinkphp_2_rce.py
│   └── thinkphp_5_rce.py
├── sqli/                     # SQL注入
│   └── boolean_blind.py
├── ssrf/                     # SSRF
│   └── soapclient_ssrf.py
└── xxe/                      # XXE
    └── simplexml_xxe.py
```

---

##  环境安装 (Installation)

1. **克隆仓库**

```bash
git clone https://github.com/你的用户名/security-scripts.git
cd security-scripts
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

---

## 脚本使用示例 (Usage Examples)

### ThinkPHP 2.x RCE 漏洞利用

仅作为举例说明，实际以代码为准

```
python rce/thinkphp_2_rce.py http://192.168.1.100:8080
```

```bash
python rce/thinkphp_2_rce.py http://192.168.1.100:8080 whoami
```

---

## 基本信息 (Basic Information)

|      项目      |        内容        |
| :----------: | :--------------: |
|   **项目名称**   | security-scripts |
|   **创建时间**   |    2026-07-13    |
| **Python版本** |      3.14.5      |
|   **目标环境**   |      Vulhub      |
|    **状态**    |      持续更新中       |

> **提示**：本仓库仅供学习研究使用，请勿用于非法用途。