---
id: 19c__DBMS_TRANSACTION.COMMIT_COMMENT
name: DBMS_TRANSACTION.COMMIT_COMMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.COMMIT_COMMENT

This procedure is equivalent to the SQL statement: COMMIT COMMENT <text>

## Syntax

```sql
DBMS_TRANSACTION.COMMIT_COMMENT (
   cmnt VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cmnt | VARCHAR2) | IN | Comment to associate with this commit. |

## Usage Notes

Syntax DBMS_TRANSACTION.COMMIT_COMMENT ( cmnt VARCHAR2); Parameters Table 179-2 COMMIT_COMMENT Procedure Parameters Parameter Description cmnt Comment to associate with this commit.