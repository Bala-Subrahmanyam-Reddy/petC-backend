
# Petc Backend

Its the backend for the petC which it provides different end points for client

Backend Docs
https://petcbackend-1-h3890731.deta.app/docs

Token to authenticate :token2
## Table of Contents

- [Petc Backend](#petc-backend)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Authors](#authors)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Documentation](#documentation)

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
source env/Scripts/activate  # for Windows
```
Change the database  url in following location 
```bash
config/db.py
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

[Access the documentation here ](https://petcbackend-1-h3890731.deta.app/docs)

