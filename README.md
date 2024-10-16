# Rule Engine Project

## Project Description

This project implements a rule engine using Python that can create, combine, and evaluate rules in the form of Abstract Syntax Trees (AST). The rules can be dynamically modified by changing operators, operands, or adding/removing sub-expressions within the AST. The project includes test cases to validate the functionality of the engine.

### Key Features:
- **Rule Creation**: Users can define rules with simple expressions like `age == 30`.
- **Rule Combination**: Rules can be combined using logical operators such as `AND` to create complex rules.
- **Rule Evaluation**: The engine evaluates rules against provided data.
- **Dynamic Rule Modification**: The rules can be modified at runtime by changing operators, operand values, or adding/removing sub-expressions.

---

## Design Choices

The engine uses an `ASTNode` class to represent individual rules, which allows for flexible and dynamic rule creation and evaluation. This design makes it easy to parse rule strings into logical components, evaluate them against data, and modify the rules dynamically.

Each rule in the engine consists of:
- **Left Operand**: Typically a string representing a field (e.g., `age`).
- **Operator**: A logical operator (`==`, `!=`, `>`, `<`, etc.).
- **Right Operand**: A value that the left operand is compared against.

The rules are evaluated based on the given data, and the result is returned as a boolean (`True` or `False`).

---

## Project Structure

├── main.py # Main application file ├── rule_engine.py # Core rule engine implementation ├── test_cases.py # Test cases for validating the rule engine ├── requirements.txt # List of dependencies └── README.md # Project documentation

## Build Instructions

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **pip**: Python’s package manager. It comes pre-installed with Python 3.x.

### Clone the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/nikeshsharma192002/Rule-Engine-with-AST.git
   cd rule-engine
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate (Linux/macOS)
   .\venv\Scripts\activate (Windows)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main application:
   ```bash
   python main.py
   ```
5. To run the test cases:
   ```bash
   python -m unittest test_cases.py
   ```

## Dependencies

  - Python 3.x: Ensure that you have Python 3.x installed.
  - Required Libraries: All dependencies can be installed via pip using the requirements.txt file.

## requirements.txt
  ```bash
  unittest
  ```

## How to Modify Rules
You can modify existing rules or add new ones by using the create_rule function or the additional modification functionalities provided in rule_engine.py.

  **Change Operators**: You can modify operators within the rules (e.g., change == to !=).
  **Update Operand Values**: You can change the operand values (e.g., modify the value from 30 to 25).
  **Add or Remove Sub-expressions**: You can dynamically add or remove sub-expressions from the AST.

## Additional Information
**Docker Support**: If required, you can containerize the application using Docker for easier deployment.
    To use Docker, create a Dockerfile and define the required environment setup.
    Example Dockerfile:
    ```bash
    FROM python:3.12
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python", "main.py"]

## License

This project is licensed under the MIT License.

