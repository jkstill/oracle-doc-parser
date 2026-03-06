---
id: 19c__DBMS_DDL.CREATE_WRAPPED
name: DBMS_DDL.CREATE_WRAPPED
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.CREATE_WRAPPED

The procedure takes as input a single CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body. It then generates a CREATE OR REPLACE statement with the PL/SQL source text obfuscated and executes the generated statement. In effect, this procedure bundles together the operations of wrapping the text and creating the PL/SQL unit.

## Syntax

```sql
DBMS_DDL.CREATE_WRAPPED (
   ddl     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ddl | VARCHAR2) | IN | A CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body |
| lb |  |  | Lower bound for indices in the string table that specify the CREATE OR REPLACE statement |
| ub |  |  | Upper bound for indices in the string table that specify the CREATE OR REPLACE statement. |

## Usage Notes

See Also: WRAP Functions This procedure has 3 overloads. Each of the three functions provides better performance than using a combination of individual WRAP Functions and DBMS_SQL.PARSE (or EXECUTE IMMEDIATE ) calls. The different functionality of each form of syntax is presented with the definition. See Also: WRAP Functions Syntax Is a shortcut for EXECUTE IMMEDIATE SYS.DBMS_DDL . WRAP ( ddl ): DBMS_DDL.CREATE_WRAPPED ( ddl VARCHAR2); Is a shortcut for DBMS_SQL . PARSE ( cursor , SYS . DBMS_DDL . WRAP ( input , lb , ub )): DBMS_DDL.CREATE_WRAPPED( ddl DBMS_SQL.VARCHAR2A, lb PLS_INTEGER, ub PLS_INTEGER); Is a shortcut for DBMS_SQL . PARSE ( cursor , SYS . DBMS_DDL . WRAP ( input , lb , ub )): DBMS_DDL.CREATE_WRAPPED( ddl DBMS_SQL.VARCHAR2S, lb PLS_INTEGER, ub PLS_INTEGER); Parameters Table 56-6 CREATE_WRAPPED Procedure Parameters Parameter Description ddl A CREATE OR REPLACE statement that specifies creation of a PL/SQL package specification, package body, function, procedure, type specification or type body lb Lower bound for indices in the string table that specify the CREATE OR REPLACE statement ub Upper bound for indices in the string table that specify the CREATE OR REPLACE statement. Usage Notes The CREATE OR REPLACE statement is executed with the privileges of the user invoking DBMS_DDL . CREATE_WRAPPED . Any PL/SQL code that attempts to call these interfaces should use the fully qualified package name SYS . DBMS_DDL to avoid the possibility that the name DBMS_DDL is captured by a locally-defined unit or by redefining the DBMS_DDL public synonym. Each invocation of any accepts only a single PL/SQL unit. By contrast, the PL/SQL wrap utility accepts a entire SQL*Plus file and obfuscates the PL/SQL units within the file leaving all other text as-is. These interfaces are intended to be used in conjunction with or as a replacement for PL/SQL's dynamic SQL interfaces ( EXECUTE IMMEDIATE and DBMS_SQL . PARSE ). Since these dynamic SQL interfaces only accept a single unit at a time (and do not understand the SQL*Plus " / " termination character), both the CREATE_WRAPPED Procedures and the WRAP Functions require input to be a single unit.