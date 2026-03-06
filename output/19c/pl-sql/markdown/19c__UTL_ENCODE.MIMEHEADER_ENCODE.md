---
id: 19c__UTL_ENCODE.MIMEHEADER_ENCODE
name: UTL_ENCODE.MIMEHEADER_ENCODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.MIMEHEADER_ENCODE

This function returns as an output an "encoded word".

## Syntax

```sql
=?<charset>?<encoding>?<encoded text>?= 
=?ISO-8859-1?Q?Here is some text?=
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buf |  |  | The text data. |
| encode_charset |  |  | The target character set. |
| encoding |  |  | The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL |

**Returns:** `UNKNOWN`

## Usage Notes

The output is in the following form: =?<charset>?<encoding>?<encoded text>?= =?ISO-8859-1?Q?Here is some text?= The buf input parameter is the text to be encoded and becomes the <encoded text> . The <encoding> value is either "Q" or "B" for quoted-printable encode or base64 encoding respectively. The ENCODING input parameter accepts as valid values UTL_ENCODE.QUOTED_PRINTABLE or UTL_ENCODE.BASE64 or NULL . If NULL , quoted-printable encoding is selected as a default value. The <charset> value is specified as the input parameter encode_charset . If NULL , the database character set is selected as a default value. The mimeheader encoding process includes conversion of the buf input string to the character set specified by the encode_charset parameter. The converted string is encoded to either quoted-printable or base64 encoded format. The mime header tags are appended and prepended. Finally, the string is converted to the base character set of the database: If this is a UTF16 platform, convert the encoded text to UTF16 If this is an EBCDIC platform, convert the encoded text to EBCDIC If this is an ASCII or UTF8 platform, no conversion needed. Syntax UTL_ENCODE.MIMEHEADER_ENCODE ( buf IN VARCHAR2 CHARACTER SET ANY_CS, encode_charset IN VARCHAR2 DEFAULT NULL, encoding IN PLS_INTEGER DEFAULT NULL) RETURN string VARCHAR2 CHARACTER SET buf%CHARSET; Parameters Table 262-8 MIMEHEADER_ENCODE Function Parameters Parameter Description buf The text data. encode_charset The target character set. encoding The encoding format. Valid values are UTL_ENCODE . BASE64 , UTL_ENCODE . QUOTED_PRINTABLE and NULL Return Values Table 262-9 MIMEHEADER_ENCODE Function Return Values Return Description string A VARCHAR2 encoded string with mime header format tags.