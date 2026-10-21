# Unit Testing with Pytest

This repository contains basic implementations of unit tests using Python and the `pytest` framework.

---

## 1. Overview of Topics Covered

* **Software Testing:** The process of validating software to prevent bugs, ensure correctness, and improve code reliability.
* **Manual vs. Automated:**
  * *Manual Testing:* Repetitive and susceptible to human error.
  * *Automated Testing:* Faster, reproducible, and seamlessly integrated into development workflows.
* **Testing Levels:**
  * *Unit Testing:* Verifies individual functions in isolation.
  * *Integration Testing:* Checks how modules work together.
  * *End-to-End (E2E):* Tests the entire flow from start to finish.
* **Pytest Framework:** A clean and powerful Python testing tool that uses standard `assert` statements, provides clear failure tracebacks, and simplifies edge-case and exception testing.

---

## 2. Project Structure

* `main.py`: Contains basic utility functions (`get_weather`, `add`, `divide`).
* `test_main.py`: Contains unit test cases covering positive cases, assertions, and exception handling.

---

## 3. Code Implementation

### Source Functions (`main.py`)
```python
def get_weather(temperature):
    if temperature > 20:
        return "hot"
    else:
        return "cold"

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b