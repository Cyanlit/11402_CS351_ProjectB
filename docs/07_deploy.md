# 07 - Build & Deployment Guide

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.8+
- **Disk Space**: 50MB (including dependencies)
- **Memory**: 256MB minimum, 512MB recommended

### Recommended Configuration
- **Python**: 3.10+
- **Disk Space**: 100MB
- **Memory**: 1GB+

## Installation Steps

### 1. Clone or Download Project

```bash
# Clone with Git
git clone https://github.com/Cyanlit/11402_CS351_ProjectB.git
cd 11402_CS351_ProjectB

# Or download and extract ZIP
unzip 11402_CS351_ProjectB.zip
cd 11402_CS351_ProjectB
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python main.py --help
```

## Local Build

### Development Mode

```bash
# Enter project directory (activate virtual environment)
cd 11402_CS351_ProjectB
source venv/bin/activate  # Or Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov  # Testing tools
```

### Running Program

#### Interactive Mode
```bash
python main.py
```
Then enter commands:
```
> load data/sample_students.csv
> query SELECT * FROM data
> exit
```

#### Command-Line Mode
```bash
python main.py --csv data/sample_students.csv --query "SELECT * WHERE score > 85"
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_csv_loader.py -v

# Show coverage
pytest tests/ --cov=src --cov-report=html

# Generate XML report
pytest tests/ --junitxml=report.xml
```

## Build & Compilation

### Using setuptools (Package Distribution)

```bash
# Install build tools
pip install build

# Build distribution package
python -m build

# Generated files in dist/ directory
```

### Using PyInstaller (Create Executable)

```bash
# Install PyInstaller
pip install pyinstaller

# Create standalone executable
pyinstaller --onefile main.py

# Executable in dist/ directory
# Windows: dist/main.exe
# macOS/Linux: dist/main
```

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
```

### Build Docker Image

```bash
# Build image
docker build -t csvdb:1.0 .

# Run container
docker run -it csvdb:1.0

# Mount local directory
docker run -it -v /path/to/data:/app/data csvdb:1.0
```

## GitHub Actions CI/CD

### Workflow Configuration

See `.github/workflows/ci.yml`

### Triggers
- Every push to main branch
- Every pull request
- Manual trigger (workflow_dispatch)

### Workflow Steps
1. Check out code
2. Setup Python environment
3. Install dependencies
4. Run linting
5. Run tests
6. Generate coverage report
7. Upload image (optional)

## Deploy to Cloud Services

### AWS Lambda

```bash
# Prepare deployment package
pip install -r requirements.txt -t ./package
cd package
zip -r ../deployment.zip .
cd ..
zip -r deployment.zip src/ main.py

# Upload to Lambda
aws lambda create-function \
  --function-name csvdb-query \
  --runtime python3.10 \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-role \
  --handler main.lambda_handler \
  --zip-file fileb://deployment.zip
```

### Heroku

```bash
# Install Heroku CLI
# Configure with Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

## Version Management

### Version Number Convention

Follow Semantic Versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Incompatible API changes
- **MINOR**: New backward-compatible features
- **PATCH**: Bug fixes

### Release Process

```bash
# Create tag
git tag v1.0.0
git push origin v1.0.0

# Create Release
# Via GitHub UI or GitHub CLI
gh release create v1.0.0 -t "Release v1.0.0" -n "Release notes"
```

## Troubleshooting

### Issue 1: Python Not Found
```
Solution: Verify Python installation and PATH
python --version
```

### Issue 2: Missing Dependencies
```
Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue 3: Test Failures
```
Solution: Check environment and clean caches
rm -rf __pycache__
pytest tests/ -v
```

### Issue 4: Performance Issues
```
Solution: Optimize queries or increase memory
# Check for large files
ls -lh data/
```

## Monitoring & Logging

### Log Configuration

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Monitoring Metrics
- Query execution time
- Memory usage
- Error rate

## Backup & Recovery

### Backup Data

```bash
# Backup CSV files
tar -czf backup_$(date +%Y%m%d).tar.gz data/

# Backup entire project
git push --all
git push --tags
```

### Restore Data

```bash
# Restore CSV
tar -xzf backup_*.tar.gz

# Restore Git history
git pull origin main
```

## Upgrade Guide

### Upgrade from v0.x to v1.0

1. Backup existing data
2. Stop current application
3. Pull new version code
4. Run migration scripts (if any)
5. Run tests
6. Restart application

```bash
git pull origin main
pip install -r requirements.txt --upgrade
pytest tests/ -v
python main.py
```

## Security Considerations

- Regularly update dependencies to fix security vulnerabilities
- Don't hardcode sensitive information (use environment variables)
- Validate all user inputs
- Limit file upload sizes

## Performance Optimization

- Use Pandas vectorized operations
- Consider adding indexes for faster queries
- Implement query result caching
- Monitor large file processing
- Profile code for bottlenecks
