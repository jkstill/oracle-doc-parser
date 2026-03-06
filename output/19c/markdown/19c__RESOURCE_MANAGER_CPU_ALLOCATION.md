---
id: 19c__RESOURCE_MANAGER_CPU_ALLOCATION
name: RESOURCE_MANAGER_CPU_ALLOCATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: RESOURCE_MANAGER_CPU_ALLOCATION.html
---

# RESOURCE_MANAGER_CPU_ALLOCATION

The number of logical CPUs reported by the operating system.

## Usage Notes

Note: The RESOURCE_MANAGER_CPU_ALLOCATION parameter is deprecated. It is retained for backward compatibility only. Use the CPU_COUNT parameter instead. The Resource Manager schedules database sessions on the CPUs according to a resource plan that has been configured and enabled by the DBA. Normally, the Resource Manager schedules enough database sessions to keep all CPUs utilized. However, in some scenarios, a DBA may only want to schedule enough database sessions to keep a subset of the CPUs utilized. See Also: " CPU_COUNT " Note: The RESOURCE_MANAGER_CPU_ALLOCATION parameter is deprecated. It is retained for backward compatibility only. Use the CPU_COUNT parameter instead. See Also: " CPU_COUNT "