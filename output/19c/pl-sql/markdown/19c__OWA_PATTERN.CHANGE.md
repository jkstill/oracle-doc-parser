---
id: 19c__OWA_PATTERN.CHANGE
name: OWA_PATTERN.CHANGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_PATTERN
tags: [owa_pattern]
source_file: OWA_PATTERN.html
---

# OWA_PATTERN.CHANGE

This function or procedure searches and replaces a string or multi_line datatype. If multiple overlapping strings match the regular expression, this subprogram takes the longest match.

## Syntax

```sql
OWA_PATTERN.CHANGE(
   line           IN OUT    VARCHAR2,
   from_str       IN        VARCHAR2,
   to_str         IN        VARCHAR2,
   flags          IN        VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.CHANGE(
   line           IN OUT   VARCHAR2,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL);

owa_pattern.change(
   mline          IN OUT   owa_text.multi_line,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.CHANGE(
   mline          IN OUT   owa_text.multi_line,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| line | VARCHAR2 | IN OUT | The text to search in. The output value of this parameter is the altered string. |
| mline | owa_text.multi_line | IN OUT | The text to search in. This is a owa_text.multi_line datatype . The output value of this parameter is the altered string. |
| from_str | VARCHAR2 | IN | The regular expression to replace. |
| to_str | VARCHAR2 | IN | The substitution pattern. |
| flags | VARCHAR2 | IN | Whether or not the search is case-sensitive, and whether or not changes are to be made globally. If " i " is specified, the search is case-insensitive. If " g " is specified, changes are made to all matches. Otherwise, the function stops after the first substitution is made. |

**Returns:** `INTEGER`

## Usage Notes

Syntax OWA_PATTERN.CHANGE( line IN OUT VARCHAR2, from_str IN VARCHAR2, to_str IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; OWA_PATTERN.CHANGE( line IN OUT VARCHAR2, from_str IN VARCHAR2, to_str IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL); owa_pattern.change( mline IN OUT owa_text.multi_line, from_str IN VARCHAR2, to_str IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; OWA_PATTERN.CHANGE( mline IN OUT owa_text.multi_line, from_str IN VARCHAR2, to_str IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL); Parameters Table 227-6 CHANGE Procedure Parameters Parameter Description line The text to search in. The output value of this parameter is the altered string. mline The text to search in. This is a owa_text.multi_line datatype . The output value of this parameter is the altered string. from_str The regular expression to replace. to_str The substitution pattern. flags Whether or not the search is case-sensitive, and whether or not changes are to be made globally. If " i " is specified, the search is case-insensitive. If " g " is specified, changes are made to all matches. Otherwise, the function stops after the first substitution is made. Return Values As a function, it returns the number of substitutions made. If the flag "g" is not used, this number can only be 0 or 1 and only the first match is replaced. The flag "g" specifies to replace all matches with the regular expression. Examples OWA_PATTERN.CHANGE('Cats in pajamas', 'C.+in', '& red ') The regular expression matches the substring " Cats in ". It then replaces this string with "& red". The ampersand character " & " indicates " Cats in " because that is what matched the regular expression. Thus, this procedure replaces the string " Cats in pajamas " with " Cats in red " If you call this as a function instead of a procedure, the value returned is 1, indicating that a single substitution has been made. Example 2: CREATE OR REPLACE PROCEDURE test_pattern as theline VARCHAR2(256); num_found INTEGER; BEGIN theline := 'what is the goal?'; num_found := OWA_PATTERN.CHANGE(theline, 'goal', 'idea', 'g'); HTP.PRINT(num_found); -- num_found is 1 HTP.PRINT(theline); -- theline is 'what is the idea?' END; / SHOW ERRORS