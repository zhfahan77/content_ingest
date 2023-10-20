# Content Ingest

This is a Python Flask-based scraping application that uses Alembic for database migrations. It also connects to Redis and PostgreSQL databases.

To make it easy to set up and run the application, there is a Docker Compose configuration for development.

## Prerequisites

Before you can run this application, ensure you have the following software installed on your system:

- Docker
- Docker Compose
- Python (3.6 or higher)

## Getting Started

Follow these steps to set up and run the application:

### **Clone this repository to your local machine:**

```shell
git clone git@github.com:zhfahan77/content_ingest.git
```

### Change to the project directory:

```shell
cd content_ingest
```

### Create a virtual environment and activate it (optional but recommended):

```shell
python -m venv venv
source venv/bin/activate
```

### Install Python dependencies:

```shell
pip install -r requirements.txt
```

### Copy .env.sample, create .env file

```shell
cp .env.sample .env
```

### Export Python Path
```shel
export PYTHONPATH=$PYTHONPATH:$PWD
```

### Run Redis and Database using Docker-Compose
```shell
docker-compose up -d
```

### Running Migrations

Run Alembic migrations to set up the database schema:

```shell
alembic upgrade head
```

### Run Application (Dev)
```shell
python run.my
```

## OR use Makefile

### **Clone this repository to your local machine:**

```shell
git clone git@github.com:zhfahan77/content_ingest.git
```

### Change to the project directory:

```shell
cd content_ingest
```

### Create a virtual environment and activate it (optional but recommended):

```shell
python -m venv venv
source venv/bin/activate
```

### Bootsrap Application

```shell
make init
```

---

### Help
```shell
make help
```

## Features

- Extract the title and body of a resource
- Extract images from a content item
    - Both body images or meta/link tag image references
- Avoid ingesting the same page with different parameters (that don’t alter the page)
    - Removed the query parameters and anchors from URL
- Save (and index) a content item
    - Saved the scraped data into a PostgreSQL DB
- Cache responses from the server
    - Using redis to cache data on deman
- Extract title and body from PDF
    - Basic scraping from PDF