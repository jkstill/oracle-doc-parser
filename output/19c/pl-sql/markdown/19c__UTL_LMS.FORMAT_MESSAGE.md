---
id: 19c__UTL_LMS.FORMAT_MESSAGE
name: UTL_LMS.FORMAT_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_LMS
tags: [utl_lms]
source_file: UTL_LMS.html
---

# UTL_LMS.FORMAT_MESSAGE

This function formats a message retrieved by the GET_MESSAGE function and returns the formatted message. If the function fails, then it returns a NULL result.

## Syntax

```sql
UTL_LMS.FORMAT_MESSAGE (
   format IN VARCHAR2 CHARACTER SET ANY_CS,
   args   IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL)
 RETURN VARCHAR2 CHARACTER SET format%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| format | VARCHAR2 | IN | Specifies the string to format |
| args | VARCHAR2 | IN | Specifies the list of arguments |

**Returns:** `VARCHAR2`

## Usage Notes

The following table shows special characters that can be used in the format string. Syntax UTL_LMS.FORMAT_MESSAGE ( format IN VARCHAR2 CHARACTER SET ANY_CS, args IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL) RETURN VARCHAR2 CHARACTER SET format%CHARSET; Parameters Table 268-2 FORMAT_MESSAGE Procedure Parameters Parameter Description format Specifies the string to format args Specifies the list of arguments Examples DECLARE s varchar2(200); i pls_integer; BEGIN i:= utl_lms.get_message(26052, 'rdbms', 'ora', 'french', s); dbms_output.put_line('before format, message is: '||s); dbms_output.put_line('formatted message is: '||utl_lms.format_message(s, 9, 'my_column_name'); END; / The following is an unformatted message: Type %d non pris en charge pour l'expression SQL sur la colonne %s. The following is the formatted message: Type 9 non pris en charge pour l'expression SQL sur la colonne my_column_name.