# 04 - Test Plan

## 1. Test Overview

This plan defines the complete testing strategy for the CSV Mini Database & Query Engine, covering unit tests, integration tests, and acceptance tests.

### Test Objectives
- Verify implementation of all functional requirements
- Ensure code quality
- Detect and fix defects
- Ensure regression testing

### Test Scope
- CSV loading and parsing
- Query parsing
- Query execution
- CLI interaction
- Error handling

## 2. Test Types

### 2.1 Unit Tests

#### CSV Loader Unit Tests (test_csv_loader.py)

| Test ID | Test Scenario | Expected Result |
|---------|---------------|-----------------|
| UT-CSV-01 | Load standard CSV file | Correctly parse all rows and columns |
| UT-CSV-02 | Auto-detect encoding | Correctly identify UTF-8 encoding |
| UT-CSV-03 | Auto-detect delimiter | Correctly identify comma, semicolon, tab |
| UT-CSV-04 | Type inference | Correctly infer int, float, string types |
| UT-CSV-05 | Missing file | Raise FileNotFoundError |
| UT-CSV-06 | Malformed CSV | Raise CSVException with error details |
| UT-CSV-07 | Empty CSV file | Correctly handle (return empty DataFrame) |

#### Query Parser Unit Tests (test_query_parser.py)

| Test ID | Test Scenario | Expected Result |
|---------|---------------|-----------------|
| UT-QP-01 | Simple SELECT * | Parse correctly |
| UT-QP-02 | SELECT specific fields | Extract correct field list |
| UT-QP-03 | Single WHERE condition | Parse condition correctly |
| UT-QP-04 | WHERE with AND | Connect multiple conditions |
| UT-QP-05 | WHERE with OR | Connect multiple conditions |
| UT-QP-06 | ORDER BY ASC | Parse sorting correctly |
| UT-QP-07 | ORDER BY DESC | Parse sorting correctly |
| UT-QP-08 | LIMIT clause | Parse limit correctly |
| UT-QP-09 | Complex query | Integrate SELECT+WHERE+ORDER BY+LIMIT |
| UT-QP-10 | Invalid syntax | Raise QueryParseException |
| UT-QP-11 | Unknown field | Show field not found error |
| UT-QP-12 | Aggregation functions | Parse COUNT, SUM, AVG correctly |

#### Query Executor Unit Tests (test_query_executor.py)

| Test ID | Test Scenario | Expected Result |
|---------|---------------|-----------------|
| UT-QE-01 | Projection all fields | Return all fields |
| UT-QE-02 | Projection specific fields | Return specified fields |
| UT-QE-03 | Selection equality | Filter correctly |
| UT-QE-04 | Selection > comparison | Filter correctly |
| UT-QE-05 | Selection < comparison | Filter correctly |
| UT-QE-06 | Selection string match | Filter correctly |
| UT-QE-07 | Sorting ascending | Sort correctly |
| UT-QE-08 | Sorting descending | Sort correctly |
| UT-QE-09 | LIMIT rows | Return correct count |
| UT-QE-10 | COUNT aggregation | Return correct count |
| UT-QE-11 | SUM aggregation | Calculate correctly |
| UT-QE-12 | AVG aggregation | Calculate correctly |
| UT-QE-13 | Empty result set | Return empty DataFrame |

### 2.2 Integration Tests (test_integration.py)

| Test ID | Test Scenario | Expected Result |
|---------|---------------|-----------------|
| IT-01 | Load + simple query | Execute successfully with correct results |
| IT-02 | Load + complex query | SELECT+WHERE+ORDER BY+LIMIT |
| IT-03 | Load + aggregation query | COUNT/SUM/AVG calculations correct |
| IT-04 | Multiple queries | State management correct |
| IT-05 | Load different CSV formats | Handle all formats correctly |
| IT-06 | Large file query | Complete within time limit for 100K records |

### 2.3 Acceptance Tests

See [05_acceptance_tests.md](05_acceptance_tests.md)

## 3. Test Tools & Environment

### Tools
- **Framework**: pytest
- **Coverage**: pytest-cov
- **Mocking**: unittest.mock (if needed)

### Environment
- Python 3.8+
- Pandas, SQLite
- pytest pre-installed

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_csv_loader.py -v

# Show coverage
pytest tests/ --cov=src --cov-report=html
```

## 4. Test Data

### Sample File (data/sample_students.csv)
```csv
name,age,class,score
Alice,18,A,95
Bob,17,B,87
Charlie,18,A,92
David,17,C,78
Eve,18,B,88
```

### Edge Case Test Files
- `empty.csv` - Empty file
- `malformed.csv` - Format errors
- `large.csv` - 100K+ records
- `special_chars.csv` - Special characters

## 5. Defect Classification & Priority

| Priority | Description | Example |
|----------|-------------|---------|
| Critical | Feature completely broken | SELECT returns empty |
| High | Partial dysfunction | WHERE filter incorrect |
| Medium | Insufficient error handling | No message for invalid file |
| Low | Performance or documentation | Slow query |

## 6. Test Pass Criteria

- ✅ All unit tests pass (100%)
- ✅ All integration tests pass
- ✅ Code coverage ≥ 80%
- ✅ All acceptance tests pass
- ✅ No Critical severity defects

## 7. Test Timeline

| Phase | Time | Work |
|-------|------|------|
| Design | Week 1 | Write test plan |
| Development & Testing | Week 2-3 | Test while developing |
| Complete Testing | Week 4 | Run full test suite |
| Regression Testing | Ongoing | Test on every commit |

## 8. CI/CD Integration

### GitHub Actions Workflow
- Automatically run tests on push and PR
- Generate coverage reports
- Send notifications on failures
