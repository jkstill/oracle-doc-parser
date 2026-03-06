---
id: 19c__UTL_ENCODE.TEXT_DECODE
name: UTL_ENCODE.TEXT_DECODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.TEXT_DECODE

This function converts the input text to the target character set as specified by the encode_charset parameter, if not NULL .

## Syntax

```sql
UTL_ENCODE.TEXT_DECODE(
   buf            IN  VARCHAR2 CHARACTER SET ANY_CS, 
   encode_charset IN  VARCHAR2 DEFAULT NULL, 
   encoding       IN  PLS_INTEGER DEFAULT NULL) 
 RETURN string VARCHAR2 CHARACTER SET buf%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buf | VARCHAR2 | IN | The encoded text data. |
| encode_charset | VARCHAR2 | IN | The source character set. |
| encoding | PLS_INTEGER | IN | The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL. |

**Returns:** `string`

## Usage Notes

The encoded text is converted to the base character set of database, as follows: If this is a UTF16 platform, convert the encoded text from UTF16 to ASCII If this is an EBCDIC platform, convert the encoded text from EBCDIC to ASCII If this is an ASCII or UTF8 platform, no conversion needed You can decode from either quoted-printable or base64 format, with regard to each encoding parameter. If NULL , quoted-printable is selected as a default decoding format. If encode_charset is not NULL , you convert the string from the specified character set to the database character set. The resulting decoded and converted text string is returned to the caller. Syntax UTL_ENCODE.TEXT_DECODE( buf IN VARCHAR2 CHARACTER SET ANY_CS, encode_charset IN VARCHAR2 DEFAULT NULL, encoding IN PLS_INTEGER DEFAULT NULL) RETURN string VARCHAR2 CHARACTER SET buf%CHARSET; Parameters Table 262-14 TEXT_DECODE Function Parameters Parameter Description buf The encoded text data. encode_charset The source character set. encoding The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL. Return Values Table 262-15 TEXT_DECODE Function Return Values Return Description string A VARCHAR2 decoded text string. Examples v2:=UTL_ENCODE.TEXT_DECODE( 'Here is some text', WE8ISO8859P1, UTL_ENCODE.BASE64);