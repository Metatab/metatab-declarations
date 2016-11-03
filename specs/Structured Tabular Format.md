Structured Tabular Format

A Method For Storing Hierarchical Data In Tables

Eric Busboom

Civic Knowledge

[eric@civicknowledge.com](mailto:eric@civicknowledge.com)

Simple structured data formats like YAML and JSON have become a common way of storing, editing and transmitting information that is logically organized as a hierarchy of objects, with both YAML and JSON providing an uncomplicated, human-readable and human-writable syntax for organizing scalars, lists and dictionaries.  While these formats are a significant improvement over more verbose, cluttered formats like XML, they still require technical skill and knowledge to be able to create syntactically-correct datasets. Additionally, they are poorly suited for comfortably editing many forms of data that are inherently tabular. 

To addresses these issues, we propose a new format which allows storing structured objects in a tabular format. Compared to JSON and YAML, this format's advantages include: 

* Easy to edit using a tool most users already have, a spreadsheet application. 

* Allows for storing structured metadata in the same spreadsheet file as data. 

* Is easier to edit and verify for data that is organized as a sequence of structures, with each structure having the same properties. 

* Non-technical users can read the data immediately, without training or additional tools.  

The Structured Tabular Format is not a replacement for other formats, and it cannot represent arbitrary data structures as easily as other formats can. Instead, it should be used primarily where it is important to provide metadata for tabular datasets, the data structure is predominantly tabular, or users have a strong preference for using spreadsheet applications.

# Example

The following table is a typical example of an STF file, representing the metadata for a dataset.

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


# STF File Structure

An STF file is organized in a grid of rows and columns. Both rows and columns must be ordered. The underlying file format is unimportant, but generally, any spreadsheet program file format meets the base requirements. 

Each row of the file holds data that will create one or more records. Records have a primary value, a scalar, and may have child terms, so parsing an STF file creates a tree of records.  When the child records are terminal, having no children themselves, they will have only a default value and they can be treated as scalar properties of the parent record.

Each column in the grid has a defined purpose:

* The first column holds a Term, which is a simple or compound name that determines what type of record will be created for the row and what the parent record of the new record will be. 

* The second column holds a Term Value, the record’s scalar value.

* The third and subsequent columns may contain Term Arguments. 

Terms are case-insensitive.

A Term may be simple or compound. A simple term is a single word, such as "Title," while a compound term has two words, separated by a ‘.’, such as “Title.Language”. A simple term create a record that is a child of the root record. A compound term creates a record as a child of another non-root record.  

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

In the second row, "Title" may be omitted. If the value of a term cell starts with a ‘.’, the parent of the record is assumed to be the most recently created record. The following example has the same result as the previous example:

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

The Language child term can also be set with a Term term, as is shown in the next example:  

<table>
  <tr>
    <td>Term</td>
    <td>value</td>
    <td>language</td>
  </tr>
  <tr>
    <td>Title</td>
    <td>An Example Data bundles</td>
    <td>en</td>
  </tr>
</table>


The first row of this table looks like a file header, but the Term term is a data row that sets the parameter map, a list of terms that set the default term name to be associated with term arguments in the same position in the term arguments list. This map can be changed by two synonymous properties, Term and Section. In this example, the Term term row sets the parameter map to a single value list, [‘language’]. Then, in subsequent rows, the value of the third column is matched to the Language term. After matching parameter names to term arguments, the parser creates child records from the matched terms, so the Title term gets a Language child record. The net result is identical to the previous two examples. 

# Parsing process

The conceptual parsing process takes a collection of metadata files, which are linked through includes, traverses them to produce a sequence of term rows, then parses the term rows to produce a sequence of term records. The sequence of term records is used to create the bundle objects, according to the data model.  

There is no header to an STF file -- the first row is data, but it is typically a  Term term, so STF files appear to have a header.  In each row, the first column is the term, and the second column is the term value. All of the remaining columns are term arguments. 

Rows are fed to the parser in the order they appear in the file, from top to bottom. 

For each row, the parser may:

* Create a record for a term.

* Alter the term parameter map

* Include another file, and begin generating rows from it

## Initialization

The parsing process begins with an initial STF file, with a set of variables initialized as:

1. The **parameter map** is empty

2. The **last record map** is empty

3. The **last record** is the Root record

## Main Loop

For each row in the STF file:

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

When an Include term is encountered, the term value is dereferenced as a new STF file to parse. The file is parsed completely, adding records to the record tree -- included files are parsed depth first. After the last row of the file is parsed, parsing resumes after the Include term in the parent file.

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

To allow simple STF file to more closely approximate specific object hierarchies, STF defines two translation term structures. 

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


If the STF input is preceded by:

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

The record hierarchies created by parsing STF files can be converted to JSON and YAML according to the following procedure. In this description, records are the components created by parsing the STF file, and objects are the components created by the conversion process. In many languages, these objects are more likely to be dictionaries or associative arrays. 

For each record in the STF record hierarchy:

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


