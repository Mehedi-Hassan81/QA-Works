# MathSpeedTest Automation

Automate **MathSpeedTest.com** to solve 20 math questions, submit the test, and extract your leaderboard stats automatically using **Python** and **Playwright**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Notes](#notes)

---

## Overview

This project demonstrates **end-to-end web automation** using Python and Playwright async API:

1. Navigate to [MathSpeedTest.com](https://mathspeedtest.com/).  
2. Enter a username and start the test.  
3. Solve 20 arithmetic questions automatically (addition, subtraction, multiplication, division).  
4. Submit answers and navigate through the test.  
5. Extract your **Rank**, **Name**, and **Time** from the results page.

This project is ideal for **QA testing practice**, **automation portfolio**, and **Python async programming practice**.

---

## Features

- Automatically enters a username and starts the test.  
- Solves 20 math questions (addition, subtraction, multiplication, division).  
- Navigates through questions using the **Enter key**.  
- Submits answers and extracts **current leaderboard stats**.  
- Clears cookies and permissions for a fresh session.  
- Fully asynchronous for faster execution.  

---

## Installation

### Prerequisites

- Python 3.10 or higher  
- Playwright library  

### Install Dependencies

```bash
pip install playwright
python -m playwright install

---

## Usage
Run the script: python -m asyncio -c "import math_test; import asyncio; asyncio.run(mathChallengeAutomation.math_challenge())"

Optional: Run with headless=False to watch the browser interaction: browser = await p.chromium.launch(headless=False)

---

### Expected Output:
Reached results page!
Rank: 12
Name: Mehedi
Time: 37.988
  " ⚠️ Note: The displayed name may differ depending on how MathSpeedTest.com handles sessions. "

--- 

## Project Structure
mathspeedtest-automation/
│
├─ mathChallengeAutomation.ipynb
├─ README.md

--- 

## Troubleshooting

1. TimeoutError: Increase the timeout in wait_for_selector() or check your internet connection.
2. Name on leaderboard differs: The site may override the name due to session handling. Use headless=False to watch browser behavior.
3. Playwright installation errors: Make sure to run python -m playwright install after pip install playwright.

---

## Notes

1. The script is asynchronous for efficiency.
2. Designed for automation practice, QA portfolio projects, and learning async Python.
3. Can be extended for similar math test websites with minimal changes.
