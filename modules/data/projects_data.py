"""
Career Copilot AI - Curated Portfolio Project Specifications
Provides concrete, production-grade project blueprints for:
- AI Engineer
- Machine Learning Engineer
- NLP Engineer
- Data Scientist
- Data Analyst
- Python Software Engineer
- Backend Developer
- Generative AI Engineer
- MLOps Engineer
"""

from typing import Dict, Any, List

PROJECT_SPECS: Dict[str, List[Dict[str, Any]]] = {
    "AI Engineer": [
        {
            "id": "ai_proj_1",
            "title": "Production-Grade Hybrid RAG Document Intelligence System",
            "role": "AI Engineer",
            "objective": "Build a multi-document RAG assistant that answers complex domain queries with verified source citations, avoiding hallucinations.",
            "why_matches": "Demonstrates enterprise-grade semantic search, vector indexing, cross-encoder reranking, and citation generation.",
            "skills_demonstrated": ["Python", "FastAPI", "ChromaDB/Qdrant", "LangChain/LlamaIndex", "Embeddings", "Reranking", "Streamlit"],
            "tech_stack": ["Python 3.11+", "FastAPI", "ChromaDB", "sentence-transformers", "OpenAI/Gemini API", "Pytest", "Docker"],
            "milestones": [
                "1. Ingestion: Recursive chunking (500 tokens, 50 overlap) with metadata preservation (page, document ID).",
                "2. Indexing: Generate embeddings (BGE or OpenAI text-embedding-3) and store in local ChromaDB.",
                "3. Retrieval: Hybrid search combining BM25 keyword matching and dense vector search via Reciprocal Rank Fusion (RRF).",
                "4. Reranking: Apply Cross-Encoder (ms-marco-MiniLM-L-6-v2) to top 20 candidates down to top 4.",
                "5. Generation & Guardrails: Grounded answer generation requiring exact inline citations; validate with Ragas evaluation."
            ],
            "testing_requirements": [
                "Unit tests verifying chunk boundary integrity without dropping sentence endings.",
                "Retrieval precision@k and Recall@k evaluation on a 25-question gold benchmark set.",
                "End-to-end API latency benchmarking under concurrent user load (<1.5s response time)."
            ],
            "deployment_options": [
                "Docker containerized microservice deployed to Render, AWS ECS, or Google Cloud Run.",
                "Interactive frontend deployed on Streamlit Community Cloud."
            ],
            "github_deliverables": [
                "Clean README.md with system architecture diagram and prompt flow.",
                "Dockerfile and docker-compose.yml for one-click local reproduction.",
                "Automated GitHub Actions CI running pytest and ruff linting.",
                "Sample benchmark notebook reporting faithfulness and context recall metrics."
            ]
        },
        {
            "id": "ai_proj_2",
            "title": "Autonomous SQL Data Analyst Agent with Schema Guardrails",
            "role": "AI Engineer",
            "objective": "Design an autonomous agent that translates natural language inquiries into safe SQL queries, executes them, and returns visual summaries.",
            "why_matches": "Demonstrates tool calling, deterministic Pydantic structured output, and safety guardrails preventing SQL injection.",
            "skills_demonstrated": ["Python", "LangChain/DSPy", "Tool Calling", "SQLite/PostgreSQL", "Pydantic", "FastAPI"],
            "tech_stack": ["Python", "LangChain", "SQLite", "Pydantic v2", "Plotly", "Streamlit"],
            "milestones": [
                "1. Database introspection: Schema extraction and dynamic few-shot prompt construction.",
                "2. Safe SQL Generation: Pydantic schema validation restricting commands strictly to read-only SELECT statements.",
                "3. Sandboxed Execution: Query execution on SQLite database with strict 5-second timeout.",
                "4. Auto-Correction Loop: If database returns SQL syntax error, pass traceback back to LLM for self-correction.",
                "5. Visualization: Automated generation of Plotly charts based on SQL query schema."
            ],
            "testing_requirements": [
                "Security unit tests verifying DROP, ALTER, and DELETE queries are strictly blocked.",
                "Self-correction loop test asserting syntax errors are corrected within 2 attempts."
            ],
            "deployment_options": ["Streamlit Cloud with bundled SQLite database or Docker on Railway."],
            "github_deliverables": ["Architecture diagram, security audit documentation, interactive web demo."]
        }
    ],

    "Machine Learning Engineer": [
        {
            "id": "ml_proj_1",
            "title": "Customer Churn Prediction Service with SHAP Interpretability & FastAPI",
            "role": "Machine Learning Engineer",
            "objective": "Build and serve an end-to-end machine learning microservice that predicts customer churn probability with localized explainability.",
            "why_matches": "Exemplifies full-lifecycle ML engineering: EDA, pipeline serialization, cross-validation, feature interpretability, and low-latency REST serving.",
            "skills_demonstrated": ["Python", "Scikit-Learn", "LightGBM/XGBoost", "Feature Engineering", "FastAPI", "SHAP", "Docker"],
            "tech_stack": ["Python 3.10+", "LightGBM", "Scikit-Learn", "SHAP", "FastAPI", "Pydantic", "Docker", "Pytest"],
            "milestones": [
                "1. EDA & Feature Engineering: Outlier clipping, categorical target encoding, and ratio feature creation.",
                "2. Cross-Validation: 5-Fold Stratified K-Fold tuning to maximize PR-AUC under class imbalance.",
                "3. Explainability: Pre-computing SHAP TreeExplainer values for top contributing risk factors.",
                "4. API Packaging: FastAPI endpoint taking customer features and returning churn probability + top 3 negative drivers.",
                "5. Containerization: Docker image optimized with multi-stage build (<200MB)."
            ],
            "testing_requirements": [
                "Data validation tests asserting feature types and acceptable numeric ranges via Pydantic.",
                "Inference latency assertions verifying single-record inference < 25ms.",
                "Regression test ensuring model PR-AUC does not degrade below 0.82 threshold."
            ],
            "deployment_options": ["Docker container on Render or AWS App Runner with Prometheus metrics endpoint."],
            "github_deliverables": [
                "Reproducible training pipeline script `train.py`.",
                "Interactive API documentation via Swagger UI (`/docs`).",
                "Model card detailing training dataset, metrics, and limitations."
            ]
        },
        {
            "id": "ml_proj_2",
            "title": "Real-Time Streaming Transaction Fraud Detection Engine",
            "role": "Machine Learning Engineer",
            "objective": "Build a low-latency fraud classifier capable of scoring high-velocity transactions under extreme class imbalance (<0.2% fraud).",
            "why_matches": "Demonstrates dealing with severe class imbalance, latency constraints, and real-time inference architecture.",
            "skills_demonstrated": ["Python", "PyTorch/XGBoost", "Redis", "FastAPI", "Cost-Sensitive Learning", "Evaluation"],
            "tech_stack": ["Python", "PyTorch", "Redis", "FastAPI", "Docker", "Plotly"],
            "milestones": [
                "1. Synthetic/Public transaction data preprocessing with SMOTE / Focal Loss weighting.",
                "2. Model training and hyperparameter search optimizing for Precision@Top 1% of transactions.",
                "3. Redis feature cache: Storing rolling transaction counts per user/card.",
                "4. Streaming inference API with async batching.",
                "5. Live monitoring dashboard displaying real-time fraud alert rates."
            ],
            "testing_requirements": ["Stress testing with Locust to verify 200 requests/sec with p95 latency < 50ms."],
            "deployment_options": ["Docker Compose with Redis and FastAPI."],
            "github_deliverables": ["Load test report, architectural diagrams, benchmark metrics."]
        }
    ],

    "NLP Engineer": [
        {
            "id": "nlp_proj_1",
            "title": "Domain-Specific Sentiment & Intent Engine: TF-IDF vs Fine-Tuned Transformer",
            "role": "NLP Engineer",
            "objective": "Develop and rigorously benchmark a multi-class text classifier comparing classical n-gram TF-IDF models against fine-tuned Transformers.",
            "why_matches": "Proves deep linguistic understanding, trade-off analysis (latency vs accuracy), and Hugging Face transformer fine-tuning.",
            "skills_demonstrated": ["Python", "Hugging Face", "PyTorch", "Scikit-Learn", "Tokenization", "Transformers", "Streamlit"],
            "tech_stack": ["Python", "Transformers", "Datasets", "Scikit-Learn", "PyTorch", "Streamlit", "Plotly"],
            "milestones": [
                "1. Corpus preprocessing: Cleaning, subword tokenization analysis, sequence length distributions.",
                "2. Baseline: Logistic Regression + TF-IDF with hyperparameter tuning on character/word n-grams.",
                "3. Transformer Fine-Tuning: Fine-tune DistilRoBERTa with early stopping, mixed precision (FP16), and learning rate warm-up.",
                "4. Benchmark Suite: Side-by-side comparison of Macro F1, GPU/CPU inference latency, and memory footprint.",
                "5. Interactive UI: Streamlit playground highlighting attention weights and classified intents."
            ],
            "testing_requirements": [
                "Subword tokenization tests handling Out-of-Vocabulary (OOV) edge cases.",
                "Evaluation suite reporting confusion matrices and per-class precision/recall."
            ],
            "deployment_options": ["Hugging Face Spaces or Streamlit Cloud with quantized ONNX model weights."],
            "github_deliverables": ["Training logs on Weights & Biases, benchmark comparison tables, ONNX conversion script."]
        }
    ],

    "Data Scientist": [
        {
            "id": "ds_proj_1",
            "title": "Customer Lifetime Value (CLV) & Dynamic Cohort Retention Modeling",
            "role": "Data Scientist",
            "objective": "Formulate a predictive statistical framework to forecast customer repeat purchase probability and future monetary value.",
            "why_matches": "Exemplifies advanced applied statistics, cohort segmentation, probabilistic modeling, and executive storytelling.",
            "skills_demonstrated": ["Python", "SQL", "Pandas", "Statistical Modeling", "A/B Testing", "Plotly"],
            "tech_stack": ["Python", "Lifetimes / Scikit-learn", "PostgreSQL/SQLite", "Seaborn", "Plotly", "Streamlit"],
            "milestones": [
                "1. Transaction ETL: Aggregating raw order logs into RFM (Recency, Frequency, Monetary) matrices using advanced SQL.",
                "2. Probabilistic Modeling: Fit BG/NBD model for transaction frequency and Gamma-Gamma model for spend value.",
                "3. Customer Segmentation: K-Means clustering on predicted CLV to define High-Value, At-Risk, and Churned cohorts.",
                "4. Simulation & Uplift: Model the financial ROI of a 5% churn reduction campaign.",
                "5. Executive Brief: Interactive dashboard summarizing cohort survival curves and revenue forecasts."
            ],
            "testing_requirements": ["Statistical goodness-of-fit validation (Holdout validation on future transaction cycles)."],
            "deployment_options": ["Interactive Streamlit dashboard hosted on Streamlit Cloud."],
            "github_deliverables": ["Executive slide deck (PDF), modular Python analysis package, clean notebook with markdown insights."]
        }
    ],

    "Data Analyst": [
        {
            "id": "da_proj_1",
            "title": "Executive Business Intelligence & SaaS Unit Economics Dashboard",
            "role": "Data Analyst",
            "objective": "Build a robust SQL data model and interactive business intelligence dashboard tracking MRR, cohort churn, and customer acquisition costs.",
            "why_matches": "Demonstrates production SQL proficiency (CTEs, Window functions), KPI architecture, and clear executive reporting.",
            "skills_demonstrated": ["SQL", "Data Modeling", "Window Functions", "Pandas", "Power BI / Streamlit", "Data Cleaning"],
            "tech_stack": ["PostgreSQL/SQLite", "SQL Window Functions", "Python", "Plotly", "Streamlit"],
            "milestones": [
                "1. Schema Design: Star schema with Fact_Subscriptions and Dim_Customers, Dim_Plans, Dim_Dates.",
                "2. SQL Metrics Layer: Complex queries utilizing ROW_NUMBER, LAG, LEAD to calculate Expansion, Contraction, and Churn MRR.",
                "3. Data Quality Checks: Automated sanity queries asserting no negative durations or mismatched revenue sums.",
                "4. Dashboard Architecture: Visualizing monthly cohort retention heatmap, LTV:CAC ratio, and payback period.",
                "5. Narrative Synthesis: 1-page executive summary outlining 3 concrete growth levers."
            ],
            "testing_requirements": ["SQL assertion script verifying reconciliation between sum of line-items and reported MRR totals."],
            "deployment_options": ["Hosted Streamlit dashboard with embedded interactive SQL query editor."],
            "github_deliverables": ["Clean SQL scripts with CTE documentation, database schema diagram, interactive live demo."]
        }
    ],

    "Python Software Engineer": [
        {
            "id": "py_proj_1",
            "title": "High-Concurrency Async Task Dispatcher & Webhook Engine",
            "role": "Python Software Engineer",
            "objective": "Engineer a production-ready asynchronous job queue and webhook delivery service with exponential retries and rate limiting.",
            "why_matches": "Proves mastery of idiomatic Python, AsyncIO concurrency, database connection pooling, and strict unit testing.",
            "skills_demonstrated": ["Python", "FastAPI", "AsyncIO", "SQLAlchemy 2.0", "Redis", "Pytest", "Docker"],
            "tech_stack": ["Python 3.11+", "FastAPI", "SQLAlchemy", "Asyncpg/SQLite", "Redis", "Pytest", "Docker"],
            "milestones": [
                "1. Domain Models: SQLAlchemy 2.0 Declarative Base with UUID primary keys and timestamp mixins.",
                "2. Async Ingestion: FastAPI endpoint accepting webhooks with HMAC-SHA256 signature verification.",
                "3. Distributed Queue: Background consumer processing tasks with exponential backoff and dead-letter queue (DLQ).",
                "4. Token-Bucket Rate Limiter: Redis-backed sliding window rate limiter per client API key.",
                "5. Comprehensive Test Suite: 95%+ coverage with pytest-asyncio and testcontainers."
            ],
            "testing_requirements": [
                "Async unit tests verifying retry countdown and DLQ routing on consecutive 500 errors.",
                "Race condition testing under simulated concurrent task submission."
            ],
            "deployment_options": ["Docker Compose running app, Redis, and database."],
            "github_deliverables": ["Clean architecture with separation of concerns, CI workflow, Postman/OpenAPI collection."]
        }
    ],

    "Backend Developer": [
        {
            "id": "be_proj_1",
            "title": "Distributed Multi-Tenant E-Commerce Inventory & Order Microservice",
            "role": "Backend Developer",
            "objective": "Architect a distributed order management service guaranteeing ACID compliance, stock locking, and idempotent payments.",
            "why_matches": "Shows distributed systems knowledge, transaction isolation, caching strategies, and defensive backend engineering.",
            "skills_demonstrated": ["Python/Go", "FastAPI", "PostgreSQL", "Redis", "Docker", "Database Transactions"],
            "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Redis", "Pytest", "Docker Compose"],
            "milestones": [
                "1. Database Architecture: Relational design handling stock reservations with row-level locking (SELECT FOR UPDATE).",
                "2. Idempotency: Distributed idempotency key middleware backed by Redis to prevent duplicate charges.",
                "3. Distributed Caching: Cache-aside pattern for catalog read traffic with cache invalidation on stock updates.",
                "4. Microservice Auth: JWT token authentication with role-based permissions (Customer vs Merchant vs Admin).",
                "5. Observability: Structured JSON logging with correlation IDs passed across requests."
            ],
            "testing_requirements": ["High concurrency race condition tests simulating 50 simultaneous checkouts on a single remaining inventory item."],
            "deployment_options": ["Docker Compose on DigitalOcean or AWS ECS."],
            "github_deliverables": ["Architecture diagram, database migration scripts, load testing benchmarks."]
        }
    ],

    "Generative AI Engineer": [
        {
            "id": "gen_proj_1",
            "title": "Autonomous Multi-Agent Market Research Analyst with Live Web Search",
            "role": "Generative AI Engineer",
            "objective": "Build a collaborative multi-agent system where specialized agents plan, browse the live web, extract tables, and compile grounded reports.",
            "why_matches": "Exemplifies bleeding-edge multi-agent orchestration, structured Pydantic schemas, and dynamic plan-and-solve execution.",
            "skills_demonstrated": ["Python", "Gemini/OpenAI APIs", "LangChain/CrewAI", "Pydantic", "Tool Calling", "Streamlit"],
            "tech_stack": ["Python", "Google Gemini API", "Pydantic", "FastAPI", "Streamlit", "DuckDuckGo API"],
            "milestones": [
                "1. Agent Roles: Planner Agent, Researcher Agent (Web search tool), and Synthesis/Fact-Checker Agent.",
                "2. Structured Schemas: Strict Pydantic output models ensuring JSON predictability.",
                "3. Fact-Checking: Automated assertion comparing final claims against retrieved source snippets.",
                "4. Streaming UI: Real-time thought step visualization showing agent reasoning in the Streamlit frontend.",
                "5. Export: One-click export to Markdown and PDF reports."
            ],
            "testing_requirements": ["Evaluation tests verifying 100% schema compliance across 30 arbitrary test queries."],
            "deployment_options": ["Streamlit Cloud with API key secret management."],
            "github_deliverables": ["Prompt flow diagrams, agent interaction logs, interactive web demo."]
        }
    ],

    "MLOps Engineer": [
        {
            "id": "mlops_proj_1",
            "title": "End-to-End MLOps Pipeline: CI/CD, MLflow Registry & Data Drift Telemetry",
            "role": "MLOps Engineer",
            "objective": "Create a fully automated continuous machine learning system featuring automated testing, MLflow model registry, and live drift alerts.",
            "why_matches": "Directly targets MLOps core responsibilities: automation, reproducibility, model governance, and telemetry monitoring.",
            "skills_demonstrated": ["Python", "Docker", "MLflow", "GitHub Actions", "Evidently AI", "FastAPI", "Prometheus"],
            "tech_stack": ["Python", "MLflow", "Evidently AI", "FastAPI", "Docker", "GitHub Actions", "Prometheus"],
            "milestones": [
                "1. Versioned Data & Pipeline: Automated training pipeline triggered on data changes.",
                "2. Model Registry: Automatic logging of hyperparameters, validation metrics, and model artifact registration in MLflow.",
                "3. Automated CI/CD: GitHub Actions pipeline that lints, tests, builds Docker image, and runs regression gates.",
                "4. Model Serving: FastAPI container exposing `/predict` and `/metrics` endpoints.",
                "5. Drift Detection: Daily cron job comparing incoming production inferences against training baseline using Evidently AI."
            ],
            "testing_requirements": ["Automated pre-deployment regression gate failing CI if new model accuracy drops >2% below current production model."],
            "deployment_options": ["Docker container on AWS / GCP with automated GitHub Actions deployment."],
            "github_deliverables": ["Complete `.github/workflows/ml_pipeline.yml`, MLflow artifact screenshots, data drift report HTML."]
        }
    ]
}


