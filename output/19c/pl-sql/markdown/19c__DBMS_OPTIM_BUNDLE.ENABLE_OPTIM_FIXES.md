---
id: 19c__DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES
name: DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OPTIM_BUNDLE
tags: [dbms_optim_bundle]
source_file: dbms_optim_bundle.html
---

# DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES

The DBMS_OPTIM_BUNDLE subprogram, ENABLE_OPTIM_FIXES procedure enables or disables fixes with plan changes up to the latest installed release update.

## Syntax

```sql
DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES ( 
   action                           IN  VARCHAR2  DEFAULT 'OFF', 
   scope                            IN  VARCHAR2  DEFAULT 'MEMORY',
   current_setting_precedence       IN  VARCHAR2  DEFAULT 'YES');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| action | VARCHAR2 | IN | Enables or disables all of the installed but disabled execution plan bug fixes up to and including the current release update. The possible values are: ON -enables the bundle fixes. OFF -disables bundle fixes by setting the _fix_controls to the value 0 . It will not remove _fix_control entries from SPFILE . The default value is OFF . |
| scope | VARCHAR2 | IN | The scope of enabling or disabling the installed but disabled execution plan bug fixes. The possible values are: MEMORY SPFILE BOTH INITORA MEMORY / SPFILE / BOTH : These three input values enables or disables the fixes in a given scope. INITORA : This input value will just display manual command syntax that the user needs to manually enter into the database's init.ora file in order to enable or disable execution plan bug fixes. When using SCOPE=INITORA in this way, the current_setting_precedence field has no significance. |
| current_setting_precedence | VARCHAR2 | IN | Sets the precedence of environment settings or release update settings, where these settings are in conflict. The possible values are: YES -the current environment settings take precedence in case of conflict NO -release update settings take precedence in case of conflict The default value is YES . |

## Usage Notes

Syntax DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES ( action IN VARCHAR2 DEFAULT 'OFF', scope IN VARCHAR2 DEFAULT 'MEMORY', current_setting_precedence IN VARCHAR2 DEFAULT 'YES'); Parameters Table 118-2 ENABLE_OPTIM_FIXES Procedure Parameters Parameter Description action Enables or disables all of the installed but disabled execution plan bug fixes up to and including the current release update. The possible values are: ON -enables the bundle fixes. OFF -disables bundle fixes by setting the _fix_controls to the value 0 . It will not remove _fix_control entries from SPFILE . The default value is OFF . scope The scope of enabling or disabling the installed but disabled execution plan bug fixes. The possible values are: MEMORY SPFILE BOTH INITORA MEMORY / SPFILE / BOTH : These three input values enables or disables the fixes in a given scope. INITORA : This input value will just display manual command syntax that the user needs to manually enter into the database's init.ora file in order to enable or disable execution plan bug fixes. When using SCOPE=INITORA in this way, the current_setting_precedence field has no significance. current_setting_precedence Sets the precedence of environment settings or release update settings, where these settings are in conflict. The possible values are: YES -the current environment settings take precedence in case of conflict NO -release update settings take precedence in case of conflict The default value is YES . Examples To enable all of the installed but disabled execution plan bug fixes up to and including those from the current release update: SQL> execute dbms_optim_bundle.enable_optim_fixes('ON','BOTH', 'YES'); This instruction would enable all fixes, in both MEMORY and in the persistant SPFILE , with a precedence of current setting. Exceptions The following exceptions are raised by the ENABLE_OPTIM_FIXES Procedure : ORA-20001 : Bad input value ORA-20002 : Internal or other errors