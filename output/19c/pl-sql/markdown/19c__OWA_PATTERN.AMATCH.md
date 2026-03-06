---
id: 19c__OWA_PATTERN.AMATCH
name: OWA_PATTERN.AMATCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_PATTERN
tags: [owa_pattern]
source_file: OWA_PATTERN.html
---

# OWA_PATTERN.AMATCH

This function specifies if a pattern occurs in a particular location in a string.

## Syntax

```sql
OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2,
   from_loc       IN       INTEGER,
   pat            IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2,
   from_loc       IN       INTEGER,
   pat            IN OUT   PATTERN,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2
   from_loc       IN       INTEGER
   pat            in       varchar2
   backrefs       OUT      owa_text.vc_arr
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2
   from_loc       IN       INTEGER
   pat            IN OUT   PATTERN
   backrefs       OUT      owa_text.vc_arr
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| line | VARCHAR2 | IN | The text to search in. |
| from_loc | INTEGER | IN | The location (in number of characters) in line where the search is to begin. |
| pat | VARCHAR2 | IN | The string to match. It can contain regular expressions. This can be either a VARCHAR2 or a pattern. If it is a pattern, the output value of this parameter is the pattern matched. |
| backrefs | owa_text.vc_arr | OUT | The text that is matched. Each token that is matched is placed in a cell in the OWA_TEXT.VC_ARR DATA TYPE PL/SQL table. |
| flags | VARCHAR2 | IN | Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. |

**Returns:** `INTEGER`

## Usage Notes

There are four versions to this function: The first and second versions of the function do not save the matched tokens (these are saved in the backrefs parameters in the third and fourth versions). The difference between the first and second versions is the pat parameter, which can be a VARCHAR2 or a pattern datatype. The third and fourth versions of the function save the matched tokens in the backrefs parameter. The difference between the third and fourth versions is the pat parameter, which can be a VARCHAR2 or a pattern datatype. Note: If multiple overlapping strings match the regular expression, this function takes the longest match. Note: If multiple overlapping strings match the regular expression, this function takes the longest match. Syntax OWA_PATTERN.AMATCH( line IN VARCHAR2, from_loc IN INTEGER, pat IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; OWA_PATTERN.AMATCH( line IN VARCHAR2, from_loc IN INTEGER, pat IN OUT PATTERN, flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; OWA_PATTERN.AMATCH( line IN VARCHAR2 from_loc IN INTEGER pat in varchar2 backrefs OUT owa_text.vc_arr flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; OWA_PATTERN.AMATCH( line IN VARCHAR2 from_loc IN INTEGER pat IN OUT PATTERN backrefs OUT owa_text.vc_arr flags IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; Parameters Table 227-5 AMATCH Function Parameters Parameter Description line The text to search in. from_loc The location (in number of characters) in line where the search is to begin. pat The string to match. It can contain regular expressions. This can be either a VARCHAR2 or a pattern. If it is a pattern, the output value of this parameter is the pattern matched. backrefs The text that is matched. Each token that is matched is placed in a cell in the OWA_TEXT.VC_ARR DATA TYPE PL/SQL table. flags Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. Return Values The index of the character after the end of the match, counting from the beginning of line . If there was no match, the function returns 0 .