# Project 2 - Backend API

## Description
A simple backend API developed using Python and Flask.

## Features
- GET endpoint
- POST endpoint
- User input handling
- Basic data validation

## Endpoints

### GET /
Returns a message confirming that the API is working.

### POST /users
Accepts user name and email.

Example:
{
  "name": "Aneeba",
  "email": "aneeba@example.com"
}

If name or email is missing, the API returns a 400 Bad Request.

## Technology
- Python
- Flask
- REST API