---
id: 19c__UTL_REF
name: UTL_REF
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_REF
tags: [utl_ref]
source_file: UTL_REF.html
---

# UTL_REF

Exceptions can be returned during execution of UTL_REF functions for various reasons.

## Usage Notes

For example, the following scenarios would result in exceptions: The object selected does not exist. This could be because either: The object has been deleted, or the given reference is dangling (invalid). The object table was dropped or does not exist. The object cannot be modified or locked in a serializable transaction. The object was modified by another transaction after the serializable transaction started. You do not have the privilege to select or modify the object. The caller of the UTL_REF subprogram must have the proper privilege on the object that is being selected or modified. The UTL_REF package does not define any named exceptions. You may define exception handling blocks to catch specific exceptions and to handle them appropriately.