---
id: 19c__UTL_I18N.GET_DEFAULT_CHARSET
name: UTL_I18N.GET_DEFAULT_CHARSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_DEFAULT_CHARSET

This function returns the default Oracle character set name or the default e-mail safe character set name from an Oracle language name.

## Syntax

```sql
UTL_I18N.GET_DEFAULT_CHARSET( 
   language  IN VARCHAR2,
   context   IN PLS_INTEGER DEFAULT GENERIC_CONTEXT,
   iswindows IN BOOLEAN DEFAULT FALSE)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| language | VARCHAR2 | IN | Specifies a valid Oracle language |
| context | PLS_INTEGER | IN | GENERIC_CONTEXT | MAIL_CONTEXT GENERIC_CONTEXT : Returns the default character set for general cases MAIL_CONTEXT : Returns the default e-mail safe character set name |
| iswindows | BOOLEAN | IN | If context is set as MAIL_CONTEXT , then iswindows should be set to TRUE if the platform is Windows and FALSE if the platform is not Windows. The default is FALSE . iswindows has no effect if context is set as GENERIC_CONTEXT . |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: " MAP_CHARSET Function " for an explanation of an e-mail safe character set See Also: " MAP_CHARSET Function " for an explanation of an e-mail safe character set Syntax UTL_I18N.GET_DEFAULT_CHARSET( language IN VARCHAR2, context IN PLS_INTEGER DEFAULT GENERIC_CONTEXT, iswindows IN BOOLEAN DEFAULT FALSE) RETURN VARCHAR2; Parameters Table 265-4 GET_DEFAULT_CHARSET Function Parameters Parameter Description language Specifies a valid Oracle language context GENERIC_CONTEXT | MAIL_CONTEXT GENERIC_CONTEXT : Returns the default character set for general cases MAIL_CONTEXT : Returns the default e-mail safe character set name iswindows If context is set as MAIL_CONTEXT , then iswindows should be set to TRUE if the platform is Windows and FALSE if the platform is not Windows. The default is FALSE . iswindows has no effect if context is set as GENERIC_CONTEXT . Usage Notes If the user specifies an invalid language name or an invalid flag, then the function returns a NULL string.