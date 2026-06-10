# 03 - Software Design Specification (SDS)

## 1. Architecture Overview

The system adopts a layered architecture with the following layers:

```
┌─────────────────────┐
│    CLI Layer       │  (Command-line interface)
├─────────────────────┤
│  Database Layer    │  (Database management)
├─────────────────────┤
│  Query Engine      │  (Query execution)
├─────────────────────┤
│  Parser Layer      │  (Query parsing)
├─────────────────────┤
│  Data Layer        │  (CSV loading & storage)
└─────────────────────┘
```

## 2. Module Design

### 2.1 csv_loader.py
**Responsibility**: Load and parse CSV files

```python
class CSVLoader:
    def load(filepath: str) -> DataFrame
    def detect_delimiter(content: str) -> str
    def infer_types(df: DataFrame) -> DataFrame
```

**Main Functions**:
- Automatic encoding detection
- Delimiter detection
- Type inference

### 2.2 query_parser.py
**Responsibility**: Parse SQL-like query strings

```python
class QueryParser:
    def parse(query_string: str) -> Query
    def validate_syntax(query: Query) -> bool
```

**Return Structure**:
```python
@dataclass
class Query:
    select_cols: List[str]
    where_condition: Optional[Condition]
    order_by: Optional[OrderBy]
    limit: Optional[int]
    offset: Optional[int]
    aggregates: Dict[str, str]
```

### 2.3 query_executor.py
**Responsibility**: Execute parsed queries

```python
class QueryExecutor:
    def execute(query: Query, df: DataFrame) -> DataFrame
    def apply_projection(df: DataFrame, cols: List[str]) -> DataFrame
    def apply_filter(df: DataFrame, condition: Condition) -> DataFrame
    def apply_sort(df: DataFrame, order_by: OrderBy) -> DataFrame
    def apply_aggregation(df: DataFrame, agg_spec: Dict) -> DataFrame
```

### 2.4 database.py
**Responsibility**: Manage database connections and storage

```python
class Database:
    def __init__(sqlite_path: str)
    def load_csv(filepath: str) -> str  # Returns table name
    def save_table(name: str, df: DataFrame)
    def query_table(name: str, query: Query) -> DataFrame
```

### 2.5 cli.py
**Responsibility**: Provide command-line interface

```python
class CLI:
    def run()
    def parse_command(input_str: str) -> Tuple[str, List[str]]
    def execute_load(filepath: str)
    def execute_query(query_str: str)
    def print_help()
```

### 2.6 main.py
**Responsibility**: Program entry point

```python
def main():
    parser = argparse.ArgumentParser()
    # Process command-line arguments
    # Launch CLI or execute single query
```

## 3. Data Flow

### Query Execution Pipeline

```
User Input
    ↓
CLI Command Parsing
    ↓
Query Parser Parsing
    ↓
Schema Validation
    ↓
Query Executor Execution
    ├─ Projection
    ├─ Selection (WHERE)
    ├─ Aggregation
    ├─ Sorting (ORDER BY)
    └─ Limiting (LIMIT)
    ↓
Result Formatting
    ↓
Output to User
```

## 4. Exception Handling Design

### Exception Classification

```python
class CSVException(Exception):
    """CSV-related errors"""
    pass

class QueryParseException(Exception):
    """Query parsing errors"""
    pass

class QueryExecutionException(Exception):
    """Query execution errors"""
    pass

class ValidationException(Exception):
    """Data validation errors"""
    pass
```

### Error Message Standards

| Error Type | Message Format |
|-----------|-----------------|
| File not found | `Error: File not found: {path}` |
| Invalid syntax | `SyntaxError: Invalid query at position {pos}: {detail}` |
| Unknown field | `FieldError: Column '{col}' not found in table` |
| Type mismatch | `TypeError: Cannot compare {type1} with {type2}` |

## 5. Data Structure Design

### CSV Table Representation

```python
@dataclass
class Table:
    name: str
    columns: List[str]
    dtypes: Dict[str, str]
    data: DataFrame
```

### Query Condition Representation

```python
@dataclass
class Condition:
    column: str
    operator: str  # '=', '>', '<', '>=', '<=', '!='
    value: Any
    logic: Optional[str]  # 'AND', 'OR'
    next_condition: Optional['Condition']
```

### Sorting Specification

```python
@dataclass
class OrderBy:
    columns: List[str]
    directions: List[str]  # 'ASC', 'DESC'
```

## 6. File Structure

```
11402_CS351_ProjectB/
├── src/
│   ├── __init__.py
│   ├── csv_loader.py
│   ├── query_parser.py
│   ├── query_executor.py
│   ├── database.py
│   ├── cli.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_csv_loader.py
│   ├── test_query_parser.py
│   ├── test_query_executor.py
│   └── test_integration.py
├── data/
│   ├── sample_students.csv
│   └── ...
├── docs/
│   ├── 00_intended_use.md
│   ├── 01_plan.md
│   ├── 02_SRS.md
│   ├── 03_SDS.md
│   └── ...
├── main.py
├── requirements.txt
└── README.md
```

## 7. Design Decisions

### Decision 1: Data Storage
**Decision**: Prioritize DataFrame (in-memory), optional SQLite (persistent)
**Rationale**: Simplify query logic, avoid ORM complexity

### Decision 2: Query Engine
**Decision**: Hand-implement instead of using SQL parsing libraries
**Rationale**: Learning purposes, complete control, support limited syntax

### Decision 3: Error Handling
**Decision**: Detailed error messages whenever possible
**Rationale**: Improve user experience, facilitate debugging

## 8. Extensibility Considerations

### Potential Improvements
- Support more aggregation functions (MEDIAN, STDDEV)
- Support JOIN operations
- Support data export (CSV, JSON)
- Support data updates (UPDATE, DELETE)
- Support multi-table queries
