# 08 - Known Limitations & TODO

## Known Limitations

### Functional Limitations

#### 1. Query Syntax Limitations
- ❌ No JOIN operations supported (single-table queries only)
- ❌ No subquery support
- ❌ No UNION support
- ❌ No complex aggregations (WINDOW functions)
- ❌ Limited regex support (LIKE pattern matching limited)

#### 2. Data Type Limitations
- ⚠️ No complex data types (JSON, arrays)
- ⚠️ Date parsing depends on auto-detection, may be inaccurate
- ⚠️ Float precision may be affected by IEEE 754

#### 3. Concurrency & Transactions
- ❌ No multi-user concurrent write support
- ❌ No transaction (Transaction) support
- ❌ No locking mechanisms

#### 4. Performance Limitations
- ⚠️ CSV file must be completely loaded into memory
- ⚠️ May fail for files > 1GB due to memory limits
- ⚠️ No query optimization or execution plan

#### 5. Data Operation Limitations
- ❌ No UPDATE operations
- ❌ No DELETE operations
- ❌ No INSERT operations (only CSV loading)

### Technical Limitations

#### 1. Encoding & Format
- ⚠️ Primarily supports UTF-8, other encodings may have issues
- ⚠️ CSV format assumes standard format (correct quotes and escapes)

#### 2. Platform Limitations
- ⚠️ Path separators need special handling on Windows
- ⚠️ File name case sensitivity depends on OS

#### 3. Environment Limitations
- ⚠️ Depends on external libraries (Pandas, SQLite)
- ⚠️ Requires specific Python version (3.8+)

### Known Defects

| Defect ID | Description | Severity | Status | Planned Fix |
|-----------|-------------|----------|--------|------------|
| BUG-001 | Special characters show garbled in some encodings | Medium | Known | v1.1 |
| BUG-002 | Large file loading is slow | Medium | Known | v1.2 |
| BUG-003 | OR logic priority in WHERE clause not as expected | Low | Known | v1.1 |
| BUG-004 | LIMIT & OFFSET interaction has edge cases | Low | Known | v1.0.1 |

## Feature Improvements TODO

### Priority 1: Core Feature Enhancement

- [ ] Implement UPDATE operation
- [ ] Implement DELETE operation
- [ ] Support IN operator (`WHERE id IN (1,2,3)`)
- [ ] Support LIKE operator (`WHERE name LIKE 'A%'`)
- [ ] Support BETWEEN operator (`WHERE score BETWEEN 80 AND 90`)
- [ ] Support NULL checking (`WHERE column IS NULL`)

### Priority 2: Advanced Features

- [ ] Support JOIN operations (INNER, LEFT, RIGHT, FULL)
- [ ] Support GROUP BY and HAVING
- [ ] Support more aggregation functions (MEDIAN, STDDEV, VARIANCE)
- [ ] Support subqueries
- [ ] Support UNION / UNION ALL
- [ ] Support views (VIEW)

### Priority 3: Performance Optimization

- [ ] Implement query result caching
- [ ] Implement indexing mechanism
- [ ] Support streaming processing (large file chunking)
- [ ] Parallel query execution
- [ ] Query optimizer

### Priority 4: User Experience

- [ ] Implement GUI interface (Qt or Web UI)
- [ ] Implement query history
- [ ] Support auto-complete and syntax highlighting
- [ ] Implement data export (JSON, Excel, SQL)
- [ ] Implement data visualization (charts)

### Priority 5: Infrastructure

- [ ] Complete API documentation (OpenAPI/Swagger)
- [ ] REST API service
- [ ] GraphQL support
- [ ] Database persistence options (PostgreSQL, MySQL)
- [ ] Distributed query support

## Documentation Enhancement TODO

- [ ] Create user manual
- [ ] Create API documentation
- [ ] Create contributor guide
- [ ] Create tutorial videos
- [ ] Translate to other languages
- [ ] Add code examples

## Test Coverage TODO

- [ ] Add boundary case tests
- [ ] Add performance benchmark tests
- [ ] Add stress tests
- [ ] Add security tests (SQL injection, etc.)
- [ ] Add compatibility tests

## Deployment & CI/CD TODO

- [ ] Setup complete GitHub Actions workflow
- [ ] Auto-generate release packages
- [ ] Docker image build and publish
- [ ] Auto-deploy to test environment
- [ ] Setup code quality checks (SonarQube)

## Completed Features

✅ Basic CSV loading & parsing
✅ SELECT with field projection
✅ WHERE condition filtering (basic comparison)
✅ ORDER BY sorting
✅ LIMIT row limiting
✅ Basic aggregation functions (COUNT, SUM, AVG)
✅ CLI interactive interface
✅ Basic error handling
✅ Unit testing framework
✅ Project documentation

## Roadmap

| Phase | Version | Expected Date | Focus |
|-------|---------|---------------|-------|
| Initial Release | v1.0.0 | 2026/06 | Core features complete |
| Bug Fixes | v1.0.1+ | 2026/06 | Known defect fixes |
| Minor Release | v1.1.0 | 2026/07 | Priority 1 features |
| Major Release | v2.0.0 | 2026/09 | Priority 2-3 features |

## Report Issues

Please report bugs through:

1. **GitHub Issues**: https://github.com/Cyanlit/11402_CS351_ProjectB/issues
   - Select "Bug report" template
   - Describe issue, reproduction steps, expected result

2. **Email**: [Contact information]
   - Subject: [BUG] Brief description
   - Attach detailed logs and reproduction case

## Feature Requests

Welcome to submit feature requests:

1. **GitHub Discussions**: https://github.com/Cyanlit/11402_CS351_ProjectB/discussions
   - Label: Feature Request
   - Explain use case and value

2. **GitHub Issues**:
   - Select "Feature request" template
   - Explain why this feature is needed
