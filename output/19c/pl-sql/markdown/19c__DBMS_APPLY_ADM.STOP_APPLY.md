---
id: 19c__DBMS_APPLY_ADM.STOP_APPLY
name: DBMS_APPLY_ADM.STOP_APPLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.STOP_APPLY

This procedure stops the apply component from applying messages and rolls back any unfinished transactions being applied.

## Syntax

```sql
DBMS_APPLY_ADM.STOP_APPLY(
   apply_name  IN  VARCHAR2,
   force       IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The apply component name. A NULL setting is not allowed. Do not specify an owner. |
| force | BOOLEAN | IN | If TRUE , then the procedure stops the apply component as soon as possible. If FALSE , then the procedure stops the apply component after ensuring that there are no gaps in the set of applied transactions. The behavior of the apply component depends on the setting specified for the force parameter and the setting specified for the commit_serialization apply component parameter. See " Usage Notes " for more information. |

## Usage Notes

Syntax DBMS_APPLY_ADM.STOP_APPLY( apply_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 21-30 STOP_APPLY Procedure Parameters Parameter Description apply_name The apply component name. A NULL setting is not allowed. Do not specify an owner. force If TRUE , then the procedure stops the apply component as soon as possible. If FALSE , then the procedure stops the apply component after ensuring that there are no gaps in the set of applied transactions. The behavior of the apply component depends on the setting specified for the force parameter and the setting specified for the commit_serialization apply component parameter. See " Usage Notes " for more information. Usage Notes The following usage notes apply to this procedure: Apply Component Status Queue Subprograms Have No Effect on Apply Component Status The STOP_APPLY force Parameter and the commit_serialization Apply Parameter The STOP_APPLY Procedure and XStream Outbound Servers The STOP_APPLY Procedure and XStream Inbound Servers Apply Component Status The apply component status is persistently recorded. Hence, if the status is DISABLED or ABORTED , then the apply component is not started upon database instance startup. Queue Subprograms Have No Effect on Apply Component Status The enqueue and dequeue state of DBMS_AQADM.START_QUEUE and DBMS_AQADM.STOP_QUEUE have no effect on the STOP status of an apply component. The STOP_APPLY force Parameter and the commit_serialization Apply Parameter The following table describes apply component behavior for each setting of the force parameter in the STOP_APPLY procedure and the commit_serialization apply component parameter. In all cases, the apply component rolls back any unfinished transactions when it stops. force commit_serialization Apply Component Behavior TRUE FULL The apply component stops immediately and does not apply any unfinished transactions. TRUE DEPENDENT_TRANSACTIONS When the apply component stops, some transactions that have been applied locally might have committed at the source database at a later point in time than some transactions that have not been applied locally. FALSE FULL The apply component stops after applying the next uncommitted transaction in the commit order, if any such transaction is in progress. FALSE DEPENDENT_TRANSACTIONS Before stopping, the apply component applies all of the transactions that have a commit time that is earlier than the applied transaction with the most recent commit time. For example, assume that the commit_serialization apply component parameter is set to DEPENDENT_TRANSACTIONS and there are three transactions: transaction 1 has the earliest commit time, transaction 2 is committed after transaction 1, and transaction 3 has the latest commit time. Also assume that an apply component has applied transaction 1 and transaction 3 and is in the process of applying transaction 2 when the STOP_APPLY procedure is run. Given this scenario, if the force parameter is set to TRUE , then transaction 2 is not applied, and the apply component stops (transaction 2 is rolled back). If, however, the force parameter is set to FALSE , then transaction 2 is applied before the apply component stops. A different scenario would result if the commit_serialization apply component parameter is set to FULL . For example, assume that the commit_serialization apply component parameter is set to FULL and there are three transactions: transaction A has the earliest commit time, transaction B is committed after transaction A, and transaction C has the latest commit time. In this case, the apply component has applied transaction A and is in the process of applying transactions B and C when the STOP_APPLY procedure is run. Given this scenario, if the force parameter is set to TRUE , then transactions B and C are not applied, and the apply component stops (transactions B and C are rolled back). If, however, the force parameter is set to FALSE , then transaction B is applied before the apply component stops, and transaction C is rolled back. See Also: SET_PARAMETER Procedure for more information about the commit_serialization apply component parameter The STOP_APPLY Procedure and XStream Outbound Servers This procedure functions the same way for apply processes and outbound servers. The STOP_APPLY Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers. See Also: SET_PARAMETER Procedure for more information about the commit_serialization apply component parameter