---
id: 19c__UTL_I18N.STRING_TO_RAW
name: UTL_I18N.STRING_TO_RAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.STRING_TO_RAW

This function converts a VARCHAR2 or NVARCHAR2 string to another valid Oracle character set and returns the result as RAW data.

## Syntax

```sql
UTL_I18N.STRING_TO_RAW( 
   data          IN VARCHAR2 CHARACTER SET ANY_CS,
   dst_charset   IN VARCHAR2 DEFAULT NULL)
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data | VARCHAR2 | IN | Specifies the VARCHAR2 or NVARCHAR2 string to convert. |
| dst_charset | VARCHAR2 | IN | Specifies the destination character set. If dst_charset is NULL , then the database character set is used for CHAR data and the national character set is used for NCHAR data. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_I18N.STRING_TO_RAW( data IN VARCHAR2 CHARACTER SET ANY_CS, dst_charset IN VARCHAR2 DEFAULT NULL) RETURN RAW; Parameters Table 265-21 STRING_TO_RAW Function Parameters Parameter Description data Specifies the VARCHAR2 or NVARCHAR2 string to convert. dst_charset Specifies the destination character set. If dst_charset is NULL , then the database character set is used for CHAR data and the national character set is used for NCHAR data. Usage Notes If the user specifies an invalid character set, a NULL string, or a string whose length is 0, then the function returns a NULL string. Examples DECLARE r raw(50); s varchar2(20); BEGIN s:='abcdef'||chr(170); r:=utl_i18n.string_to_raw(s,'utf8'); dbms_output.put_line(rawtohex(r)); end; / This returns a hex value of '616263646566C2AA' .