# Auto generated from uco_core.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-05T22:38:21
# Schema: uco-core
#
# id: https://w3id.org/lmodel/uco/core
# description: This ontology defines classes and properties that are shared across the various UCO ontologies. At
#              a high-level, the UCO core ontology provides base classes, relationship-oriented classes,
#              content-aggregation classes, and shared classes.
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDTime

metamodel_version = "1.7.0"
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
UCO_CORE = CurieNamespace('uco_core', 'https://w3id.org/lmodel/uco-core/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = UCO_CORE


# Types
class StringType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = UCO_CORE.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = UCO_CORE.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = UCO_CORE.NonNegativeIntegerType


class StatementType(StringType):
    """ meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = UCO_CORE.StatementType


class IriType(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = UCO_CORE.IriType


class BooleanType(Boolean):
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = UCO_CORE.BooleanType


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = UCO_CORE.TimeType


# Class references



class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.UcoThing
    class_class_curie: ClassVar[str] = "uco_core:UcoThing"
    class_name: ClassVar[str] = "uco thing"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "uco_core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "uco inherent characterization thing"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.UcoInherentCharacterizationThing


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.ExternalReference
    class_class_curie: ClassVar[str] = "uco_core:ExternalReference"
    class_name: ClassVar[str] = "external reference"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Facet
    class_class_curie: ClassVar[str] = "uco_core:Facet"
    class_name: ClassVar[str] = "facet"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Facet


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "uco_core:ConfidenceFacet"
    class_name: ClassVar[str] = "confidence facet"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.UcoObject
    class_class_curie: ClassVar[str] = "uco_core:UcoObject"
    class_name: ClassVar[str] = "uco object"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.UcoObject

    objectMarking: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, TimeType]] = None
    modifiedTime: Optional[Union[Union[str, TimeType], List[Union[str, TimeType]]]] = empty_list()
    name: Optional[Union[str, StringType]] = None
    specVersion: Optional[Union[str, StringType]] = None
    description: Optional[str] = None
    createdBy: Optional[Union[str, IriType]] = None
    externalReference: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    hasFacet: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    tag: Optional[Union[Union[str, StringType], List[Union[str, StringType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, IriType) else IriType(v) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, TimeType):
            self.objectCreatedTime = TimeType(self.objectCreatedTime)

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, TimeType) else TimeType(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, StringType):
            self.name = StringType(self.name)

        if self.specVersion is not None and not isinstance(self.specVersion, StringType):
            self.specVersion = StringType(self.specVersion)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.createdBy is not None and not isinstance(self.createdBy, IriType):
            self.createdBy = IriType(self.createdBy)

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, IriType) else IriType(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, IriType) else IriType(v) for v in self.hasFacet]

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, StringType) else StringType(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Assertion
    class_class_curie: ClassVar[str] = "uco_core:Assertion"
    class_name: ClassVar[str] = "assertion"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Assertion

    statement: Optional[Union[Union[str, StringType], List[Union[str, StringType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, StringType) else StringType(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Annotation
    class_class_curie: ClassVar[str] = "uco_core:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Annotation

    object: Union[Union[str, IriType], List[Union[str, IriType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, IriType) else IriType(v) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.AttributedName
    class_class_curie: ClassVar[str] = "uco_core:AttributedName"
    class_name: ClassVar[str] = "attributed name"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.AttributedName

    namingAuthority: Optional[Union[str, StringType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, StringType):
            self.namingAuthority = StringType(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Compilation
    class_class_curie: ClassVar[str] = "uco_core:Compilation"
    class_name: ClassVar[str] = "compilation"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "uco_core:ContextualCompilation"
    class_name: ClassVar[str] = "contextual compilation"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "uco_core:ControlledVocabulary"
    class_name: ClassVar[str] = "controlled vocabulary"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.ControlledVocabulary

    value: Union[str, StringType] = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, StringType):
            self.value = StringType(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "uco_core:EnclosingCompilation"
    class_name: ClassVar[str] = "enclosing compilation"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.EnclosingCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Bundle
    class_class_curie: ClassVar[str] = "uco_core:Bundle"
    class_name: ClassVar[str] = "bundle"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Bundle

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Grouping
    class_class_curie: ClassVar[str] = "uco_core:Grouping"
    class_name: ClassVar[str] = "grouping"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "uco_core:IdentityAbstraction"
    class_name: ClassVar[str] = "identity abstraction"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.IdentityAbstraction


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Item
    class_class_curie: ClassVar[str] = "uco_core:Item"
    class_name: ClassVar[str] = "item"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking:MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "uco_core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "marking definition abstraction"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.MarkingDefinitionAbstraction


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "uco_core:ModusOperandi"
    class_name: ClassVar[str] = "modus operandi"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE.Relationship
    class_class_curie: ClassVar[str] = "uco_core:Relationship"
    class_name: ClassVar[str] = "relationship"
    class_model_uri: ClassVar[URIRef] = UCO_CORE.Relationship

    target: Union[str, IriType] = None
    source: Union[Union[str, IriType], List[Union[str, IriType]]] = None
    isDirectional: Union[bool, BooleanType] = None
    endTime: Optional[Union[str, TimeType]] = None
    startTime: Optional[Union[str, TimeType]] = None
    kindOfRelationship: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, IriType):
            self.target = IriType(self.target)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, IriType) else IriType(v) for v in self.source]

        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self.endTime is not None and not isinstance(self.endTime, TimeType):
            self.endTime = TimeType(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, TimeType):
            self.startTime = TimeType(self.startTime)

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.confidence = Slot(uri=UCO_CORE.confidence, name="confidence", curie=UCO_CORE.curie('confidence'),
                   model_uri=UCO_CORE.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=UCO_CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=UCO_CORE.curie('constrainingVocabularyName'),
                   model_uri=UCO_CORE.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=UCO_CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=UCO_CORE.curie('constrainingVocabularyReference'),
                   model_uri=UCO_CORE.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=UCO_CORE.context, name="context", curie=UCO_CORE.curie('context'),
                   model_uri=UCO_CORE.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=UCO_CORE.createdBy, name="createdBy", curie=UCO_CORE.curie('createdBy'),
                   model_uri=UCO_CORE.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=UCO_CORE.definingContext, name="definingContext", curie=UCO_CORE.curie('definingContext'),
                   model_uri=UCO_CORE.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=UCO_CORE.description, name="description", curie=UCO_CORE.curie('description'),
                   model_uri=UCO_CORE.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=UCO_CORE.endTime, name="endTime", curie=UCO_CORE.curie('endTime'),
                   model_uri=UCO_CORE.endTime, domain=None, range=Optional[Union[str, TimeType]])

slots.externalIdentifier = Slot(uri=UCO_CORE.externalIdentifier, name="externalIdentifier", curie=UCO_CORE.curie('externalIdentifier'),
                   model_uri=UCO_CORE.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=UCO_CORE.externalReference, name="externalReference", curie=UCO_CORE.curie('externalReference'),
                   model_uri=UCO_CORE.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=UCO_CORE.hasFacet, name="hasFacet", curie=UCO_CORE.curie('hasFacet'),
                   model_uri=UCO_CORE.hasFacet, domain=Facet, range=Optional[str])

slots.isDirectional = Slot(uri=UCO_CORE.isDirectional, name="isDirectional", curie=UCO_CORE.curie('isDirectional'),
                   model_uri=UCO_CORE.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=UCO_CORE.kindOfRelationship, name="kindOfRelationship", curie=UCO_CORE.curie('kindOfRelationship'),
                   model_uri=UCO_CORE.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=UCO_CORE.modifiedTime, name="modifiedTime", curie=UCO_CORE.curie('modifiedTime'),
                   model_uri=UCO_CORE.modifiedTime, domain=None, range=Optional[Union[str, TimeType]])

slots.name = Slot(uri=UCO_CORE.name, name="name", curie=UCO_CORE.curie('name'),
                   model_uri=UCO_CORE.name, domain=None, range=Optional[Union[str, StringType]])

slots.namingAuthority = Slot(uri=UCO_CORE.namingAuthority, name="namingAuthority", curie=UCO_CORE.curie('namingAuthority'),
                   model_uri=UCO_CORE.namingAuthority, domain=None, range=Optional[Union[str, StringType]])

slots.object = Slot(uri=UCO_CORE.object, name="object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_CORE.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=UCO_CORE.objectCreatedTime, name="objectCreatedTime", curie=UCO_CORE.curie('objectCreatedTime'),
                   model_uri=UCO_CORE.objectCreatedTime, domain=None, range=Optional[Union[str, TimeType]])

slots.objectMarking = Slot(uri=UCO_CORE.objectMarking, name="objectMarking", curie=UCO_CORE.curie('objectMarking'),
                   model_uri=UCO_CORE.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=UCO_CORE.referenceURL, name="referenceURL", curie=UCO_CORE.curie('referenceURL'),
                   model_uri=UCO_CORE.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=UCO_CORE.source, name="source", curie=UCO_CORE.curie('source'),
                   model_uri=UCO_CORE.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=UCO_CORE.specVersion, name="specVersion", curie=UCO_CORE.curie('specVersion'),
                   model_uri=UCO_CORE.specVersion, domain=None, range=Optional[Union[str, StringType]])

slots.startTime = Slot(uri=UCO_CORE.startTime, name="startTime", curie=UCO_CORE.curie('startTime'),
                   model_uri=UCO_CORE.startTime, domain=None, range=Optional[Union[str, TimeType]])

slots.statement = Slot(uri=UCO_CORE.statement, name="statement", curie=UCO_CORE.curie('statement'),
                   model_uri=UCO_CORE.statement, domain=None, range=Optional[Union[str, StringType]])

slots.tag = Slot(uri=UCO_CORE.tag, name="tag", curie=UCO_CORE.curie('tag'),
                   model_uri=UCO_CORE.tag, domain=None, range=Optional[Union[str, StringType]])

slots.target = Slot(uri=UCO_CORE.target, name="target", curie=UCO_CORE.curie('target'),
                   model_uri=UCO_CORE.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=UCO_CORE.value, name="value", curie=UCO_CORE.curie('value'),
                   model_uri=UCO_CORE.value, domain=None, range=Optional[Union[str, StringType]])

slots.annotation_object = Slot(uri=UCO_CORE.object, name="annotation_object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_CORE.annotation_object, domain=Annotation, range=Union[Union[str, IriType], List[Union[str, IriType]]])

slots.assertion_statement = Slot(uri=UCO_CORE.statement, name="assertion_statement", curie=UCO_CORE.curie('statement'),
                   model_uri=UCO_CORE.assertion_statement, domain=Assertion, range=Optional[Union[Union[str, StringType], List[Union[str, StringType]]]])

slots.confidence_facet_confidence = Slot(uri=UCO_CORE.confidence, name="confidence facet_confidence", curie=UCO_CORE.curie('confidence'),
                   model_uri=UCO_CORE.confidence_facet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.contextual_compilation_object = Slot(uri=UCO_CORE.object, name="contextual compilation_object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_CORE.contextual_compilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.controlled_vocabulary_value = Slot(uri=UCO_CORE.value, name="controlled vocabulary_value", curie=UCO_CORE.curie('value'),
                   model_uri=UCO_CORE.controlled_vocabulary_value, domain=ControlledVocabulary, range=Union[str, StringType])

slots.enclosing_compilation_object = Slot(uri=UCO_CORE.object, name="enclosing compilation_object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_CORE.enclosing_compilation_object, domain=EnclosingCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.grouping_context = Slot(uri=UCO_CORE.context, name="grouping_context", curie=UCO_CORE.curie('context'),
                   model_uri=UCO_CORE.grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.relationship_target = Slot(uri=UCO_CORE.target, name="relationship_target", curie=UCO_CORE.curie('target'),
                   model_uri=UCO_CORE.relationship_target, domain=Relationship, range=Union[str, IriType])

slots.relationship_source = Slot(uri=UCO_CORE.source, name="relationship_source", curie=UCO_CORE.curie('source'),
                   model_uri=UCO_CORE.relationship_source, domain=Relationship, range=Union[Union[str, IriType], List[Union[str, IriType]]])

slots.relationship_isDirectional = Slot(uri=UCO_CORE.isDirectional, name="relationship_isDirectional", curie=UCO_CORE.curie('isDirectional'),
                   model_uri=UCO_CORE.relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.uco_object_createdBy = Slot(uri=UCO_CORE.createdBy, name="uco object_createdBy", curie=UCO_CORE.curie('createdBy'),
                   model_uri=UCO_CORE.uco_object_createdBy, domain=UcoObject, range=Optional[Union[str, IriType]])

slots.uco_object_externalReference = Slot(uri=UCO_CORE.externalReference, name="uco object_externalReference", curie=UCO_CORE.curie('externalReference'),
                   model_uri=UCO_CORE.uco_object_externalReference, domain=UcoObject, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.uco_object_hasFacet = Slot(uri=UCO_CORE.hasFacet, name="uco object_hasFacet", curie=UCO_CORE.curie('hasFacet'),
                   model_uri=UCO_CORE.uco_object_hasFacet, domain=UcoObject, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.uco_object_modifiedTime = Slot(uri=UCO_CORE.modifiedTime, name="uco object_modifiedTime", curie=UCO_CORE.curie('modifiedTime'),
                   model_uri=UCO_CORE.uco_object_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, TimeType], List[Union[str, TimeType]]]])

slots.uco_object_objectMarking = Slot(uri=UCO_CORE.objectMarking, name="uco object_objectMarking", curie=UCO_CORE.curie('objectMarking'),
                   model_uri=UCO_CORE.uco_object_objectMarking, domain=UcoObject, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.uco_object_tag = Slot(uri=UCO_CORE.tag, name="uco object_tag", curie=UCO_CORE.curie('tag'),
                   model_uri=UCO_CORE.uco_object_tag, domain=UcoObject, range=Optional[Union[Union[str, StringType], List[Union[str, StringType]]]])