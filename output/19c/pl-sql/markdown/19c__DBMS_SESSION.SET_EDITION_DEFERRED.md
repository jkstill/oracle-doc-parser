---
id: 19c__DBMS_SESSION.SET_EDITION_DEFERRED
name: DBMS_SESSION.SET_EDITION_DEFERRED
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_EDITION_DEFERRED

This procedure requests a switch to the specified edition. The switch takes effect at the end of the current client call.

## Syntax

```sql
DBMS_SESSION.SET_EDITION_DEFERRED (
   edition    IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| edition | VARCHAR2) | IN | Name of the edition to which to switch. The contents of the string are processed as a SQL identifier; double quotation marks must surround the remainder of the string if special characters or lower case characters are present in the edition's actual name and, if double quotation marks are not used, the contents are set in uppercase. The caller must have USE privilege on the named edition. |

## Usage Notes

Syntax DBMS_SESSION.SET_EDITION_DEFERRED ( edition IN VARCHAR2); Parameters Table 154-19 SET_EDITION_DEFERRED Procedure Parameters Parameter Description edition Name of the edition to which to switch. The contents of the string are processed as a SQL identifier; double quotation marks must surround the remainder of the string if special characters or lower case characters are present in the edition's actual name and, if double quotation marks are not used, the contents are set in uppercase. The caller must have USE privilege on the named edition.