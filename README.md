# Password Strength Checker (Project 1) - DecodeLabs

This project is developed as part of the **DecodeLabs Industrial Training Kit**. It serves as a defensive security tool designed to evaluate the strength of user passwords through pure string-handling and conditional logic.

## 🛡️ Project Overview
The core objective is to analyze a "Raw Byte Stream" (user input) and classify its risk level based on industrial security standards. This tool focuses on **Security Logic** and **Data Validation** rather than simple hacking.

### Key Features
- **Zero Point Verification:** Enforces a minimum 8-character limit to mitigate exponential brute force risks.
- **Pattern Recognition:** Detects uppercase, lowercase, digits, and special symbols.
- **Computational Efficiency:** Implements a **Linear Scan (O(n))** approach using Pythonic short-circuiting to ensure high performance.
- **Memory Safety:** Addresses the "Immutability Trap" by attempting to minimize the data's lifespan in RAM.

## 🚀 Technical Implementation

### IPO Model (Input-Process-Output)
1.  **Input:** User provides a string through the terminal.
2.  **Process:** The string is scanned linearly. Each character type is identified using C-optimized Python built-ins.
3.  **Output:** A risk classification is generated:
    -   🔴 **FAIL/WEAK:** Critical risk, missing entropy.
    -   🟡 **MODERATE:** Basic security met, but needs more complexity.
    -   🟢 **STRONG:** Meets all industrial standards for credential safety.



## 🛠️ Installation & Usage

1.  **Environment:** Ensure you have **Python 3.13.9** installed (preferred environment: Kali Linux).
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Password-Strength-Checker.git](https://github.com/YOUR_USERNAME/Password-Strength-Checker.git)
    cd Password-Strength-Checker
    ```
3.  **Run the Tool:**
    ```bash
    python3 task1.py
    ```

## 🧠 Defensive Logic Concepts
This project covers the following foundational security concepts:
- **Entropy:** Increasing the search space for attackers by requiring multiple character sets (Unicode expansion).
- **Linear Complexity:** Ensuring validation time grows linearly, preventing potential ReDoS (Regular Expression Denial of Service) style bottlenecks.
- **Garbage Collection Awareness:** Understanding how sensitive data lingers in heap memory.

---
**Author:** Meryem Şahin  
**Track:** Junior Cybersecurity Analyst  
**Batch:** 2026 | Powered by **DecodeLabs**