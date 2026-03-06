---
id: 19c__LOGICAL.COMMON
name: LOGICAL.COMMON
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: LOGICAL
tags: [logical]
source_file: Logical-Change-Record-TYPEs.html
---

# LOGICAL.COMMON

These functions and procedures are common to both the LCR$_DDL_RECORD and LCR$_ROW_RECORD type.

## Syntax

```sql
MEMBER FUNCTION GET_COMMAND_TYPE() 
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| position |  |  | The position You can obtain the position by using the GET_POSITION member function or by querying the DBA_XSTREAM_OUTBOUND_PROGRESS data dictionary view. |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: For descriptions of the subprograms for these types that are exclusive to each type: " LCR$_DDL_RECORD Type " " LCR$_ROW_RECORD Type " See Also: For descriptions of the subprograms for these types that are exclusive to each type: " LCR$_DDL_RECORD Type " " LCR$_ROW_RECORD Type " GET_COMMAND_TYPE Member Function Gets the command type of the LCR. See Also: The "SQL Command Codes" table in the Oracle Call Interface Programmer's Guide for a complete list of command types See Also: The "SQL Command Codes" table in the Oracle Call Interface Programmer's Guide for a complete list of command types Syntax MEMBER FUNCTION GET_COMMAND_TYPE() RETURN VARCHAR2;