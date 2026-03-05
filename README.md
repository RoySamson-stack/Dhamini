# Dhamini - Automated Loan Repayment & Direct Debit Platform

Kenyan Fintech Market

## Project Structure

```
Dhamini/
├── backend/                 # Core middleware & API
│   ├── src/
│   │   ├── api/            # API routes, middleware, schemas
│   │   ├── core/           # Core configuration
│   │   ├── db/             # Database migrations & setup
│   │   ├── models/        # SQL models
│   │   ├── services/      # Business logic
│   │   ├── utils/         # Utilities
│   │   └── workers/       # Background workers
│   └── tests/
├── frontend/               # Web & Mobile apps
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom hooks
│   │   ├── services/      # API services
│   │   ├── contexts/      # React contexts
│   │   └── assets/        # Static assets
│   └── public/
├── infrastructure/         # IaC & K8s configs
│   ├── terraform/
│   ├── k8s/
│   └── scripts/
├── docs/                   # Documentation
└── README.md
```

## Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/db/init_db.py
uvicorn src.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Technology Stack

- **Backend**: Python/FastAPI, PostgreSQL, Redis, Celery
- **Frontend**: React, TypeScript, TailwindCSS
- **Infrastructure**: AWS (af-south-1), Kubernetes, Terraform
- **AI**: TensorFlow/PyTorch for ML models

## License

CONFIDENTIAL & PROPRIETARY
# Dhamini
