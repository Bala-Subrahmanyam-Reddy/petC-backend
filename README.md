
# Petc Backend

Its the backend for the petC which it provides different end points for client

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Prerequisites

- Python (3>)
- pip 


## Authors

- [@Reddy Bala Subrahmanyam](https://github.com/Bala-Subrahmanyam-Reddy/)


## Installation

Clone the project

```bash
  git clone https://github.com/Bala-Subrahmanyam-Reddy/petC-backend
```

Go to the project directory

```bash
  cd petC-backend
```

Set up a virtual environment
```bash
python -m venv env
source env/bin/activate  # for macOS/Linux
.\env\Scripts\activate  # for Windows
```

Install dependencies
```bash
pip install -r requirements.txt
```
## Usage

Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

Open a web browser and navigate to http://localhost:8000 to access the API.




## Documentation

[Access the documentation here ](http://localhost:8000/docs)

