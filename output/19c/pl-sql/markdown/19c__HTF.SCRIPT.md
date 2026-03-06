---
id: 19c__HTF.SCRIPT
name: HTF.SCRIPT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.SCRIPT

This function generates the <SCRIPT> and </SCRIPT> tags which contain a script written in languages such as JavaScript and VBscript.

## Syntax

```sql
HTF.SCRIPT (
   cscript        IN       VARCHAR2,
   clanguage      IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cscript | VARCHAR2 | IN | The text of the script. This is the text that makes up the script itself, not the name of a file containing the script. |
| clanguage | VARCHAR2 | IN | The language in which the script is written. If this parameter is omitted, the user's browser determines the scripting language. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.SCRIPT ( cscript IN VARCHAR2, clanguage IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-75 SCRIPT Function Parameters Parameter Description cscript The text of the script. This is the text that makes up the script itself, not the name of a file containing the script. clanguage The language in which the script is written. If this parameter is omitted, the user's browser determines the scripting language. Examples This function generates <SCRIPT LANGUAGE=clanguage>cscript</SCRIPT> so that HTF.script ('Erupting_Volcano', 'Javascript'); generates <SCRIPT LANGUAGE=Javascript>"script text here"</SCRIPT> This causes the browser to run the script enclosed in the tags.