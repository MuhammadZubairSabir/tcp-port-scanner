🔍 TCP Port Scanner (Python)

A simple and efficient **TCP Port Scanner** built with **Python**, designed for learning **socket programming, multithreading, and basic cybersecurity concepts**.

This tool scans a target host to identify **open, closed, or timeout ports** within a specified range and logs the results to a file.

---

## 🚀 Features

* ✅ Scan a **single host** (IP address or domain)
* 🔢 Scan a **custom port range**
* ⚡ Fast scanning using **multithreading**
* 📄 Logs results to a file
* 🛡️ Handles errors and timeouts gracefully
* 🧠 Beginner-friendly cybersecurity project

---

## 🛠️ Technologies Used

* **Python 3**
* `socket` (TCP connections)
* `threading` (concurrency)
* `datetime` (logging timestamps)

---

## 📂 Project Structure

```
port-scanner/
│
├── port_scanner.py
├── scan_results.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
```

2. Navigate to the project folder:

```bash
cd port-scanner
```

3. Run the scanner:

```bash
python port_scanner.py
```

---

## 🧪 Example Usage

```
Enter target host (IP / Domain): scanme.nmap.org
Enter start port: 20
Enter end port: 100
```

### Sample Output

```
Port 22: OPEN
Port 80: OPEN
Port 443: CLOSED
```

Results are also saved in **scan_results.txt**.

---

## 📘 What I Learned

* TCP socket programming
* Port scanning fundamentals
* Multithreading for performance
* Exception handling in Python
* Basic cybersecurity concepts

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Do **NOT** scan systems or networks without proper authorization.

---

## 👤 Author

**Muhammad Zubair Sabir**
Cybersecurity Student | Python Developer
