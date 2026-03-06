---
id: 19c__UTL_I18N.GET_TRANSLATION
name: UTL_I18N.GET_TRANSLATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_TRANSLATION

This function returns the translation of the language and territory name in the specified translation language.

## Syntax

```sql
UTL_I18N.GET_TRANSLATION ( 
   parameter        IN VARCHAR2 CHARACTER SET ANY_CS,
   trans_language   IN VARCHAR2 'AMERICAN',
   flag             IN PLS_INTEGER DEFAULT LANGUAGE_TRANS)
RETURN VARCHAR2 CHARACTER SET parameter%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter | VARCHAR2 | IN | Specifies a valid language name, territory name, or a combined string in the form of language_territory . It is case-insensitive. |
| trans_language | VARCHAR2 | IN | Specifies a translation language name. For example, ITALIAN is for the Italian language. The default is AMERICAN , which indicates American English. |
| flag | PLS_INTEGER | IN | Specifies the translation type: LANGUAGE_TRANS : The function returns the language translation. TERRITORY_TRANS : The function returns the territory translation. LANGUAGE_TERRITORY_TRANS : The function returns the language and territory translation. The default translation type is LANGUAGE_TRANS . |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_I18N.GET_TRANSLATION ( parameter IN VARCHAR2 CHARACTER SET ANY_CS, trans_language IN VARCHAR2 'AMERICAN', flag IN PLS_INTEGER DEFAULT LANGUAGE_TRANS) RETURN VARCHAR2 CHARACTER SET parameter%CHARSET; Parameters Table 265-12 GET_TRANSLATION Function Parameters Parameter Description parameter Specifies a valid language name, territory name, or a combined string in the form of language_territory . It is case-insensitive. trans_language Specifies a translation language name. For example, ITALIAN is for the Italian language. The default is AMERICAN , which indicates American English. flag Specifies the translation type: LANGUAGE_TRANS : The function returns the language translation. TERRITORY_TRANS : The function returns the territory translation. LANGUAGE_TERRITORY_TRANS : The function returns the language and territory translation. The default translation type is LANGUAGE_TRANS . Usage Notes If VARCHAR2 is used as a parameter type, the returned translation text can be corrupted due to the conversion to the database character set. Using NVARCHAR2 as the parameter type will preserve the translation text because Unicode can encode all translated languages. If the specified translation language is not available or an invalid name is provided, the default "American English" translations are returned. For example, Oracle does not provide GUJARATI translations, so the returned translation would be in American English. Examples The following returns the names of all the Oracle-supported languages in Italian. DECLARE CURSOR c1 IS SELECT value FROM V$NLS_VALID_VALUES WHERE parameter = 'LANGUAGE' ORDER BY value; retval NVARCHAR2(100); BEGIN FOR item IN c1 LOOP retval := UTL_I18N.GET_TRANSLATION (TO_NCHAR(item.value), 'italian'); END LOOP; END;