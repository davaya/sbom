# SPDX License List converter

This program reads the SPDX license list data in JSON format from GitHub, extracts the fields needed
to create **LicenseList** and **ExceptionList** enums, and creates a JADN schema module that can
be referenced by other schemas.

* **license_list_source.jidl:** JADN Schema for the SPDX license list, derived from the current contents.
If additional fields are populated, or if some fields shown as required are not populated, the schema should
be modified accordingly.

* **license_list_source.json:** derived JSON Schema file.

* **data/** output directory containing:
    * JADN schema module created by the *make* script
    * JIDL, HTML, and Markdown versions of the schema, for use in documentation
    * JSON schema containing the LicenseList and ExceptionList enumerations
