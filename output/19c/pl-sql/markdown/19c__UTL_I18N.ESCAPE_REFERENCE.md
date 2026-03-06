---
id: 19c__UTL_I18N.ESCAPE_REFERENCE
name: UTL_I18N.ESCAPE_REFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.ESCAPE_REFERENCE

This function converts a text string to its character reference counterparts for characters that fall outside the character set used by the current document.

## Syntax

```sql
UTL_I18N.ESCAPE_REFERENCE(
    str            IN VARCHAR2 CHARACTER SET ANY_CS,
    page_cs_name   IN VARCHAR2 DEFAULT NULL)
 RETURN VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Specifies the input string |
| page_cs_name | VARCHAR2 | IN | Specifies the character set of the document. If page_cs_name is NULL , then the database character set is used for CHAR data and the national character set is used for NCHAR data. |

**Returns:** `VARCHAR2`

## Usage Notes

Character references are mainly used in HTML and XML documents to represent characters independently of the encoding of the document. Character references may appear in two forms, numeric character references and character entity references. Numeric character references specify the Unicode code point value of a character, while character entity references use symbolic names to refer to the same character. For example, &#xe5; is the numeric character reference for the small letter "a" with a ring above, whereas &aring; is the character entity reference for the same character. Character entity references are also used to escape special characters, as an example, &lt; represents the < (less than) sign. This is to avoid possible confusion with the beginning of a tag in Markup languages. Syntax UTL_I18N.ESCAPE_REFERENCE( str IN VARCHAR2 CHARACTER SET ANY_CS, page_cs_name IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 265-3 ESCAPE_REFERENCE Function Parameters Parameter Description str Specifies the input string page_cs_name Specifies the character set of the document. If page_cs_name is NULL , then the database character set is used for CHAR data and the national character set is used for NCHAR data. Usage Notes If the user specifies an invalid character set or a NULL string, then the function returns a NULL string. Examples UTL_I18N.ESCAPE_REFERENCE('hello < '||chr(229),'us7ascii') This returns 'hello &lt; &#xe5;' .