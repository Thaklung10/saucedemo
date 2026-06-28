# SauceDemo Automation

Selenium WebDriver automation script for [SauceDemo](https://www.saucedemo.com/) — a full end-to-end purchase flow using Microsoft Edge.

## Prerequisites

- Python 3.x
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (must match your Edge browser version and be in `PATH`)
- Install dependencies:

```bash
pip install selenium
```

## What It Does

| Step | Action |
|------|--------|
| 1 | Launches Edge browser and navigates to saucedemo.com |
| 2 | Logs in with `standard_user` / `secret_sauce` |
| 3 | Scrolls to the bottom of the inventory page |
| 4 | Adds **Sauce Labs Onesie** and **Test.allTheThings T-Shirt (Red)** to the cart |
| 5 | Scrolls to top and opens the shopping cart |
| 6 | Proceeds to checkout |
| 7 | Fills in first name, last name, and postal code |
| 8 | Continues to the overview and clicks **Finish** |
| 9 | Verifies the purchase was successful |
| 10 | Returns to the product page |
| 11 | Sorts products by price (low to high) |
| 12 | Opens the menu and logs out |
| 13 | Verifies logout was successful |

## Usage

```bash
python automation_secretsauce.py
```

The script will open an Edge browser window and walk through the entire flow automatically.

## Notes

- Uses `WebDriverWait` with explicit waits for the login button.
- Implicit wait is commented out; adjust if needed.
- `ActionChains` import is present but unused (double-click on login is commented out).
- Scrolls are done via `execute_script` for both top and bottom navigation.