def get_projects_for_role(role_title: str) -> List[Dict[str, Any]]:
    """Return curated projects for given role title with dynamic fallback to ROLES_DATA portfolio specifications."""
    if role_title in PROJECT_SPECS:
        return PROJECT_SPECS[role_title]

    from modules.data.roles_data import ROLES_DATA
    role_data = ROLES_DATA.get(role_title)
    if not role_data:
        return PROJECT_SPECS["Machine Learning Engineer"]

    role_projects = role_data.get("portfolio_projects", [])
    specs = []
    for idx, p in enumerate(role_projects):
        specs.append({
            "id": f"{role_data.get('id', 'role')}_proj_{idx + 1}",
            "title": p.get("title", f"Portfolio Benchmark Project {idx + 1}"),
            "role": role_title,
            "objective": p.get("desc", f"Comprehensive proof-of-work project demonstrating mastery in {role_title}."),
            "why_matches": f"Demonstrates core competency in {', '.join(p.get('tech', role_data.get('essential_skills', [])[:4]))}.",
            "skills_demonstrated": p.get("tech", role_data.get("essential_skills", [])[:5]),
            "tech_stack": p.get("tech", role_data.get("essential_skills", [])[:5]),
            "milestones": [
                f"1. Specification & Standards: Review relevant industry codes, boundary conditions, and design parameters.",
                f"2. Core Modeling & Simulation: Implement primary system model using {p.get('tech', ['standard tools'])[0]}.",
                f"3. Verification & Stress Testing: Execute validation checks, error bounds, or finite element / testbench simulations.",
                f"4. Quality & Compliance Gate: Verify design against statutory standards, safety factors, and peer review checklists.",
                f"5. Portfolio Deliverable: Prepare professional design brief, technical calculation drawings, and case study documentation."
            ],
            "testing_requirements": [
                "Validation report verifying mathematical bounds and compliance against reference baseline data.",
                "Peer-review QA/QC verification checklist signed off with zero unhandled edge cases."
            ],
            "deployment_options": [
                "Documented portfolio case study with full source/CAD/simulation artifacts in a public repository."
            ],
            "github_deliverables": [
                "Comprehensive technical report with methodology, formulas, and visual diagrams.",
                "Reproducible configuration files, CAD drawings, or source code files."
            ]
        })
    return specs if specs else PROJECT_SPECS["Machine Learning Engineer"]

