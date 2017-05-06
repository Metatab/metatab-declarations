Metatab

A Method For Storing Hierarchical Data In Tables

Eric Busboom

Civic Knowledge

[eric@civicknowledge.com](mailto:eric@civicknowledge.com)

[ *These specs still have some naming inconsistencies, dues to evolving names. "Metatab" is now the name of the tabular data format; it was previously “STF”. ]*

*[ The **[Metadata Terms* ](https://docs.google.com/document/d/15eYapCeDeqX5uDa-g77CmKpmeu4INUJSQCxewqHJ02I/edit?usp=sharing)*document covers how to declare terms for a Metatab file for specific use ]*

Simple structured data formats like YAML and JSON have become a common way of storing, editing and transmitting information that is logically organized as a hierarchy of objects, with both YAML and JSON providing an uncomplicated, human-readable and human-writable syntax for organizing scalars, lists and dictionaries.  While these formats are a significant improvement over more verbose, cluttered formats like XML, they still require technical skill and knowledge to be able to create syntactically-correct datasets. Additionally, they are poorly suited for comfortably editing many forms of data that are inherently tabular. 

To addresses these issues, we propose a new format which allows storing structured objects in a tabular format. Compared to JSON and YAML, this format's advantages include: 

* Easy to edit using a tool most users already have, a spreadsheet application. 

* Allows for storing structured metadata in the same spreadsheet file as data. 

* Is easier to edit and verify for data that is organized as a sequence of structures, with each structure having the same properties. 

* Non-technical users can read the data immediately, without training or additional tools.  

The Metatab Format is not a replacement for other formats, and it cannot represent arbitrary data structures as easily as other formats can. Instead, it should be used primarily where it is important to provide metadata for tabular datasets, the data structure is predominantly tabular, users have a strong preference for using spreadsheet applications, or users are uncomfortable with structured formats like JSON or XML.

# Example

The following table is a typical example of a Metatab file, representing the metadata for a dataset.

<table>
  <tr>
    <td>Title</td>
    <td>Registered Voters, By County</td>
    <td></td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Percent of the eligible population registered to vote .</td>
    <td></td>
  </tr>
  <tr>
    <td>Section</td>
    <td>documentation</td>
    <td>title</td>
  </tr>
  <tr>
    <td>Homepage</td>
    <td>https://www.cdph.ca.gov//healthycommunityindicators.aspx</td>
    <td>Healthy Communities Data</td>
  </tr>
  <tr>
    <td>Documentation</td>
    <td>https://www.cdph.ca.gov/programs/examples_6-2-14.pdf</td>
    <td>Indicator Documentation for Voter </td>
  </tr>
  <tr>
    <td>.description</td>
    <td>Voter Registration/Participation: Percent of the eligible population.</td>
    <td></td>
  </tr>
</table>


# Metatab File Structure And Terms

A Metatab file is organized in a table, a grid of rows and columns. Both rows and columns must be ordered, so a program reading rows and columns will iterate through them in the same order that the user sees them in the program. The underlying file format is unimportant, but generally, any spreadsheet program file format, such as Excel, Open Office or CSV,  meets the base requirements. 

Each row of the file holds data that will create one or more records. Records have a primary value, a scalar, and may have child terms, so parsing a Metatab file creates a tree of records.  When the child records are terminal, having no children themselves, they will have only a default value and they can be treated as scalar properties of the parent record. Non-terminal records create either lists or dictionaries. 

Each column in the grid has a defined purpose:

* The first column holds a Term, which is a simple or compound name that determines what type of record will be created for the row and what the parent record of the new record will be. 

* The second column holds a Term Value, the record’s scalar value.

* The third and subsequent columns may contain Term Arguments, which generate child terms.  

Terms are case-insensitive.

A Term may be simple or qualified. A simple term is a single word, such as Title, while a qualified term has two words, separated by a ‘.’, such as Title.Language. A simple term create a record that is a child of the root record. A qualified term creates a record as a child of another non-root record.  Simple terms have a qualified form, created by prepending Root, so the qualified form of a Title term is Root.Title. Identity comparison operations on record use the fully qualified terms, so, for instance a Root.Title term is different from a Table.Title term, even though both may appear in the metatab file as Title.  

Here is an example of a Title term and a Title.language child Term:

<table>
  <tr>
    <td>Title</td>
    <td>An Example Data bundles</td>
  </tr>
  <tr>
    <td>Title.Language</td>
    <td>en</td>
  </tr>
</table>


In this example, the first row creates a new Title record with a value as shown in the second column, and the second row adds a Language child record to the Title record. Because the Language record has no children, it can be considered to be a property of the Title record. 

Also note that the Title term in the first row has the qualified version of Root.Title. 

In the second row, "Title" may be omitted. If the value of a term cell starts with a ‘.’, the parent of the record is assumed to be the most recently created record.  The following example has the same result as the previous example:

<table>
  <tr>
    <td>Title</td>
    <td>An Example Data bundles</td>
  </tr>
  <tr>
    <td>.language</td>
    <td>en</td>
  </tr>
</table>


For readability, the child Term is right justified. Cell formatting has no meaning and is ignored. 

The Language child term can also be set with an argument child, as is shown in the next example:  

<table>
  <tr>
    <td>Section</td>
    <td>SectionName</td>
    <td>language</td>
  </tr>
  <tr>
    <td>Title</td>
    <td>An Example Data bundles</td>
    <td>en</td>
  </tr>
</table>


The first row of this table looks like a file header, but the Section term is a data row that sets the parameter map, a list of terms that set the default term name to be associated with term arguments in the same position in the term arguments list. In this example, the Section term row sets the parameter map to a single value list, [‘language’]. Then, in subsequent rows, the value of the third column is matched to the Language term. After matching parameter names to term arguments, the parser creates child records from the matched terms, so the Title term gets a Language child record. The net result is identical to the previous two examples. 

# Labels and Codes

Some terms may have compound values, using a similar form to email addresses, that include both a code and a label. The label is human readable, and the code is a machine readable identifier. The code portion is encapsulated in angle bracket, "<" and “>”. For instance, a value that has a code value of the Census geoid for California might be: 

California <04000US06>

The code is the value between the two brackets, and the label is everything from the start of the string to the first bracket. It is illegal ( or undefined, TBD) to have more than one "<" or more than one “>” in the value, the “<” must come before “>”, and the “>” must be the last non blank in the value. Both the code and the label are stripped of any leading or trailing blanks. 

Terms that have values of this form may produce two term records, one for the label and one for the value. Depending on how the term is configured in the Declare doc, the either the code or the label may be retained in the original term, and the new term may be a sibling or a child. TBD. 

# Parsing process

The conceptual parsing process takes a collection of metadata files, which are linked through includes, traverses them to produce a sequence of term rows, then parses the term rows to produce a sequence of term records. The sequence of term records can then be processed or converted to a hierarchical data structure.  

Rows are fed to the parser in the order they appear in the file, from top to bottom. 

For each row, the parser may:

* Create a record for a term.

* Alter the term parameter map

* Include another file, and begin generating rows from it

## Initialization

The parsing process begins with an initial Metatab file, with a set of variables initialized as:

1. The **parameter map** is empty

2. The **last record map** is empty

3. The **last record** is the Root record

## Main Loop

For each row in the Metatab file:

1. Assign parts of each row to variables

2. Handle special, non-generating terms

3. Handle record generating terms

### Assign Components To Variables

Assign components of the parsed row from the input row to variables

1. The **term** is the first column of the row.

2. The **value** is the second column of the row

3. The **term arguments** are the third through remaining columns of the row

If the **term** includes a ‘.’:

1. If there is a term before the ‘.’, assign it to the **parent term**

2. If there is not a term before the ‘.’, the **parent term** is the term of the** last record**.

3. The term after the ‘.’ is the **record term**

If the term does not include a ‘.’, 

1. The **record term** is set to the **term**. 

2. The **parent term** is ‘Root’

### Handle special terms

Some terms, Term and Section, have a side effect of setting the parameter name map to the term arguments. The value of each argument position is assigned to the parameter map, so the Nth argument is assigned as the name to the Nth parameter in the parameter map. 

When a future term creates a record, and the row has term arguments, the names in the parameter map are assigned to the arguments by matching the each parameter with the argument in the same position. Then, the terms and their values are used to create child records. 

<table>
  <tr>
    <td>term</td>
    <td>value</td>
    <td>Arg1</td>
    <td>Arg2</td>
  </tr>
  <tr>
    <td>Record</td>
    <td>Value</td>
    <td>value1</td>
    <td>value2</td>
  </tr>
</table>


In the first row of this table, the Term term causes the parameter map to be updated to [‘Arg1’,’Arg2’]. In the second row, the term arguments are [‘value1’,’value2’]. The parameter map and the term arguments are joined element-wise to result in the creation of two children of the Record record with these terms and term values

* Arg1: value1

* Arg2: value2

When an Include term is encountered, the term value is dereferenced as a new Metatab file to parse. The file is parsed completely, adding records to the record tree -- included files are parsed depth first. After the last row of the file is parsed, parsing resumes after the Include term in the parent file.

The active section at the start of every included file is Root. The active section for the term after an Include is the section that was active before the Include term.

Parsing steps:

1. If the **record term** is Include, begin the parsing process on the file referenced by the value. 

    1. When parsing a new file, the** parameter map, ** l**ast record map** and **last record **are applied only to the file in which they are set. 

    2. It is the responsibility of the parsing application to determine how to resolve the value of an Include term to a file.

2. If the **record term** is Term or Section, set the **parameter map** to the **term arguments. **Parameter maps apply only to the file in which they are set.

In parsing, the Declare term is is a synonym for Includes, and has the same effect. 

After handing a special term, continue with the next row.  

### Handle record generating terms

The most important result of parsing a term row is creating a record for the term. For instance, a "Table" term will create a Table record, and a “Title” term will create a “Title” record. When the record is created, the value in the term value column is set as the primary record value. If the row has values in other columns, these values are term argument. The term arguments are given names, according to the current parameter map, then the terms and their values are used to create child records for the record created by the main term in the row.  

Term values that include a ‘.’ will cause the record to be created as a child of a previously created record.  If the term value starts with ‘.’, the parent record is the one most recently created. If there is a term value before the ‘.’, the parent record is the one of that term that was most recently created. 

Parsing steps for a record generating term

1. Create a new record for the **record term**, assign it as the **last record **and add it to the** last record map.**

2. Add the new record as a child to the last record created with the same term as the **parent term**, as determined from the **last record map.**

3. If there are **term arguments**, create a new record for each of the arguments, using the **parameter map** for term names and the **term arguments** for term values. The new records are added as children of the record created for the **record term**. Child records created from term arguments are not assigned to the last record or last record map. 

# Special Terms

There is a set of built-in terms that have special meaning. These terms are: 

* Section

* Include

* Declare

* DeclareTerm

    * TermValueName

    * ChildPropertyType

    * Section

    * Synonym

    * ValueSet

* DeclareSection

* DeclareValueSet

    * DisplayValue

The Section term introduces a new section. TDB. Resets the parameter map and clears the last parent. 

The Include and Declare terms both include files, as described above. The Declare term has the additional meaning that the included file defines how to parse and interpret a file, using the DeclareTerm, DeclareSection , and DeclareValueSet terms described below. A File referenced by Declare may contain any term, but it should contain only special, non-record generating terms, or terms that provide general metadata. 

## Declaration Documents

The Declare term specifies a file, usually as a URL, that holds other declaration terms that identify sections, terms and values that are permissible, as well as some values that alter parsing and conversion to JSON. Unlike Include documents, Declares documents never produce terms — all of the terms are consumed to produce declaration information. 

All of the declaration terms have pre-defined  child terms, which are always specified in term arguments. 

### DeclareTerm

The DeclareTerm term creates an entry for pre-defined term and also specifies important modifiers for the declared term with term children. The child terms are: 

* TermValueName. Sets the name f the key for values when the document is converted to JSON. If it is not set, the key is ‘@value’. 

* ChildPropertyType. Forces the value of a key to be a specific data type, such as a list, scalar or dictionary. 

* Section. What section the term is value for. 

* Synonym. During the parsing process, terms with replaces the term name with a different name.  

* ValueSet. Names a value set which defines permissible values for the term. 

To allow simple Metatab file to more closely approximate specific object hierarchies, Metatab defines two translation term structures. 

The Synonym term defines a translation from terms equal to the Synonym terms value to the value of the terms first argument. 

For instance after encountering the row:

<table>
  <tr>
    <td>Synonym</td>
    <td>Column</td>
    <td>Table.Column</td>
  </tr>
</table>


All simple Column terms will be translated to compound Table.Column terms. The effect is to require that all Column records are children of the most recently created Table. 

The Synonym term operation compares the term value for Synonym to the term for subsequent rows, case insensitively, and makes a simple substitution. The term value can be of the same same as any valid term, such as Parent.Term, .Term, or Term.

The TermValueName term sets the name of the property in an object, when records are converted to JSON or other formats, for a record’s term value. If this value is not set for a record, and the record hierarchy is expressed in JSON, YAML or XML, the record term values will have a default name that is appropriate for the format. For JSON and YAML, this name is ‘_value’

The ChildPropertyType forces a datatype for children of a record when converting a record hierarchy to JSON or YAML.  The term value is a compound term with the names of the parent and child record terms, and the first term argument is the datatype, which must be one of:

* scalar

* list

* nonlist

* dict

* any

Consider the following input:

<table>
  <tr>
    <td>Parent</td>
    <td>parent</td>
  </tr>
  <tr>
    <td>Parent.Child</td>
    <td>child1</td>
  </tr>
  <tr>
    <td>Parent.Child</td>
    <td>child2</td>
  </tr>
</table>


The JSON conversion is:

<table>
  <tr>
    <td>{
    "parent": {
        "@value": "parent", 
        "child": [
            "child1", 
            "child2"
        ]
    }
}</td>
  </tr>
</table>


If the Metatab input is preceded by:

<table>
  <tr>
    <td>ChildProperryType</td>
    <td>Parent.Child</td>
    <td>scalar</td>
  </tr>
</table>


The value "child" entry in the dictionary will be forced to be a scalar, with later values overwriting earlier ones:

<table>
  <tr>
    <td>{
    "parent": {
        "@value": "parent", 
        "child": "child2"
    }
}
</td>
  </tr>
</table>


The effects of all of the data types are:

* scalar: force the property value to be a scalar, with later values overwriting earlier ones

* list: force the property value to be a list, even if there is only one child record

* dict: force the value to be a sub-dictionary, even if the child record has no children, with later values overwriting earlier ones

* nonlist: force the property value to be either a scalar or a dict, depending on whether the record has children, but regardless of whether there is one or more than one record of the same term. 

* any: Clear the forced type for this term. 

### DeclareSection

The DeclareSection term declares a section name and specifies the arguments for the section. The arguments aren’t checked in parsing, but can be used for setting section arguments after a user selects a new section to add to a document. 

### DeclareValueSet

The DeclareValueSet term

TBD: This term should probably just be called ValueSet, or DefineValueSet, since it is a definition, not a declaration. 

# Conversion to JSON and YAML

The record hierarchies created by parsing Metatab files can be converted to JSON and YAML according to the following procedure. In this description, records are the components created by parsing the Metatab file, and objects are the components created by the conversion process. In many languages, these objects are more likely to be dictionaries or associative arrays. 

For each record in the Metatab record hierarchy:

1. If the record has no children, it will have only the term value, so it can be treated as a scalar property of it’s parent.  Create a scalar property in the parent object (the object associated with the record’s parent). The property name, in the parent object,  is the term name of the record, and the property value is the term value. 

2. If the record has children, create a new object for the record.

    1. If the parent object does not already have a property named for the record term, add the record object as a property of the parent object. The property name in the parent object is the record term name, and the property value is another object. In the child, set a property name ‘@value’ to the term value. 

    2. If the parent does have a property named for the child term, convert the existing value to a list if it is not already a list, and add the child object to the end of the list.

After building the object hierarchy from the record hierarchy,  convert the root object to JSON according to [ECMA 404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf). 

# Example

<table>
  <tr>
    <td>1</td>
    <td>Term</td>
    <td>value</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Title</td>
    <td>Registered Voters, By County</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Description</td>
    <td>Percent of the eligible population registered to vote and the percent who voted in statewide elections.</td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Identifier</td>
    <td>cdph.ca.gov-hci-registered_voters-county</td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Version</td>
    <td>201404</td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Section</td>
    <td>documentation</td>
    <td>title</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Homepage</td>
    <td>https://www.cdph.ca.gov/programs/pages/healthycommunityindicators.aspx</td>
    <td>Healthy Communities Data and Indicators Project (HCI)</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Documentation</td>
    <td>https://www.cdph.ca.gov/programs/Documents/HCI_RegisteredVoters_653_Narrative_and_examples_6-2-14.pdf</td>
    <td>Indicator Documentation for Voter Registration / Participation</td>
  </tr>
  <tr>
    <td>10</td>
    <td>.description</td>
    <td>Voter Registration/Participation: Percent of the eligible population registered to vote and the percent who voted in statewide elections</td>
    <td></td>
  </tr>
</table>


Row 1. Sets the parameter map to be empty. This row may be omitted, but is often included because users expect a header.  

Row 2-5 create records in the Root object.

Row 7 sets the parameter map to be [‘title’], so the third column specifies a Title child record for new records. The value of the second column, "documentation" is for information and has no effect. 

Rows 8 and 9 create new records, both of which have Title children

Row 10 creates a new Description child for the record created in Row 9.

This example table, if parsed to an object tree and jumped as JSON, with default values being given dictionary keys of @value, would be equivalent to:

<table>
  <tr>
    <td>{
    "description": "Percent of ... percent who voted in statewide elections.", 
    "title": "Registered Voters, By County", 
    "documentation": {
        "description": "Voter Registration ... voted in statewide elections", 
        "_value": "https://www.cdph.ca.gov..._examples_6-2-14.pdf", 
        "title": "Indicator Documentation for Voter Registration / Participation"
    }, 
    "version": "201404", 
    "identifier": "cdph.ca.gov-hci-registered_voters-county", 
    "homepage": {
        "_value": "https://www.cdph.ca.gov/..indicators.aspx", 
        "title": "Healthy Communities Data and Indicators Project (HCI)"
    }
}
</td>
  </tr>
</table>


# Term Namespaces

The most common terms are simple words, such as "Title" or “Description,” but many of these words are also part of other metadata specifications, and sometimes, the same word may have conflicting meanings in two specifications.  To account for these discrepancies, it is common practice to assign terms to a namespace. The namespace is the name of a collection of self-consistent terms. When using namespaces, each term has a URL, and the namespace is the common prefix for all of the terms in the collection. For instance, in Dublin Core, the Title term has a URL of “http://purl.org/dc/terms/title” and the Description term has the URL “[http://purl.org/dc/terms/description](http://purl.org/dc/terms/description)”; the namespace is “[http://purl.org/dc/terms/](http://purl.org/dc/terms/).” Because namespace URIs are long, most metadata systems allow the namespace to be assigned to a shorter code. The  “[http://purl.org/dc/terms/](http://purl.org/dc/terms/)” is commonly named dct, so the Title term has a formal name of dct:Title. 

The namespace for Simple Data Bundles is "[http://xuid.net/sdb](http://xuid.net/sdb)/" and the common namespace prefix is sdb:. The sdb: prefix is assumed for terms in the core, so it is not required. 

Many of the terms in the core are defined as synonyms to terms in other namespaces. For instance, the "Title" term which is formally known as sdb:Title is a synonym for dct:Title, So, these terms are all equivalent: 

* Title

* sdb:Title

* dct:Title

In general, the Bundle Metadata can include any terms from any other collection, provided that terms that are not in the core are prefixed with a namespace prefix. If the term is not part of one of the predeclared namespaces, the namespace should be declared with the Namespace term. 

## Predeclared namespaces

These namespace values are predeclared and should not be overridden or changed.

<table>
  <tr>
    <td>Prefix</td>
    <td>Namespace</td>
  </tr>
  <tr>
    <td>mtb</td>
    <td>http://metatab.org</td>
  </tr>
  <tr>
    <td>dcat</td>
    <td>http://www.w3.org/ns/dcat#</td>
  </tr>
  <tr>
    <td>dct</td>
    <td>http://purl.org/dc/terms/</td>
  </tr>
  <tr>
    <td>dctype</td>
    <td>http://purl.org/dc/dcmitype/</td>
  </tr>
  <tr>
    <td>foaf</td>
    <td>http://xmlns.com/foaf/0.1/</td>
  </tr>
  <tr>
    <td>rdf</td>
    <td>http://www.w3.org/1999/02/22-rdf-syntax-ns#</td>
  </tr>
  <tr>
    <td>rdfs</td>
    <td>http://www.w3.org/2000/01/rdf-schema#</td>
  </tr>
  <tr>
    <td>skos</td>
    <td>http://www.w3.org/2004/02/skos/core#</td>
  </tr>
  <tr>
    <td>vcard</td>
    <td>http://www.w3.org/2006/vcard/ns#</td>
  </tr>
  <tr>
    <td>xsd</td>
    <td>http://www.w3.org/2001/XMLSchema#</td>
  </tr>
</table>


