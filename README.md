# Selenium Test Automation Project

This project contains automated tests for a web application using Selenium WebDriver and pytest.

## Project Structure

```
test-ia/
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_login.py      # Login tests
│   └── test_product.py    # Product management tests
├── config/                 # Configuration files
│   ├── __init__.py
│   └── config.py          # Test configuration and selectors
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── helpers.py         # Helper functions for tests
├── data/                   # Test data
│   └── test_image.jpg     # Test image for product upload
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd test-ia
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The `config/config.py` file contains all the necessary configuration:
- URLs
- Selectors
- Credentials
- Wait times

Update these values according to your environment.

## Running Tests

To run all tests:
```bash
pytest -v
```

To run specific test files:
```bash
pytest tests/test_login.py -v
pytest tests/test_product.py -v
```

## Test Structure

### Login Tests (`test_login.py`)
- Test successful login with valid credentials
- Test login with invalid credentials

### Product Tests (`test_product.py`)
- Test adding a new product
- Test product image upload
- Test category selection

## Helper Functions

The `utils/helpers.py` file contains reusable functions:
- `wait_and_click`: Wait for element and click it
- `wait_and_send_keys`: Wait for element and send keys
- `wait_for_element`: Wait for element to be present
- `click_radio_button`: Click radio buttons using ActionChains
- `upload_image`: Upload and verify image

## Best Practices

1. Always use explicit waits instead of implicit waits
2. Use helper functions for common operations
3. Keep selectors in the config file
4. Use meaningful test names and descriptions
5. Clean up resources in fixtures

## Contributing

1. Create a new branch for your feature
2. Write tests for new functionality
3. Update documentation as needed
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 