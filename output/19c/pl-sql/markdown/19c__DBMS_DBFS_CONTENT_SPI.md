---
id: 19c__DBMS_DBFS_CONTENT_SPI
name: DBMS_DBFS_CONTENT_SPI
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI

This topic lists operational notes for DBMS_DBFS_CONTENT_SPI implementation, path names, and other operations.

## Usage Notes

Implementation Path Names Other DBMS_DBFS_CONTENT Operations Since the interconnection of the DBMS_DBFS_CONTENT interface and the provider SPI is a 1-to-many pluggable architecture, the interface uses dynamic SQL to invoke methods in the provider SPI, this can lead to runtime errors. There are no explicit INIT or FINI methods to indicate when the DBMS_DBFS_CONTENT interface plugs or unplugs a particular provider SPI. Provider SPIs must be willing to auto-initialize themselves at any SPI entry-point. All operations performed by a store provider are "stateless" in that they are complete operations unto themselves. If state is necessary to be maintained for some reason, then the state must be maintained in data structures such as auxiliary tables that can be queried as needed. All path names used in the provider SPI are store-qualified in pair form ( store_name , pathname ) where the path name is rooted within the store namespace. Stores and their providers that support contentID-based access (see FEATURE_CONTENT_ID in Table 52-5 ) also support a form of addressing that is not based on path names. Content items are identified by an explicit store name, a NULL path name, and possibly a contentID specified as a parameter or by way of the OPT_CONTENT_ID (see Table 52-8 ) property. Not all operations are supported with contentID-based access, and applications should depend only on the simplest create or delete functionality being available. Other DBMS_DBFS_CONTENT Operations This table lists other operations and provides links to related discussions.