"""
Career Copilot AI - Personalized Learning Roadmap Curricula
Provides multi-week structured engineering roadmaps across:
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

ROADMAP_CURRICULA: Dict[str, List[Dict[str, Any]]] = {
    "AI Engineer": [
        {
            "week": 1,
            "title": "Foundation Models & LLM API Architecture",
            "hours": "10-12 hrs",
            "focus": "API patterns, Tokenization, Prompt Engineering, Structured JSON Outputs",
            "tasks": [
                {"id": "ai_w1_t1", "desc": "Master OpenAI and Gemini API Python SDKs (system prompts, temperature, top-p, seed)."},
                {"id": "ai_w1_t2", "desc": "Implement few-shot prompting and system instruction engineering."},
                {"id": "ai_w1_t3", "desc": "Enforce deterministic structured output using Pydantic schemas and Tool Calling mode."},
                {"id": "ai_w1_t4", "desc": "Interview Prep: Explain tokenization, context window limits, and how LLM sampling operates."}
            ]
        },
        {
            "week": 2,
            "title": "Embeddings & Vector Databases",
            "hours": "10-12 hrs",
            "focus": "Dense Embeddings, Vector Indexing (HNSW/IVF), Similarity Metrics",
            "tasks": [
                {"id": "ai_w2_t1", "desc": "Generate embeddings with sentence-transformers and measure Cosine vs Dot Product distances."},
                {"id": "ai_w2_t2", "desc": "Spin up local ChromaDB/Qdrant and implement metadata filtering queries."},
                {"id": "ai_w2_t3", "desc": "Compare chunking strategies: Fixed character vs Recursive vs Markdown-aware splitting."},
                {"id": "ai_w2_t4", "desc": "Interview Prep: What are HNSW graphs and why do vector databases use Approximate Nearest Neighbors (ANN)?"}
            ]
        },
        {
            "week": 3,
            "title": "Production RAG & Advanced Retrieval",
            "hours": "12-14 hrs",
            "focus": "Hybrid Search, Cross-Encoder Reranking, Contextual Compression",
            "tasks": [
                {"id": "ai_w3_t1", "desc": "Build hybrid retrieval combining BM25 keyword search and dense embeddings with RRF fusion."},
                {"id": "ai_w3_t2", "desc": "Implement cross-encoder reranking (e.g. ms-marco-MiniLM-L-6-v2) to filter top-4 chunks."},
                {"id": "ai_w3_t3", "desc": "Add source citation extraction and groundness verification to generated responses."},
                {"id": "ai_w3_t4", "desc": "Portfolio Milestone: Complete MVP of the Hybrid RAG Document Intelligence System."}
            ]
        },
        {
            "week": 4,
            "title": "Autonomous Agents, Evals & Deployment",
            "hours": "12-14 hrs",
            "focus": "Tool Calling, ReAct Loops, Ragas Evaluation, FastAPI & Docker",
            "tasks": [
                {"id": "ai_w4_t1", "desc": "Implement an autonomous agent with ReAct reasoning loop and external SQL/Calculator tools."},
                {"id": "ai_w4_t2", "desc": "Set up automated evaluation suite testing Faithfulness, Answer Relevance, and Context Recall."},
                {"id": "ai_w4_t3", "desc": "Package the application into a Docker container and expose a clean FastAPI REST interface."},
                {"id": "ai_w4_t4", "desc": "Interview Prep: System Design - Design an enterprise RAG assistant serving 10,000 daily internal employees."}
            ]
        }
    ],

    "Machine Learning Engineer": [
        {
            "week": 1,
            "title": "Applied Linear Algebra, NumPy & Vectorized Pipelines",
            "hours": "10-12 hrs",
            "focus": "Matrix operations, Vectorization, Pandas ETL, Data Profiling",
            "tasks": [
                {"id": "ml_w1_t1", "desc": "Implement matrix multiplication, vector projections, and gradient calculations in pure NumPy."},
                {"id": "ml_w1_t2", "desc": "Perform robust EDA: Outlier identification with IQR/Z-score and handling missing data."},
                {"id": "ml_w1_t3", "desc": "Engineer domain interaction features, polynomial terms, and one-hot/target encodings."},
                {"id": "ml_w1_t4", "desc": "Interview Prep: Explain the bias-variance tradeoff mathematically and how regularization affects it."}
            ]
        },
        {
            "week": 2,
            "title": "Supervised Learning, Cross-Validation & Imbalance",
            "hours": "12-14 hrs",
            "focus": "Logistic Regression, Gradient Boosted Trees (LightGBM/XGBoost), PR-AUC",
            "tasks": [
                {"id": "ml_w2_t1", "desc": "Build Stratified K-Fold cross-validation loops to prevent target leakage."},
                {"id": "ml_w2_t2", "desc": "Train LightGBM and XGBoost classifiers; tune learning rate, max depth, and regularization."},
                {"id": "ml_w2_t3", "desc": "Address extreme class imbalance: Benchmark class weighting vs SMOTE vs Focal Loss."},
                {"id": "ml_w2_t4", "desc": "Interview Prep: When is PR-AUC preferred over ROC-AUC in classification evaluations?"}
            ]
        },
        {
            "week": 3,
            "title": "Model Interpretability, PyTorch & Deep Learning Foundations",
            "hours": "12-14 hrs",
            "focus": "SHAP values, Feature Importance, PyTorch Tensors, Autograd, Custom Loops",
            "tasks": [
                {"id": "ml_w3_t1", "desc": "Compute global and local SHAP TreeExplainer explanations for individual predictions."},
                {"id": "ml_w3_t2", "desc": "Write a custom PyTorch training loop from scratch with AdamW and learning rate scheduler."},
                {"id": "ml_w3_t3", "desc": "Implement early stopping, model checkpointing, and gradient clipping."},
                {"id": "ml_w3_t4", "desc": "Portfolio Milestone: Complete Churn Prediction microservice with SHAP outputs."}
            ]
        },
        {
            "week": 4,
            "title": "Model Serving, Docker & Production ML Systems",
            "hours": "10-12 hrs",
            "focus": "FastAPI, Pydantic, ONNX Runtime, Multi-Stage Docker, CI/CD",
            "tasks": [
                {"id": "ml_w4_t1", "desc": "Serialize trained model pipeline and serve via FastAPI with strict Pydantic validation."},
                {"id": "ml_w4_t2", "desc": "Optimize model with ONNX Runtime to reduce single-item latency under 20ms."},
                {"id": "ml_w4_t3", "desc": "Build a production multi-stage Docker container and write automated Pytest regression gates."},
                {"id": "ml_w4_t4", "desc": "Interview Prep: System Design - Design a real-time e-commerce recommendation system."}
            ]
        }
    ],

    "NLP Engineer": [
        {
            "week": 1,
            "title": "Linguistic Foundations & Classical Text Processing",
            "hours": "10-12 hrs",
            "focus": "Regex, Tokenization, Lemmatization, TF-IDF, Naive Bayes",
            "tasks": [
                {"id": "nlp_w1_t1", "desc": "Implement text normalization, regex cleaning, and stopword removal with spaCy."},
                {"id": "nlp_w1_t2", "desc": "Construct n-gram TF-IDF representations and train baseline Logistic Regression classifiers."},
                {"id": "nlp_w1_t3", "desc": "Analyze confusion matrix and misclassified examples across text categories."},
                {"id": "nlp_w1_t4", "desc": "Interview Prep: What is subword tokenization (BPE/WordPiece) and how does it solve OOV?"}
            ]
        },
        {
            "week": 2,
            "title": "Word Embeddings & Sequence Models",
            "hours": "12-14 hrs",
            "focus": "Word2Vec, FastText, BiLSTM, Sequence Tagging (NER)",
            "tasks": [
                {"id": "nlp_w2_t1", "desc": "Train Word2Vec embeddings and evaluate vector analogies (King - Man + Woman = Queen)."},
                {"id": "nlp_w2_t2", "desc": "Build a Bidirectional LSTM in PyTorch for sequence classification."},
                {"id": "nlp_w2_t3", "desc": "Implement Named Entity Recognition (NER) pipeline with spaCy or Hugging Face token classification."},
                {"id": "nlp_w2_t4", "desc": "Interview Prep: Explain the vanishing gradient problem in RNNs vs LSTMs."}
            ]
        },
        {
            "week": 3,
            "title": "Transformer Architecture & Hugging Face",
            "hours": "12-14 hrs",
            "focus": "Self-Attention, BERT, RoBERTa, Fine-Tuning with Trainer API",
            "tasks": [
                {"id": "nlp_w3_t1", "desc": "Implement Scaled Dot-Product Attention in PyTorch from mathematical equations."},
                {"id": "nlp_w3_t2", "desc": "Fine-tune DistilRoBERTa on domain text using Hugging Face Trainer and evaluate Macro F1."},
                {"id": "nlp_w3_t3", "desc": "Compare fine-tuned transformer latency and accuracy directly against the TF-IDF baseline."},
                {"id": "nlp_w3_t4", "desc": "Portfolio Milestone: Complete Domain-Specific Sentiment & Intent Engine."}
            ]
        },
        {
            "week": 4,
            "title": "Efficient Inference & Modern LLM Tooling",
            "hours": "10-12 hrs",
            "focus": "Quantization (GGUF/bitsandbytes), LoRA fine-tuning, vLLM serving",
            "tasks": [
                {"id": "nlp_w4_t1", "desc": "Experiment with Parameter-Efficient Fine-Tuning (PEFT / LoRA) on Hugging Face."},
                {"id": "nlp_w4_t2", "desc": "Quantize model weights to 4-bit / 8-bit and profile GPU memory consumption."},
                {"id": "nlp_w4_t3", "desc": "Deploy inference endpoint via FastAPI with streaming response capabilities."},
                {"id": "nlp_w4_t4", "desc": "Interview Prep: System Design - Design a real-time toxic comment filter for a social platform."}
            ]
        }
    ],

    "Data Scientist": [
        {
            "week": 1,
            "title": "Advanced SQL & Exploratory Data Analysis",
            "hours": "10-12 hrs",
            "focus": "Window functions, CTEs, Aggregation, Pandas profiling, Imputation",
            "tasks": [
                {"id": "ds_w1_t1", "desc": "Author advanced SQL queries using ROW_NUMBER, LAG, LEAD, and PARTITION BY."},
                {"id": "ds_w1_t2", "desc": "Conduct rigorous Exploratory Data Analysis (EDA) on a 1M+ row transactional dataset."},
                {"id": "ds_w1_t3", "desc": "Create interactive Seaborn and Plotly charts highlighting distributions and correlations."},
                {"id": "ds_w1_t4", "desc": "Interview Prep: How to diagnose multicollinearity using Variance Inflation Factor (VIF)?"}
            ]
        },
        {
            "week": 2,
            "title": "Inferential Statistics & Hypothesis Testing",
            "hours": "12-14 hrs",
            "focus": "Central Limit Theorem, t-tests, ANOVA, Chi-Square, P-values",
            "tasks": [
                {"id": "ds_w2_t1", "desc": "Run two-sample t-tests and Mann-Whitney U tests on non-normal business metrics."},
                {"id": "ds_w2_t2", "desc": "Formulate null/alternative hypotheses and control for Type I & Type II error trade-offs."},
                {"id": "ds_w2_t3", "desc": "Implement multiple testing corrections (Bonferroni, Benjamini-Hochberg FDR)."},
                {"id": "ds_w2_t4", "desc": "Interview Prep: Explain p-values in plain English to a non-technical executive stakeholder."}
            ]
        },
        {
            "week": 3,
            "title": "A/B Testing & Experimentation Frameworks",
            "hours": "12-14 hrs",
            "focus": "Sample size determination, Power analysis, CUPED, Novelty bias",
            "tasks": [
                {"id": "ds_w3_t1", "desc": "Calculate minimum detectable effect (MDE) and sample size requirements before experiment launch."},
                {"id": "ds_w3_t2", "desc": "Simulate A/B experiment data with variance reduction using CUPED."},
                {"id": "ds_w3_t3", "desc": "Diagnose common experimentation pitfalls: Network spillover effects and sample ratio mismatch."},
                {"id": "ds_w3_t4", "desc": "Portfolio Milestone: Complete Customer Lifetime Value & Dynamic Cohort Retention Model."}
            ]
        },
        {
            "week": 4,
            "title": "Predictive Modeling & Business Storytelling",
            "hours": "10-12 hrs",
            "focus": "Probabilistic modeling, Cohort survival, Executive presentation",
            "tasks": [
                {"id": "ds_w4_t1", "desc": "Fit BG/NBD and Gamma-Gamma probabilistic models to forecast customer transactions and spend."},
                {"id": "ds_w4_t2", "desc": "Perform customer segmentation using K-Means and visualize radar charts."},
                {"id": "ds_w4_t3", "desc": "Synthesize analytical findings into an executive-ready slide deck with actionable recommendations."},
                {"id": "ds_w4_t4", "desc": "Interview Prep: Product Data Science - How would you measure success for Instagram Reels?"}
            ]
        }
    ],

    "Data Analyst": [
        {
            "week": 1,
            "title": "Relational Databases & Core SQL Mastery",
            "hours": "8-10 hrs",
            "focus": "JOINs, Subqueries, GROUP BY, HAVING, Data Cleaning",
            "tasks": [
                {"id": "da_w1_t1", "desc": "Master all SQL JOIN types (INNER, LEFT, FULL, CROSS) and avoid duplicate records."},
                {"id": "da_w1_t2", "desc": "Clean and format messy string, timestamp, and numeric data in SQL."},
                {"id": "da_w1_t3", "desc": "Write aggregate queries answering fundamental business KPI questions."},
                {"id": "da_w1_t4", "desc": "Interview Prep: Explain the execution order of a SQL query (FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY)."}
            ]
        },
        {
            "week": 2,
            "title": "Advanced SQL & Metric Modeling",
            "hours": "10-12 hrs",
            "focus": "Window functions (RANK, DENSE_RANK, NTILE), CTEs, Cohorts",
            "tasks": [
                {"id": "da_w2_t1", "desc": "Compute running totals, moving 7-day averages, and month-over-month growth rates in SQL."},
                {"id": "da_w2_t2", "desc": "Construct Common Table Expressions (CTEs) for readable multi-stage data models."},
                {"id": "da_w2_t3", "desc": "Build monthly user acquisition and retention cohort tables in SQL."},
                {"id": "da_w2_t4", "desc": "Interview Prep: What is the difference between RANK() and DENSE_RANK() in SQL?"}
            ]
        },
        {
            "week": 3,
            "title": "Data Visualization & Dashboard Architecture",
            "hours": "10-12 hrs",
            "focus": "Power BI / Tableau / Plotly, Star Schema, Chart Selection",
            "tasks": [
                {"id": "da_w3_t1", "desc": "Design a dimensional Star Schema (Fact and Dimension tables) for clean reporting."},
                {"id": "da_w3_t2", "desc": "Select the right visual encodings: Bar charts vs Lines vs Heatmaps vs Treemaps."},
                {"id": "da_w3_t3", "desc": "Build interactive filter drill-downs (by region, plan tier, and date range)."},
                {"id": "da_w3_t4", "desc": "Portfolio Milestone: Complete Executive Business Intelligence & SaaS Unit Economics Dashboard."}
            ]
        },
        {
            "week": 4,
            "title": "Executive Communication & Insight Delivery",
            "hours": "8-10 hrs",
            "focus": "KPI definition, Root-cause analysis, Stakeholder presentation",
            "tasks": [
                {"id": "da_w4_t1", "desc": "Document metric definitions (CAC, LTV, Churn, ARPU) in a company data dictionary."},
                {"id": "da_w4_t2", "desc": "Perform root cause analysis on a simulated 15% revenue drop across customer cohorts."},
                {"id": "da_w4_t3", "desc": "Author a 1-page executive brief summarizing actionable takeaways for leadership."},
                {"id": "da_w4_t4", "desc": "Interview Prep: How do you prioritize conflicting dashboard requests from sales and marketing?"}
            ]
        }
    ],

    "Python Software Engineer": [
        {
            "week": 1,
            "title": "Modern Idiomatic Python & Object-Oriented Design",
            "hours": "10-12 hrs",
            "focus": "Type Hinting, Dataclasses, Generators, Decorators, Context Managers",
            "tasks": [
                {"id": "py_w1_t1", "desc": "Refactor procedural code into clean OOP classes with Python type hinting and Pydantic."},
                {"id": "py_w1_t2", "desc": "Build custom decorators for latency timing, retry backoff, and caching."},
                {"id": "py_w1_t3", "desc": "Implement memory-efficient generators for processing large datasets line-by-line."},
                {"id": "py_w1_t4", "desc": "Interview Prep: How do Python generators manage state and save memory?"}
            ]
        },
        {
            "week": 2,
            "title": "REST API Development & Persistence with FastAPI",
            "hours": "12-14 hrs",
            "focus": "FastAPI, SQLAlchemy 2.0, Alembic, PostgreSQL, Dependency Injection",
            "tasks": [
                {"id": "py_w2_t1", "desc": "Design REST endpoints with path/query parameters, status codes, and error handlers."},
                {"id": "py_w2_t2", "desc": "Define database models with SQLAlchemy 2.0 and manage schema migrations via Alembic."},
                {"id": "py_w2_t3", "desc": "Implement JWT authentication with password hashing (bcrypt) and dependency injection."},
                {"id": "py_w2_t4", "desc": "Interview Prep: What are the benefits of Dependency Injection in FastAPI?"}
            ]
        },
        {
            "week": 3,
            "title": "Concurrency & Asynchronous Architectures",
            "hours": "12-14 hrs",
            "focus": "AsyncIO, Tasks, Connection Pooling, Redis Caching",
            "tasks": [
                {"id": "py_w3_t1", "desc": "Implement async HTTP clients with httpx/aiohttp using asyncio.gather."},
                {"id": "py_w3_t2", "desc": "Integrate Redis caching using the cache-aside pattern with TTL expiration."},
                {"id": "py_w3_t3", "desc": "Build asynchronous background task queue with Redis and Celery."},
                {"id": "py_w3_t4", "desc": "Portfolio Milestone: Complete High-Concurrency Async Task Dispatcher."}
            ]
        },
        {
            "week": 4,
            "title": "Testing, Dockerization & CI/CD Pipelines",
            "hours": "10-12 hrs",
            "focus": "Pytest, Fixtures, Mocking, Multi-Stage Docker, GitHub Actions",
            "tasks": [
                {"id": "py_w4_t1", "desc": "Write unit and integration tests achieving >90% coverage with pytest and pytest-cov."},
                {"id": "py_w4_t2", "desc": "Mock external API calls and database connections using pytest fixtures and unittest.mock."},
                {"id": "py_w4_t3", "desc": "Build a secure non-root multi-stage Docker container and automate tests in GitHub Actions."},
                {"id": "py_w4_t4", "desc": "Interview Prep: System Design - Design a distributed rate limiter for a public API."}
            ]
        }
    ],

    "Backend Developer": [
        {
            "week": 1,
            "title": "Network Protocols & API Design Standards",
            "hours": "10-12 hrs",
            "focus": "HTTP/HTTPS, RESTful design, Headers, Status codes, Idempotency",
            "tasks": [
                {"id": "be_w1_t1", "desc": "Design REST APIs following strict idempotent PUT, POST, DELETE, GET semantics."},
                {"id": "be_w1_t2", "desc": "Implement pagination strategies: Offset/Limit vs Cursor-based keyset pagination."},
                {"id": "be_w1_t3", "desc": "Add CORS, rate limiting, and security headers (CSP, HSTS) to web services."},
                {"id": "be_w1_t4", "desc": "Interview Prep: What is the difference between TCP and UDP, and how does HTTP/2 improve over HTTP/1.1?"}
            ]
        },
        {
            "week": 2,
            "title": "Relational Data Modeling & Transaction Integrity",
            "hours": "12-14 hrs",
            "focus": "PostgreSQL, ACID, Isolation Levels, Indexes (B-Tree/Hash), EXPLAIN ANALYZE",
            "tasks": [
                {"id": "be_w2_t1", "desc": "Design 3NF relational schemas with foreign key cascades and integrity constraints."},
                {"id": "be_w2_t2", "desc": "Analyze query performance using EXPLAIN ANALYZE and add composite B-Tree indexes."},
                {"id": "be_w2_t3", "desc": "Implement database transactions with pessimistic locking (SELECT FOR UPDATE) to prevent race conditions."},
                {"id": "be_w2_t4", "desc": "Interview Prep: Explain the four ACID properties and describe phantom reads."}
            ]
        },
        {
            "week": 3,
            "title": "Caching Strategies & Message Brokers",
            "hours": "12-14 hrs",
            "focus": "Redis, Cache Invalidation, Pub/Sub, RabbitMQ/Kafka basics",
            "tasks": [
                {"id": "be_w3_t1", "desc": "Implement Redis cache-aside and write-through patterns for heavy read endpoints."},
                {"id": "be_w3_t2", "desc": "Build event-driven decoupling using Redis Pub/Sub or RabbitMQ queues."},
                {"id": "be_w3_t3", "desc": "Handle distributed locking using Redis Redlock or optimistic locking versions."},
                {"id": "be_w3_t4", "desc": "Portfolio Milestone: Complete Distributed E-Commerce Order Microservice."}
            ]
        },
        {
            "week": 4,
            "title": "Microservices, Container Orchestration & System Design",
            "hours": "12-14 hrs",
            "focus": "Docker Compose, API Gateways, Observability, Distributed System Design",
            "tasks": [
                {"id": "be_w4_t1", "desc": "Orchestrate multi-container backend with Docker Compose (App, Postgres, Redis)."},
                {"id": "be_w4_t2", "desc": "Implement distributed tracing and structured JSON logging with correlation IDs."},
                {"id": "be_w4_t3", "desc": "Simulate and benchmark failover resilience and graceful degradation."},
                {"id": "be_w4_t4", "desc": "Interview Prep: System Design - Design a URL shortener (TinyURL) handling 100M daily writes."}
            ]
        }
    ],

    "Generative AI Engineer": [
        {
            "week": 1,
            "title": "Foundation Models & Structured Generation",
            "hours": "10-12 hrs",
            "focus": "Prompt Engineering, Pydantic Structured Outputs, Model Parameters",
            "tasks": [
                {"id": "gen_w1_t1", "desc": "Configure foundation model parameters and compare outputs across temperature and top-p."},
                {"id": "gen_w1_t2", "desc": "Enforce strict JSON schema validation using Pydantic v2 and tool calling."},
                {"id": "gen_w1_t3", "desc": "Implement streaming generation with Server-Sent Events (SSE) in FastAPI."},
                {"id": "gen_w1_t4", "desc": "Interview Prep: How does temperature affect next-token probability distribution in LLMs?"}
            ]
        },
        {
            "week": 2,
            "title": "Agentic Reasoning & Tool Orchestration",
            "hours": "12-14 hrs",
            "focus": "ReAct Framework, Function Calling, Memory Buffers, Guardrails",
            "tasks": [
                {"id": "gen_w2_t1", "desc": "Build a custom agent loop that dynamically selects between web search, calculator, and database tools."},
                {"id": "gen_w2_t2", "desc": "Implement token-managed conversational memory with sliding window summarization."},
                {"id": "gen_w2_t3", "desc": "Integrate safety guardrails preventing prompt injection and jailbreak attempts."},
                {"id": "gen_w2_t4", "desc": "Interview Prep: What are the primary failure modes of autonomous LLM agents?"}
            ]
        },
        {
            "week": 3,
            "title": "Multi-Agent Architectures & Multi-Modal Workflows",
            "hours": "12-14 hrs",
            "focus": "Planner-Worker patterns, Multi-modal (Image/Audio) processing",
            "tasks": [
                {"id": "gen_w3_t1", "desc": "Design a collaborative multi-agent system with supervisor and specialized workers."},
                {"id": "gen_w3_t2", "desc": "Process multimodal inputs: Parse image charts and documents using Gemini Vision."},
                {"id": "gen_w3_t3", "desc": "Implement automated fact-checking and self-reflection loops before emitting output."},
                {"id": "gen_w3_t4", "desc": "Portfolio Milestone: Complete Autonomous Multi-Agent Market Research Analyst."}
            ]
        },
        {
            "week": 4,
            "title": "Evaluation, Fine-Tuning & Production Guardrails",
            "hours": "10-12 hrs",
            "focus": "DSPy, Synthetic evaluation, LoRA/QLoRA, Observability",
            "tasks": [
                {"id": "gen_w4_t1", "desc": "Program prompts systematically using the DSPy framework to compile optimal instructions."},
                {"id": "gen_w4_t2", "desc": "Set up continuous automated LLM evaluations using synthetic ground-truth datasets."},
                {"id": "gen_w4_t3", "desc": "Deploy streaming agent application to Streamlit Cloud with secure API key management."},
                {"id": "gen_w4_t4", "desc": "Interview Prep: System Design - Design a real-time multimodal customer support copilot."}
            ]
        }
    ],

    "MLOps Engineer": [
        {
            "week": 1,
            "title": "Linux, Containerization & Git Workflows",
            "hours": "10-12 hrs",
            "focus": "Linux Shell, Multi-Stage Docker, Conventional Commits, Pre-commit hooks",
            "tasks": [
                {"id": "mlops_w1_t1", "desc": "Write robust Bash scripts for automated data downloading and environment verification."},
                {"id": "mlops_w1_t2", "desc": "Author optimized multi-stage Dockerfiles for ML environments with pinned dependencies."},
                {"id": "mlops_w1_t3", "desc": "Configure pre-commit hooks for ruff linting, black formatting, and security scanning."},
                {"id": "mlops_w1_t4", "desc": "Interview Prep: How does Docker layer caching work and how to order instructions for minimum build time?"}
            ]
        },
        {
            "week": 2,
            "title": "Experiment Tracking & Model Governance with MLflow",
            "hours": "12-14 hrs",
            "focus": "MLflow Tracking Server, Model Registry, Artifact storage",
            "tasks": [
                {"id": "mlops_w2_t1", "desc": "Spin up a local MLflow server with SQLite backend and artifact store."},
                {"id": "mlops_w2_t2", "desc": "Instrument training code to log hyperparameters, evaluation metrics, and ROC curves."},
                {"id": "mlops_w2_t3", "desc": "Implement model registry transitions: Staging -> Production -> Archived."},
                {"id": "mlops_w2_t4", "desc": "Interview Prep: What are the trade-offs of storing model weights in Git LFS vs Cloud Object Storage (S3/GCS)?"}
            ]
        },
        {
            "week": 3,
            "title": "Continuous Integration & Automated Testing for ML",
            "hours": "12-14 hrs",
            "focus": "GitHub Actions, Great Expectations, Data Quality Gates, Regression Testing",
            "tasks": [
                {"id": "mlops_w3_t1", "desc": "Implement data validation suites with Great Expectations before model ingestion."},
                {"id": "mlops_w3_t2", "desc": "Build GitHub Actions CI pipeline running unit tests and building Docker containers."},
                {"id": "mlops_w3_t3", "desc": "Set up automated regression testing comparing new candidate models against production baseline."},
                {"id": "mlops_w3_t4", "desc": "Portfolio Milestone: Complete End-to-End MLOps Pipeline with Drift Monitoring."}
            ]
        },
        {
            "week": 4,
            "title": "Model Monitoring, Drift Telemetry & Serving",
            "hours": "12-14 hrs",
            "focus": "Data Drift (Evidently), Prometheus, Model Retraining Triggers, FastAPI",
            "tasks": [
                {"id": "mlops_w4_t1", "desc": "Serve model with FastAPI and expose Prometheus `/metrics` for inference count and latency."},
                {"id": "mlops_w4_t2", "desc": "Implement data drift detection using Evidently AI and generate automated HTML reports."},
                {"id": "mlops_w4_t3", "desc": "Design automated alerting triggers when drift score exceeds statistical thresholds."},
                {"id": "mlops_w4_t4", "desc": "Interview Prep: System Design - Design an enterprise automated retraining and canary rollout system."}
            ]
        }
    ]
}


def get_roadmap_for_role(role_title: str) -> List[Dict[str, Any]]:
    """Return roadmap curriculum for given role title with dynamic generation for all engineering & medical tracks."""
    if role_title in ROADMAP_CURRICULA:
        return ROADMAP_CURRICULA[role_title]

    from modules.data.roles_data import ROLES_DATA
    role_data = ROLES_DATA.get(role_title)
    if not role_data:
        return ROADMAP_CURRICULA["Machine Learning Engineer"]

    learning_topics = role_data.get("learning_topics", [])
    essential_skills = role_data.get("essential_skills", [])
    interview_topics = role_data.get("interview_topics", [])

    # Split learning topics into 4 weekly sprints
    safe_id = role_data.get("id", "role")
    weeks = [
        {
            "week": 1,
            "title": f"Foundations & Core Principles: {essential_skills[0] if essential_skills else 'Fundamentals'}",
            "hours": "10-12 hrs",
            "focus": f"Foundational theory, core standards, and primary industry tools ({', '.join(essential_skills[:3])}).",
            "tasks": [
                {"id": f"{safe_id}_w1_t1", "desc": learning_topics[0]["topic"] if len(learning_topics) > 0 else "Review core domain fundamentals and mathematical foundations."},
                {"id": f"{safe_id}_w1_t2", "desc": learning_topics[1]["topic"] if len(learning_topics) > 1 else "Set up professional simulation/CAD/IDE software environment."},
                {"id": f"{safe_id}_w1_t3", "desc": f"Complete hands-on introductory lab exercising {essential_skills[0] if essential_skills else 'core skill'}."},
                {"id": f"{safe_id}_w1_t4", "desc": f"Interview Prep: {interview_topics[0] if interview_topics else 'Master fundamental technical definitions.'}"}
            ]
        },
        {
            "week": 2,
            "title": f"Intermediate Modeling & Applied Analysis: {essential_skills[1] if len(essential_skills) > 1 else 'Analysis'}",
            "hours": "10-12 hrs",
            "focus": f"Advanced calculation, simulation pipelines, and quality verification ({', '.join(essential_skills[2:5])}).",
            "tasks": [
                {"id": f"{safe_id}_w2_t1", "desc": learning_topics[2]["topic"] if len(learning_topics) > 2 else "Execute multi-parameter analysis under realistic boundary constraints."},
                {"id": f"{safe_id}_w2_t2", "desc": learning_topics[3]["topic"] if len(learning_topics) > 3 else "Implement automated validation scripts or testbench checks."},
                {"id": f"{safe_id}_w2_t3", "desc": f"Conduct practical design exercise conforming to industry codes and safety factors."},
                {"id": f"{safe_id}_w2_t4", "desc": f"Interview Prep: {interview_topics[1] if len(interview_topics) > 1 else 'Explain failure modes and optimization trade-offs.'}"}
            ]
        },
        {
            "week": 3,
            "title": f"Advanced Design, QA & Compliance: {essential_skills[2] if len(essential_skills) > 2 else 'Optimization'}",
            "hours": "12-14 hrs",
            "focus": "Compliance codes, system integration, tolerance budgeting, and professional documentation.",
            "tasks": [
                {"id": f"{safe_id}_w3_t1", "desc": learning_topics[4]["topic"] if len(learning_topics) > 4 else "Conduct advanced stress/stability/risk assessment."},
                {"id": f"{safe_id}_w3_t2", "desc": f"Review statutory regulatory codes and industry benchmarks for {role_title}."},
                {"id": f"{safe_id}_w3_t3", "desc": "Draft comprehensive technical specification sheet with complete verification evidence."},
                {"id": f"{safe_id}_w3_t4", "desc": f"Portfolio Milestone: Complete MVP of the {role_data.get('portfolio_projects', [{}])[0].get('title', 'Capstone Portfolio Project')}."}
            ]
        },
        {
            "week": 4,
            "title": "System Integration, Portfolio Delivery & Interview Readiness",
            "hours": "12-14 hrs",
            "focus": "Peer review, technical defense, end-to-end portfolio presentation, and mock interviews.",
            "tasks": [
                {"id": f"{safe_id}_w4_t1", "desc": learning_topics[5]["topic"] if len(learning_topics) > 5 else "Perform comprehensive regression review and error analysis."},
                {"id": f"{safe_id}_w4_t2", "desc": "Document reproducible portfolio case study with clean methodology and quantified outcomes."},
                {"id": f"{safe_id}_w4_t3", "desc": f"Interview Prep: {interview_topics[-1] if interview_topics else 'Conduct system design defense under interview conditions.'}"},
                {"id": f"{safe_id}_w4_t4", "desc": "Final Milestone: Complete full interview simulation with the AI Interview Coach."}
            ]
        }
    ]
    return weeks


def get_total_roadmap_tasks(role_title: str) -> int:
    """Return total number of tasks in a role's roadmap."""
    curriculum = get_roadmap_for_role(role_title)
    return sum(len(week.get("tasks", [])) for week in curriculum)

