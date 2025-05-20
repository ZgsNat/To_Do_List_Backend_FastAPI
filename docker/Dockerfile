# 1. Base image
FROM python:3.11-slim

# 2. Set workdir
WORKDIR /app

# 3. Copy requirements
COPY requirements.txt .

# 4. Install deps
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code
COPY . .

# 6. Run app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
