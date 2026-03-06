---
id: 19c__UTL_I18N.VALIDATE_CHARACTER_ENCODING
name: UTL_I18N.VALIDATE_CHARACTER_ENCODING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.VALIDATE_CHARACTER_ENCODING

This function validates the character encoding of VARCHAR2, NVARCHAR2, CLOB, and NCLOB data. The validation is based on the database character set for VARCHAR2 and CLOB data and national character set for NVARCHAR2 and NCLOB data.

## Syntax

```sql
UTL_I18N.VALIDATE_CHARACTER_ENCODING (
   data IN VARCHAR2 CHARACTER SET ANY_CS)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data | VARCHAR2 | IN | VARCHAR2 or NVARCHAR2 data to validate. |
| lob_loc |  |  | CLOB or NCLOB data to validate. |

**Returns:** `PLS_INTEGER`

## Usage Notes

For Unicode character sets, such as AL32UTF8, AL16UTF16, AL16UTF16LE, UTF8, and UTFE, any byte sequences mapped to the following Unicode code points are considered invalid: Unpaired surrogate code point Non-character code point In addition, any irregular or illegal UTF-8 byte sequence is considered invalid for AL32UTF8 and UTF8 character sets. The VALIDATE_CHARACTER_ENCODING function is overloaded. One function is for validating VARCHAR2 and NVARCHAR2 data, while the other function is for validating CLOB and NCLOB data. Validating VARCHAR2 and NVARCHAR2 data A VARCHAR2 or NVARCHAR2 byte or its byte sequence is considered invalid for a character set, if it does not map to any of the characters defined in the character set. Validating CLOB and NCLOB data A LOB character is considered invalid for a character set if a byte (in case of a single-byte database character set) or a byte pair (in case of UTF-16 encoding used with a multibyte database character set) corresponding to the encoding of the LOB character does not map to any of the characters defined in the character set. Syntax This function validates VARCHAR2 and NVARCHAR2 data: UTL_I18N.VALIDATE_CHARACTER_ENCODING ( data IN VARCHAR2 CHARACTER SET ANY_CS) RETURN PLS_INTEGER; This function validates CLOB and NCLOB data: UTL_I18N.VALIDATE_CHARACTER_ENCODING ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN PLS_INTEGER; Parameters Table 265-25 VALIDATE_CHARACTER_ENCODING Function Parameters Parameter Description data VARCHAR2 or NVARCHAR2 data to validate. lob_loc CLOB or NCLOB data to validate. Usage Notes This function returns the offset of the first invalid byte for the VARCHAR2 or NVARCHAR2 data. It returns the offset of the first invalid character for the CLOB or NCLOB data. It returns 0, if all the bytes in the character data are valid. It returns NULL , if the value of the parameter data or lob_loc is NULL . Examples This example validates the character encoding of NVARCHAR2 and CLOB data where the database character set is AL32UTF8 while the national character set is AL16UTF16. CREATE TABLE temp(col1 NVARCHAR2(20), col2 CLOB); INSERT INTO temp VALUES(UNISTR('foo\D800bar'), UNISTR('foo\D800bar')); COMMIT; SELECT UTL_I18N.VALIDATE_CHARACTER_ENCODING(col1) invalid_offset_column1, UTL_I18N.VALIDATE_CHARACTER_ENCODING(col2) invalid_offset_column2 FROM temp; The query returns: INVALID_OFFSET_COLUMN1 INVALID_OFFSET_COLUMN2 ---------------------- ---------------------- 7 4 Here, the surrogate code point U+D800 is invalid. The number 7 is returned as INVALID_OFFSET_COLUMN1 , because for col1 , ‘foo’ is encoded in 6 bytes in NVARCHAR2 and the invalid code point U+D800 starts at offset 7. The number 4 is returned as INVALID_OFFSET_COLUMN2 , because for col2 , ‘foo’ is encoded in 3 UTF-16 code points in CLOB and the invalid code point U+D800 starts at offset 4.