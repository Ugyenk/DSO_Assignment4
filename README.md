# 🚀 DSO_ASSIGNMENT4 — CI/CD Pipeline with Docker & Render

**GitHub:** [Ugyenk/DSO_ASSIGNMENT4](https://github.com/Ugyenk/DSO_ASSIGNMENT4)  
**Docker Hub:** [aizenchan/dso_assignment4](https://hub.docker.com/r/aizenchan/dso_assignment4)

---

## 📂 Project Structure

```
DSO_ASSIGNMENT4/
├── app.py                          # Flask application
├── test_app.py                     # Unit tests (pytest)
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker image definition
├── .dockerignore                   # Docker build exclusions
├── render.yaml                     # Render deployment config
└── .github/
    └── workflows/
        └── ci.yml                  # GitHub Actions CI/CD pipeline
```

---

## 🌐 API Endpoints

| Method | Route            | Description            |
|--------|------------------|------------------------|
| GET    | `/`              | Home — app info + status |
| GET    | `/health`        | Health check           |
| GET    | `/add/<a>/<b>`   | Returns sum of a and b |

---

## 🔄 CI/CD Pipeline

Triggers on every **push to `main`**:

```
push to main
    │
    ▼
📥 Checkout code
    │
    ▼
🐍 Setup Python 3.9
    │
    ▼
📦 Install dependencies
    │
    ▼
🧪 Run pytest (5 tests)
    │
    ▼  (only if tests pass)
🐳 Build & Push Docker image → aizenchan/dso_assignment4:latest
    │
    ▼
🚀 Trigger Render Deploy Hook
```

---

## 🐳 Docker

### Pull and run the image:
```bash
docker pull aizenchan/dso_assignment4:latest
docker run -p 5000:5000 aizenchan/dso_assignment4:latest
```

App available at `http://localhost:5000`

### Build locally:
```bash
docker build -t dso_assignment4 .
docker run -p 5000:5000 dso_assignment4
```

---

## 🔑 GitHub Secrets Required

Go to: **Repo → Settings → Secrets and variables → Actions → New repository secret**

| Secret Name             | Value                              |
|-------------------------|------------------------------------|
| `DOCKERHUB_USERNAME`    | `aizenchan`                        |
| `DOCKERHUB_TOKEN`       | Your DockerHub Access Token        |
| `RENDER_DEPLOY_HOOK_URL`| Your Render Deploy Hook URL        |

### How to get DockerHub Token:
1. [hub.docker.com](https://hub.docker.com) → Account Settings → Security
2. New Access Token → copy it → paste as `DOCKERHUB_TOKEN`

### How to get Render Deploy Hook:
1. Render dashboard → your service → Settings → Deploy Hook → copy URL

---

## 🚢 Deploy on Render

1. [render.com](https://render.com) → **New → Web Service**
2. Connect `Ugyenk/DSO_ASSIGNMENT4`
3. Set:
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `gunicorn app:app`
   - **Runtime:** Python 3

---

## 🧪 Test Output

```
collected 5 items

test_app.py::test_home         PASSED  ✓
test_app.py::test_health       PASSED  ✓
test_app.py::test_add          PASSED  ✓
test_app.py::test_add_zero     PASSED  ✓
test_app.py::test_basic_math   PASSED  ✓

===== 5 passed in 0.11s =====
```

---

## 📋 Marking Criteria

| Criteria | Implementation |
|----------|---------------|
| ✅ Project structure | All required files present |
| ✅ CI pipeline (build + test) | GitHub Actions: install → pytest → Docker build |
| ✅ Test implementation | 5 pytest unit tests |
| ✅ Deployment automation | Docker push to aizenchan/dso_assignment4 + Render hook |
| ✅ Documentation | This README |
