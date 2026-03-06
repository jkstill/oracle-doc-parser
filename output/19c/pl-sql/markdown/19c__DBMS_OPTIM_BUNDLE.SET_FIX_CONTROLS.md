---
id: 19c__DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS
name: DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OPTIM_BUNDLE
tags: [dbms_optim_bundle]
source_file: dbms_optim_bundle.html
---

# DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS

The DBMS_OPTIM_BUNDLE subprogram, SET_FIX_CONTROLS procedure enables or disables a list of fixes with _fix_controls . The fixes can be present in a base version, in a release update, or in a one-off release. This procedure appends the new fix control settings to the existing ones.

## Syntax

```sql
DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS ( 
   fix_control_string               IN  VARCHAR2,
   sid                              IN  VARCHAR2  DEFAULT '*', 
   scope                            IN  VARCHAR2  DEFAULT 'MEMORY',
   current_setting_precedence       IN  VARCHAR2  DEFAULT 'YES');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| fix_control_string | VARCHAR2 | IN | Comma separated list of fix_control:value pair. For example: '13329748:0,20355502:4, 27060221:1' |
| sid | VARCHAR2 | IN | The name of the instance on which fix_control setting need to be made. Acceptable values are * or valid instance_name from sys.gv$instance . The default value is * . |
| scope | VARCHAR2 | IN | The scope of enabling or disabling the installed but disabled execution plan bug fixes. The possible values are: MEMORY SPFILE BOTH The default value is MEMORY . |
| current_setting_precedence | VARCHAR2 | IN | Precedence of current setting over user supplied setting. The possible values are: YES –the current environment settings take precedence in case of conflict NO –input settings take precedence in case of conflict The default value is YES . |

## Usage Notes

Syntax DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS ( fix_control_string IN VARCHAR2, sid IN VARCHAR2 DEFAULT '*', scope IN VARCHAR2 DEFAULT 'MEMORY', current_setting_precedence IN VARCHAR2 DEFAULT 'YES'); Parameters Table 118-4 SET_FIX_CONTROLS Procedure Parameters Parameter Description fix_control_string Comma separated list of fix_control:value pair. For example: '13329748:0,20355502:4, 27060221:1' sid The name of the instance on which fix_control setting need to be made. Acceptable values are * or valid instance_name from sys.gv$instance . The default value is * . scope The scope of enabling or disabling the installed but disabled execution plan bug fixes. The possible values are: MEMORY SPFILE BOTH The default value is MEMORY . current_setting_precedence Precedence of current setting over user supplied setting. The possible values are: YES –the current environment settings take precedence in case of conflict NO –input settings take precedence in case of conflict The default value is YES . Exceptions The following exceptions are raised by the SET_FIX_CONTROLS Procedure : ORA-20001 : Bad input value ORA-20002 : Internal or other errors