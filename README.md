🔥 Hack You

Hack You ek advanced penetration testing aur reconnaissance framework hai jo Python me develop kiya gaya hai. Ye tool security researchers aur ethical hackers ke liye bana hai jo target systems ka deep analysis karna chahte hain.

🚀 Features
🔍 DNS Enumeration (A, MX, NS Records)
🌐 Subdomain Discovery (Wordlist-based)
⚡ Fast & Full Port Scanning (Nmap powered)
🧠 Service & Version Detection
📂 Directory & Endpoint Enumeration
🛡️ Risk Analysis (HIGH / MEDIUM / LOW)
🎨 Colorized CLI Output
⚙️ Multi-threaded Scanning
📄 Auto Report Generation (Timestamp based)
🧠 Tech Stack
Python 3.12
python-nmap
requests
tqdm
colorama
⚙️ Installation
git clone https://github.com/synkodi606/hack-you.git
cd hack-you
🪟 Windows Setup
py -3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🐧 Linux / macOS Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
📦 Install Nmap (Required)

Hack You uses Nmap for scanning.

Windows

Download: https://nmap.org/download.html

Linux (Debian/Ubuntu)
sudo apt update
sudo apt install nmap
macOS
brew install nmap

▶️ Usage
python main.py

🖥️ Sample Output
[INFO]========== PORT SCAN ==========

[OPEN] 21 → ftp → HIGH
[OPEN] 22 → ssh → HIGH
[OPEN] 80 → http → MEDIUM
[OPEN] 443 → https → MEDIUM

--------------------------------------------------

[FOUND] /admin → 200
[FOUND] /dashboard → 200

[WARNING] No subdomains found

📄 Reports
Reports automatically output/ folder me save hote hain
Har scan ka unique timestamp file banta hai
output/
 └── target_com/
      ├── 20260402_120000.txt
📁 Project Structure
HackYou/
 ├── core/
 ├── engine/
 ├── utils/
 │    └── colors.py
 ├── data/
 ├── output/
 ├── main.py
 ├── requirements.txt
 └── README.md

⚠️ Disclaimer

Ye tool sirf educational purpose aur authorized testing ke liye hai.
Unauthorized use illegal ho sakta hai.

👤 Author

Your Name
GitHub: https://github.com/Hck You

⭐ Support

Agar project pasand aaye to ⭐ zaroor dena!