---
id: 19c__UTL_LMS.GET_MESSAGE
name: UTL_LMS.GET_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_LMS
tags: [utl_lms]
source_file: UTL_LMS.html
---

# UTL_LMS.GET_MESSAGE

This function retrieves an Oracle error message. The user can define user-specific error messages with the lmsgen utility.

## Syntax

```sql
UTL_LMS.GET_MESSAGE (
   errnum    IN PLS_INTEGER,
   product   IN VARCHAR2,
   facility  IN VARCHAR2,
   language  IN VARCHAR2,
   message   OUT NOCOPY VARCHAR2CHARCTER SET ANY_CS)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| errnum | PLS_INTEGER | IN | Specifies the error number. Example: '972' (for ORA-00972) |
| product | VARCHAR2 | IN | Specifies the product to which the error message applies Example: ' rdbms ' |
| facility | VARCHAR2 | IN | Specifies the error message prefix Example: 'ora' |
| language | VARCHAR2 | IN | Specifies the language of the message. The parameter is case-insensitive. The default is NULL , which causes GET_MESSAGE to use the value of the NLS_LANGUAGE session parameter. |
| message | NOCOPY | OUT | Specifies the output buffer for the retrieved message |

**Returns:** `PLS_INTEGER`

## Usage Notes

It returns 0 when it is successful. It returns -1 when it fails. See Also: Oracle Database Globalization Support Guide for more information about the lmsgen utility See Also: Oracle Database Globalization Support Guide for more information about the lmsgen utility Syntax UTL_LMS.GET_MESSAGE ( errnum IN PLS_INTEGER, product IN VARCHAR2, facility IN VARCHAR2, language IN VARCHAR2, message OUT NOCOPY VARCHAR2CHARCTER SET ANY_CS) RETURN PLS_INTEGER; Parameters Table 268-3 GET_MESSAGE Function Parameters Parameter Description errnum Specifies the error number. Example: '972' (for ORA-00972) product Specifies the product to which the error message applies Example: ' rdbms ' facility Specifies the error message prefix Example: 'ora' language Specifies the language of the message. The parameter is case-insensitive. The default is NULL , which causes GET_MESSAGE to use the value of the NLS_LANGUAGE session parameter. message Specifies the output buffer for the retrieved message Usage Notes If the language parameter is set to NULL , then the value of the NLS_LANGUAGE session parameter is used as the default.