---
id: 19c__ALL_CONSTRAINTS
name: ALL_CONSTRAINTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: integrity
tags: [all]
source_file: ALL_CONSTRAINTS.html
---

# ALL_CONSTRAINTS

ALL_CONSTRAINTS describes constraint definitions on tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the constraint definition |
| CONSTRAINT_NAME | VARCHAR2(128) | Name of the constraint definition |
| CONSTRAINT_TYPE | VARCHAR2(1) | Type of the constraint definition: C - Check constraint on a table P - Primary key U - Unique key R - Referential integrity V - With check option, on a view O - With read only, on a view H - Hash expression F - Constraint that involves a REF column S - Supplemental logging |
| TABLE_NAME | VARCHAR2(128) | Name associated with the table (or view) with the constraint definition |
| SEARCH_CONDITION | LONG | Text of search condition for a check constraint. This column returns the correct value only when the row originates from the current container. |
| SEARCH_CONDITION_VC | VARCHAR2(4000) | Text of search condition for a check constraint. This column may truncate the search condition. |
| R_OWNER | VARCHAR2(128) | Owner of the table referred to in a referential constraint |
| R_CONSTRAINT_NAME | VARCHAR2(128) | Name of the unique constraint definition for the referenced table |
| DELETE_RULE | VARCHAR2(9) | Delete rule for a referential constraint: CASCADE SET NULL NO ACTION |
| STATUS | VARCHAR2(8) | Enforcement status of the constraint: ENABLED DISABLED |
| DEFERRABLE | VARCHAR2(14) | Indicates whether the constraint is deferrable ( DEFERRABLE ) or not ( NOT DEFERRABLE ) |
| DEFERRED | VARCHAR2(9) | Indicates whether the constraint was initially deferred ( DEFERRED ) or not ( IMMEDIATE ) |
| VALIDATED | VARCHAR2(13) | When STATUS = ENABLED , possible values are: VALIDATED - All data obeys the constraint (that is, the existing data in the table was validated when the constraint was enabled, as well as any subsequent data entered into the table) NOT VALIDATED - All data may not obey the constraint (that is, the existing data in the table was not validated when the constraint was enabled, but subsequent data entered into the table was validated) When STATUS = DISABLED , possible values are: VALIDATED - All data obeys the constraint, but the unique index on the constraint has been dropped. This setting is useful in data warehousing environments, but has some restrictions. Refer to Oracle Database Data Warehousing Guide for more information on this setting. NOT VALIDATED - All data may not obey the constraint |
| GENERATED | VARCHAR2(14) | Indicates whether the name of the constraint is user-generated ( USER NAME ) or system-generated ( GENERATED NAME ) |
| BAD | VARCHAR2(3) | Indicates whether this constraint specifies a century in an ambiguous manner ( BAD ) or not (NULL). To avoid errors resulting from this ambiguity, rewrite the constraint using the TO_DATE function with a four-digit year. See Also: the TO_DATE function in Oracle Database SQL Language Reference and Oracle Database Development Guide |
| RELY | VARCHAR2(4) | When VALIDATED = NOT VALIDATED , this column indicates whether the constraint is to be taken into account for query rewrite ( RELY ) or not (NULL). When VALIDATED = VALIDATED , this column is not meaningful. See Also: constraints in Oracle Database SQL Language Reference |
| LAST_CHANGE | DATE | When the constraint was last enabled or disabled |
| INDEX_OWNER | VARCHAR2(128) | Name of the user owning the index |
| INDEX_NAME | VARCHAR2(128) | Name of the index (only shown for unique and primary-key constraints) |
| INVALID | VARCHAR2(7) | Indicates whether the constraint is invalid ( INVALID ) or not (NULL) |
| VIEW_RELATED | VARCHAR2(14) | Indicates whether the constraint depends on a view ( DEPEND ON VIEW ) or not (NULL) |
| ORIGIN_CON_ID | VARCHAR2(256) | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CONSTRAINTS describes all constraint definitions in the database. USER_CONSTRAINTS describes constraint definitions on tables in the current user's schema. See Also: " DBA_CONSTRAINTS " " USER_CONSTRAINTS " See Also: " DBA_CONSTRAINTS " " USER_CONSTRAINTS "