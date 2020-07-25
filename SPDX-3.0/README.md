# SPDX 3.0 Base Model Schemas

### Notation

This directory contains a text-format [Information Model](https://en.wikipedia.org/wiki/Information_model)
for SPDX 3.0 derived from the graphic-format Base Model diagram.

> Within the field of software engineering and data modeling an information model is usually an abstract,
> formal representation of entity types that may include their properties, relationships and the operations
> that can be performed on them.
> An information model provides formalism to the description of a problem domain without constraining how
> that description is mapped to an actual implementation in software.

The text and graphical representations describe the identical SPDX 3.0 information model; the two viewpoints are
intended to complement each other for developing and documenting that model. The text representation is
JSON Abstract Data Notation ([JADN](https://github.com/oasis-tcs/openc2-jadn/blob/working/jadn-v1.0-wd01.md)),
a formalism initially created for the OpenC2 protocol.

### Observations

* The diagram does not designate a root type. The schema dependency graph shows that no type definitions refer
to *SpdxElement*, so somewhat counter-intuitively, that definition is designated as the schema root. It may be
worth investigating if the entity relationships can be refactored so that *SpdxDocument* becomes the top-level
(unreferenced) definition.

* Types not defined on the diagram, such as IdString, Relationship/Type, Hash/Algorithm, etc. are maintained
in a separate "types" schema. Large enumerations should remain separate. Simple definitions such as the format
of IdString may also be maintained separately from the diagram, but everything referenced by the diagram must
be defined somewhere.

* There are two ways of interpreting items shown as empty arrowheads on the diagram: incorporating (inheriting)
properties from the head of the arrow into the object at the tail, or referencing the tail objects as a
discriminated union (choice) property within the head object.  Since Person/Organization/Tool are not
referenced anywhere except by Identity, it seems reasonable to interpret them as subtypes of Identity
rather than interpreting Identity as properties of Person and Organization and Tool.

* The SpdxDocument/Creator property has a singular name, but the arrowhead end at Identity has multiplicity
"1..*".  Presumably a document has one creator, and the multiplicity is a typo that should be 1.

* ExternalReference doesn't show types for Category, Type and Locator. They should be given names like
AnnotationType or IdString so that they can be defined somewhere.

* Hash is shown as an entity with two properties named "Algorithm" and "Value".  This is an example of what
[W3C Transformations] calls "Grotesque" or "UnFriendly" style in which the literal property strings "Algorithm"
and "Value" appear in the data, as opposed to "Friendly" styles where the properties are algorithm name and
hash value directly.  We may want to consider using friendly definitions, for the reasons given in the slides.