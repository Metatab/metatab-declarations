Data Package Interoperability 

Rules For Packaging Data with a Variety of Metadata

Eric Busboom, Civic Knowledge

eric@civicknowledge.com


# Introduction


Efficient data sharing requires predictable ways to link data to metadata and store both in easily transportable formats. This document proposes a set of rules for storing data and documentation in ZIP archives, file systems, object stores and spreadsheets and linking the data to metadata. 

Data packaging has one overarching goal: link metadata and documentation to data and make them difficult to separate but easy to use. A Data Package is a collection of data, documentation and metadata that describes the data, linked together in the same spreadsheet, ZIP archive, filesystem or webpage. The components of a data bundle include: 

* **Data**. The bundle format is designed for datasets can can be stored in a spreadsheet or relational database, as tabular data organized into rows and columns, in Excel or CSV format.  

* **Documentation**, usually in the form of a Word or PDF document. 

* **Metadata**, which describes the whole bundle, such as the title,  author, and date of publication, and a data dictionary, which describes tables and columns. Metadata is stored in [the Metatab format,](http://metatab.org) in an Excel spreadsheet tab or a CSV file. 

This document describes how to store data, documentation and metadata in these hierarchical container formats: 

* file systems 
* object stores like S3
* web accessible resources, particularly for the FTP and HTTP schemes. 
* file archives, such as ZIP or TAR archives. 

Data Packages may also adhere to the [BagIt file packaging format](https://tools.ietf.org/html/draft-kunze-bagit-14) packaging format by including required BagIt files. 

# Package Structure

A Data Package must include a primary metadata file and one or more data files. A Data Package may also include zero or more secondary metadata files, documentation, scripts and other files. Any files that are not metadata are payload files. All payload files should be referenced by the primary metadata, but this is not required. 

A package has a base directory which holds the primary metadata file and the "data/" directory. In an archive file, the base directory may be root of the archive, or it may be a directory in the root of the archive. If the base directory is a sub-directory of the root, the archive must contain only that one directory, and the directory should be named with the same name as the package, which should be included in the metadata. 

The base directory may contain other optional directories. Directories defined by this specification are:

* "data/" For all data files
* "metadata/" for secondary metadata
* "documentation/" for documentation files
* "scripts/" for scripts that create data files
* "analysis/" for analysis files, such as scripts for statistical packages. 

The base directory may contain other directories that are not defined in this specification, but the directories described above must not be used for other purposes that what is described in this specification. 

## Metadata Files

This specification does not specify a particular metadata scheme, but does require that: 

* The base directory must contain a metadata file
* If the metadata file is one of the recommended schemes, it must have the file name assigned to it in this specification.


[ Maybe it should specify particular schemes. There are only a few that make sense. ]

### Recommended Schemes and File Names


These three are the most complete, and are best designed for datasets

* Tabular Data Packages: datapackage.json
* Metatab: metadata.csv, metadata.json
* POD: data.json

These could be secondary. 

* Dublin Core: dcmetadata.xml
* DCAT: dcat.rdf
* DataCite datacite.xml



Alternate: maybe the root includes a metadata.txt file that describes the primary and secondary metadata, along with its location. 


### Primary and Secondary Metadata Files

The primary metadata file, stored in the base directory, should be the metadata that the data publisher first created. The secondary metadata files, stored in the "metadata/" directory, should be derived from the primary metadata file. 


