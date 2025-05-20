# To_Do_List_Backend_FastAPI

Template
project_name/
├── alembic/                     # Migrations cho DB (dùng Alembic)
│   └── env.py
├── docker/
│   ├── Dockerfile               # Docker build
│   └── docker-compose.yml      # Dịch vụ chạy kèm DB
├── scripts/
│   └── init_db.sh              # Khởi tạo DB ban đầu (nếu cần)
├── src/
│   ├── domain/                 # 🧠 Business rules: logic & contracts
│   │   ├── entities/           # Các class nghiệp vụ (không phụ thuộc ORM)
│   │   │   └── user.py
│   │   ├── repositories/       # Interface trừu tượng hóa thao tác DB
│   │   │   └── user_repository.py
│   │   └── exceptions.py       # Domain-specific exceptions
│
│   ├── application/            # 💼 Nghiệp vụ phối hợp
│   │   ├── use_cases/          # Các kịch bản cụ thể: login, register, ...
│   │   │   └── auth_use_case.py
│   │   └── services/           # Dịch vụ phụ trợ: gửi email, mã hóa,...
│   │       └── auth_service.py
│
│   ├── infrastructure/         # ⚙️ Thực thi (kết nối, framework, 3rd)
│   │   ├── database/           # ORM models & kết nối DB
│   │   │   ├── db.py
│   │   │   └── models/
│   │   │       └── user_model.py
│   │   ├── repositories/       # Repo triển khai từ interface domain
│   │   │   └── user_repository_impl.py
│   │   ├── config/             # Load config từ env/file
│   │   │   └── settings.py
│   │   ├── security/           # OAuth2, JWT,...
│   │   │   └── oauth.py
│   │   └── services/           # Service triển khai (gửi email,...)
│   │       └── email_service.py
│
│   ├── presentation/           # 🌐 Giao tiếp HTTP (FastAPI)
│   │   └── routes/
│   │       ├── auth_routes.py
│   │       └── user_routes.py
│
│   ├── schemas/                # 📦 DTOs (input/output schemas - Pydantic)
│   │   ├── auth_schema.py
│   │   └── user_schema.py
│
│   ├── utils/                  # 🛠 Tiện ích chung
│   │   └── security.py
│
│   ├── deps.py                 # Dependency Injection (FastAPI Depends)
│   └── main.py                 # Điểm khởi chạy app
│
├── tests/                      # ✅ Test
│   ├── unit/                   # Test riêng từng module
│   ├── integration/            # Test end-to-end HTTP
│   └── conftest.py             # Pytest fixtures
├── .env
├── .gitignore
├── requirements.txt
└── README.md