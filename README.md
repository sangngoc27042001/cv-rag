# CV RAG API

A FastAPI application for CV (resume) upload and search using RAG (Retrieval-Augmented Generation).

## Features

- Upload CV in PDF format
- Search for CVs based on natural language input
- Automatic extraction of CV information using LLM
- MongoDB storage for CV data

## Prerequisites

- Python 3.8+
- MongoDB

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install the required packages:

```bash
uv venv
uv pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:

```
MONGODB_CONNECTION_STRING=mongodb://localhost:27017
MONGODB_DATABASE=cv_rag_db
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

Start the application with:

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

You can access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

### Upload CV

```
POST /cv/upload
```

Upload a CV in PDF format.

**Request:**
- Form data with a file field named "file" containing the PDF file.

**Response:**
```json
{
  "message": "CV uploaded successfully",
  "data": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "year_of_birth": 1990,
    "year_of_experience": 5,
    "roles": ["Software Engineer", "Backend Developer"],
    "english_level": "Advanced",
    "skills": ["Python", "JavaScript", "SQL", "Django", "Flask"],
    "companies": ["ABC Corp", "XYZ Inc"]
  }
}
```

### Search CV

```
POST /cv/search
```

Search for CVs based on natural language input.

**Request:**
```json
{
  "user_input": "Find me a software engineer with 5 years of experience in Python and Django"
}
```

**Response:**
```json
{
  "message": "Search completed",
  "data": [
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "+1234567890",
      "year_of_birth": 1990,
      "year_of_experience": 5,
      "roles": ["Software Engineer", "Backend Developer"],
      "english_level": "Advanced",
      "skills": ["Python", "JavaScript", "SQL", "Django", "Flask"],
      "companies": ["ABC Corp", "XYZ Inc"]
    }
  ]
}
```

## Development

To run the application in development mode with auto-reload:

```bash
uvicorn main:app --reload
```
