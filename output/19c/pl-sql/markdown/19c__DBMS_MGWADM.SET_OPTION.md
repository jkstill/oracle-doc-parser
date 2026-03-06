---
id: 19c__DBMS_MGWADM.SET_OPTION
name: DBMS_MGWADM.SET_OPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.SET_OPTION

This procedure sets a Messaging Gateway configuration option. It can be used to set an agent option, a messaging link option, or a propagation job option.

## Syntax

```sql
DBMS_MGWADM.SET_OPTION (
   target_type   IN   PLS_INTEGER,
   target_name   IN   VARCHAR2,
   option_name   IN   VARCHAR2,
   option_value  IN   VARCHAR2,
   encrypted     IN   BOOLEAN DEFAULT FALSE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| target_type | PLS_INTEGER | IN | Specifies the target type of the Messaging Gateway entity: DBMS_MGWADM . AGENT_JAVA_PROP to set a Java System property for a Messaging Gateway agent DBMS_MGWADM . MSGLINK_OPTION to set a messaging link option DBMS_MGWADM . JOB_OPTION to set a propagation job option |
| target_name | VARCHAR2 | IN | Name or identifier of the target. The value for this parameter depends on the value specified for target_type parameter. This must not be NULL . |
| option_name | VARCHAR2 | IN | Option name. This must not be NULL . |
| option_value | VARCHAR2 | IN | Option value |
| encrypted | BOOLEAN | IN | Indicates whether the value should be stored as encrypted: TRUE if the value should be stored in an encrypted form FALSE if the value should be stored in a cleartext form |

## Usage Notes

Syntax DBMS_MGWADM.SET_OPTION ( target_type IN PLS_INTEGER, target_name IN VARCHAR2, option_name IN VARCHAR2, option_value IN VARCHAR2, encrypted IN BOOLEAN DEFAULT FALSE ); Parameters Table 110-47 SET_OPTION Procedure Parameters Parameter Description target_type Specifies the target type of the Messaging Gateway entity: DBMS_MGWADM . AGENT_JAVA_PROP to set a Java System property for a Messaging Gateway agent DBMS_MGWADM . MSGLINK_OPTION to set a messaging link option DBMS_MGWADM . JOB_OPTION to set a propagation job option target_name Name or identifier of the target. The value for this parameter depends on the value specified for target_type parameter. This must not be NULL . option_name Option name. This must not be NULL . option_value Option value encrypted Indicates whether the value should be stored as encrypted: TRUE if the value should be stored in an encrypted form FALSE if the value should be stored in a cleartext form See Also: Table 110-10 regarding options for the option_type parameter See Also: Table 110-10 regarding options for the option_type parameter Usage Notes DBMS_MGWADM.AGENT_JAVA_PROP Target The procedure will store an agent option used to set a Java System property when the Messaging Gateway agent is started. The agent must be restarted for the change to take effect. The parameters are interpreted as follows: target_name specifies the name of the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT can be used for the default agent. option_name specifies the Java System property encrypted can be either TRUE or FALSE DBMS_MGWADM.MSGLINK_OPTION Target The procedure will set or alter a single option for a Messaging Gateway messaging system link. This is equivalent to calling DBMS_MGWADM . ALTER_MSGSYSTEM_LINK and using the options parameter to set an option. The parameters are interpreted as follows: target_name specifies the name of the message system link option_name specifies the option to set encrypted must be FALSE DBMS_MGWADM.JOB_OPTION Target The procedure will set or alter a single option for a Messaging Gateway propagation job. This is equivalent to calling DBMS_MGWADM . ALTER_JOB and using the options parameter to set an option. The parameters are interpreted as follows: target_name specifies the name of the propagation job option_name specifies the option to set encrypted must be FALSE