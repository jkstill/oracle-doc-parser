---
id: 19c__UTL_I18N.RAW_TO_NCHAR
name: UTL_I18N.RAW_TO_NCHAR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.RAW_TO_NCHAR

This function converts RAW data from a valid Oracle character set to an NVARCHAR2 string in the national character set.

## Syntax

```sql
UTL_I18N.RAW_TO_NCHAR ( 
   data         IN RAW,
   src_charset  IN VARCHAR2 DEFAULT NULL)
 RETURN NVARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data | RAW | IN | Specifies the RAW data to be converted to an NVARCHAR2 string |
| src_charset | VARCHAR2 | IN | Specifies the character set that the RAW data was derived from. If src_charset is NULL , then the database character set is used. |
| scanned_length |  |  | Specifies the number of bytes of source data scanned |
| shift_status |  |  | Specifies the shift status at the end of the scan. The user must set it to SHIFT_IN the first time it is called in piecewise conversion. Note: ISO 2022 character sets use escape sequences instead of shift characters to indicate the encoding method. shift_status cannot hold the encoding method information that is provided by the escape sequences for the next function call. As a result, this function cannot be used to reconstruct ISO 2022 character from raw data in a piecewise way unless each unit of input can be guaranteed to be a closed string. A closed string begins and ends in a 7-bit escape state. |

**Returns:** `NVARCHAR2`

## Usage Notes

The function is overloaded. The different forms of functionality are described along with the syntax declarations. Syntax Buffer Conversion: UTL_I18N.RAW_TO_NCHAR ( data IN RAW, src_charset IN VARCHAR2 DEFAULT NULL) RETURN NVARCHAR2; Piecewise conversion converts raw data into character data piece by piece: UTL_I18N.RAW_TO_NCHAR ( data IN RAW, src_charset IN VARCHAR2 DEFAULT NULL, scanned_length OUT PLS_INTEGER, shift_status IN OUT PLS_INTEGER) RETURN NVARCHAR2; Parameters Table 265-20 RAW_TO_NCHAR Function Parameters Parameter Description data Specifies the RAW data to be converted to an NVARCHAR2 string src_charset Specifies the character set that the RAW data was derived from. If src_charset is NULL , then the database character set is used. scanned_length Specifies the number of bytes of source data scanned shift_status Specifies the shift status at the end of the scan. The user must set it to SHIFT_IN the first time it is called in piecewise conversion. Note: ISO 2022 character sets use escape sequences instead of shift characters to indicate the encoding method. shift_status cannot hold the encoding method information that is provided by the escape sequences for the next function call. As a result, this function cannot be used to reconstruct ISO 2022 character from raw data in a piecewise way unless each unit of input can be guaranteed to be a closed string. A closed string begins and ends in a 7-bit escape state. Usage Notes If the user specifies an invalid character set, NULL data, or data whose length is 0, then the function returns a NULL string. Examples Buffer Conversion UTL_I18N.RAW_TO_NCHAR(hextoraw('616263646566C2AA'),'utf8') This returns the following string in the national character set: 'abcde'||chr(170) Piecewise Conversion UTL_I18N.RAW_TO_NCHAR(hextoraw('616263646566C2AA'),'utf8', shf, slen) This expression returns the following string in the national character set: 'abcde'||chr(170) It also sets shf to SHIFT_IN and slen to 8 . The following example converts data from the Internet piece by piece to the national character set. rvalue RAW(1050); nvalue NVARCHAR2(1024); converstion_state PLS_INTEGER = 0; converted_len PLS_INTEGER; rtemp RAW(10) = ''; conn utl_tcp.connection; tlen PLS_INTEGER; ... conn := utl_tcp.open_connection ( remote_host => 'localhost', remote_port => 2000); LOOP tlen := utl_tcp.read_raw(conn, rvalue, 1024); rvalue := utl_raw.concat(rtemp, rvalue); nvalue := utl_i18n.raw_to_nchar(rvalue, 'JA16SJIS', converted_len, conversion_stat); if (converted_len < utl_raw.length(rvalue) ) then rtemp := utl_raw.substr(rvalue, converted_len+1); else rtemp := ''; end if; /* do anything you want with nvalue */ /* e.g htp.prn(nvalue); */ END LOOP; utl_tcp.close_connection(conn); EXCEPTION WHEN utl_tcp.end_of_input THEN utl_tcp.close_connection(conn); END;