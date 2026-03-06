---
id: 19c__UTL_I18N.TRANSLITERATE
name: UTL_I18N.TRANSLITERATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.TRANSLITERATE

This function performs script transliteration. In this release, the TRANSLITERATE function only supports Japanese Kana conversion.

## Syntax

```sql
UTL_I18N.TRANSLITERATE (
  data IN VARCHAR2 CHARACTER SET ANY_CS,
  name IN VARCHAR2)
RETURN VARCHAR2 CHARACTER SET data%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data | VARCHAR2 | IN | Specifies the data to be converted. Either CHAR or NCHAR datatype can be specified. |
| name | VARCHAR2) | IN | Specifies the transliteration name string. For a list of valid names, see Table 265-23 . |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.TRANSLITERATE ( data IN VARCHAR2 CHARACTER SET ANY_CS, name IN VARCHAR2) RETURN VARCHAR2 CHARACTER SET data%CHARSET; Parameters Table 265-22 TRANSLITERATE Function Parameters Parameter Description data Specifies the data to be converted. Either CHAR or NCHAR datatype can be specified. name Specifies the transliteration name string. For a list of valid names, see Table 265-23 . Constants These options specify Japanese Kana conversions. Table 265-23 TRANSLITERATE Function Constants Constant Name Value Description KANA_FWKATAKANA 'kana_fwkatakana' Converts any type of Kana character to a fullwidth Katakana character. KANA_HWKATAKANA 'kana_hwkatakana' Converts any type of Kana character to a halfwidth Katakana character. KANA_HIRAGANA 'kana_hiragana' Converts any type of Kana character to a fullwidth Hiragana character. FWKATAKANA_HWKATAKANA 'fwkatakana_hwkatakana' Converts only fullwidth Katakana characters to halfwidth Katakana characters. FWKATAKANA_HIRAGANA 'fwkatakana_hiragana' Converts only fullwidth Katakana characters to fullwidth Hiragana characters. HWKATAKANA_FWKATAKANA 'hwkatakana_fwkatakana' Converts only halfwidth Katakana characters to fullwidth Katakana characters. HWKATAKANA_HIRAGANA 'hwkatakana_hiragana' Converts only halfwidth Katakana characters to fullwidth Hiragana characters. HIRAGANA_FWKATAKANA 'hiragana_fwkatakana' Converts only fullwidth Hiragana characters to fullwidth Katakana characters. HIRAGANA_HWKATAKANA 'hiragana_hwkatakana' Converts only fullwidth Hiragana characters to halfwidth Katakana characters. Usage Notes The function returns the converted string. Examples Given a table japanese_emp , containing an NVARCHAR2 column ename , the following statement can be used to normalize all the kana names in ename to hiragana: UPDATE japanese_emp SET ename = UTL_I18N.TRANSLITERATE (ename, 'kana_hiragana'); The following figure shows how this output might look. Figure 265-1 Loading Locale-Specific Data to the Database Description of "Figure 265-1 Loading Locale-Specific Data to the Database" The following statement normalizes one kana name to hiragana: DECLARE Name japanese_emp.ename%TYPE; Eno CONSTANT NUMBER(4) := 1; BEGIN SELECT ename INTO name FROM japanese_emp WHERE enumber = eno; name := UTL_I18N.TRANSLITERATE(name, UTL_I18N.KANA_HIRAGANA); UPDATE japanese_emp SET ename = name WHERE enumber = eno; EXCEPTION WHEN UTL_I18N.UNSUPPORTED_TRANSLITERATION THEN DBMS_OUTPUT.PUT_LINE('transliteration not supported'); END; /