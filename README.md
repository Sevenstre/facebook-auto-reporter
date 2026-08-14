# Facebook Auto Reporter

**⭐ Star this repository if you find it useful!**

## Overview

**Facebook Auto Reporter** is a Python-based automation project built using **Selenium** and **pystyle**.  
It demonstrates how to:
- Automate web browser actions with Selenium
- Perform login flows securely
- Handle dynamic web elements using `WebDriverWait`
- Use colored CLI output for better UX


## Features

✅ Automated login flow using Selenium  
✅ Repeated report simulation with randomized delays  
✅ Colorful console interface with `pystyle`  
✅ Exception handling for robust execution  
✅ Adjustable report count and timing via configuration variables  

## Requirements

Before running, make sure you have:

- **Python 3.8+**
- **Google Chrome** (latest)
- **ChromeDriver** (same version as Chrome)

### Python Libraries:
You can install all dependencies with:
```bash
pip install -r requirements.txt
```


## Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/xlrrr1111/facebook-auto-reporter.git
cd facebook-auto-reporter
```

### Run the Script

```bash
python reporter.py
```

### Follow Prompts

* Enter your **Facebook email or phone number**
* Enter your **password**
* Paste the **profile URL** you want to test
* Enter how many "reports" to simulate

---

## Example Output

```text
Facebook Auto Reporter

Logging into Facebook...
[✓] Login successful.
[+] Starting report #1 for: https://facebook.com/exampleuser
[✓] Report submitted.
```

---

## Code Structure

```
facebook-auto-reporter/
│
├── reporter.py         # Main script
├── README.md           # Documentation
└── requirements.txt    # Dependencies
```

---

## Core Functions

| Function           | Description                                        |
| ------------------ | -------------------------------------------------- |
| `init_driver()`    | Initializes Selenium WebDriver with Chrome options |
| `login_facebook()` | Logs into Facebook using credentials               |
| `report_account()` | Simulates a reporting flow on a given profile      |
| `banner()`         | Displays styled ASCII art header                   |
| `main()`           | Orchestrates the script                            |

---

## Contributing

Contributions are welcome!
If you’d like to improve the structure, update the XPaths, or make the automation framework more modular:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request 🎉

## Disclaimer 

This project is created **for educational and automation learning purposes only.**
It demonstrates concepts such as **browser automation, Selenium waits, and Python scripting practices.**

Using automated scripts to report users, spam, or perform actions on social media platforms **violates their Terms of Service** and may result in **account suspension or legal consequences.**

The author assumes **no responsibility** for any misuse of this code.

Please use this project **ethically**:

* Do **not** use it to harass, spam, or harm others.

## License

This project is licensed under the MIT License. Refer to the LICENSE file for more information.
