# 🚀 Vault Environment Variables API

A simple FastAPI microservice to **fetch environment variables for any service/environment from HashiCorp Vault**.

---

## Features

- 🔒 Securely connects to HashiCorp Vault using [hvac](https://github.com/hvac/hvac)
- 🧑‍💻 Exposes a `/get_env` API endpoint to fetch secrets for a service/environment
- 📦 Returns all variables, variable count, and Vault path
- 🐍 Built with [FastAPI](https://fastapi.tiangolo.com/)

---

## Requirements

- Python 3.8+
- HashiCorp Vault (API accessible)
- Environment variables:
  - `VAULT_URL` – Vault server URL (e.g. `https://vault.example.com`)
  - `VAULT_TOKEN` – Vault token with read access

Install dependencies:

```bash
pip install fastapi hvac uvicorn pydantic
```

## Usage

### Start the Server

```bash
export VAULT_URL="https://your-vault-url"
export VAULT_TOKEN="your-vault-token"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

##

# How get the envs

### POST /get_env

```json
{
  "service_name": "test",
  "environment": "test-dev"
}
```

# Example curl:

```bash
curl -X POST http://localhost:8000/get_env \
  -H "Content-Type: application/json" \
  -d '{"service_name": "svc-name", "environment": "svc-name-{env}"}'
```

# Example Response 

```bash
{
  "success": true,
  "service_name": "svc-name",
  "environment": "svc-name-{env}",
  "path": "secret/svc-name/svc-name-{env}",
  "variable_count": 4,
  "all_variables": {
    "DB_HOST": "db.example.com",
    "DB_USER": "user",
    "DB_PASS": "password",
    "SECRET_KEY": "abcdef"
  }
}
```

# On error:

```bash
{
  "error": "No data found in response"
}
```
