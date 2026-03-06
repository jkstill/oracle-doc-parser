---
id: 19c__DBMS_METADATA.PUT
name: DBMS_METADATA.PUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA
tags: [dbms_metadata]
source_file: DBMS_METADATA.html
---

# DBMS_METADATA.PUT

This function submits an XML document containing object metadata to the database to create the object.

## Syntax

```sql
DBMS_METADATA.PUT (
   handle     IN             NUMBER,
   document   IN             sys.XMLType,
   flags      IN             NUMBER,
   results    IN OUT NOCOPY  sys.ku$_SubmitResults)
  RETURN BOOLEAN;

DBMS_METADATA.PUT (
   handle     IN             NUMBER,
   document   IN             CLOB,
   flags      IN             NUMBER,
   results    IN OUT NOCOPY  sys.ku$_SubmitResults)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle returned from OPENW . |
| document | sys.XMLType | IN | The XML document containing object metadata for the type of the OPENW handle. |
| flags | NUMBER | IN | Reserved for future use |
| results | NOCOPY | IN OUT | Detailed results of the operation. |

**Returns:** `BOOLEAN`

## Usage Notes

See Also: For more information about related subprograms: Subprograms for Submitting XML to the Database See Also: For more information about related subprograms: Subprograms for Submitting XML to the Database Syntax DBMS_METADATA.PUT ( handle IN NUMBER, document IN sys.XMLType, flags IN NUMBER, results IN OUT NOCOPY sys.ku$_SubmitResults) RETURN BOOLEAN; DBMS_METADATA.PUT ( handle IN NUMBER, document IN CLOB, flags IN NUMBER, results IN OUT NOCOPY sys.ku$_SubmitResults) RETURN BOOLEAN; Parameters Table 107-15 PUT Function Parameters Parameter Description handle The handle returned from OPENW . document The XML document containing object metadata for the type of the OPENW handle. flags Reserved for future use results Detailed results of the operation. Return Values TRUE if all SQL operations succeeded; FALSE if there were any errors.