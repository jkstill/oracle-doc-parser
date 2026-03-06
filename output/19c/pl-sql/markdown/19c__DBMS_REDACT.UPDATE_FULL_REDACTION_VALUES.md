---
id: 19c__DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES
name: DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES

This procedure modifies the default displayed values for a Data Redaction policy for full redaction.

## Syntax

```sql
DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES (
   number_val       IN NUMBER                    :=  NULL,
   binfloat_val     IN BINARY_FLOAT              :=  NULL,
   bindouble_val    IN BINARY_DOUBLE             :=  NULL,
   char_val         IN CHAR                      :=  NULL,
   varchar_val      IN VARCHAR2                  :=  NULL,
   nchar_val        IN NCHAR                     :=  NULL,
   nvarchar_val     IN NVARCHAR2                 :=  NULL,
   date_val         IN DATE                      :=  NULL,
   ts_val           IN TIMESTAMP                 :=  NULL,
   tswtz_val        IN TIMESTAMP WITH TIME ZONE  :=  NULL,
   blob_val         IN BLOB                      :=  NULL,
   clob_val         IN CLOB                      :=  NULL,
   nclob_val        IN NCLOB                     NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| number_val | NUMBER | IN | Modifies the default value for columns of the NUMBER datatype |
| binfloat_val | BINARY_FLOAT | IN | Modifies the default value for columns of the BINARY_FLOAT datatype |
| bindouble_val | BINARY_DOUBLE | IN | Modifies the default value for columns of the BINARY_DOUBLE datatype |
| char_val | CHAR | IN | Modifies the default value for columns of the CHAR datatype |
| varchar_val | VARCHAR2 | IN | Modifies the default value for columns of the VARCHAR2 datatype |
| nchar_val | NCHAR | IN | Modifies the default value for columns of the NCHAR datatype |
| nvarchar_val | NVARCHAR2 | IN | Modifies the default value for columns of the NVARCHAR2 datatype |
| date |  |  | Modifies the default value for columns of the DATE datatype |
| ts_val | TIMESTAMP | IN | Modifies the default value for columns of the TIMESTAMP datatype |
| tswtz_val | TIMESTAMP | IN | Modifies the default value for columns of the TIMESTAMP WITH TIME ZONE datatype |
| blob_val | BLOB | IN | Modifies the default value for columns of the BLOB datatype |
| clob_val | CLOB | IN | Modifies the default value for columns of the CLOB datatype |
| nclob_val | NCLOB | IN | Modifies the default value for columns of the NCLOB datatype |

## Usage Notes

Syntax DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES ( number_val IN NUMBER := NULL, binfloat_val IN BINARY_FLOAT := NULL, bindouble_val IN BINARY_DOUBLE := NULL, char_val IN CHAR := NULL, varchar_val IN VARCHAR2 := NULL, nchar_val IN NCHAR := NULL, nvarchar_val IN NVARCHAR2 := NULL, date_val IN DATE := NULL, ts_val IN TIMESTAMP := NULL, tswtz_val IN TIMESTAMP WITH TIME ZONE := NULL, blob_val IN BLOB := NULL, clob_val IN CLOB := NULL, nclob_val IN NCLOB NULL); Parameters Table 137-14 UPDATE_FULL_REDACTION_VALUES Procedure Parameters Parameter Description number_val Modifies the default value for columns of the NUMBER datatype binfloat_val Modifies the default value for columns of the BINARY_FLOAT datatype bindouble_val Modifies the default value for columns of the BINARY_DOUBLE datatype char_val Modifies the default value for columns of the CHAR datatype varchar_val Modifies the default value for columns of the VARCHAR2 datatype nchar_val Modifies the default value for columns of the NCHAR datatype nvarchar_val Modifies the default value for columns of the NVARCHAR2 datatype date Modifies the default value for columns of the DATE datatype ts_val Modifies the default value for columns of the TIMESTAMP datatype tswtz_val Modifies the default value for columns of the TIMESTAMP WITH TIME ZONE datatype blob_val Modifies the default value for columns of the BLOB datatype clob_val Modifies the default value for columns of the CLOB datatype nclob_val Modifies the default value for columns of the NCLOB datatype Exceptions ORA-28082 - The parameter parameter is invalid (where the possible values are char_val , nchar_val , varchar_val and nvarchar_val )