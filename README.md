# Lua Script Analyzer

[![Tests](https://github.com/Stupidoodle/lua-auto-approve/actions/workflows/tests.yml/badge.svg)](https://github.com/Stupidoodle/lua-auto-approve/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/Stupidoodle/lua-auto-approve/branch/main/graph/badge.svg)](https://codecov.io/gh/Stupidoodle/lua-auto-approve)

A FastAPI-based service that analyzes Lua scripts for potential security risks and obfuscation.

## Features

- Detection of dangerous functions and potential security risks
- Identification of obfuscated code
- Analysis of script entropy
- Testing environment with FatalityAPI mocks
- Comprehensive test coverage

## Installation

```bash
# Clone the repository
git clone https://github.com/username/repo-name.git
cd repo-name

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run tests with coverage report
pytest --cov=./

# Run tests with verbose output
pytest -v
```

## API Usage

The service provides a single endpoint for analyzing Lua scripts:

```bash
POST /analyze-script
```

Example using curl:
```bash
curl -X POST -F "file=@script.lua" http://localhost:8000/analyze-script
```

The response will indicate whether the script is approved or flagged:

```json
{
    "status": "approved"
}
```

or 

```json
{
    "status": "flagged",
    "reason": "Contains dangerous function"
}
```

## Project Structure

```
├── main.py                 # FastAPI application and core logic
├── tests/
│   ├── test_main.py       # Core functionality tests
│   ├── test_fatality_api_class.py  # API mock tests
│   └── test_main_integration.py    # Integration tests
└── .github/
    └── workflows/
        └── tests.yml      # GitHub Actions workflow
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request