---
id: 19c__DBMS_METADATA_DIFF.ADD_DOCUMENT
name: DBMS_METADATA_DIFF.ADD_DOCUMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA_DIFF
tags: [dbms_metadata_diff]
source_file: DBMS_METADATA_DIFF.html
---

# DBMS_METADATA_DIFF.ADD_DOCUMENT

This procedure specifies an SXML document that is to be compared.

## Syntax

```sql
DBMS_METADATA_DIFF.ADD_DOCUMENT(
handle IN NUMBER, document IN sys.XMLType);

DBMS_METADATA_DIFF.ADD_DOCUMENT(
handle IN NUMBER, document IN CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle returned from OPENC |
| document | sys.XMLType) | IN | A document to be compared. The document must be of the type specified in OPENC . |

## Usage Notes

Syntax DBMS_METADATA_DIFF.ADD_DOCUMENT( handle IN NUMBER, document IN sys.XMLType); DBMS_METADATA_DIFF.ADD_DOCUMENT( handle IN NUMBER, document IN CLOB); Parameters Table 108-4 ADD_DOCUMENT Procedure Parameters Parameter Description handle The handle returned from OPENC document A document to be compared. The document must be of the type specified in OPENC . Usage Notes Because the comparison interface allows you to compare exactly two SXML documents, a program must call ADD_DOCUMENT exactly twice for each OPENC handle. In the comparison result, the document specified by the first call is document 1, and the document specified by the second call is document 2. Exceptions INVALID_ARGVAL A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter.