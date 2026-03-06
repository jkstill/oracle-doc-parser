---
id: 19c__DBMS_STATS.SET_PARAM
name: DBMS_STATS.SET_PARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_PARAM

This deprecated procedure sets default values for parameters of DBMS_STATS procedures.

## Syntax

```sql
DBMS_STATS.SET_PARAM (
   pname      IN    VARCHAR2, 
   pval       IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2 | IN | The parameter name The default value for following parameters can be set. CASCADE - The default value for CASCADE set by SET_PARAM is not used by export/import procedures.It is used only by gather procedures. DEGREE ESTIMATE_PERCENT METHOD_OPT NO_INVALIDATE GRANULARITY AUTOSTATS_TARGET - This parameter is applicable only for auto statistics collection. The value of this parameter controls the objects considered for statistics collection (see pval ) |
| pval | VARCHAR2) | IN | The parameter value. If NULL is specified, it will set the default value determined by Oracle. When pname is AUTOSTATS_TARGET , the following are valid values: 'ALL' - Statistics are collected for all objects in the system 'ORACLE' - Statistics are collected for all Oracle owned objects 'AUTO' - Oracle decides for which objects to collect statistics |

## Usage Notes

Note: This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the SET_GLOBAL_PREFS Procedure . See also DBMS_STATS Deprecated Subprograms . You can use the GET_PARAM Function to get the current default value of a parameter. Note: This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the SET_GLOBAL_PREFS Procedure . See also DBMS_STATS Deprecated Subprograms . Syntax DBMS_STATS.SET_PARAM ( pname IN VARCHAR2, pval IN VARCHAR2); Parameters Table 171-126 SET_PARAM Procedure Parameters Parameter Description pname The parameter name The default value for following parameters can be set. CASCADE - The default value for CASCADE set by SET_PARAM is not used by export/import procedures.It is used only by gather procedures. DEGREE ESTIMATE_PERCENT METHOD_OPT NO_INVALIDATE GRANULARITY AUTOSTATS_TARGET - This parameter is applicable only for auto statistics collection. The value of this parameter controls the objects considered for statistics collection (see pval ) pval The parameter value. If NULL is specified, it will set the default value determined by Oracle. When pname is AUTOSTATS_TARGET , the following are valid values: 'ALL' - Statistics are collected for all objects in the system 'ORACLE' - Statistics are collected for all Oracle owned objects 'AUTO' - Oracle decides for which objects to collect statistics Usage Notes To run this procedure, you must have the SYSDBA or both the ANALYZE ANY DICTIONARY and ANALYZE ANY system privileges. Note that both arguments are of type VARCHAR2 and the values need to be enclosed in quotes even when they represent numbers. Note also the difference between NULL and 'NULL' : When NULL is unquoted, this sets the parameter to the value Oracle recommends. In the case of the quoted 'NULL' , this sets the value of the parameter to NULL .