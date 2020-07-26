# Software Bill of Materials (SBOM) Abstract Schemas

This repository contains abstract schemas (format-independent Information Models) for several SBOM standards,
some of which define multiple data models.  Deriving multiple DMs from a single IM ensures content
consistency and enables seamless bridging between data formats.

## License List
Most SBOM formats make use of the software license list maintained by SPDX. [SPDX-3.0](SPDX-3.0/dev)
contains a script that retrieves the latest version of the license list, and versions of the list in
multiple formats.

## Formats
* NTIA Survey - https://www.ntia.gov/SBOM
* CycloneDX - https://cyclonedx.org/, https://github.com/CycloneDX/specification/tree/master/schema
* Software Package Data Exchange (SPDX) - https://spdx.org/specifications
* Software Identification (SWID) Tags - https://webstore.ansi.org/Standards/ISO/ISOIEC197702015
* Concise Software Identification Tags - https://datatracker.ietf.org/doc/draft-ietf-sacm-coswid/