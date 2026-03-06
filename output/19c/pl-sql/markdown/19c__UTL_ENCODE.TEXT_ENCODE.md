---
id: 19c__UTL_ENCODE.TEXT_ENCODE
name: UTL_ENCODE.TEXT_ENCODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.TEXT_ENCODE

This function converts the input text to the target character set as specified by the encode_charset parameter, if not NULL .

## Syntax

```sql
UTL_ENCODE.TEXT_ENCODE (
   buf            IN  VARCHAR2 CHARACTER SET ANY_CS, 
   encode_charset IN  VARCHAR2 DEFAULT NULL, 
   encoding       IN  PLS_INTEGER DEFAULT NULL) 
 RETURN string VARCHAR2 CHARACTER SET buf%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buf | VARCHAR2 | IN | The text data. |
| encode_charset | VARCHAR2 | IN | The target character set. |
| encoding | PLS_INTEGER | IN | The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL |

**Returns:** `string`

## Usage Notes

The text is encoded to either base64 or quoted-printable format, as specified by the encoding parameter. Quoted-printable is selected as a default if ENCODING is NULL. The encoded text is converted to the base character set of the database: If this is a UTF16 platform, convert the encoded text to UTF16 If this is an EBCDIC platform, convert the encoded text to EBCDIC If this is an ASCII or UTF8 platform, no conversion needed The resulting encoded and converted text string is returned to the caller. Syntax UTL_ENCODE.TEXT_ENCODE ( buf IN VARCHAR2 CHARACTER SET ANY_CS, encode_charset IN VARCHAR2 DEFAULT NULL, encoding IN PLS_INTEGER DEFAULT NULL) RETURN string VARCHAR2 CHARACTER SET buf%CHARSET; Parameters Table 262-16 TEXT_ENCODE Function Parameters Parameter Description buf The text data. encode_charset The target character set. encoding The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL Return Values Table 262-17 TEXT_ENCODE Function Return Values Return Description string A VARCHAR2 encoded string with mime header format tags. Examples v2:=utl_encode.text_encode( 'Here is some text', 'WE8ISO8859P1', UTL_ENCODE.BASE64);