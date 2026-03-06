---
id: 19c__DBMS_STAT_FUNCS.POISSON_DIST_FIT
name: DBMS_STAT_FUNCS.POISSON_DIST_FIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STAT_FUNCS
tags: [dbms_stat_funcs]
source_file: DBMS_STAT_FUNCS.html
---

# DBMS_STAT_FUNCS.POISSON_DIST_FIT

This procedure tests how well a sample of values fits a Poisson distribution.

## Syntax

```sql
DBMS_STAT_FUNCS.POISSON_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   test_type    IN    VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV',
   lambda       IN    NUMBER,
   sig          OUT   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownername | VARCHAR2 | IN | The schema where the table resides. |
| tablename | VARCHAR2 | IN | The table where the column resides. |
| columnname | VARCHAR2 | IN | The column of the table against which to run the test. |
| test_type | VARCHAR2 | IN | The type of test to use: ' KOLMOGOROV_SMIRNOV' or ' ANDERSON_DARLING' . |
| lambda | NUMBER | IN | The lambda parameter is the shape parameter. |
| sig | NUMBER) | OUT | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the Poisson distribution. A number close to 1 indicates a close match. |

## Usage Notes

Syntax DBMS_STAT_FUNCS.POISSON_DIST_FIT ( ownername IN VARCHAR2, tablename IN VARCHAR2, columnname IN VARCHAR2, test_type IN VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV', lambda IN NUMBER, sig OUT NUMBER); Parameters Table 170-4 POISSON_DIST_FIT Procedure Parameters Parameter Description ownername The schema where the table resides. tablename The table where the column resides. columnname The column of the table against which to run the test. test_type The type of test to use: ' KOLMOGOROV_SMIRNOV' or ' ANDERSON_DARLING' . lambda The lambda parameter is the shape parameter. sig The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the Poisson distribution. A number close to 1 indicates a close match.