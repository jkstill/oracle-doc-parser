---
id: 19c__DBMS_XSTREAM_ADM.RENAME_TABLE
name: DBMS_XSTREAM_ADM.RENAME_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.RENAME_TABLE

This procedure either adds or removes a declarative rule-based transformation which renames a table in a row logical change record (row LCR) that satisfies the specified rule.

## Syntax

```sql
DBMS_XSTREAM_ADM.RENAME_TABLE(
   rule_name        IN  VARCHAR2,
   from_table_name  IN  VARCHAR2,
   to_table_name    IN  VARCHAR2,
   step_number      IN  NUMBER    DEFAULT 0,
   operation        IN  VARCHAR2  DEFAULT 'ADD');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. |
| from_table_name | VARCHAR2 | IN | The name of the table to be renamed in each row LCR that satisfies the rule, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. |
| to_table_name | VARCHAR2 | IN | The new name of the table in each row LCR that satisfies the rule, specified as [ schema_name .] object_name . For example, humres.staff . The transformation can rename the table only, the schema only, or the table and the schema. If the schema is not specified, then the current user is the default. |
| step_number | NUMBER | IN | The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering |
| operation | VARCHAR2 | IN | Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule. |

## Usage Notes

For the transformation to be performed when the specified rule evaluates to TRUE , the rule must be in the positive rule set of an XStream client. XStream clients include capture processes, propagations, and apply processes. Note: Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations Note: Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error. See Also: Oracle Database XStream Guide for more information about declarative rule-based transformations Syntax DBMS_XSTREAM_ADM.RENAME_TABLE( rule_name IN VARCHAR2, from_table_name IN VARCHAR2, to_table_name IN VARCHAR2, step_number IN NUMBER DEFAULT 0, operation IN VARCHAR2 DEFAULT 'ADD'); Parameters Table 217-31 RENAME_TABLE Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . If NULL , then the procedure raises an error. For example, to specify a rule in the hr schema named employees12 , enter hr.employees12 . If the schema is not specified, then the current user is the default. from_table_name The name of the table to be renamed in each row LCR that satisfies the rule, specified as [ schema_name .] object_name . For example, hr.employees . If the schema is not specified, then the current user is the default. to_table_name The new name of the table in each row LCR that satisfies the rule, specified as [ schema_name .] object_name . For example, humres.staff . The transformation can rename the table only, the schema only, or the table and the schema. If the schema is not specified, then the current user is the default. step_number The order of execution of the transformation. See Also: Oracle Database XStream Guide for more information about transformation ordering operation Specify 'ADD' to add the transformation to the rule. Specify 'REMOVE' to remove the transformation from the rule.