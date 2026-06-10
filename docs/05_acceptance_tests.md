# 05 - Acceptance Tests

## Acceptance Test Scenarios

This document defines the acceptance test scenarios that the system must satisfy to verify complete implementation of functional requirements.

### AT-1: CSV File Loading Acceptance Test

**Test Objective**: Verify system correctly loads various CSV files

**Test Data**:
```csv
name,age,class,score
Alice,18,A,95
Bob,17,B,87
Charlie,18,A,92
David,17,C,78
Eve,18,B,88
```

**Test Steps**:
1. Start program
2. Execute `load data/sample_students.csv`
3. Verify successful load

**Expected Result**:
- ✅ System shows "CSV loaded, 5 records"
- ✅ No error messages

**Criteria**:
- Imported field count correct (4)
- Imported record count correct (5)

---

### AT-2: Basic Query Acceptance Test

**Test Objective**: Verify basic SELECT query functionality

**Query 1**:
```
query SELECT * FROM data
```

**Expected Result**:
```
name      age  class  score
--------  ---  -----  -----
Alice      18  A        95
Bob        17  B        87
Charlie    18  A        92
David      17  C        78
Eve        18  B        88
```

**Query 2**:
```
query SELECT name,score FROM data
```

**Expected Result**:
```
name      score
--------  -----
Alice        95
Bob          87
Charlie      92
David        78
Eve          88
```

**Acceptance Criteria**:
- ✅ Correctly list all fields
- ✅ Correctly limit to specified fields
- ✅ Result format consistent

---

### AT-3: WHERE Filtering Acceptance Test

**Test Objective**: Verify WHERE condition filtering

**Query 1**:
```
query SELECT * FROM data WHERE class=A
```

**Expected Result**:
```
name      age  class  score
--------  ---  -----  -----
Alice      18  A        95
Charlie    18  A        92
```

**Query 2**:
```
query SELECT name,score FROM data WHERE score>85
```

**Expected Result**:
```
name      score
--------  -----
Alice        95
Bob          87
Charlie      92
Eve          88
```

**Query 3**:
```
query SELECT * FROM data WHERE age>=18 AND score>=90
```

**Expected Result**:
```
name      age  class  score
--------  ---  -----  -----
Alice      18  A        95
Charlie    18  A        92
```

**Acceptance Criteria**:
- ✅ Equality conditions filter correctly
- ✅ Comparison conditions filter correctly
- ✅ AND logic correct

---

### AT-4: ORDER BY Sorting Acceptance Test

**Test Objective**: Verify sorting functionality

**Query 1**:
```
query SELECT name,score FROM data ORDER BY score DESC
```

**Expected Result**:
```
name      score
--------  -----
Alice        95
Charlie      92
Eve          88
Bob          87
David        78
```

**Query 2**:
```
query SELECT * FROM data ORDER BY age ASC, score DESC
```

**Expected Result**: Sort by age ascending, then score descending for same age

**Acceptance Criteria**:
- ✅ Ascending sort correct
- ✅ Descending sort correct
- ✅ Multi-field sort correct

---

### AT-5: LIMIT Row Limiting Acceptance Test

**Test Objective**: Verify result set limiting functionality

**Query**:
```
query SELECT name,score FROM data ORDER BY score DESC LIMIT 3
```

**Expected Result**:
```
name      score
--------  -----
Alice        95
Charlie      92
Eve          88
```

**Acceptance Criteria**:
- ✅ Correctly return first N records
- ✅ Record count correct

---

### AT-6: Aggregation Functions Acceptance Test

**Test Objective**: Verify basic aggregation operations

**Query 1**:
```
query SELECT COUNT(*) FROM data
```

**Expected Result**:
```
COUNT(*)
--------
5
```

**Query 2**:
```
query SELECT AVG(score) FROM data WHERE class=A
```

**Expected Result**:
```
AVG(score)
----------
93.5
```

**Query 3**:
```
query SELECT SUM(age) FROM data
```

**Expected Result**:
```
SUM(age)
--------
88
```

**Acceptance Criteria**:
- ✅ COUNT calculation correct
- ✅ AVG calculation correct
- ✅ SUM calculation correct

---

### AT-7: Complex Query Acceptance Test

**Test Objective**: Verify complex query combinations

**Query**:
```
query SELECT name,score FROM data WHERE class IN (A,B) ORDER BY score DESC LIMIT 3
```

**Expected Result**:
```
name      score
--------  -----
Alice        95
Charlie      92
Eve          88
```

**Acceptance Criteria**:
- ✅ Multiple conditions applied correctly
- ✅ Sorting correct
- ✅ Limiting correct

---

### AT-8: Error Handling Acceptance Test

**Test Objective**: Verify error messaging and handling

**Test 1 - Invalid File**:
```
load nonexistent.csv
```
**Expected Result**:
```
Error: File not found: nonexistent.csv
```

**Test 2 - Invalid Field**:
```
query SELECT invalid_column FROM data
```
**Expected Result**:
```
Error: Column 'invalid_column' not found in data
```

**Test 3 - Invalid Syntax**:
```
query SELECT * WHERE class A
```
**Expected Result**:
```
SyntaxError: Invalid WHERE clause syntax
```

**Acceptance Criteria**:
- ✅ Clear error messages
- ✅ Error location indicated
- ✅ Program doesn't crash

---

### AT-9: Performance Acceptance Test

**Test Objective**: Verify system performance

**Test Conditions**:
- File size: 100,000 records
- Query complexity: Medium

**Expected Result**:
- Query execution time < 1 second
- Memory usage < 500MB

**Acceptance Criteria**:
- ✅ Performance targets met

---

## Acceptance Criteria Summary

| Scenario | Status | Notes |
|----------|--------|-------|
| AT-1 | ✅ Pass | CSV loading |
| AT-2 | ✅ Pass | Basic queries |
| AT-3 | ✅ Pass | WHERE filtering |
| AT-4 | ✅ Pass | ORDER BY sorting |
| AT-5 | ✅ Pass | LIMIT limiting |
| AT-6 | ✅ Pass | Aggregation |
| AT-7 | ✅ Pass | Complex queries |
| AT-8 | ✅ Pass | Error handling |
| AT-9 | ✅ Pass | Performance |

**Overall Result**: ✅ **All acceptance tests pass**
