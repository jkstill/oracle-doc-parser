---
id: 19c__DBMS_ASSERT.ENQUOTE_NAME
name: DBMS_ASSERT.ENQUOTE_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.ENQUOTE_NAME

This function encloses the provided string in double quotes (quotation marks). No additional quotes are added if the string was already in quotes (quotation marks). The quoted string is then checked to see if it is a valid (quoted) simple SQL name.

## Syntax

```sql
DBMS_ASSERT.ENQUOTE_NAME (
   str            VARCHAR2, 
   capitalize     BOOLEAN DEFAULT TRUE)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | String to enquote |
| capitalize | BOOLEAN | IN | If TRUE or defaulted, alphabetic characters of str which was not in quotes are translated to upper case |

**Returns:** `VARCHAR2`

## Usage Notes

For more information on Database object names and qualifiers, see Oracle Database SQL Language Reference . Syntax DBMS_ASSERT.ENQUOTE_NAME ( str VARCHAR2, capitalize BOOLEAN DEFAULT TRUE) RETURN VARCHAR2; Parameters Table 26-3 ENQUOTE_NAME Function Parameters Parameter Description str String to enquote capitalize If TRUE or defaulted, alphabetic characters of str which was not in quotes are translated to upper case Usage Notes No additional quotes are added if the name was already in quotes. Verify that all other double quotes in the string are adjacent pairs of double quotes. Examples -- This procedure creates a single column table in the createOneColumnTable's schema. create or replace procedure createOneColumnTable(proposedTableNamevarchar2) is BEGIN IF (proposedTableName is NULL) THEN raise value_error; END IF; -- The use of ENQUOTE_NAME ensures that the table will be created in the -- definer's schema and not in some other schema even if the definer has -- privileges to create tables in other schemas. EXECUTE IMMEDIATE 'create table ' || DBMS_ASSERT.ENQUOTE_NAME(proposedTableName) || ' (c1 number)'; EXCEPTION WHEN others THEN dbms_output.put_line('Table creation failed due to: ' || SQLERRM); END; / -- Examples of ENQUOTE_NAME showing input/output relationships BEGIN -- 'eMp' becomes '"EMP"' since it is unquoted dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('eMp')); END; / BEGIN -- For quoted strings, the case is preserved dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('"EmP"')); END; / -- Invalid identifier example BEGIN dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('SCOTT."EMP"')); END; / -- CHR(0) examples -- The following examples illustrates that CHR(0), the NULL character, cannot appear -- in the string; such a string poses a SQL injection risk. BEGIN dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('BAD' || CHR(0) || 'IDENTIFIER')); END; / BEGIN dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('"SCOTT' || CHR(0) || '.EMP"')); END; / -- Oracle allows a period (.) to be a part of a quoted string BEGIN dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('"SCOTT.EMP"')); END; / -- The single quotation mark ('), as opposed to a double quotation mark, can appear in the string -- Note: In Oracle, a single quotation mark is specified in a literal using two single -- quotes. The first quotation mark escapes the second quotation mark in the same way that -- backslash (\) in POSIX is an escape character. BEGIN dbms_output.put_line(DBMS_ASSERT.ENQUOTE_NAME('"O''LEARY"')); END; /