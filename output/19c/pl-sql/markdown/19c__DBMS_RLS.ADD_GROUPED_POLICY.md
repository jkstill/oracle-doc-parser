---
id: 19c__DBMS_RLS.ADD_GROUPED_POLICY
name: DBMS_RLS.ADD_GROUPED_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.ADD_GROUPED_POLICY

This procedure adds a policy associated with a policy group.

## Syntax

```sql
DBMS_RLS.ADD_GROUPED_POLICY(
   object_schema            IN  VARCHAR2        DEFAULT NULL,
   object_name              IN  VARCHAR2,
   policy_group             IN  VARCHAR2        DEFAULT 'SYS_DEFAULT',
   policy_name              IN  VARCHAR2,
   function_schema          IN  VARCHAR2        DEFAULT NULL,
   policy_function          IN  VARCHAR2,
   statement_types          IN  VARCHAR2        DEFAULT NULL,
   update_check             IN  BOOLEAN         DEFAULT FALSE,
   enable                   IN  BOOLEAN         DEFAULT TRUE,
   static_policy            IN  BOOLEAN         DEFAULT FALSE,
   policy_type              IN  BINARY_INTEGER  DEFAULT NULL,
   long_predicate           IN  BOOLEAN         DEFAULT FALSE,
   sec_relevant_cols        IN  VARCHAR2,
   sec_relevant_cols_opt    IN  BINARY_INTEGER  DEFAULT NULL,
   namespace                IN  VARCHAR2        DEFAULT NULL,
   attribute                IN  VARCHAR2        DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is added |
| policy_group | VARCHAR2 | IN | Name of the policy group to which the policy belongs |
| policy_name | VARCHAR2 | IN | Name of the policy; must be unique for the same table or view |
| function_schema | VARCHAR2 | IN | Schema owning the policy function. If no function_schema is specified or is NULL , then the current schema is used. |
| policy_function | VARCHAR2 | IN | Name of the function that generates a predicate for the policy. If the function is defined within a package, the name of the package must be present. |
| statement_types | VARCHAR2 | IN | Statement types to which the policy applies. It can be any combination of INDEX, SELECT , UPDATE , or DELETE . The default is to apply to all of these types except INSERT and INDEX . |
| update_check | BOOLEAN | IN | For INSERT and UPDATE statements only, setting update_check to TRUE causes the server to check the policy against the value after INSERT or UPDATE. The check applies only to the security relevant columns that are included in the policy definition. In other words, the INSERT or UPDATE operation will fail only if the security relevant column that is defined in the policy is added or updated in the INSERT or UPDATE statement. |
| enable | BOOLEAN | IN | Indicates if the policy is enable when it is added. The default is TRUE . |
| static_policy | BOOLEAN | IN | Default is FALSE . If it is set to TRUE , the server assumes that the policy function for the static policy produces the same predicate string for anyone accessing the object, except for SYS or the privilege user who has the EXEMPT ACCESS POLICY privilege. |
| policy_type | BINARY_INTEGER | IN | Default is NULL , which means policy_type is decided by the value of static_policy . The available policy types are listed in Table 146-5 . Specifying any of these policy types overrides the value of static_policy . |
| long_predicate | BOOLEAN | IN | Default is FALSE , which means the policy function can return a predicate with a length of up to 4000 bytes. TRUE means the predicate text string length can be up to 32K bytes.Policies existing prior to the availability of this parameter retain a 32K limit. |
| sec_relevant_cols | VARCHAR2 | IN | Enables column-level Virtual Private Database (VPD), which enforces security policies when a column containing sensitive information is referenced in a query. Applies to tables and views, but not to synonyms. Specify a list of comma- or space-separated valid column names of the policy-protected object. The policy is enforced only if a specified column is referenced (or, for an abstract datatype column, its attributes are referenced) in the user SQL statement or its underlying view definition. Default is all the user-defined columns for the object. |
| namespace | VARCHAR2 | IN | Name which determines the application context namespace |
| attribute | VARCHAR2 | IN | Attribute which determines the application context attribute name |

## Usage Notes

Syntax DBMS_RLS.ADD_GROUPED_POLICY( object_schema IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2, policy_group IN VARCHAR2 DEFAULT 'SYS_DEFAULT', policy_name IN VARCHAR2, function_schema IN VARCHAR2 DEFAULT NULL, policy_function IN VARCHAR2, statement_types IN VARCHAR2 DEFAULT NULL, update_check IN BOOLEAN DEFAULT FALSE, enable IN BOOLEAN DEFAULT TRUE, static_policy IN BOOLEAN DEFAULT FALSE, policy_type IN BINARY_INTEGER DEFAULT NULL, long_predicate IN BOOLEAN DEFAULT FALSE, sec_relevant_cols IN VARCHAR2, sec_relevant_cols_opt IN BINARY_INTEGER DEFAULT NULL, namespace IN VARCHAR2 DEFAULT NULL, attribute IN VARCHAR2 DEFAULT NULL); Parameters Table 146-3 ADD_GROUPED_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is added policy_group Name of the policy group to which the policy belongs policy_name Name of the policy; must be unique for the same table or view function_schema Schema owning the policy function. If no function_schema is specified or is NULL , then the current schema is used. policy_function Name of the function that generates a predicate for the policy. If the function is defined within a package, the name of the package must be present. statement_types Statement types to which the policy applies. It can be any combination of INDEX, SELECT , UPDATE , or DELETE . The default is to apply to all of these types except INSERT and INDEX . update_check For INSERT and UPDATE statements only, setting update_check to TRUE causes the server to check the policy against the value after INSERT or UPDATE. The check applies only to the security relevant columns that are included in the policy definition. In other words, the INSERT or UPDATE operation will fail only if the security relevant column that is defined in the policy is added or updated in the INSERT or UPDATE statement. enable Indicates if the policy is enable when it is added. The default is TRUE . static_policy Default is FALSE . If it is set to TRUE , the server assumes that the policy function for the static policy produces the same predicate string for anyone accessing the object, except for SYS or the privilege user who has the EXEMPT ACCESS POLICY privilege. policy_type Default is NULL , which means policy_type is decided by the value of static_policy . The available policy types are listed in Table 146-5 . Specifying any of these policy types overrides the value of static_policy . long_predicate Default is FALSE , which means the policy function can return a predicate with a length of up to 4000 bytes. TRUE means the predicate text string length can be up to 32K bytes.Policies existing prior to the availability of this parameter retain a 32K limit. sec_relevant_cols Enables column-level Virtual Private Database (VPD), which enforces security policies when a column containing sensitive information is referenced in a query. Applies to tables and views, but not to synonyms. Specify a list of comma- or space-separated valid column names of the policy-protected object. The policy is enforced only if a specified column is referenced (or, for an abstract datatype column, its attributes are referenced) in the user SQL statement or its underlying view definition. Default is all the user-defined columns for the object. namespace Name which determines the application context namespace attribute Attribute which determines the application context attribute name Usage Notes This procedure adds a policy to the specified table, view, or synonym and associates the policy with the specified policy group. The policy group must have been created by using the CREATE_POLICY_GROUP Procedure . The policy name must be unique within a policy group for a specific object. Policies from the default policy group, SYS_DEFAULT , are always executed regardless of the active policy group; however, fine-grained access control policies do not apply to users with EXEMPT ACCESS POLICY system privilege.