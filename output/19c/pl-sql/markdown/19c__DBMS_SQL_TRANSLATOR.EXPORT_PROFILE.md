---
id: 19c__DBMS_SQL_TRANSLATOR.EXPORT_PROFILE
name: DBMS_SQL_TRANSLATOR.EXPORT_PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_TRANSLATOR
tags: [dbms_sql_translator]
source_file: DBMS_SQL_TRANSLATOR.html
---

# DBMS_SQL_TRANSLATOR.EXPORT_PROFILE

This procedure exports the content of a SQL translation profile.

## Syntax

```sql
DBMS_SQL_TRANSLATOR.EXPORT_PROFILE (
   profile_name     IN          VARCHAR2,
   content          OUT NOCOPY  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | Name of profile |
| content | NOCOPY | OUT | Content of profile |

## Usage Notes

Syntax DBMS_SQL_TRANSLATOR.EXPORT_PROFILE ( profile_name IN VARCHAR2, content OUT NOCOPY CLOB); Parameters Table 164-16 EXPORT_PROFILE Procedure Parameters Parameter Description profile_name Name of profile content Content of profile Exceptions Table 164-17 EXPORT_PROFILE Procedure Exceptions Exception Description BAD_ARGUMENT Bad argument is passed to the PL/SQL interface INSUFFICIENT_PRIVILEGE User has insufficient privilege for the operation NO_SUCH_USER Profile owner does not exist NO_SUCH_PROFILE Profile does not exist Usage Notes The content of the SQL translation profile is exported in XML format as follows. Note that the profile name will not be exported. SQLTranslationProfile Translator="translator package name" ForeignSQLSyntax="TRUE|FALSE" TranslateNewSQL="TRUE|FALSE" RaiseTranslationError="TRUE|FALSE" LogTranslationError="TRUE|FALSE" TraceTranslation="TRUE|FALSE" Editionable="TRUE|FALSE"> <SQLTranslations> <SQLTranslation Enabled="TRUE|FALSE"> <SQLText>original SQL text</SQLText> <TranslatedText>translated SQL text</TranslatedText> </SQLTranslation> ... </SQLTranslations> <ErrorTranslations> <ErrorTranslation Enabled="TRUE|FALSE"> <ErrorCode>Oracle error code</ErrorCode> <TranslatedCode>translated error code</TranslatedCode> <TranslatedSQLSTATE>translated SQLSTATE</TranslatedSQLSTATE> </ErrorTranslation> ... </ErrorTranslations> </SQLTranslationProfile> To import the content to a SQL translation profile, use the IMPORT_PROFILE Procedure . Examples DECLARE content CLOB; BEGIN DBMS_SQL_TRANSLATOR.EXPORT_PROFILE( profile_name => 'tsql_application', content => content); END;