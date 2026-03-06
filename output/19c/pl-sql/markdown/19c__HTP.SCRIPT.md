---
id: 19c__HTP.SCRIPT
name: HTP.SCRIPT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.SCRIPT

This procedure generates the <SCRIPT> and </SCRIPT> tags which contain a script written in languages such as JavaScript and VBscript.

## Syntax

```sql
HTP.SCRIPT (
   cscript        IN       VARCHAR2,
   clanguage      IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cscript | VARCHAR2 | IN | The text of the script. This is the text that makes up the script itself, not the name of a file containing the script. |
| clanguage | VARCHAR2 | IN | The language in which the script is written. If this parameter is omitted, the user's browser determines the scripting language. |

## Usage Notes

Syntax HTP.SCRIPT ( cscript IN VARCHAR2, clanguage IN VARCHAR2 DEFAULT NULL); Parameters Table 221-75 SCRIPT Procedure Parameters Parameter Description cscript The text of the script. This is the text that makes up the script itself, not the name of a file containing the script. clanguage The language in which the script is written. If this parameter is omitted, the user's browser determines the scripting language. Examples This procedure generates <SCRIPT LANGUAGE= clanguage > cscript </SCRIPT> so that HTP.script ('Erupting_Volcano', 'Javascript'); generates <SCRIPT LANGUAGE=Javascript>" script text here" </SCRIPT> This causes the browser to run the script enclosed in the tags.