---
id: 19c__ALL_OBJECTS
name: ALL_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_OBJECTS.html
---

# ALL_OBJECTS

ALL_OBJECTS describes all objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the subobject (for example, partition) |
| OBJECT_ID | NUMBER | Dictionary object number of the object |
| DATA_OBJECT_ID | NUMBER | Dictionary object number of the segment that contains the object. Note: OBJECT_ID and DATA_OBJECT_ID display data dictionary metadata. Do not confuse these numbers with the unique 16-byte object identifier ( object ID ) that Oracle Database assigns to row objects in object tables in the system. |
| OBJECT_TYPE | VARCHAR2(23) | Type of the object (such as TABLE , INDEX ) |
| CREATED | DATE | Timestamp for the creation of the object |
| LAST_DDL_TIME | DATE | Timestamp for the last modification of the object and dependent objects resulting from a DDL statement (including grants and revokes) |
| TIMESTAMP | VARCHAR2(19) | Timestamp for the specification of the object (character data) |
| STATUS | VARCHAR2(7) | Status of the object: VALID INVALID N/A |
| TEMPORARY | VARCHAR2(1) | Indicates whether the object is temporary (the current session can see only data that it placed in this object itself) ( Y ) or not ( N ) |
| GENERATED | VARCHAR2(1) | Indicates whether the name of this object was system-generated ( Y ) or not ( N ) |
| SECONDARY | VARCHAR2(1) | Indicates whether this is a secondary object created by the ODCIIndexCreate method of the Oracle Data Cartridge ( Y ) or not ( N ) |
| NAMESPACE | NUMBER | Namespace for the object |
| EDITION_NAME | VARCHAR2(128) | Name of the edition in which the object is actual |
| SHARING | VARCHAR2(18) | Values: DATA LINK - If the object is data-linked or a data link to an object in the root METADATA LINK - If the object is metadata-linked or a metadata link to an object in the root EXTENDED DATA LINK - If the object is extended-data-linked or an extended data link to an object in the root NONE - If none of the above applies |
| EDITIONABLE | VARCHAR2(1) | Values: Y - For objects marked EDITIONABLE N - For objects marked NONEDITIONABLE NULL - For objects whose type is not editionable in the database |
| ORACLE_MAINTAINED | VARCHAR2(1) | Denotes whether the object was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). An object for which this column has the value Y must not be changed in any way except by running an Oracle-supplied script. |
| APPLICATION | VARCHAR2(1) | Indicates whether the object is an Application common object ( Y ) or not ( N ) |
| DEFAULT_COLLATION | VARCHAR2(100) | Default collation for the object |
| DUPLICATED | VARCHAR2(1) | Indicates whether this object is duplicated on this shard ( Y ) or not ( N ) |
| SHARDED | VARCHAR2(1) | Indicates whether this object is sharded ( Y ) or not ( N ) |
| CREATED_APPID | NUMBER | ID of the Application that created the object |
| CREATED_VSNID | NUMBER | ID of the Application Version that created the object |
| MODIFIED_APPID | NUMBER | ID of the Application that last modified the object |
| MODIFIED_VSNID | NUMBER | ID of the Application Version that last modified the object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_OBJECTS describes all objects in the database. USER_OBJECTS describes all objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_OBJECTS " " USER_OBJECTS " See Also: " DBA_OBJECTS " " USER_OBJECTS "