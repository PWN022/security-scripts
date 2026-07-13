# security-scripts

<div align="center">

[![中文](https://img.shields.io/badge/语言-中文-red.svg)](README.md)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](README_EN.md)

</div>

## Description

This project is primarily used for **automated verification of Vulhub vulnerability environments**.

It includes Python exploit scripts for common web vulnerabilities (RCE, SQLi, SSRF, deserialization), intended **only for local research and learning**.

## Disclaimer

**Important Notice:**

1. All scripts in this repository are for **local vulnerability reproduction only**.
2. Unauthorized system attacks are illegal. Users bear all legal consequences.
3. All rights reserved by the author.

---

## Directory Structure

```bash
security-scripts/
├── README.md                 # Project description
├── requirements.txt          # Dependencies (requests, etc.)
├── rce/                      # Remote Code Execution
│   ├── thinkphp_2_rce.py
│   └── thinkphp_5_rce.py
├── sqli/                     # SQL Injection
│   └── boolean_blind.py
├── ssrf/                     # Server-Side Request Forgery
│   └── soapclient_ssrf.py
└── xxe/                      # XML External Entity
    └── simplexml_xxe.py
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/security-scripts.git
cd security-scripts
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage Examples

### ThinkPHP 2.x RCE Exploit

This is only for illustrative purposes. The actual content is subject to the code.

```bash
python rce/thinkphp_2_rce.py http://192.168.1.100:8080
```

```bash
python rce/thinkphp_2_rce.py http://192.168.1.100:8080 whoami
```

---

## Basic Information

|         Field          |        Value         |
| :--------------------: | :------------------: |
|    **Project Name**    |   security-scripts   |
|   **Creation Date**    |      2026-07-13      |
|   **Python Version**   |        3.14.5        |
| **Target Environment** |        Vulhub        |
|       **Status**       | Continuously updated |

>**Note**: This repository is for educational and research purposes only. Do not use for illegal activities.