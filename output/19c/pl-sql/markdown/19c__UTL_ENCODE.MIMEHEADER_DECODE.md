---
id: 19c__UTL_ENCODE.MIMEHEADER_DECODE
name: UTL_ENCODE.MIMEHEADER_DECODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.MIMEHEADER_DECODE

This function accepts as input an "encoded word.”

## Syntax

```sql
=?<charset>?<encoding>?<encoded text>?= 
=?ISO-8859-1?Q?Here is some encoded text?=
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buf |  |  | The encoded text data with mime header format tags. |

**Returns:** `UNKNOWN`

## Usage Notes

It uses the form: =?<charset>?<encoding>?<encoded text>?= =?ISO-8859-1?Q?Here is some encoded text?= The <encoded text> is encapsulated in mime header tags which give the MIMEHEADER_DECODE function information about how to decode the string. The mime header metadata tags are stripped from the input string and the <encoded text> is converted to the base database character set as follows: If this is a UTF16 platform, convert the encoded text from UTF16 to ASCII If this is an EBCDIC platform, convert the encoded text from EBCDIC to ASCII If this is an ASCII or UTF8 platform, no conversion needed The string is decoded using either quoted-printable or base64 decoding, as specified by the <encoding> metadata tag in the encoded word. The resulting converted and decoded text is returned to the caller as a VARCHAR2 string. Syntax UTL_ENCODE.MIMEHEADER_DECODE ( buf IN VARCHAR2 CHARACTER SET ANY_CS) RETURN data VARCHAR2 CHARACTER SET buf%CHARSET; Parameters Table 262-6 MIMEHEADER_DECODE Function Parameters Parameter Description buf The encoded text data with mime header format tags. Return Values Table 262-7 MIMEHEADER_DECODE Function Return Values Return Description data The encoded text data with mime header format tags Examples v2:=utl_encode.mimeheader_decode('=?ISO-8859-1?Q?Here is some encoded text?=');