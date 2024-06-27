# UTF-8 Validation

This project aims to implement a UTF-8 validation algorithm in C. The algorithm will check if a given sequence of bytes represents a valid UTF-8 encoded character.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

UTF-8 is a widely used character encoding that can represent any Unicode character. It uses variable-length encoding, where each character can be represented by 1 to 4 bytes.

The purpose of this project is to provide a function that validates whether a given sequence of bytes is a valid UTF-8 encoded character or not. The function will return `true` if the sequence is valid, and `false` otherwise.

## Usage

To use this UTF-8 validation function in your C program, follow these steps:

1. Clone this repository: `git clone https://github.com/your-username/utf8-validation.git`
2. Include the `utf8_validation.h` header file in your source code: `#include "utf8_validation.h"`
3. Call the `is_valid_utf8()` function, passing the sequence of bytes as an argument.
4. The function will return `true` if the sequence is valid UTF-8, and `false` otherwise.
# UTF-8 Validation

This project aims to implement a UTF-8 validation algorithm in Python. The algorithm will check if a given sequence of bytes represents a valid UTF-8 encoded character.
## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
## Introduction
UTF-8 is a widely used character encoding that can represent any Unicode character. It uses variable-length encoding, where each character can be represented by 1 to 4 bytes.
The purpose of this project is to provide a function that validates whether a given sequence of bytes is a valid UTF-8 encoded character or not. The function will return `True` if the sequence is valid, and `False` otherwise.
## Usage
To use this UTF-8 validation function in your Python program, follow these steps:
1. Clone this repository: `git clone https://github.com/your-username/utf8-validation.git`
2. Include the `utf8_validation.py` module in your source code: `import utf8_validation`
3. Call the `is_valid_utf8()` function, passing the sequence of bytes as an argument.
4. The function will return `True` if the sequence is valid UTF-8, and `False` otherwise.
```python
import utf8_validation

bytes = [0xE2, 0x82, 0xAC] # Euro sign (€)

if utf8_validation.is_valid_utf8(bytes):
    print("Valid UTF-8 sequence")
else:
    print("Invalid UTF-8 sequence")
```
## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
