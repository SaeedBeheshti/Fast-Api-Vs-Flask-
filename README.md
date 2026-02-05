# FastAPI vs Flask – Identical API Responses (Dockerized)

This project demonstrates two separate web services built with **FastAPI** and **Flask**, fully **Dockerized**, that expose identical endpoints and return the **same status codes, headers, and response bodies**.

The goal is to make the two services **indistinguishable from the outside**, so when you send HTTP requests (e.g. using `curl`) to either service, you receive the exact same response.

This can be useful for:
- Comparing frameworks under identical conditions
- Load testing and benchmarking
- API gateway or reverse proxy testing
- Educational purposes

---

## 🚀 Features

- Two separate services:
  - One implemented with **FastAPI**
  - One implemented with **Flask**
- Both services:
  - Expose the same routes
  - Support the same HTTP methods
  - Return identical:
    - Status codes
    - Headers
    - Response bodies
- Fully **Dockerized**
- Easy to run with **Docker Compose**
- Can be tested with simple tools like `curl`

---

## 🧱 Project Structure

```text
.
├── fastapi_app/
│   ├── Dockerfile
│   └── main.py
├── flask_app/
│   ├── Dockerfile
│   └── app.py
├── docker-compose.yml
└── README.md
