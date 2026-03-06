---
id: 19c__OWA_PATTERN.MATCH
name: OWA_PATTERN.MATCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_PATTERN
tags: [owa_pattern]
source_file: OWA_PATTERN.html
---

# OWA_PATTERN.MATCH

This function determines if a string contains the specified pattern. The pattern can contain regular expressions. If multiple overlapping strings can match the regular expression, this function takes the longest match.

## Syntax

```sql
owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN OUT   PATTERN,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN       VARCHAR2,
   backrefs       OUT      owa_text.vc_arr,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

OWA_PATTERN.MATCH(
   line           IN       VARCHAR2,
   pat            IN OUT   PATTERN,
   backrefs       OUT      owa_text.vc_arr,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   mline          IN       owa_text.multi_line,
   pat            IN       VARCHAR2,
   rlist          OUT      owa_text.row_list,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

OWA_PATTERN.MATCH(
   mline          IN       owa_text.multi_line,
   pat            IN OUT   pattern,
   rlist          OUT      owa_text.row_list,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| line | VARCHAR2 | IN | The line to search in. |
| mline | owa_text.multi_line | IN | The text to search in. This is a owa_text.multi_line datatype .. |
| pat | VARCHAR2 | IN | The pattern to match. This is either a VARCHAR2 or a OWA_PATTERN.PATTERN DATA TYPE . It is a pattern, the output value of this parameter is the pattern matched. |
| backrefs | owa_text.vc_arr | OUT | The text that is matched. Each token that is matched is placed in a cell in the OWA_TEXT.VC_ARR DATA TYPE PL/SQL table. This parameter is a row_list that holds each string in the target that was matched by a sequence of tokens in the regular expression. |
| rlist | owa_text.row_list | OUT | An output parameter containing a list of matches. |
| flags | VARCHAR2 | IN | Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax owa_pattern.match( line IN VARCHAR2, pat IN VARCHAR2, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; owa_pattern.match( line IN VARCHAR2, pat IN OUT PATTERN, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; owa_pattern.match( line IN VARCHAR2, pat IN VARCHAR2, backrefs OUT owa_text.vc_arr, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; OWA_PATTERN.MATCH( line IN VARCHAR2, pat IN OUT PATTERN, backrefs OUT owa_text.vc_arr, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; owa_pattern.match( mline IN owa_text.multi_line, pat IN VARCHAR2, rlist OUT owa_text.row_list, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; OWA_PATTERN.MATCH( mline IN owa_text.multi_line, pat IN OUT pattern, rlist OUT owa_text.row_list, flags IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; Parameters Table 227-8 MATCH Function Parameters Parameter Description line The line to search in. mline The text to search in. This is a owa_text.multi_line datatype .. pat The pattern to match. This is either a VARCHAR2 or a OWA_PATTERN.PATTERN DATA TYPE . It is a pattern, the output value of this parameter is the pattern matched. backrefs The text that is matched. Each token that is matched is placed in a cell in the OWA_TEXT.VC_ARR DATA TYPE PL/SQL table. This parameter is a row_list that holds each string in the target that was matched by a sequence of tokens in the regular expression. rlist An output parameter containing a list of matches. flags Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. Return Values TRUE if a match was found, FALSE otherwise. Examples KAZOO is the target where it is searching for the zoo.* regular expression. The period indicates any character other than newline, and the asterisk matches 0 or more of the preceding characters. In this case, it matches any character other than the newline. Therefore, this regular expression specifies that a matching target consists of zoo , followed by any set of characters neither ending in nor including a newline (which does not match the period). The i flag indicates to ignore case in the search. In this case, the function returns TRUE , which indicates that a match had been found. boolean foundMatch; foundMatch := owa_pattern.match('KAZOO', 'zoo.*', 'i'); The following example searches for the string "goal" followed by any number of characters in sometext . If found, sometext VARCHAR2(256); pat VARCHAR2(256); sometext := 'what is the goal?' pat := 'goal.*'; IF OWA_PATTERN.MATCH(sometext, pat) THEN HTP.PRINT('Match found'); ELSE HTP.PRINT('Match not found'); END IF; Operational Notes The regular expression in this function can be either a VARCHAR2 or an OWA_PATTERN.PATTERN DATA TYPE. Create AN OWA_PATTERN.PATTERN DATA TYPE from a string using the OWA_PATTERN.GETPAT procedure. Create a MULTI_LINE DATA TYPE from a long string using the OWA_TEXT.STREAM2MULTI procedure. If a multi_line is used, the rlist parameter specifies a list of chunks where matches were found. If the line is a string and not a multi_line , you can add an optional output parameter called backrefs . This parameter is a row_list that holds each string in the target that was matched by a sequence of tokens in the regular expression.