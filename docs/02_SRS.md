# 02 - Software Requirements Specification (SRS)

## 1. Introduction

This document defines the complete software requirements for the CSV Mini Database & Query Engine. The system is a lightweight query engine for performing SQL-like operations on CSV files.

## 2. System Overview

### 2.1 Objectives
Provide a simple yet functional platform that enables users to:
- Load CSV files
- Query data using SQL-like syntax
- Obtain structured result outputs

### 2.2 Key Features
- Automatic CSV file parsing
- SQL-like query support
- Command-line interface
- Comprehensive error messaging

## 3. Functional Requirements

### 3.1 FR-1: CSV File Loading
**Description**: System must load and parse CSV files.

**Details**:
- Support UTF-8 encoding
- Auto-detect delimiters (comma, semicolon, tab)
- Recognize first row as header
- Auto-infer field data types

**Acceptance Criteria**:
- Successfully load standard format CSV files
- Correctly parse various encodings
- Provide clear error messages for format errors

### 3.2 FR-2: SELECT Operation
**Description**: System must support SELECT statements.

**Syntax**:
```
SELECT column1, column2, ... [WHERE ...] [ORDER BY ...] [LIMIT ...]
```
- Support specifying fields or `*` (all fields)
- Support field aliases (optional)

**Acceptance Criteria**:
- `SELECT *` returns all fields
- `SELECT col1,col2` returns specified fields
- Invalid field names raise errors

### 3.3 FR-3: WHERE Clause
**Description**: System must support condition filtering.

**Syntax**:
```
WHERE column = value [AND/OR condition]*
```
- Support `=`, `>`, `<`, `>=`, `<=`, `!=` operators
- Support AND, OR logic
- Support string, numeric, and date comparisons

**Acceptance Criteria**:
- Correctly filter rows matching conditions
- Return empty result set for non-matching conditions

### 3.4 FR-4: ORDER BY Clause
**Description**: System must support sorting functionality.

**Syntax**:
```
ORDER BY column [ASC|DESC] [, column2 ...]
```
- Support ascending (ASC) and descending (DESC)
- Support multi-field sorting
- Default to ascending

**Acceptance Criteria**:
- Correctly sort by specified field
- Proper descending order

### 3.5 FR-5: LIMIT Clause
**Description**: System must support result set size limitation.

**Syntax**:
```
LIMIT count [OFFSET offset]
```
- Limit returned row count
- Support offset

**Acceptance Criteria**:
- Correctly limit returned rows
- Proper offset handling

### 3.6 FR-6: Aggregation Functions
**Description**: System must support basic aggregation operations.

**Syntax**:
```
SELECT COUNT(*), SUM(column), AVG(column), MIN(column), MAX(column)
```

**Acceptance Criteria**:
- COUNT(*) returns correct row count
- SUM, AVG calculations are correct
- Empty set returns NULL or 0

### 3.7 FR-7: Command-Line Interface
**Description**: System must provide interactive CLI.

**Commands**:
- `load <filename>` - Load CSV file
- `query <query_string>` - Execute query
- `help` - Display help
- `exit` - Exit program

**Acceptance Criteria**:
- Commands execute correctly
- Invalid commands show error messages

## 4. Non-Functional Requirements

### 4.1 NFR-1: Performance
- Process up to 100,000 records
- Query execution time < 1 second (100K records)
- Memory usage < 500MB

### 4.2 NFR-2: Reliability
- Correctly handle malformed CSV files
- Provide meaningful error messages for all exceptions
- Graceful degradation (no crashes)

### 4.3 NFR-3: Usability
- Clear command help text
- Intuitive error messages
- Support Windows / macOS / Linux

### 4.4 NFR-4: Maintainability
- Modular code structure for easy extension
- Sufficient documentation and comments
- Automated test coverage

## 5. Interface Requirements

### 5.1 Command-Line Parameters
```bash
python main.py [--csv FILE] [--query QUERY]
```

### 5.2 Output Format
- Table format (using tabulate or similar library)
- JSON format (optional)

## 6. Constraints

- Use Python 3.8+
- Use Pandas, SQLite libraries
- No external GUI dependencies
- Open source license

## 7. Assumptions & Dependencies

### Assumptions
- CSV files are well-formed
- Users are familiar with basic SQL concepts
- NULL value handling is optional

### Dependencies
- Python standard library
- Pandas library
- SQLite driver
- pytest (testing)

## 8. Conflicts & Priorities

| Feature | Priority |
|---------|----------|
| CSV loading + SELECT | MUST |
| WHERE + ORDER BY | MUST |
| LIMIT | SHOULD |
| Aggregation | SHOULD |
| Complex joins | COULD |
