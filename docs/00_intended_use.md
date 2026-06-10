# 00 - Intended Use & Scope

## System Use Cases

### Primary Users
- Educators: For demonstrating basic database concepts
- Students: Learning SQL queries, data manipulation, and CLI tool development
- Small-scale data analysts: Processing simple CSV file queries

### Use Scenarios

#### Scenario 1: Load and Query
A user has a CSV file (e.g., student grades table) and wants to:
1. Load the file into the query engine
2. Execute filtered queries (e.g., filter passing students)
3. Sort results (by score in descending order)
4. Retrieve result summaries (count, average, etc.)

#### Scenario 2: CLI Interaction
```bash
$ python main.py
> load data/students.csv
> query SELECT name,score WHERE class=A ORDER BY score DESC LIMIT 5
```

#### Scenario 3: Batch Operations
```bash
$ python main.py << EOF
load data/students.csv
query SELECT * WHERE score > 80
EOF
```

## Scope - In Scope

### Core Features
- ✅ CSV file loading and parsing
- ✅ Automatic schema detection
- ✅ SQL-like query support:
  - SELECT (specify fields or *)
  - WHERE (condition filtering)
  - ORDER BY (sorting)
  - LIMIT (result set size limit)
  - Basic aggregation (COUNT, AVG, SUM)
- ✅ CLI interface
- ✅ Error messaging

### Technical Requirements
- Python 3.8+
- Pandas for data processing
- SQLite for persistent storage
- Unit + Integration testing

## Scope - Out of Scope

### Not Supported in This Version
- ❌ Full SQL compatibility (JOIN, UNION, subqueries, etc.)
- ❌ Multi-user concurrent control
- ❌ Transaction processing
- ❌ Complex aggregation functions (WINDOW functions)
- ❌ Persistent storage beyond CSV (only CSV and SQLite)
- ❌ GUI interface (CLI only)

## Expected Deliverables

### Deliverables
1. Complete source code (modular design)
2. Unit tests + Integration tests
3. Sample CSV data
4. Build and deployment guide
5. API documentation
6. Known limitations documentation

### Non-Functional Requirements
- **Usability**: Intuitive CLI operations, clear error messages
- **Reliability**: Properly handle malformed CSV files
- **Performance**: Support up to 100,000 records
- **Maintainability**: Modular code structure for easy extension
