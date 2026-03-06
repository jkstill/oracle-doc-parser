---
id: 19c__UTL_I18N.MAP_CHARSET
name: UTL_I18N.MAP_CHARSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.MAP_CHARSET

This function maps a character set to another character set.

## Syntax

```sql
UTL_I18N.MAP_CHARSET( 
   charset   IN VARCHAR2,
   context   IN PLS_INTEGER DEFAULT GENERIC_CONTEXT,
   flag      IN PLS_INTEGER DEFAULT ORACLE_TO_IANA)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| charset | VARCHAR2 | IN | Specifies the character set name to be mapped. The mapping is case-insensitive. |
| context | PLS_INTEGER | IN | GENERIC_CONTEXT | MAIL_CONTEXT GENERIC_CONTEXT : The mapping is between an Oracle character set name and an IANA character set name. This is the default value. MAIL_CONTEXT : The mapping is between an Oracle character set name and an email safe character set name. |
| flag | PLS_INTEGER | IN | ORACLE_TO_IANA | IANA_TO_ORACLE if GENERIC_CONTEXT is set ORACLE_TO_IANA : Map from an Oracle character set name to an IANA character set name. This is the default. IANA_TO_ORACLE : Map from an IANA character set name to an Oracle character set name. MAIL_GENERIC | MAIL_WINDOWS if MAIL_CONTEXT is set MAIL_GENERIC : Map from an Oracle character set name to an email safe character set name on a non-Windows platform. MAIL_WINDOWS : Map from an Oracle character set name to an email safe character set name on a Windows platform. |

**Returns:** `VARCHAR2`

## Usage Notes

It maps the following: An Oracle character set name to an IANA character set name. An IANA character set name to an Oracle character set name. An Oracle character set to an e-mail safe character set name. Syntax UTL_I18N.MAP_CHARSET( charset IN VARCHAR2, context IN PLS_INTEGER DEFAULT GENERIC_CONTEXT, flag IN PLS_INTEGER DEFAULT ORACLE_TO_IANA) RETURN VARCHAR2; Parameters Table 265-13 MAP_CHARSET Function Parameters Parameter Description charset Specifies the character set name to be mapped. The mapping is case-insensitive. context GENERIC_CONTEXT | MAIL_CONTEXT GENERIC_CONTEXT : The mapping is between an Oracle character set name and an IANA character set name. This is the default value. MAIL_CONTEXT : The mapping is between an Oracle character set name and an email safe character set name. flag ORACLE_TO_IANA | IANA_TO_ORACLE if GENERIC_CONTEXT is set ORACLE_TO_IANA : Map from an Oracle character set name to an IANA character set name. This is the default. IANA_TO_ORACLE : Map from an IANA character set name to an Oracle character set name. MAIL_GENERIC | MAIL_WINDOWS if MAIL_CONTEXT is set MAIL_GENERIC : Map from an Oracle character set name to an email safe character set name on a non-Windows platform. MAIL_WINDOWS : Map from an Oracle character set name to an email safe character set name on a Windows platform. Usage Notes An e-mail safe character set is an Oracle character set that is commonly used by applications when they submit e-mail messages. The character set is usually used to convert contents in the database character set to e-mail safe contents. To specify the character set name in the mail header, you should use the corresponding IANA character set name obtained by calling the MAP_CHARSET function with the ORACLE_TO_IANA option, providing the e-mail safe character set name as input. For example, no e-mail client recognizes message contents in the WE8DEC character set, whose corresponding IANA name is DEC-MCS . If WE8DEC is passed to the MAP_CHARSET function with the MAIL_CONTEXT option, then the function returns WE8ISO8859P1 . Its corresponding IANA name, ISO-8859-1 , is recognized by most e-mail clients. The steps in this example are as follows: Call the MAP_CHARSET function with the MAIL_CONTEXT | MAIL_GENERIC option with the database character set name, WE8DEC . The result is WE8ISO8859P1 . Convert the contents stored in the database to WE8ISO8859P1 . Call the MAP_CHARSET function with the ORACLE_TO_IANA | GENERIC_CONTEXT option with the e-mail safe character set, WE8ISO8859P1 . The result is ISO-8859-1 . Specify ISO-8859-1 in the mail header when the e-mail message is submitted. The function returns a character set name if a match is found. If no match is found or if the flag is invalid, then it returns NULL . Note: Many Oracle character sets can map to one e-mail safe character set. There is no function that maps an e-mail safe character set to an Oracle character set name. Note: Many Oracle character sets can map to one e-mail safe character set. There is no function that maps an e-mail safe character set to an Oracle character set name.