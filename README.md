# Translation API Test Automation

## Objective
Automated test suite for a simulated translation API.  
Example endpoint: `www.mytranslator.com?query=apple&locale=es-ES` → `"manzana"`

---

## Setup & Execution

1. **Activate virtual environment**
   ```bash
   .\venv\Scripts\activate
   ```
2. **Activate virtual environment**
    ```bash
    pip install pytest pytest-html
    ```
3. **Run tests**
    ```bash
    pytest -v
    ```
4. **Generate HTML report (optional)**
    ```bash
    pytest --html=report.html --self-contained-html
    ```

## Notes
Translations are simulated using a Python dictionary.

If a translation doesn’t exist, "N/A" is returned.

Example translations include:

    "apple" → "manzana" (Spanish)

    "bread" → "brot" (German)

    "lemon" → "limone" (Italian)