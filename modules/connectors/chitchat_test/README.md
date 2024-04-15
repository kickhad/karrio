
# karrio.chitchat_test

This package is a Chitchat extension of the [karrio](https://pypi.org/project/karrio) multi carrier shipping SDK.

## Requirements

`Python 3.7+`

## Installation

```bash
pip install karrio.chitchat_test
```

## Usage

```python
import karrio
from karrio.mappers.chitchat_test.settings import Settings


# Initialize a carrier gateway
chitchat_test = karrio.gateway["chitchat_test"].create(
    Settings(
        ...
    )
)
```

Check the [Karrio Mutli-carrier SDK docs](https://docs.karrio.io) for Shipping API requests
