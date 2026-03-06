---
id: 19c__DBMS_DDL.WRAP
name: DBMS_DDL.WRAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.WRAP

This function takes as input a single CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body and returns a CREATE OR REPLACE statement where the text of the PL/SQL unit has been obfuscated.

## Syntax

```sql
DBMS_DDL.WRAP(
   ddl      VARCHAR2) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ddl | VARCHAR2) | IN | A CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body |
| lb |  |  | Lower bound for indices in the string table that specify the CREATE OR REPLACE statement |
| ub |  |  | Upper bound for indices in the string table that specify the CREATE OR REPLACE statement. |

**Returns:** `VARCHAR2`

## Usage Notes

The function has 3 overloads to allow for the different ways in which DDL statements can be generated dynamically and presented to DBMS_SQL or EXECUTE IMMEDIATE . The different functionality of each form of syntax is presented with the definition. See Also: CREATE_WRAPPED Procedures See Also: CREATE_WRAPPED Procedures Syntax Provides basic functionality: DBMS_DDL.WRAP( ddl VARCHAR2) RETURN VARCHAR2; Provides the same functionality as the first form, but allows for larger inputs. This function is intended to be used with the PARSE Procedures in the DBMS_SQL package and its argument list follows the convention of DBMS_SQL.PARSE: DBMS_DDL.WRAP( ddl DBMS_SQL.VARCHAR2S, lb PLS_INTEGER, ub PLS_INTEGER) RETURN DBMS_SQL.VARCHAR2S; Provides the same functionality as the second form and is provided for compatibility with multiple forms of the PARSE Procedures in the DBMS_SQL package: DBMS_DDL.WRAP( ddl DBMS_SQL.VARCHAR2A, lb PLS_INTEGER, ub PLS_INTEGER) RETURN DBMS_SQL.VARCHAR2A; Parameters Table 56-9 WRAP Function Parameters Parameter Description ddl A CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body lb Lower bound for indices in the string table that specify the CREATE OR REPLACE statement ub Upper bound for indices in the string table that specify the CREATE OR REPLACE statement. Return Values A CREATE OR REPLACE statement with the text obfuscated. In the case of the second and third form, the return value is a table of strings that need to be concatenated in order to construct the CREATE OR REPLACE string containing obfuscated source text.