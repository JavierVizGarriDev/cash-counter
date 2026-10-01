# Cash Counter

A small Tkinter desktop app to count cash by denomination. Built in 2024 as my first real programming project, to speed up cash counting at a retail job.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

> 🇬🇧 English · 🇪🇸 [Versión en español](README.es.md)

---

## 📖 Context

At the store where I worked, counting the cash register at the end of the day was slow. You had to multiply each denomination by how many bills you had and add everything up manually, every single day.

This app replaces that. You enter how many bills you have of each denomination (1000, 500, 200, 100, 50, 20, 10, 5, 3, 1), and it calculates the subtotal per denomination and the grand total instantly.

---

## ⚠️ A note on this project

This is my **first programming project**. It was written before I learned about Git, version control, testing, or code best practices. It's preserved here as a historical record of where I started.

It has no tests, no documentation, and some rough edges (no input validation, for example). But it solved a real problem for me, and it's the reason I kept learning.

I intentionally left the code as it was originally written. No refactoring, no cleanup.

---

## 🛠️ Tech Stack

- Python 3
- Tkinter (standard library)

No external dependencies.

---

## 🚀 How to run

No installation needed. Clone the repo and run the script:

```bash
git clone https://github.com/JavierVizGarriDev/cash-counter.git
cd cash-counter
python cash_counter.py
```

A window will open with the denominations table. Enter the quantity of bills you have for each denomination, and the app will calculate the subtotals and the grand total.

---

## 📸 Screenshot

| Empty window | Filled and calculated |
|---|---|
| ![Empty](screenshots/screenshot-empty.png) | ![Filled](screenshots/screenshot-filled.png) |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Javier A. Vizcaino Garriga**
- GitHub: [@JavierVizGarriDev](https://github.com/JavierVizGarriDev)
- Email: javieralejandrovizcainogarriga@gmail.com

---

<p align="center">
  <i>My first project. Rough, but it worked.</i>
</p>