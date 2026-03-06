---
id: 19c__DBMS_TSDP_PROTECT.ADD_POLICY
name: DBMS_TSDP_PROTECT.ADD_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.ADD_POLICY

This procedure creates a TDSP policy.

## Syntax

```sql
DBMS_TSDP_PROTECT.ADD_POLICY (
   policy_name              IN VARCHAR2, 
   security_feature         IN PLS_INTEGER,
   policy_enable_options    IN FEATURE_OPTIONS,
   policy_apply_condition   IN POLICY_CONDITION DEFAULT TSDP$default_condition);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_name | VARCHAR2 | IN | Name of the policy being created. The maximum length for this identifier is M_IDEN . This follows the Oracle naming convention. |
| security_feature | PLS_INTEGER | IN | Oracle security feature with which the policy is associated. Allowed values: DBMS_TSDP_PROTECT.REDACT DBMS_TSDP_PROTECT.VPD DBMS_TSDP_PROTECT.UNIFIED_AUDIT DBMS_TSDP_PROTECT.FINE_GRAINED_AUDIT DBMS_TSDP_PROTECT.COLUMN_ENCRYPTION |
| policy_enable_options | FEATURE_OPTIONS | IN | Initialized with the parameter-value pairs corresponding to the security_feature setting |
| policy_apply_condition | POLICY_CONDITION | IN | Initialized with the property-value pairs that must be satisfied in order to apply the corresponding policy_enable_options . This is an associative array with Property as the key ( PLS_INTEGER ). Example: example_policy_condition ( Property )= property_value . Permissible values for Property: DBMS_TSDP_PROPERTY.DATATYPE DBMS_TSDP_PROPERTY.LENGTH DBMS_TSDP_PROPERTY.PARENT_SCHEMA DBMS_TSDP_PROPERTY.PARENT_TABLE |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.ADD_POLICY ( policy_name IN VARCHAR2, security_feature IN PLS_INTEGER, policy_enable_options IN FEATURE_OPTIONS, policy_apply_condition IN POLICY_CONDITION DEFAULT TSDP$default_condition); Parameters Table 182-3 ADD_POLICY Procedure Parameters Parameter Description policy_name Name of the policy being created. The maximum length for this identifier is M_IDEN . This follows the Oracle naming convention. security_feature Oracle security feature with which the policy is associated. Allowed values: DBMS_TSDP_PROTECT.REDACT DBMS_TSDP_PROTECT.VPD DBMS_TSDP_PROTECT.UNIFIED_AUDIT DBMS_TSDP_PROTECT.FINE_GRAINED_AUDIT DBMS_TSDP_PROTECT.COLUMN_ENCRYPTION policy_enable_options Initialized with the parameter-value pairs corresponding to the security_feature setting policy_apply_condition Initialized with the property-value pairs that must be satisfied in order to apply the corresponding policy_enable_options . This is an associative array with Property as the key ( PLS_INTEGER ). Example: example_policy_condition ( Property )= property_value . Permissible values for Property: DBMS_TSDP_PROPERTY.DATATYPE DBMS_TSDP_PROPERTY.LENGTH DBMS_TSDP_PROPERTY.PARENT_SCHEMA DBMS_TSDP_PROPERTY.PARENT_TABLE Usage Notes To create the TDSP policy, you must include the procedure in an anonymous block that defines the type of security feature that will use the policy and conditions to test when the policy is enabled. For more information, see Oracle Database Security Guide . Examples Create a policy PARTIAL_MASK_POLICY : DECLARE redact_feature_options DBMS_TSDP_PROTECT.FEATURE_OPTIONS; policy_conditions DBMS_TSDP_PROTECT.POLICY_CONDITIONS; BEGIN redact_feature_options ('expression') := 'SYS_CONTEXT(''USERENV'',''SESSION_USER'') =''APPUSER'''; redact_feature_options ('function_type') := 'DBMS_REDACT.PARTIAL'; redact_feature_options ('function_parameters') := 'STR, VVVVVVVVV,VVVVVVVVV, *, 1, 6'; policy_conditions(DBMS_TSDP_PROTECT.DATATYPE) := 'VARCHAR2'; DBMS_TSDP_PROTECT.ADD_POLICY ('PARTIAL_MASK_POLICY', DBMS_TSDP_PROTECT.REDACT, redact_feature_options, policy_conditions); END;