# 11402_CS351_ProjectB
# CSV Mini Database and Query Engine Development

## Problem Description

The objective of this project is to develop a lightweight CSV Mini Database and Query Engine capable of efficiently handling CSV files. The system should support data loading, parsing, and querying operations, enabling users to perform meaningful data analysis without the overhead of a full-featured database management system.

### Key Objectives
- Load and parse CSV files seamlessly
- Support basic CRUD (Create, Read, Update, Delete) operations
- Execute complex queries to filter, sort, and manipulate data
- Provide an intuitive user interface for database interactions
- Ensure efficient data processing and retrieval

### Assumptions
- CSV files are well-formatted with consistent column structures
- Data types can be inferred from the content
- Users have basic familiarity with database query concepts

## Requirements

### Core Implementation
- **CSV File Management**: Load, parse, and manage CSV files with automatic schema detection
- **Query Engine**: Support SELECT, WHERE, ORDER BY, and JOIN operations
- **Data Manipulation**: Implement INSERT, UPDATE, and DELETE operations
- **Performance**: Optimize query execution for datasets up to 100,000 rows

### Function Specifications
The system must:
- Accept CSV file paths and load data into an in-memory or persistent database
- Process user queries and return results in a readable format
- Handle various data types (strings, integers, floats, dates)
- Support filtering, sorting, and aggregation operations
- Maintain data integrity through proper transaction handling

### Testing Requirements
Include comprehensive test cases covering:
- CSV file loading with various formats
- Basic CRUD operations
- Query filtering with multiple conditions
- Data aggregation and sorting
- Error handling for malformed files
- Performance testing with large datasets

### Technology Stack
- **Programming Language**: Python 3.8+
- **Data Processing**: Pandas for data manipulation
- **Database**: SQLite for persistent storage
- **Testing**: pytest for unit and integration tests

## Repository Structure

```
.
├── main.py                        # Entry point and main application
├── test_run.py                    # Manual test runner
├── requirements.txt               # Project dependencies
├── README.md                      # This file
├── tests/                         # Test files and sample data
│   └── sample.csv                 # Sample CSV file for testing
└── docs/                          # Documentation (future)
    ├── design.md                  # System design documentation
    ├── API.md                     # API reference
    └── examples.md                # Usage examples
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Installation
```bash
# Clone the repository
git clone https://github.com/Cyanlit/11402_CS351_ProjectB.git
cd 11402_CS351_ProjectB

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Basic Usage
```bash
# Load a CSV file
load tests/sample.csv

# Execute a query
query SELECT * FROM data WHERE column_name = 'value'

# Exit the application
exit
```

### Running Tests
```bash
# Run all tests
python test_run.py

# Run specific test file
pytest tests/ -v
```

## Usage Examples

### Load CSV File
```
load tests/sample.csv
```

### Query Data
```
query SELECT * FROM data
query SELECT name, age FROM data WHERE age > 18 ORDER BY name
query SELECT COUNT(*) FROM data GROUP BY category
```

### Update Data
```
update SET status = 'active' WHERE id = 5
```

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - Pandas for data manipulation and analysis
  - SQLite for database management
  - pytest for testing

## Project Status
- ✅ Core CSV file loading implemented
- ✅ Basic query engine functionality
- ✅ Sample test data and test suite
- 🔄 Performance optimization in progress
- 🔄 Documentation expansion

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is part of CS351 coursework and is subject to academic integrity guidelines.


