

CREATE TABLE annotation (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	statement TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, statement, object)
);

CREATE TABLE assertion (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	statement TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, statement)
);

CREATE TABLE attributed_name (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	"namingAuthority" TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, "namingAuthority")
);

CREATE TABLE bundle (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, object)
);

CREATE TABLE compilation (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);

CREATE TABLE confidence_facet (
	confidence INTEGER NOT NULL, 
	PRIMARY KEY (confidence)
);

CREATE TABLE contextual_compilation (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, object)
);

CREATE TABLE controlled_vocabulary (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	"constrainingVocabularyReference" TEXT, 
	"constrainingVocabularyName" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, "constrainingVocabularyReference", "constrainingVocabularyName", value)
);

CREATE TABLE enclosing_compilation (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, object)
);

CREATE TABLE external_reference (
	"referenceURL" TEXT, 
	"definingContext" TEXT, 
	"externalIdentifier" TEXT, 
	PRIMARY KEY ("referenceURL", "definingContext", "externalIdentifier")
);

CREATE TABLE grouping (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	context TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, object, context)
);

CREATE TABLE identity_abstraction (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);

CREATE TABLE item (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);

CREATE TABLE marking_definition_abstraction (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);

CREATE TABLE modus_operandi (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);

CREATE TABLE relationship (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	"endTime" TIME, 
	"startTime" TIME, 
	"kindOfRelationship" TEXT, 
	target TEXT NOT NULL, 
	source TEXT NOT NULL, 
	"isDirectional" BOOLEAN NOT NULL, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag, "endTime", "startTime", "kindOfRelationship", target, source, "isDirectional")
);

CREATE TABLE uco_object (
	"objectMarking" TEXT, 
	"objectCreatedTime" TIME, 
	"modifiedTime" TIME, 
	name TEXT, 
	"specVersion" TEXT, 
	description TEXT, 
	"createdBy" TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("objectMarking", "objectCreatedTime", "modifiedTime", name, "specVersion", description, "createdBy", "externalReference", "hasFacet", tag)
);
