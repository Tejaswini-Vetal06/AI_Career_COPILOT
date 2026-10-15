"""
Career Copilot AI - Tech Career Roles & Skills Taxonomy
Curated industry profiles for high-demand engineering roles:
1. AI Engineer
2. Machine Learning Engineer
3. NLP Engineer
4. Data Scientist
5. Data Analyst
6. Python Software Engineer
7. Backend Developer
8. Generative AI Engineer
9. MLOps Engineer
"""

from typing import Dict, Any, List

ROLES_DATA: Dict[str, Dict[str, Any]] = {
    "AI Engineer": {
        "id": "ai_engineer",
        "title": "AI Engineer",
        "short_desc": "Bridges research AI models with production applications through APIs, embeddings, and RAG pipelines.",
        "overview": (
            "An AI Engineer specializes in integrating cutting-edge foundation models, generative AI APIs, "
            "vector databases, and semantic search into reliable, scalable software applications. They focus on "
            "practical application engineering rather than fundamental model training from scratch."
        ),
        "essential_skills": [
            "Python", "LangChain / LlamaIndex", "OpenAI / Gemini APIs", "Vector Databases (Pinecone/Chroma/Qdrant)",
            "Prompt Engineering", "FastAPI", "RAG Systems", "RESTful APIs", "Git & GitHub"
        ],
        "optional_skills": [
            "Fine-tuning (PEFT/LoRA)", "Docker", "Model Evaluation (Ragas)", "LangSmith / Phoenix",
            "Next.js / Frontend Basics", "Redis Caching", "Cloud Services (AWS/GCP)"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Computer Science, Software Engineering, Data Science, or related STEM field. "
            "Strong GitHub portfolio demonstrating working generative AI applications frequently weighs heavily for junior roles."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Python 3 OOP, AsyncIO, REST API development with FastAPI"},
            {"level": "Beginner", "topic": "Prompt Engineering, Few-shot prompting, JSON output mode"},
            {"level": "Intermediate", "topic": "Embeddings, Vector Search algorithms (HNSW, Cosine), Chunking strategies"},
            {"level": "Intermediate", "topic": "RAG architecture: Hybrid search, Reciprocal Rank Fusion, Reranking"},
            {"level": "Advanced", "topic": "Autonomous AI Agents with Tool Calling, Memory, Multi-agent workflows"},
            {"level": "Advanced", "topic": "Production safety, guardrails (NeMo), latency caching, Ragas evaluation"}
        ],
        "portfolio_projects": [
            {
                "title": "Production RAG Document Assistant",
                "desc": "Multi-document RAG assistant with hybrid semantic search, cross-encoder reranking, and citation source verification.",
                "tech": ["Python", "FastAPI", "ChromaDB", "Gemini/OpenAI", "Streamlit"]
            },
            {
                "title": "Autonomous Data Extraction Agent",
                "desc": "Autonomous agent capable of querying SQL databases, verifying schemas, and executing tool calls to generate executive summaries.",
                "tech": ["Python", "LangChain", "SQLite", "Pydantic", "Docker"]
            }
        ],
        "interview_topics": [
            "Chunking strategy trade-offs (recursive vs semantic)",
            "Handling context window overflow and hallucination mitigation",
            "Vector database indexing (IVF vs HNSW)",
            "System design: Designing an enterprise RAG query engine with auth & caching"
        ],
        "job_query": "AI Engineer"
    },

    "Machine Learning Engineer": {
        "id": "ml_engineer",
        "title": "Machine Learning Engineer",
        "short_desc": "Designs, trains, evaluates, and deploys predictive machine learning models at scale.",
        "overview": (
            "A Machine Learning Engineer bridges theoretical data science and software engineering. "
            "They develop feature pipelines, train classical and deep learning models, optimize hyperparameters, "
            "package models in microservices, and deploy inference pipelines to production."
        ),
        "essential_skills": [
            "Python", "Scikit-Learn", "PyTorch / TensorFlow", "Pandas & NumPy",
            "Feature Engineering", "Model Evaluation & Cross-Validation", "Docker", "FastAPI / Flask", "SQL"
        ],
        "optional_skills": [
            "MLflow / Weights & Biases", "ONNX Runtime", "Kubernetes", "Apache Spark",
            "CI/CD for ML (GitHub Actions)", "Ray Serve", "Feature Stores (Feast)"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Computer Science, Machine Learning, Applied Math, Statistics, or Electrical Engineering. "
            "Strong understanding of linear algebra, calculus, and algorithms."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Applied Linear Algebra, Vectorized NumPy computations, Pandas ETL"},
            {"level": "Beginner", "topic": "Supervised Learning: Linear/Logistic Regression, Decision Trees, Ensembles (XGBoost/LightGBM)"},
            {"level": "Intermediate", "topic": "Unsupervised Learning, Dimensionality Reduction (PCA, t-SNE), Clustering"},
            {"level": "Intermediate", "topic": "Deep Learning fundamentals with PyTorch (Tensors, Autograd, Custom Training Loops)"},
            {"level": "Advanced", "topic": "Model Serialization, ONNX optimization, Batch vs Real-time Inference serving"},
            {"level": "Advanced", "topic": "ML System Design: Recommendation Engines, Fraud Detection Pipelines"}
        ],
        "portfolio_projects": [
            {
                "title": "Customer Churn Prediction Service",
                "desc": "End-to-end churn prediction with LightGBM, rigorous cross-validation, SHAP interpretability, and FastAPI deployment.",
                "tech": ["Python", "Scikit-Learn", "LightGBM", "SHAP", "FastAPI", "Docker"]
            },
            {
                "title": "Real-Time Fraud Detection Engine",
                "desc": "Streaming fraud scoring engine handling class imbalance via SMOTE/Focal Loss with sub-50ms inference latency.",
                "tech": ["Python", "PyTorch", "Redis", "FastAPI", "Prometheus"]
            }
        ],
        "interview_topics": [
            "Bias-variance tradeoff and regularization (L1 vs L2 vs ElasticNet)",
            "Addressing extreme class imbalance (precision-recall curves, cost-sensitive learning)",
            "Gradient descent optimization variants (AdamW, SGD with momentum)",
            "System design: Designing a real-time ads click-through rate (CTR) prediction system"
        ],
        "job_query": "Machine Learning Engineer"
    },

    "NLP Engineer": {
        "id": "nlp_engineer",
        "title": "NLP Engineer",
        "short_desc": "Builds linguistic algorithms, text classifiers, entity extractors, and transformer architectures.",
        "overview": (
            "Natural Language Processing (NLP) Engineers specialize in unstructured text and speech data. "
            "They design tokenization pipelines, build Named Entity Recognition (NER) systems, implement semantic "
            "text search, and fine-tune transformer models like BERT, RoBERTa, and T5."
        ),
        "essential_skills": [
            "Python", "Hugging Face Transformers", "PyTorch", "spaCy / NLTK",
            "Tokenization (BPE/WordPiece)", "Text Preprocessing & Cleaning", "Scikit-Learn", "Regex", "FastAPI"
        ],
        "optional_skills": [
            "Parameter-Efficient Fine-Tuning (LoRA)", "Quantization (bitsandbytes/GGUF)",
            "Information Retrieval (BM25)", "vLLM / TGI", "Audio Processing (Whisper)", "LangChain"
        ],
        "education_expectations": (
            "Degree in Computer Science, Computational Linguistics, Data Science, or related analytical disciplines."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Text Processing, Bag-of-Words, TF-IDF representations, N-grams"},
            {"level": "Beginner", "topic": "Classical Text Classification (Logistic Regression, Naive Bayes) with Scikit-learn"},
            {"level": "Intermediate", "topic": "Word Embeddings (Word2Vec, FastText) and Sequence Models (LSTM, GRU)"},
            {"level": "Intermediate", "topic": "Self-Attention Mechanism and Transformer Architecture from scratch"},
            {"level": "Advanced", "topic": "Fine-Tuning BERT/RoBERTa for Sequence Classification and Token Tagging (NER)"},
            {"level": "Advanced", "topic": "Quantization, FlashAttention, and Low-Latency Serving with vLLM"}
        ],
        "portfolio_projects": [
            {
                "title": "Financial Sentiment & Entity Intelligence Hub",
                "desc": "Domain-specific financial news classifier and ticker NER extractor using fine-tuned FinBERT with benchmark comparisons against TF-IDF.",
                "tech": ["Python", "Hugging Face", "PyTorch", "spaCy", "Streamlit"]
            },
            {
                "title": "Automated Legal Clause Extractor",
                "desc": "Legal agreement analysis tool classifying risky clauses and highlighting liability sections using RoBERTa.",
                "tech": ["Python", "Transformers", "FastAPI", "SQLite"]
            }
        ],
        "interview_topics": [
            "Attention mechanism mathematical formulation: Scaled Dot-Product Attention",
            "Difference between BERT (encoder-only), GPT (decoder-only), and T5 (encoder-decoder)",
            "Handling Out-of-Vocabulary (OOV) tokens with subword tokenization",
            "Evaluating classification models under severe label skew"
        ],
        "job_query": "NLP Engineer"
    },

    "Data Scientist": {
        "id": "data_scientist",
        "title": "Data Scientist",
        "short_desc": "Transforms complex business data into statistical insights, predictive models, and experimental results.",
        "overview": (
            "Data Scientists utilize statistical rigor, exploratory data analysis, hypothesis testing, and predictive "
            "modeling to answer strategic business questions. They translate ambiguous business problems into mathematical "
            "hypotheses and actionable executive roadmaps."
        ),
        "essential_skills": [
            "Python / R", "SQL (Advanced Joins, CTEs, Window Functions)", "Pandas & NumPy",
            "Statistical Hypothesis Testing & A/B Testing", "Scikit-Learn", "Data Visualization (Seaborn/Plotly)",
            "Business Communication & Storytelling"
        ],
        "optional_skills": [
            "BigQuery / Snowflake", "Time Series Forecasting (Prophet/ARIMA)", "Causal Inference",
            "Tableau / PowerBI", "PySpark", "Machine Learning Deployment"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Statistics, Mathematics, Economics, Computer Science, or Quantitative Engineering."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Descriptive Statistics, Probability Distributions, Advanced SQL Queries"},
            {"level": "Beginner", "topic": "Exploratory Data Analysis (EDA), Missing Data Imputation, Outlier Handling"},
            {"level": "Intermediate", "topic": "Inferential Statistics, Central Limit Theorem, Hypothesis Testing (t-test, ANOVA, Chi-Square)"},
            {"level": "Intermediate", "topic": "A/B Testing: Sample size determination, Power analysis, Statistical significance"},
            {"level": "Advanced", "topic": "Time Series Forecasting: Seasonality, Stationarity, ARIMA vs Tree-based forecasters"},
            {"level": "Advanced", "topic": "Causal Inference: Propensity Score Matching, Difference-in-Differences"}
        ],
        "portfolio_projects": [
            {
                "title": "E-Commerce Customer Lifetime Value & Churn Cohort Study",
                "desc": "Cohort analysis and probabilistic BG/NBD modeling to predict customer lifetime value (CLV) and repeat purchase likelihood.",
                "tech": ["Python", "Pandas", "Lifetimes / Scikit-learn", "Plotly", "PostgreSQL"]
            },
            {
                "title": "A/B Test Experimentation Framework",
                "desc": "End-to-end simulation of pricing experiment with statistical power calculation, CUPED variance reduction, and interactive reporting.",
                "tech": ["Python", "SciPy", "Statsmodels", "Streamlit"]
            }
        ],
        "interview_topics": [
            "P-values, Type I vs Type II errors, and multiple testing correction (Bonferroni/FDR)",
            "How to structure and evaluate an A/B test with network effects or novelty bias",
            "Interpreting regression coefficients and diagnosing multicollinearity (VIF)",
            "Translating model metrics (e.g. AUC-ROC, Recall) into dollar impact for stakeholders"
        ],
        "job_query": "Data Scientist"
    },

    "Data Analyst": {
        "id": "data_analyst",
        "title": "Data Analyst",
        "short_desc": "Cleans, organizes, and visualizes structured data to deliver executive dashboards and actionable BI.",
        "overview": (
            "Data Analysts empower organizations by synthesizing structured data from transactional databases and warehouses "
            "into interactive dashboards, diagnostic metrics, and trend reports. They excel at SQL queries, KPI tracking, and "
            "clear stakeholder presentations."
        ),
        "essential_skills": [
            "SQL (Window functions, Aggregate queries, CTEs)", "Excel / Google Sheets (VLOOKUP, Pivot, Modeling)",
            "Power BI or Tableau", "Python (Pandas, Matplotlib/Plotly)", "Data Cleaning & Normalization",
            "KPI Definition & Metric Architecture"
        ],
        "optional_skills": [
            "dbt (data build tool)", "BigQuery / Snowflake", "Basic Statistical Analysis",
            "Git version control", "Airflow basics"
        ],
        "education_expectations": (
            "Bachelor's in Information Systems, Business Analytics, Computer Science, Economics, Mathematics, or equivalent practical experience."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Relational database concepts, SQL SELECT, JOINs, GROUP BY, HAVING"},
            {"level": "Beginner", "topic": "Spreadsheet modeling, INDEX/MATCH, Dynamic Arrays, Pivot Tables"},
            {"level": "Intermediate", "topic": "Advanced SQL: Window functions (RANK, ROW_NUMBER, LAG/LEAD), Self-joins, CTEs"},
            {"level": "Intermediate", "topic": "BI Dashboard Design: Data modeling (Star schema, Snowflake schema), DAX or Tableau calculations"},
            {"level": "Advanced", "topic": "Automated reporting with Python (Pandas) and scheduled ETL transformations"},
            {"level": "Advanced", "topic": "Cohort retention curves, funnel drop-off analysis, executive KPI presentations"}
        ],
        "portfolio_projects": [
            {
                "title": "SaaS Executive Growth & Retention BI Dashboard",
                "desc": "Comprehensive SQL & Power BI analytics suite analyzing MRR, ARR, churn rate, LTV, and net revenue retention across user cohorts.",
                "tech": ["SQL", "PostgreSQL", "Power BI / Streamlit", "Python"]
            },
            {
                "title": "Global Supply Chain Logistics & Inventory Analyzer",
                "desc": "Operational intelligence dashboard uncovering supplier delivery bottlenecks and stockout risks using advanced window SQL.",
                "tech": ["SQL", "Pandas", "Plotly", "SQLite"]
            }
        ],
        "interview_topics": [
            "SQL query optimization: Index usage, execution plans, and avoiding Cartesian products",
            "Difference between OLTP and OLAP architectures",
            "How to define and validate high-stakes business KPIs across mismatched data sources",
            "Presenting conflicting data findings to executive decision-makers"
        ],
        "job_query": "Data Analyst"
    },

    "Python Software Engineer": {
        "id": "python_developer",
        "title": "Python Software Engineer",
        "short_desc": "Architects robust backend systems, RESTful microservices, and automated data pipelines using Python.",
        "overview": (
            "A Python Software Engineer builds resilient, maintainable, and high-performance applications. "
            "They write idiomatic Python, design clean object-oriented and functional architectures, implement "
            "asynchronous task queues, write automated unit tests, and integrate databases."
        ),
        "essential_skills": [
            "Python (OOP, Generators, Decorators, Typing, AsyncIO)", "FastAPI / Django / Flask",
            "Relational Databases (PostgreSQL / SQLite) & SQLAlchemy", "Pytest & Test-Driven Development",
            "Git & Code Review Standards", "Docker Containerization", "RESTful API Architecture"
        ],
        "optional_skills": [
            "Redis & Celery (Asynchronous task queues)", "Kafka / RabbitMQ", "GraphQL",
            "CI/CD Pipelines (GitHub Actions)", "AWS / GCP deployments", "Poetry / uv package management"
        ],
        "education_expectations": (
            "Bachelor's in Computer Science, Software Engineering, or equivalent practical coding proficiency with verifiable GitHub code."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Core Python idioms, Data structures (lists, dicts, sets, tuples), Context managers"},
            {"level": "Beginner", "topic": "Object-Oriented Programming, Polymorphism, Abstract Base Classes, Type hints"},
            {"level": "Intermediate", "topic": "FastAPI: Pydantic schemas, Dependency Injection, JWT Authentication"},
            {"level": "Intermediate", "topic": "Database persistence with SQLAlchemy 2.0 ORM and Alembic schema migrations"},
            {"level": "Advanced", "topic": "Concurrency in Python: AsyncIO, ThreadPoolExecutor, ProcessPoolExecutor, GIL limits"},
            {"level": "Advanced", "topic": "High-throughput asynchronous background job processing with Celery and Redis"}
        ],
        "portfolio_projects": [
            {
                "title": "Production Async Task Queue & Webhook Dispatcher",
                "desc": "Distributed job processing service with FastAPI, Celery, Redis, exponential backoff retries, and comprehensive pytest coverage (>90%).",
                "tech": ["Python", "FastAPI", "Celery", "Redis", "PostgreSQL", "Pytest", "Docker"]
            },
            {
                "title": "Multi-Tenant Enterprise API with Role-Based Access Control",
                "desc": "RESTful API platform featuring JWT authentication, granular RBAC permissions, Alembic migrations, and rate-limiting middleware.",
                "tech": ["Python", "FastAPI", "SQLAlchemy", "Alembic", "SQLite", "Pytest"]
            }
        ],
        "interview_topics": [
            "Python internals: Global Interpreter Lock (GIL), garbage collection, reference counting",
            "Difference between processes, threads, and AsyncIO event loops",
            "Designing REST APIs following idempotency, proper HTTP status codes, and pagination",
            "Writing effective unit, integration, and mocking tests with pytest"
        ],
        "job_query": "Python Developer"
    },

    "Backend Developer": {
        "id": "backend_developer",
        "title": "Backend Developer",
        "short_desc": "Constructs reliable server-side architectures, database schemas, and secure API gateways.",
        "overview": (
            "Backend Developers engineer the backbone of digital systems. They are responsible for server architecture, "
            "database modeling, transaction integrity, authentication systems, caching layers, and high-availability "
            "service orchestration."
        ),
        "essential_skills": [
            "Backend Languages (Python, Node.js, Go, or Java)", "Relational Databases & Schema Normalization",
            "REST & gRPC APIs", "Authentication & Security (OAuth2, JWT, HTTPS)", "Docker & Microservices",
            "Caching (Redis)", "Unit & Integration Testing"
        ],
        "optional_skills": [
            "Message Brokers (Kafka/RabbitMQ)", "Kubernetes (K8s)", "System Monitoring (Prometheus/Grafana)",
            "NoSQL (MongoDB/DynamoDB)", "CI/CD & Infrastructure as Code (Terraform)"
        ],
        "education_expectations": (
            "Bachelor's in Computer Science or Software Engineering, or proven portfolio of production backend architectures."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "HTTP protocol, Request-Response lifecycles, RESTful conventions, JSON payloads"},
            {"level": "Beginner", "topic": "Relational database schema design, Foreign keys, Indexes, ACID transactions"},
            {"level": "Intermediate", "topic": "API Security: Token authentication, CORS, CSRF, Rate-limiting, SQL Injection defense"},
            {"level": "Intermediate", "topic": "Database optimization: Index types (B-Tree, Hash), Query explain plans, N+1 query fixes"},
            {"level": "Advanced", "topic": "Distributed System Design: Microservices, Event-driven messaging with Kafka/RabbitMQ"},
            {"level": "Advanced", "topic": "High-availability caching strategies (Cache-aside, Write-through, Cache invalidation)"}
        ],
        "portfolio_projects": [
            {
                "title": "Distributed E-Commerce Order & Inventory Service",
                "desc": "Microservice architecture managing inventory locking, ACID payment processing, and event emission with Redis and SQLite.",
                "tech": ["Python/Go", "FastAPI", "Redis", "SQLite", "Docker Compose"]
            },
            {
                "title": "Real-time Notification & Webhook Pipeline",
                "desc": "Scalable notification dispatching engine with rate limiting, signature verification, and delivery logging.",
                "tech": ["Python", "FastAPI", "WebSockets", "Redis", "Pytest"]
            }
        ],
        "interview_topics": [
            "Database indexing strategies and when not to add an index",
            "Handling database transactions under concurrency (Isolation levels, Optimistic vs Pessimistic locking)",
            "System design: Designing a distributed URL shortener (TinyURL) or rate limiter",
            "CAP theorem and eventual consistency trade-offs"
        ],
        "job_query": "Backend Developer"
    },

    "Generative AI Engineer": {
        "id": "genai_engineer",
        "title": "Generative AI Engineer",
        "short_desc": "Architects agentic AI applications, multi-modal workflows, prompt chains, and synthetic data systems.",
        "overview": (
            "A Generative AI Engineer focuses on the emerging paradigm of agentic reasoning, multimodal foundation models, "
            "structured outputs, and fine-tuning. They design resilient pipelines that guide probabilistic LLM outputs into "
            "deterministic enterprise software."
        ),
        "essential_skills": [
            "Python", "Advanced Prompt Engineering & Evals", "LangChain / LlamaIndex / DSPy",
            "OpenAI / Gemini / Anthropic APIs", "Function Calling & Structured Outputs (Pydantic)",
            "Vector Search & Hybrid Retrieval", "FastAPI", "Evaluation Frameworks (Ragas / Deepeval)"
        ],
        "optional_skills": [
            "Model Fine-Tuning (LoRA/QLoRA on Hugging Face)", "Multi-modal processing (Audio, Vision, Video)",
            "Model distillation", "Streaming architectures (Server-Sent Events / WebSockets)", "Guardrails AI"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Computer Science, AI, or equivalent demonstrable open-source projects or deployed agents."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Foundation model capabilities, context tokenization, system prompting"},
            {"level": "Beginner", "topic": "Structured LLM output generation using Pydantic schemas and Tool Calling"},
            {"level": "Intermediate", "topic": "Advanced Retrieval: Multi-query expansion, Parent-document retriever, Contextual compression"},
            {"level": "Intermediate", "topic": "Agent architectures: ReAct loops, Plan-and-Solve, Memory persistence"},
            {"level": "Advanced", "topic": "DSPy programming framework: Compiling prompts into optimized programmatic modules"},
            {"level": "Advanced", "topic": "Continuous LLM Evaluation: Synthetic test set generation, Automated regression testing"}
        ],
        "portfolio_projects": [
            {
                "title": "Autonomous Multimodal Research Analyst Agent",
                "desc": "Intelligent agent capable of parsing research PDFs, extracting charts, conducting live web searches, and compiling grounded analytical reports.",
                "tech": ["Python", "Gemini API", "ChromaDB", "FastAPI", "Streamlit"]
            },
            {
                "title": "Enterprise Code Review & Refactoring Copilot",
                "desc": "Automated pull-request reviewer analyzing code diffs, identifying security vulnerabilities, and running automated test assertions.",
                "tech": ["Python", "GitHub API", "OpenAI/Gemini", "Pytest", "Docker"]
            }
        ],
        "interview_topics": [
            "Strategies for mitigating hallucinations in enterprise applications",
            "Trade-offs between in-context learning (RAG) vs fine-tuning (LoRA)",
            "How to structure deterministic evaluation for probabilistic generative models",
            "System design: Designing a low-latency voice-to-voice AI assistant"
        ],
        "job_query": "Generative AI Engineer"
    },

    "MLOps Engineer": {
        "id": "mlops_engineer",
        "title": "MLOps Engineer",
        "short_desc": "Automates the lifecycle of machine learning systems from CI/CD to deployment and data drift monitoring.",
        "overview": (
            "An MLOps Engineer treats machine learning as an engineered production software discipline. They design "
            "continuous training pipelines, model registries, automated testing, containerized deployments, and telemetry "
            "monitoring for concept drift and data degradation."
        ),
        "essential_skills": [
            "Python & Bash Scripting", "Docker & Container Registries", "CI/CD (GitHub Actions / GitLab CI)",
            "MLflow / Weights & Biases (Experiment Tracking & Registry)", "FastAPI / BentoML (Model Serving)",
            "Data & Model Monitoring (Evidently / Great Expectations)", "Linux System Administration"
        ],
        "optional_skills": [
            "Kubernetes & Kubeflow", "Terraform (IaC)", "Apache Airflow",
            "Cloud ML Platforms (AWS SageMaker / GCP Vertex AI)", "Feature Stores (Feast)"
        ],
        "education_expectations": (
            "Bachelor's in Computer Science, Software Engineering, DevOps, or Data Engineering with strong DevOps and ML tooling experience."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Linux environments, Shell scripting, Git workflows, Docker packaging of ML models"},
            {"level": "Beginner", "topic": "Experiment tracking: Logging parameters, metrics, and model artifacts with MLflow"},
            {"level": "Intermediate", "topic": "Continuous Integration for ML: Linting, automated unit testing, model packaging in GitHub Actions"},
            {"level": "Intermediate", "topic": "Model Serving: Packaging Scikit-Learn/PyTorch models into production FastAPI / BentoML servers"},
            {"level": "Advanced", "topic": "Data Validation and Quality Gates with Great Expectations before model ingestion"},
            {"level": "Advanced", "topic": "Continuous Monitoring: Drift detection (Evidently AI), Prometheus metrics, Model retraining triggers"}
        ],
        "portfolio_projects": [
            {
                "title": "End-to-End MLOps Pipeline with Drift Monitoring",
                "desc": "Full ML lifecycle system featuring MLflow model registry, automated GitHub Actions CI/CD, Docker deployment, and Evidently data drift alerts.",
                "tech": ["Python", "MLflow", "FastAPI", "Evidently AI", "Docker", "GitHub Actions"]
            },
            {
                "title": "Automated Model Deployment & Canary Testing Platform",
                "desc": "Model serving infrastructure supporting zero-downtime blue/green rollouts, health probes, and latency profiling.",
                "tech": ["Python", "FastAPI", "Docker", "Prometheus", "Grafana"]
            }
        ],
        "interview_topics": [
            "Differences between data drift, concept drift, and covariate shift, and how to detect each",
            "Designing an automated retraining pipeline without catastrophic forgetting",
            "Model versioning and roll-back strategies during catastrophic production incidents",
            "System design: Designing an enterprise model governance and deployment gateway"
        ],
        "job_query": "MLOps Engineer"
    },

    # --- CIVIL ENGINEERING ---
    "Civil Structural Engineer": {
        "id": "civil_structural_engineer",
        "title": "Civil Structural Engineer",
        "branch": "Civil Engineering",
        "short_desc": "Analyzes, models, and designs load-bearing RCC and steel infrastructure compliant with national building codes.",
        "overview": (
            "A Civil Structural Engineer designs, analyzes, and models safe, resilient structures—including high-rise towers, "
            "bridges, and industrial foundations. They utilize finite element modeling (ETABS, STAAD.Pro), verify bending moments, "
            "shear forces, and seismic drift, and generate compliant structural fabrication drawings."
        ),
        "essential_skills": [
            "STAAD.Pro", "ETABS", "AutoCAD", "RCC Design (IS 456 / ACI 318)", "Structural Analysis",
            "Steel Structures Design", "Seismic & Wind Load Analysis", "Foundation Engineering", "BIM / Revit Structure"
        ],
        "optional_skills": [
            "SAFE Foundation Software", "Civil 3D", "Tekla Structures", "Soil-Structure Interaction", "Nonlinear Pushover Analysis"
        ],
        "education_expectations": (
            "Bachelor's or Master's (B.Tech / B.E. / M.Tech) in Civil or Structural Engineering. "
            "Professional engineer (PE / chartered) licensure or proficiency in local building codes (IS/ACI/Eurocodes) is highly valued."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Strength of Materials, Shear Force & Bending Moment Diagrams, Determinacy"},
            {"level": "Beginner", "topic": "Reinforced Concrete Mechanics: Singly/Doubly Reinforced Beams, Columns, and Slabs (IS 456)"},
            {"level": "Intermediate", "topic": "3D Finite Element Modeling in ETABS & STAAD.Pro: Framing, Diaphragms, and Load Combinations"},
            {"level": "Intermediate", "topic": "Seismic Zone Response Spectra, Equivalent Static Method, and Wind Pressure Calculations"},
            {"level": "Advanced", "topic": "Deep Foundation Design: Pile Caps, Raft Foundations, and Retaining Walls in SAFE"},
            {"level": "Advanced", "topic": "Structural Detailing, Bar Bending Schedules (BBS), and Seismic Ductile Detailing (IS 13920)"}
        ],
        "portfolio_projects": [
            {
                "title": "G+15 High-Rise RCC Residential Tower Seismic Design",
                "desc": "3D structural modeling in ETABS with response spectrum dynamic analysis, ductile column-beam joint detailing, and raft foundation design in SAFE.",
                "tech": ["ETABS", "AutoCAD", "SAFE", "IS 456", "IS 1893"]
            },
            {
                "title": "Industrial Steel Portal Frame & Truss Design",
                "desc": "Analysis of a 30m span industrial warehouse with crane girder loads, wind load combinations, bolted connection design, and fabrication drawings.",
                "tech": ["STAAD.Pro", "AutoCAD", "IS 800", "Steel Detailing"]
            }
        ],
        "interview_topics": [
            "Difference between short columns and slender columns and buckling failure modes",
            "Code requirements for minimum shear reinforcement and ductile detailing around plastic hinges",
            "Calculating base shear using response spectrum method vs equivalent static method",
            "Addressing soft-storey and torsional irregularity in multi-storey frames"
        ],
        "job_query": "Structural Engineer"
    },

    "Construction Site & Project Engineer": {
        "id": "construction_site_engineer",
        "title": "Construction Site & Project Engineer",
        "branch": "Civil Engineering",
        "short_desc": "Manages on-site execution, concrete pour quality, contractor schedules, safety compliance, and quantity surveying.",
        "overview": (
            "A Construction Site & Project Engineer coordinates real-world civil execution on construction sites. "
            "They interpret architectural/structural blueprints, supervise concrete batching and curing, conduct quality inspections (QA/QC), "
            "manage subcontractor crews, track schedule baselines with Primavera P6, and verify quantity estimations."
        ),
        "essential_skills": [
            "Site Supervision", "Quantity Surveying & Estimation", "AutoCAD", "Primavera P6 / MS Project",
            "Concrete Technology & QA/QC", "Bar Bending Schedule (BBS)", "Total Station Surveying", "Site Safety Protocols (HSE)"
        ],
        "optional_skills": [
            "BIM Coordination (Navisworks)", "Vendor Billing & Contract Management", "Geotechnical Field Testing", "LEED Green Building"
        ],
        "education_expectations": (
            "Bachelor's or Diploma in Civil Engineering or Construction Management. "
            "Field internship or site experience demonstrating hands-on QA/QC and blueprint interpretation is critical."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Blueprint Reading: Translating architectural and structural drawings into site gridlines"},
            {"level": "Beginner", "topic": "Field Testing: Slump test, cube compression strength tests, and soil compaction verification"},
            {"level": "Intermediate", "topic": "Quantity Estimation: Material takeoff for concrete, steel reinforcement, formwork, and masonry"},
            {"level": "Intermediate", "topic": "Project Scheduling: Critical Path Method (CPM), Gantt charts, and resource allocation in Primavera"},
            {"level": "Advanced", "topic": "Subcontractor Management, Site Safety Audits (OSHA/HSE), and dispute resolution"},
            {"level": "Advanced", "topic": "BIM Clash Detection in Navisworks and 4D construction sequencing"}
        ],
        "portfolio_projects": [
            {
                "title": "Commercial Complex Construction Schedule & Resource Baseline",
                "desc": "End-to-end WBS, CPM schedule, material cash-flow curve, and milestone tracking in Primavera P6 for a 200,000 sq ft commercial facility.",
                "tech": ["Primavera P6", "MS Excel", "Quantity Estimation", "AutoCAD"]
            },
            {
                "title": "Comprehensive Site QA/QC & Material Takeoff Audit",
                "desc": "Complete quantity surveying report, Bar Bending Schedule (BBS), and slump test logging protocol for a multi-unit housing project.",
                "tech": ["AutoCAD", "Excel BBS", "Concrete QA/QC", "IS 456"]
            }
        ],
        "interview_topics": [
            "Causes and remediation of honeycomb defects and cold joints in freshly placed concrete",
            "Calculating the development length and lap length for high-yield deformed bars",
            "Managing float, critical path delays, and resource leveling on an active site",
            "Handling site safety violations and implementing mandatory PPE compliance protocols"
        ],
        "job_query": "Civil Site Engineer"
    },

    # --- MECHANICAL ENGINEERING ---
    "Mechanical Design & CAD/FEA Engineer": {
        "id": "mechanical_design_engineer",
        "title": "Mechanical Design & CAD/FEA Engineer",
        "branch": "Mechanical Engineering",
        "short_desc": "Transforms functional concepts into precision CAD models, performs structural FEA, and specifies GD&T for production.",
        "overview": (
            "A Mechanical Design Engineer designs industrial mechanisms, automotive components, and consumer products. "
            "They produce parametric 3D CAD assemblies (SolidWorks, CATIA, Creo), apply Geometric Dimensioning and Tolerancing (GD&T ASME Y14.5), "
            "conduct static and fatigue Finite Element Analysis (FEA) in ANSYS, and design for manufacturing and assembly (DFMA)."
        ),
        "essential_skills": [
            "SolidWorks / CATIA", "ANSYS FEA", "GD&T (ASME Y14.5)", "Machine Design", "DFMA Principles",
            "Material Selection (Metals/Polymers)", "Tolerance Stack-up Analysis", "Manufacturing Processes (CNC/Injection Molding)"
        ],
        "optional_skills": [
            "Creo Parametric", "Topology Optimization", "Fatigue Life Prediction", "Additive Manufacturing Design", "PDM / PLM Systems"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Mechanical, Production, or Automotive Engineering. "
            "A portfolio of 3D CAD models, exploded assemblies, and verified FEA stress reports is a primary hiring criterion."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "2D Drafting to Parametric 3D Solid Modeling, Feature Tree Best Practices, and Assembly Mates"},
            {"level": "Beginner", "topic": "Fundamentals of Machine Design: Shafts, Bearings, Gears, Fasteners, and Stress Concentrations"},
            {"level": "Intermediate", "topic": "GD&T Symbols, Datum References, MMC/LMC Modifiers, and Worst-Case Tolerance Stackups"},
            {"level": "Intermediate", "topic": "Finite Element Analysis (FEA): Mesh Independence, Boundary Constraints, Von Mises Stress in ANSYS"},
            {"level": "Advanced", "topic": "Nonlinear FEA, Plastic Deformation, Contact Mechanics, and Modal Vibration Analysis"},
            {"level": "Advanced", "topic": "Design for Injection Molding (Draft Angles, Ribs) and Sheet Metal Stamping"}
        ],
        "portfolio_projects": [
            {
                "title": "Automotive Suspension Control Arm Design & FEA Optimization",
                "desc": "CAD modeling in SolidWorks, topology optimization reducing component weight by 22%, and ANSYS static structural stress & fatigue verification.",
                "tech": ["SolidWorks", "ANSYS Workbench", "GD&T", "DFMA"]
            },
            {
                "title": "Precision 2-Stage Planetary Gearbox Reduction Drive",
                "desc": "Parametric gear tooth profile generation, bearing life calculation, thermal rating verification, and complete 2D manufacturing drawings with GD&T.",
                "tech": ["CATIA", "AGMA Gear Standards", "Tolerance Stackup", "ANSYS"]
            }
        ],
        "interview_topics": [
            "Explaining True Position tolerance with MMC modifier and how datum references constrain degrees of freedom",
            "Determining whether Von Mises or Tresca yield criterion applies for ductile vs brittle materials",
            "Handling stress singularities at re-entrant corners in FEA simulations",
            "Design principles for injection-molded parts to prevent sink marks and warpage"
        ],
        "job_query": "Mechanical Design Engineer"
    },

    "Thermal, HVAC & Energy Engineer": {
        "id": "thermal_hvac_engineer",
        "title": "Thermal, HVAC & Energy Engineer",
        "branch": "Mechanical Engineering",
        "short_desc": "Simulates heat transfer, designs building HVAC ventilation networks, and models fluid flow via CFD.",
        "overview": (
            "A Thermal & HVAC Engineer specializes in heat transfer, fluid mechanics, refrigeration cycles, and building climate control. "
            "They calculate heating/cooling heat loads, design ductwork and hydronic piping systems, simulate airflow and cooling with ANSYS Fluent, "
            "and optimize thermal efficiency for electric vehicle battery packs, data centers, and commercial facilities."
        ),
        "essential_skills": [
            "Thermodynamics & Heat Transfer", "HVAC Load Calculation (HAP / ASHRAE)", "ANSYS Fluent / CFD",
            "Duct & Piping Design", "Refrigeration Cycles", "Psychrometrics", "Energy Efficiency Standards (ASHRAE 90.1 / ECBC)"
        ],
        "optional_skills": [
            "Revit MEP", "OpenFOAM", "Battery Thermal Management Systems (BTMS)", "Cleanroom & Hospital HVAC Design"
        ],
        "education_expectations": (
            "Bachelor's in Mechanical, Energy, or Chemical Engineering. "
            "Familiarity with ASHRAE standards, psychrometric analysis, and fluid dynamics simulation tools."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Conduction, Convection, Radiation, and Vapor Compression Refrigeration Cycles"},
            {"level": "Beginner", "topic": "Psychrometric Charts: Sensible Heat, Latent Heat, Enthalpy, and Relative Humidity"},
            {"level": "Intermediate", "topic": "Cooling Load Estimation: Solar Heat Gain, Occupancy, Equipment, and Ventilation Loads in HAP"},
            {"level": "Intermediate", "topic": "Duct Sizing (Equal Friction Method), Fan Static Pressure Losses, and Pump Sizing"},
            {"level": "Advanced", "topic": "Computational Fluid Dynamics (CFD): Boundary Layer Meshing, Turbulence Models (k-epsilon, SST)"},
            {"level": "Advanced", "topic": "EV Battery Pack Liquid Cold-Plate Thermal Simulation and Thermal Runaway Prevention"}
        ],
        "portfolio_projects": [
            {
                "title": "EV Lithium-Ion Battery Pack Thermal Management Simulation",
                "desc": "ANSYS Fluent CFD simulation of liquid cooling channels maintaining cell temperatures below 38°C under 3C fast-charge discharge cycles.",
                "tech": ["ANSYS Fluent", "Heat Transfer", "CFD", "SolidWorks"]
            },
            {
                "title": "Multi-Story Hospital Isolation Ward HVAC & Air Quality Design",
                "desc": "ASHRAE 170 compliant negative-pressure isolation room airflow model, HEPA filtration sizing, and complete duct distribution design.",
                "tech": ["HAP", "Revit MEP", "ASHRAE 62.1", "Psychrometrics"]
            }
        ],
        "interview_topics": [
            "Difference between sensible heat ratio and latent heat in humid climates",
            "Selecting turbulence models (k-epsilon vs k-omega SST) for near-wall flow separation",
            "Explaining pump cavitation, NPSH (Net Positive Suction Head), and how to prevent it",
            "ASHRAE air changes per hour (ACH) standards for critical healthcare facilities"
        ],
        "job_query": "HVAC Thermal Engineer"
    },

    "Robotics & Mechatronics Automation Engineer": {
        "id": "robotics_mechatronics_engineer",
        "title": "Robotics & Mechatronics Automation Engineer",
        "branch": "Mechanical / Mechatronics",
        "short_desc": "Combines mechanical linkages, electronic actuators, sensors, and real-time control algorithms into autonomous robotics.",
        "overview": (
            "A Robotics & Mechatronics Engineer integrates mechanical hardware with sensors, actuators, and embedded control software. "
            "They design robotic kinematic arms, automated guided vehicles (AGVs), and industrial pick-and-place systems using ROS (Robot Operating System), "
            "MATLAB Simulink control loops (PID, state-space), motor drives, and sensor fusion."
        ),
        "essential_skills": [
            "ROS / ROS 2", "Python / C++", "Kinematics & Dynamics (DH Parameters)", "MATLAB & Simulink",
            "Motor Drives & Actuators (BLDC, Steppers, Servos)", "Sensors (LiDAR, Encoders, IMU)", "PID & Motion Control", "SolidWorks"
        ],
        "optional_skills": [
            "Gazebo Simulation", "SLAM (Cartographer)", "Computer Vision (OpenCV)", "MoveIt Motion Planning", "CAN bus & EtherCAT"
        ],
        "education_expectations": (
            "Bachelor's in Mechatronics, Mechanical, Electrical, or Robotics Engineering. "
            "Working physical robot prototypes or high-fidelity Gazebo simulation projects are strongly valued."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Forward & Inverse Kinematics: Coordinate Transformations, Rotation Matrices, DH Parameters"},
            {"level": "Beginner", "topic": "Actuator Selection: Torque calculations, Gear ratios, Motor driver H-bridges, and Encoders"},
            {"level": "Intermediate", "topic": "Feedback Control: Root Locus, Bode plots, and Tuning Digital PID Controllers in Simulink"},
            {"level": "Intermediate", "topic": "ROS 2 Architecture: Nodes, Topics, Services, Actions, and URDF Robot Description Files"},
            {"level": "Advanced", "topic": "Simulation in Gazebo: Physics engines, Sensor plugins (LiDAR/Camera), and Teleoperation"},
            {"level": "Advanced", "topic": "Autonomous Navigation: Costmaps, Nav2 stack, and 2D/3D SLAM mapping"}
        ],
        "portfolio_projects": [
            {
                "title": "6-DOF Robotic Manipulator Inverse Kinematics & Trajectory Planner",
                "desc": "Full URDF design, forward and numerical inverse kinematics solver in Python/C++, and MoveIt trajectory planning in ROS 2.",
                "tech": ["ROS 2", "C++", "MoveIt", "Gazebo", "SolidWorks"]
            },
            {
                "title": "Autonomous Mobile Robot (AMR) with LiDAR SLAM Navigation",
                "desc": "Differential-drive robot equipped with 2D LiDAR and wheel odometry, implementing Nav2 path planning and obstacle avoidance in Gazebo.",
                "tech": ["ROS 2", "Python", "SLAM Cartographer", "Nav2", "Linux"]
            }
        ],
        "interview_topics": [
            "Explaining the Denavit-Hartenberg (DH) convention for robotic link frames",
            "Anti-windup strategies for PID controllers subjected to actuator saturation",
            "Difference between ROS topics, services, and action servers, and when to use each",
            "Sensor fusion of IMU accelerometer and gyroscope data using Kalman filters"
        ],
        "job_query": "Robotics Engineer"
    },

    # --- ELECTRICAL & ELECTRONICS ENGINEERING ---
    "Electrical Power Systems & Grid Engineer": {
        "id": "electrical_power_engineer",
        "title": "Electrical Power Systems & Grid Engineer",
        "branch": "Electrical Engineering",
        "short_desc": "Models high-voltage generation, transmission networks, substation protection relays, and renewable grid tie-in.",
        "overview": (
            "An Electrical Power Systems Engineer analyzes and designs electrical substations, transmission networks, and industrial distribution grids. "
            "They perform load flow, short circuit, and motor acceleration studies in ETAP and MATLAB Simulink, coordinate overcurrent and distance "
            "protection relays, and design solar PV / battery energy storage system (BESS) grid interconnections."
        ),
        "essential_skills": [
            "ETAP", "MATLAB Simulink", "Power System Analysis", "Short Circuit & Load Flow Studies",
            "Substation Design", "Protection Relay Coordination", "Transformers & Switchgear", "National Electrical Code (NEC / IEEE)"
        ],
        "optional_skills": [
            "PSCADE / EMTDC", "Solar PVsyst", "Battery Energy Storage Systems (BESS)", "Arc Flash Hazard Analysis", "Power Quality Analysis"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Electrical Engineering (EEE / EE). "
            "Strong grasp of three-phase power calculations, per-unit systems, and IEEE/IEC grid standards."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Three-Phase Power, Symmetrical Components, Per-Unit System Calculations, and Phasor Diagrams"},
            {"level": "Beginner", "topic": "Transformer Connections (Delta-Wye), Vector Groups, and Transmission Line Impedance Models"},
            {"level": "Intermediate", "topic": "ETAP Modeling: Single Line Diagrams (SLD), Newton-Raphson Load Flow, and Fault Current Analysis"},
            {"level": "Intermediate", "topic": "Protection Coordination: Time-Current Characteristic (TCC) Curves, Overcurrent (50/51), Differential (87)"},
            {"level": "Advanced", "topic": "Arc Flash Hazard Assessment (IEEE 1584) and Incident Energy Reduction Techniques"},
            {"level": "Advanced", "topic": "Grid Integration of Utility-Scale Solar PV Inverters and Battery Storage (IEEE 1547)"}
        ],
        "portfolio_projects": [
            {
                "title": "33kV/11kV Distribution Substation Protection & Load Flow Study",
                "desc": "Complete single-line diagram, load flow, 3-phase symmetrical/unsymmetrical fault analysis, and relay coordination in ETAP.",
                "tech": ["ETAP", "IEEE Standards", "Protection Relays", "AutoCAD Electrical"]
            },
            {
                "title": "50 MW Solar PV Plant Grid Interconnection & Power Quality Model",
                "desc": "Simulink simulation of central solar inverters, harmonic distortion filter design, and reactive power voltage support during grid faults.",
                "tech": ["MATLAB Simulink", "Power Electronics", "PVsyst", "Grid Code"]
            }
        ],
        "interview_topics": [
            "Explaining symmetrical components (Positive, Negative, Zero sequence) in unsymmetrical fault analysis",
            "Operating principle of transformer percentage differential protection (ANSI 87T)",
            "Mitigating voltage sags and harmonic distortion generated by high-power variable frequency drives (VFDs)",
            "Procedure for calculating transformer short-circuit impedance and let-through fault current"
        ],
        "job_query": "Power Systems Engineer"
    },

    "Industrial Automation & PLC/SCADA Engineer": {
        "id": "industrial_automation_engineer",
        "title": "Industrial Automation & PLC/SCADA Engineer",
        "branch": "Electrical / Instrumentation",
        "short_desc": "Programs programmable logic controllers (PLCs), configures SCADA/HMI screens, and automates industrial manufacturing lines.",
        "overview": (
            "An Industrial Automation Engineer designs and programs control systems for manufacturing, packaging, and process plants. "
            "They write PLC logic (Ladder Logic, Structured Text per IEC 61131-3) for Siemens, Allen-Bradley, or Schneider controllers, "
            "develop intuitive SCADA/HMI operator dashboards, configure industrial communication buses (Modbus, Profinet), and tune VFD motor drives."
        ),
        "essential_skills": [
            "PLC Programming (Ladder Logic, Structured Text)", "Siemens TIA Portal / Rockwell RSLogix", "SCADA Systems (Wonderware / WinCC / Ignition)",
            "HMI Screen Design", "Industrial Protocols (Modbus, Profinet, Ethernet/IP)", "Sensors & Actuators", "VFD Drive Commissioning"
        ],
        "optional_skills": [
            "DCS Systems (Yokogawa / Emerson)", "OPC UA & Industry 4.0", "Safety PLCs (SIL 2/3)", "SQL Integration for Manufacturing"
        ],
        "education_expectations": (
            "Bachelor's or Diploma in Electrical, Electronics, Instrumentation, or Mechatronics Engineering. "
            "Practical laboratory or plant experience with physical PLC racks, wiring panels, and field instruments."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Control Panel Electrical Schematics: Relays, Contactors, Fuses, 24VDC Power Supplies, and I/O Wiring"},
            {"level": "Beginner", "topic": "IEC 61131-3 Standard: Ladder Logic (LD), Functional Block Diagrams (FBD), Timers, Counters"},
            {"level": "Intermediate", "topic": "Analog I/O Scaling: 4-20mA and 0-10V sensor scaling, temperature transmitters, pressure transducers"},
            {"level": "Intermediate", "topic": "Structured Text (ST) Programming for complex math, state machines, and recipe management"},
            {"level": "Advanced", "topic": "SCADA Development in Ignition / WinCC: Real-time Alarms, Historical Trending, User Security"},
            {"level": "Advanced", "topic": "Industrial Networking: Subnetting, Profinet IO configuration, Modbus TCP client/server"}
        ],
        "portfolio_projects": [
            {
                "title": "Automated Bottling & Packaging Assembly Line Controller",
                "desc": "Modular PLC logic in Siemens TIA Portal with state-machine sequencing, conveyor jam detection, and recipe parameter management.",
                "tech": ["Siemens TIA Portal", "S7-1200", "Ladder Logic", "HMI Simulation"]
            },
            {
                "title": "Plant-Wide Water Treatment Plant SCADA Dashboard",
                "desc": "Interactive SCADA application in Ignition with dynamic tank level indicators, PID flow rate regulation, and automated emergency alarm logging.",
                "tech": ["Ignition SCADA", "Modbus TCP", "Structured Text", "PID Control"]
            }
        ],
        "interview_topics": [
            "Difference between sinking (NPN) and sourcing (PNP) digital inputs and how to wire each",
            "Implementing a fail-safe E-Stop safety circuit compliant with Category 4 / PLe standards",
            "Tuning an analog PID loop on a PLC controlling variable frequency fluid flow",
            "Troubleshooting communication loss between a SCADA supervisory host and remote PLC racks"
        ],
        "job_query": "Automation Engineer"
    },

    # --- ELECTRONICS & COMMUNICATION ENGINEERING (ECE) ---
    "Embedded Systems & IoT Engineer": {
        "id": "embedded_systems_engineer",
        "title": "Embedded Systems & IoT Engineer",
        "branch": "Electronics & Communication (ECE)",
        "short_desc": "Writes bare-metal and RTOS firmware in Embedded C for ARM microcontrollers, designs custom PCBs, and interfaces IoT sensors.",
        "overview": (
            "An Embedded Systems Engineer develops low-level firmware and hardware interfaces that power smart devices, automotive ECUs, and medical monitors. "
            "They write memory-efficient Embedded C/C++ running on ARM Cortex-M microcontrollers and ESP32, implement multi-tasking with FreeRTOS, "
            "write drivers for hardware peripheral protocols (I2C, SPI, UART, CAN), and design custom circuit schematics and PCBs in KiCad."
        ),
        "essential_skills": [
            "Embedded C / C++", "ARM Cortex-M (STM32)", "FreeRTOS", "Communication Protocols (I2C, SPI, UART, CAN)",
            "PCB Design (KiCad / Altium)", "Hardware Debugging (Oscilloscope, Logic Analyzer)", "ESP32 & Wi-Fi/BLE IoT", "Git"
        ],
        "optional_skills": [
            "Embedded Linux / Yocto", "MQTT / AWS IoT Core", "Low-Power Firmware Optimization", "Device Driver Architecture"
        ],
        "education_expectations": (
            "Bachelor's in Electronics & Communication (ECE), Electrical Engineering, or Computer Engineering. "
            "Hands-on portfolio featuring custom designed PCBs, breadboard prototypes, and clean GitHub firmware repositories."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Microcontroller Architecture: Memory Maps, GPIO Registers, Interrupt Service Routines (ISRs)"},
            {"level": "Beginner", "topic": "Peripheral Driver Authoring: Bit manipulation, Clock configuration, and polling UART/I2C"},
            {"level": "Intermediate", "topic": "Direct Memory Access (DMA), Hardware Timers, PWM generation, and ADC sampling"},
            {"level": "Intermediate", "topic": "Real-Time Operating Systems: FreeRTOS Tasks, Semaphores, Mutexes, and Queue Management"},
            {"level": "Advanced", "topic": "Schematic Capture & 4-Layer PCB Layout in KiCad: High-speed differential routing, decoupling, DRC"},
            {"level": "Advanced", "topic": "IoT Security: TLS encryption on ESP32, OTA (Over-The-Air) firmware updates, and power profiling"}
        ],
        "portfolio_projects": [
            {
                "title": "Low-Power BLE Remote Patient Health Monitor",
                "desc": "Custom STM32/ESP32 firmware logging PPG pulse oximeter data, managing FreeRTOS task queues, and streaming via Bluetooth LE with <15uA sleep current.",
                "tech": ["Embedded C", "STM32", "FreeRTOS", "BLE", "KiCad PCB"]
            },
            {
                "title": "Automotive CAN-Bus Telemetry Node & Custom 2-Layer PCB",
                "desc": "Hardware PCB designed in KiCad with CAN transceiver, TVS protection, and firmware parsing vehicle speed/RPM messages onto an OLED display.",
                "tech": ["KiCad", "ARM Cortex-M", "CAN Bus", "Oscilloscope Debugging"]
            }
        ],
        "interview_topics": [
            "Explaining priority inversion in real-time operating systems and how priority inheritance resolves it",
            "Why the 'volatile' keyword is mandatory for memory-mapped I/O registers and variables modified inside ISRs",
            "Troubleshooting I2C bus lockup and clock stretching with an oscilloscope",
            "Best practices for ground plane layout and bypassing capacitors on mixed-signal PCBs"
        ],
        "job_query": "Embedded Engineer"
    },

    "VLSI & Digital ASIC Design Engineer": {
        "id": "vlsi_design_engineer",
        "title": "VLSI & Digital ASIC Design Engineer",
        "branch": "Electronics & Communication (ECE)",
        "short_desc": "Architects digital hardware in Verilog/SystemVerilog, simulates RTL, and verifies timing constraints for FPGA/ASIC tape-outs.",
        "overview": (
            "A VLSI & Digital Design Engineer designs and verifies the silicon microarchitecture that powers modern processors and AI accelerators. "
            "They write synthesizable Register Transfer Level (RTL) code in Verilog or SystemVerilog, verify functionality using testbenches (UVM), "
            "implement designs on FPGAs (Xilinx Vivado), and analyze Static Timing Analysis (STA) setup/hold constraints."
        ),
        "essential_skills": [
            "Verilog / SystemVerilog", "RTL Design", "Digital Logic & State Machines (FSM)", "Static Timing Analysis (STA)",
            "FPGA Prototyping (Xilinx Vivado)", "Simulation & Testbenches", "Computer Architecture (RISC-V / ARM)", "Linux & Scripting (Python/Tcl)"
        ],
        "optional_skills": [
            "Universal Verification Methodology (UVM)", "Synopsys Design Compiler", "Cadence Innovus (Physical Design)", "AXI4 Bus Protocol"
        ],
        "education_expectations": (
            "Bachelor's or Master's in Electronics Engineering, Microelectronics, or Computer Engineering. "
            "Solid comprehension of CMOS circuits, setup/hold timing, pipelining, and digital synthesis."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Digital Logic: Combinational gates, Flip-flops, Setup/Hold times, Metastability"},
            {"level": "Beginner", "topic": "Synthesizable Verilog: Blocking vs Non-blocking assignments, Moore & Mealy Finite State Machines"},
            {"level": "Intermediate", "topic": "Computer Architecture: Instruction Fetch, Decode, Execute, Memory, Writeback pipeline stages"},
            {"level": "Intermediate", "topic": "FPGA Synthesis in Vivado: Pin constraints (XDC), Clock domain crossing (CDC), and Resource utilization"},
            {"level": "Advanced", "topic": "Static Timing Analysis (STA): Slack calculation, False paths, Multi-cycle paths, and Clock jitter"},
            {"level": "Advanced", "topic": "SystemVerilog Verification: Assertions (SVA), Constrained random testbenches, and Coverage metrics"}
        ],
        "portfolio_projects": [
            {
                "title": "5-Stage Pipelined 32-bit RISC-V Processor Core (RV32I)",
                "desc": "Complete synthesizable Verilog implementation with hazard detection unit, data forwarding, branch prediction, and verification in Vivado.",
                "tech": ["Verilog", "RISC-V", "Xilinx Vivado", "ModelSim", "Git"]
            },
            {
                "title": "High-Throughput Hardware AES-128 Encryption Accelerator",
                "desc": "Pipelined cryptographic core processing 128-bit blocks per clock cycle, meeting zero setup/hold timing violations at 250MHz on an Artix-7 FPGA.",
                "tech": ["SystemVerilog", "FPGA", "STA Timing Closure", "Tcl"]
            }
        ],
        "interview_topics": [
            "Detailed difference between setup time and hold time violations, and how to remediate each in physical design",
            "Why non-blocking (<=) statements must be strictly used for sequential logic and blocking (=) for combinational logic",
            "Handling clock domain crossing (CDC) safely using 2-flip-flop synchronizers and asynchronous FIFOs",
            "Explaining data forwarding and branch hazards in a 5-stage RISC processor pipeline"
        ],
        "job_query": "VLSI Design Engineer"
    },

    # --- MEDICAL & HEALTHCARE PROFESSIONS ---
    "General Physician / Medical Officer (MBBS)": {
        "id": "medical_officer_physician",
        "title": "General Physician / Medical Officer (MBBS)",
        "branch": "Medical & Healthcare",
        "short_desc": "Conducts clinical patient examinations, formulates differential diagnoses, prescribes pharmacotherapy, and directs emergency triage.",
        "overview": (
            "A General Physician / Medical Officer provides primary and secondary clinical care in outpatient departments (OPD), inpatient wards, "
            "and emergency trauma units. They conduct structured physical examinations, interpret diagnostic lab results and ECGs, formulate evidence-based "
            "treatment plans, prescribe rational pharmacotherapy, and perform Basic/Advanced Life Support (BLS/ACLS)."
        ),
        "essential_skills": [
            "Clinical Diagnosis", "Patient Assessment & Physical Examination", "Pharmacotherapy & Prescription",
            "Emergency Medicine & Triage", "BLS / ACLS Protocols", "ECG & Chest X-Ray Interpretation",
            "Electronic Medical Records (EMR)", "Patient Communication & Medical Ethics"
        ],
        "optional_skills": [
            "Infection Control Protocols", "Minor Surgical Procedures (Suturing/Debridement)", "Telemedicine Consultation", "NABH Hospital Accreditation"
        ],
        "education_expectations": (
            "MBBS (Bachelor of Medicine, Bachelor of Surgery) or equivalent international MD degree with registered Medical Council license. "
            "Completed 1-year rotatory clinical internship across Medicine, Surgery, OBGYN, and Pediatrics."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Systemic Clinical Examination: Cardiovascular, Respiratory, Abdominal, and Central Nervous Systems"},
            {"level": "Beginner", "topic": "Diagnostic Interpretation: Complete Blood Count, Liver/Renal Function Panels, and 12-Lead ECGs"},
            {"level": "Intermediate", "topic": "Evidence-Based Pharmacotherapy: Rational antibiotic usage, antihypertensive titration, diabetic insulin regimens"},
            {"level": "Intermediate", "topic": "Emergency Resuscitation: ABCDE approach, acute coronary syndromes, anaphylaxis, and shock management"},
            {"level": "Advanced", "topic": "Preventive Medicine: Adult immunization, chronic disease counseling, and lifestyle interventions"},
            {"level": "Advanced", "topic": "Clinical Audit & Quality Improvement: Standardizing admission-to-discharge clinical handover protocols"}
        ],
        "portfolio_projects": [
            {
                "title": "Clinical Audit on Rational Empirical Antibiotic Prescribing in Emergency Wards",
                "desc": "Retrospective quality improvement audit of 250 patient charts evaluating adherence to ICMR/WHO antibiotic stewardship guidelines.",
                "tech": ["Clinical Audit", "Antibiotic Stewardship", "EMR Analysis", "Medical Statistics"]
            },
            {
                "title": "Standardized Outpatient Triage & SBAR Clinical Handover Protocol",
                "desc": "Formulated structured clinical documentation workflow reducing patient emergency transit time and communication handoff errors by 30%.",
                "tech": ["Emergency Triage", "SBAR Protocol", "NABH Standards", "Patient Safety"]
            }
        ],
        "interview_topics": [
            "Step-by-step diagnostic and therapeutic management of acute ST-elevation myocardial infarction (STEMI) in the ED",
            "Approach to an unconscious patient presenting with suspected diabetic ketoacidosis (DKA)",
            "Rational selection of first-line anti-hypertensive therapy in patients with concomitant chronic kidney disease",
            "Ethical and legal guidelines around patient informed consent and confidentiality under medical regulations"
        ],
        "job_query": "Medical Officer MBBS"
    },

    "Critical Care & Nursing Officer": {
        "id": "critical_care_nursing",
        "title": "Critical Care & Nursing Officer",
        "branch": "Medical & Healthcare",
        "short_desc": "Monitors hemodynamic stability, administers intravenous therapy, manages ICU ventilators, and ensures patient safety.",
        "overview": (
            "A Critical Care & Nursing Officer provides direct patient care in Intensive Care Units (ICU), emergency departments, and high-dependency wards. "
            "They continuously monitor vital hemodynamic telemetry, titrate life-saving inotropic infusions, manage mechanical ventilation airways, "
            "administer scheduled medications with strict five-rights safety, and lead patient infection-control protocols."
        ),
        "essential_skills": [
            "Critical Care Nursing", "Hemodynamic Monitoring", "IV Infusion & Inotrope Titration",
            "Mechanical Ventilation Airway Care", "BLS / ACLS", "Infection Control & Aseptic Technique",
            "Electronic Health Records (EHR)", "Patient & Family Communication"
        ],
        "optional_skills": [
            "Arterial Blood Gas (ABG) Analysis", "Central Line Dressing & Maintenance", "Wound & Stoma Care", "NABH Quality Indicators"
        ],
        "education_expectations": (
            "B.Sc Nursing or GNM (General Nursing and Midwifery) with active state nursing council registration. "
            "BLS/ACLS certification and ICU/emergency clinical training are preferred."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Patient Assessment: Head-to-toe examination, Glasgow Coma Scale (GCS), and vital telemetry logging"},
            {"level": "Beginner", "topic": "Medication Administration: 5 Rights of Medication, IV dosage calculations, and drug compatibility"},
            {"level": "Intermediate", "topic": "Hemodynamic Monitoring: Invasive arterial lines, central venous pressure (CVP), and inotropic infusions"},
            {"level": "Intermediate", "topic": "Arterial Blood Gas (ABG) Interpretation: Metabolic vs Respiratory acidosis and compensatory mechanisms"},
            {"level": "Advanced", "topic": "Invasive Mechanical Ventilation: Modes (AC/SIMV), alarm troubleshooting, suctioning, and weaning protocols"},
            {"level": "Advanced", "topic": "Hospital-Acquired Infection Prevention: CLABSI, CAUTI, and VAP bundles implementation"}
        ],
        "portfolio_projects": [
            {
                "title": "Ventilator-Associated Pneumonia (VAP) Care Bundle Implementation",
                "desc": "Led a quality improvement bundle (head-of-bed elevation, oral chlorhexidine, subglottic suctioning) reducing ICU VAP rates by 45%.",
                "tech": ["ICU Quality Bundle", "Infection Control", "Patient Care", "NABH"]
            },
            {
                "title": "Standardized ICU Medication Double-Check & Infusion Titration Protocol",
                "desc": "Designed a visual bedside checklist for high-alert vasopressor infusions reducing nursing calculation discrepancies to zero.",
                "tech": ["Patient Safety", "IV Pharmacology", "Hemodynamics", "EHR Documentation"]
            }
        ],
        "interview_topics": [
            "Immediate nursing actions during acute severe hypotension or ventricular tachycardia in an ICU patient",
            "Interpreting an ABG showing pH 7.22, pCO2 58, and HCO3 24 and identifying the underlying pathology",
            "Steps of the aseptic technique during central line catheter dressing change to prevent CLABSI",
            "Managing patient delirium and pain scoring in mechanically ventilated patients"
        ],
        "job_query": "Staff Nurse ICU"
    },

    "Healthcare & Hospital Administrator": {
        "id": "healthcare_administrator",
        "title": "Healthcare & Hospital Administrator",
        "branch": "Medical & Healthcare",
        "short_desc": "Oversees hospital operations, healthcare regulatory compliance (NABH/JCI), medical staff workflows, and quality metrics.",
        "overview": (
            "A Healthcare & Hospital Administrator manages the organizational, financial, and regulatory operations of hospitals and clinical systems. "
            "They coordinate patient flow across OPD and IPD, ensure strict compliance with accreditation standards (NABH, JCI), optimize bed turnover, "
            "manage health insurance/TPA claims, and implement hospital information management systems (HIMS)."
        ),
        "essential_skills": [
            "Hospital Operations", "NABH / JCI Accreditation Standards", "Health Informatics & HIMS",
            "Patient Flow & Bed Management", "Healthcare Quality Indicators", "Medical Billing & Insurance (TPA)",
            "Staff Scheduling & HR", "Statutory Health Compliance"
        ],
        "optional_skills": [
            "Six Sigma in Healthcare", "Supply Chain & Biomedical Equipment Procurement", "Biomedical Waste Management Rules", "Healthcare Financial Modeling"
        ],
        "education_expectations": (
            "MHA (Master of Hospital Administration), MBA in Healthcare Management, or MBBS/B.Sc with healthcare administration postgraduate credentials."
        ),
        "learning_topics": [
            {"level": "Beginner", "topic": "Hospital Departmental Workflows: OPD, Inpatient, Emergency, Diagnostics, and Support Services"},
            {"level": "Beginner", "topic": "Statutory Healthcare Regulations: Biomedical waste disposal, Clinical Establishments Act, organ transplant laws"},
            {"level": "Intermediate", "topic": "NABH & JCI Quality Standards: Patient safety goals, credentialing, medication safety audit protocols"},
            {"level": "Intermediate", "topic": "Health Informatics: HIMS integration, Electronic Medical Record (EMR) adoption, and digital billing"},
            {"level": "Advanced", "topic": "Operational Efficiency: Lean tools to reduce emergency department wait times and discharge turnaround time"},
            {"level": "Advanced", "topic": "Revenue Cycle Management: Pre-authorization, denial analysis, and cashless insurance reconciliation"}
        ],
        "portfolio_projects": [
            {
                "title": "Hospital Inpatient Discharge Turnaround Time (TAT) Optimization",
                "desc": "Applied Lean workflow analysis across pharmacy, billing, and nursing to reduce average discharge TAT from 4.5 hours down to 1.8 hours.",
                "tech": ["Lean Healthcare", "HIMS Analytics", "Process Mapping", "NABH Auditing"]
            },
            {
                "title": "NABH 5th Edition Mock Accreditation & Quality Compliance Blueprint",
                "desc": "Comprehensive documentation framework covering 10 chapters, SOP audits, and key performance indicator dashboards for a 150-bed hospital.",
                "tech": ["NABH Standards", "Quality Indicators", "Hospital Policy", "Patient Safety"]
            }
        ],
        "interview_topics": [
            "Strategies to reduce Emergency Room (ER) crowding and boarding times during surge hours",
            "Key clinical quality indicators mandated by NABH (e.g., bed occupancy, average length of stay, medication error rate)",
            "Managing biomedical waste segregation color-coding rules and handling needle-stick injury protocols",
            "Reconciling revenue leakages in the hospital insurance / cashless TPA claims workflow"
        ],
        "job_query": "Hospital Administrator"
    }
}


def get_all_roles() -> List[Dict[str, Any]]:
    """Return all role dictionaries."""
    return list(ROLES_DATA.values())


def get_role_by_title(title: str) -> Dict[str, Any]:
    """Lookup role data by display title."""
    return ROLES_DATA.get(title, ROLES_DATA["Machine Learning Engineer"])


def get_role_titles() -> List[str]:
    """Return list of role titles."""
    return list(ROLES_DATA.keys())


def get_role_branches() -> List[str]:
    """Return list of unique branches/fields."""
    branches = set()
    for r in ROLES_DATA.values():
        branches.add(r.get("branch", "Computer Science & AI"))
    return ["All Disciplines"] + sorted(list(branches))


def get_roles_by_branch(branch: str) -> List[str]:
    """Return role titles filtered by branch."""
    if branch == "All Disciplines":
        return list(ROLES_DATA.keys())
    return [
        title for title, data in ROLES_DATA.items()
        if data.get("branch", "Computer Science & AI") == branch
    ]

