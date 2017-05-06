Metatab Packages 

A method for linking data to metadata

Eric Busboom, Civic Knowledge

eric@civicknowledge.com

Despite decades of enthusiasm for data, it is still difficult and expensive to distribute data from producers to consumers. Skilled data analysts have access to more data than ever, but the broader range of data users, such as journalists, nonprofits, businesses and consumers still have difficulty finding and using data. Websites such as Census Reporter and DataUSA.io offer a model for how to increase data use, but these types of sites are very expensive to produce. 

To solve these problems, this proposal describes a way of packaging data that can make data distribution sites like [Census Reporter](https://censusreporter.org/) much easier to create and maintain, and ensure traditional analysts can find the data they need.  These methods add some cost to the data production process, but will yield enormous benefits to data consumers. 

By developing simple standards for how to bundle data, data producers can make their datasets "machine comprehensible," permitting the creation of better data access software that can store, publish, and visualize any properly bundled dataset. Better data packaging will result in making data:

* Easier to find, because the bundles can be indexed in search engines.

* Easier to view, because software can automatically create charts.

* Easier to analyze, because the files will reliably load into statistical software

* Easier to publish, because there are fewer decisions for data publishers to make. 

The standard proposed here is very simple. In the simplest case, for data in Excel format, it involves adding an additional worksheet, named ‘meta’, which holds information about the name, title and creators of the data, and another worksheet called ‘schema’ with a list of the data columns and their data types and descriptions.  This proposal defines similar package structures for ZIP archives, file systems and web pages. 

In this example of a[ data bundle in an Google Spreadsheet](https://docs.google.com/spreadsheets/d/1-xeyxkbDMbKDxG5jhsrtBsKgtBSHn0gn05tP9GgPY5w/edit?usp=sharing), one worksheet holds the data, while the other two hold metadata. This format is easy for both humans and programs to read, and easy for humans to create, with no additional tools. Here is a [more complex example](https://drive.google.com/file/d/0B4dCPpfYVDivdUp6Q0N5cG03YUU/view?usp=sharing), extracted from the [Healthy Communities Indicators](https://www.cdph.ca.gov/programs/pages/healthycommunityindicators.aspx) and stored in an Excel file. In this form, the data can be automatically processed in a variety of ways:

* **Generate web pages**. Software can read one or more bundles to create entire data repository websites, based entirely on the data bundle, with no additional input. 

* **Improved search engine indexing**. When generating a webpage, the webpage can be designed to make the dataset easy to find, which is currently difficult when the metadata and data dictionary are in different files. 

* **Automatic visualization**. Visualization programs can use the metadata to infer the most important charts and graph, and create them automatically. 

* **Automatically import metadata into data repositories**. With a plugin, data repository software could automatically import metadata from the bundle file.  

Because the information each component is stored in a human-writable and machine-readable format, regardless of the structure of the bundle, it is easy to write programs that can read and understand the bundles, data creators have a range of options for packaging data, and the standard can handle small bundles that consists of only a single file  for simple datasets,  or complex datasets with multiple tables and multiple files.

To make the metadata each to read and write, the primary form for metadata is [Metatab](http://metatab.org), a way of storing structured metadata in a tabular format. This format is easier for non-technical data users to read and write, and it can be stored in a spreadsheet. 

When possible, the metadata files use existing standards to specify metadata terms or permissible values for metadata elements. Metadata terms are linked to [Dublin Core](http://dublincore.org/), [foaf](http://www.foaf-project.org/), [DCAT](https://www.dcat.org/), [POD Schema](https://project-open-data.cio.gov/v1.1/schema/),  [Frictionless Data Package](http://specs.frictionlessdata.io/data-packages/) and other established standards, and domain values for the elements are well-defined terms from standards like the Library of Congress subject headings, or this specifications own vocabulary for data types. 

Because there are links to other common standards, data bundles can be imported and exported to data repositories like CKAN or Socrata, described in collections with DCAT,  or transformed into other data bundle formats. 

# Differences from Frictionless Tabular Data Packages

This data package specification is very similar to the [Frictionless Tabular Data Packages](http://frictionlessdata.io/guides/tabular-data-package/) in many respects, and can be considered an extension of the specification to make data packages easier to create and use for less technical creators and publishers. Some of the differences are arbitrary, and this spec will be altered to harmonize with the Frictionless specification. Important differences include: 

* Primary metadata format is tabular, not JSON. This difference is important to make the bundles easier to create and use for non technical users, and to allow Excel as a data package format.  

* Data can be packaged in an Excel file. The tabular metadata form allows storing metadata in a spreadsheet, and most non-technical data users are most comfortable with Excel, so Excel is a critical data package format. 

* ZIP Package format. This spec defines a profile for storing data packages in a ZIP file. ZIP is a very simple extension of the Frictionless spec, and not a substantial change, but ZIP archives are important for many data users. 

Additional work that will result in differences: 

* Numbering and registration. This specification will define a scheme for generating unique dataset identifiers and registering them as DOIs, allowing datasets to be uniquely identified in research publications. 

* Defined locations for stat package loading scripts. Several statistical packages, such as SAS, R and Pandas, have particular ways of loading data that considers metadata, such as type information. This specification will define a location and naming structure for loading scripts that are generated when a package is built. ( There will probably be a ‘scripts’ directory in ZIP packages. ) 

* Partitioning. This specification may include metadata for describing how a single datafile is decomposed into multiple files, and how those files are decomposed. This will allow for programs that only load, for instance, files for a single year. 

* Subpackages. Some very large datasets are decomposed as separate, smaller packages. This specification may consider how to link multiple packages. 

* Authority. This specification may include a way to determine if a package was downloaded from an authoritative source. 

* Harmonize with other metadata standards. This specification will specifically consider how to map the metadata terms to other metadata standards, or to account for metadata term namespaces.  For instance, here should be a defined, automatic process for converting bundle metadata to POD or datapackage.json formats. 

# Overview

Data packaging has one overarching goal: link metadata and documentation to data and make them difficult to separate but easy to use. A Data Bundle is a collection of data, documentation and metadata that describes the data, linked together in the same spreadsheet, ZIP archive or webpage. The components of a data bundle include: 

* **Data**. The bundle format is designed for datasets can can be stored in a spreadsheet or relational database, as tabular data organized into rows and columns, in Excel or CSV format.  

* **Documentation**, usually in the form of a Word or PDF document. 

* **Metadata**, which describes the whole bundle, such as the title,  author, and date of publication, and a data dictionary, which describes tables and columns. Metadata is stored in [the Metatab format,](http://metatab.org) in an Excel spreadsheet tab or a CSV file. 

Using tabular data for the metadata allows data creators to create the files using tools they already have, their spreadsheet programs, and makes it easy to write programs to read the data. The result is that bundles are both easy to create and easy to use. 

Data, metadata and documentation can be bundled in a variety of ways, including a single Excel file with multiple worksheets, a ZIP archive with CSV files or a web page with links.  If the components are stored in separate files, they are linked together either by including them in the same ZIP archive, by publishing them to the web and linking them with URLs, or by referencing them from a manifest file. These two considerations -- the form of the components and how they are linked together, results in several options for the structure of the bundle. These are called bundle containers: 

* **A Single Excel file**. The data, metadata and schema are stored on separate sheets in a single spreadsheet document, so the whole bundle is one file. Documentation is referenced with a URL. 

* **Separate files in a ZIP archive**. The data, metadata, schema and documentation have separate CSV files, and they are all bundled in a ZIP archive. Some datasets are more complex, and will have multiple tables of data. In this case, there is one metadata file, multiple schema files, and multiple data files, all in the same ZIP archive. 

* **A Web page**. The data, metadata, schema and documentation are published to the web, and a dataset page links to each of the files. The links are tagged in HTML, so a program that reads the page knows it is for a data bundle and can locate all of the components. In this case, the web page serves as the bundle manifest. 

* **A filesystem**. Bundles can be stored on file systems, with the file system representation being the unpacked version of the ZIP archive representation. 

These different packaging options are each defined by a profile. 

Bundles are referenced with URLs, which can refer to the bundle container, such as a ZIP archive, the bundle metadata file, or to a path from which a metadata file can be inferred by adding ‘/metadata.csv’. The contents of a bundle container, such as a data or document file, is referenced by adding a fragment to the URL. 

# Examples

## ZIP Bundle

URL is http://example.com/bundles/bundle.zip.

Downloading and extracting the zip file results in these directories and files:

* Bundle

    * metadata.csv

    * data/data-file-1.csv

    * doc/doc-file-1.pdf

The metadata file has:

* A Datafile term with the value ‘data/data-file-1.csv’

* A Documentation term with the value ‘doc/doc-file-1.pdf’

Tooling can refer to the first datafile with the absolute URL ‘http://example.com/bundles/bundle.zip#data/data-file-1.csv’

## Excel file 

URL is http://example.com/bundles/bundle.xls

The Excel file has these worksheets:

* Meta. Holds the metadata

* Data. Hold the data. 

The metadata has these terms:

* A Documentation term with the value of ‘http://example.com/bundles/doc-file-1.pdf’

* A Datafile term with the value of ‘Data’

Externally, the data in this Excel file would be referred to with: ‘http://example.com/bundles/bundle.xls#Data’

# Definitions

**Bundle**: A collection of data, metadata, schema and documentation The collection may be implemented as a ZIP archive, spreadsheet, filesystem director, or other way of associating multiple files. 

**Data**: the primary data that is published in the bundle. 

**Metadata**: All of the metadata about the bundle, including the schema, bundle metadata, manifest and documentation

**Schema**: The description of all tables and all of their columns. 

**Table**: The description of the structure of data that is organized into rows and columns, in the same sense as a spreadsheet table or a database table. It does not, however, refer to the structure of metadata, which, even when it is in a tabular form, is described as a collection of records. 

**Column**: A collection of data of the same type, representing values of a single variable. It has the same sense as a spreadsheet column or a database column. 

**Term**: A defined name for a metadata element, such as "Title" “Creator” or “Table”

**Record**: a collection of properties in the schema, bundles metadata or manifest. Records are named by terms. 

**Property**: A value, stored in a metadata record. A property may be a scalar value, or a collection of scalars, but not a record or collection of records. Properties are actually child records, but they have a scalar value and no children.  

**Variable**: Any characteristic or attribute that can be measured or counted. In the data, the values of a variable are stored in a column. 

**Producer**: Someone who creates data. 

**Consumer**: Someone who uses data. 

# Bundle Container Profiles

A bundle container is specific structure for holding the files in a bundle. Defined types of bundle containers are: 

* ZIP Archive

* Spreadsheet

* Web resource

* Filesystem

Within a bundle container, files are referenced with relative paths. Paths follow the URI syntax for path-rootless as specified in RFC 3986: one or more segments separated by "/".  Relative paths are all relative to the level in the hierarchy of the metadata.csv file. Some profiles allow multi-level  hierarchies, while other allow only a single level. Relative paths do not allow ‘.’ or ‘..’ segments. 

## ZIP Archives

ZIP Archives allows sub-directories, so relative paths may have multiple levels. 

The ZIP archive must have a single directory in its root, so expanding the ZIP Archive should expand to a directory. The directory should have a unique name, including a name of the bundle and a unique id. This would allow many bundles to be decompressed in the same directory.

The metadata file must be in the single, top level directory. 

All relative paths are relative to the  single top level directory. 

## Spreadsheets

Relative paths are single-level, with only one segment. The segment must be the name of a worksheet in the spreadsheet. 

Spreadsheet bundles are most frequently Excel files, which can hold multiple spreadsheets. However, a single CSV file can also be a valid bundle, if it is named metadata.csv.  In that case,  the bundle contains only metadata, and all data and documentation are referenced with URS. 

## Web 

The ‘root’ of a web bundle is the location of the metadata.csv file. For URLS that include the metadata.csv path segment, the base url is the url with the metadata.csv segment removed. URLS that do not include the metadata.csv segment are already base URLs. 

Relative paths are relative to the base URL. 

## Filesystems

The ‘root’ of a filesystem bundle is the level in the hierarchy of the metadata file . 

# Bundle Contents

Bundle containers hold files for the bundle’s metadata, data and documentation. The types of these files are:

* **Metadata. ***Required*. Every bundle must have at least one metadata file, named according to the container profile, which holds metadata in Metatab format. 

* **Data. ***Optional.* Bundle containers may include data. The data must be in CSV format that follows the rules for [Frictionless Tabular Data Packages](http://specs.frictionlessdata.io/tabular-data-package/#csv-files). 

* **Documentation**, *Optional*. Documentation files may be of any format, but should be PDF or HTML. 

## Metadata

The primary form for metadata is [Metatab](http://metatab.org). A bundle may have metadata in other forms, such as JSON or XML, and in particular, [Frictionless Data Package](http://specs.frictionlessdata.io/),  but it must be generated from the Metatab representation and contain the same information. 

[There must be defined conversions from Metatab to other formats. Maybe Metatab can have a  core metadata term set that unified several other schemes, such as with this [spreadsheet of mapping metadata data term schemes](https://docs.google.com/spreadsheets/d/1mO5nHNXpImT2w_M9VlhUJ0OeMp0x2Zq5OwiiTPXJ-M8/edit?usp=sharing). ]

The metadata must refer to all of the data and documentation in the bundle, using the bundle URL schema. 

Bundle metadata must explicitly refer to all of the resources in the bundle, including:

* Data files

* Documentation

* Other metadata files

The bundles refer to other files using URLs or relative paths. URLs indicate that the resource is separate from the bundle and can be downloaded from the Web. Relative paths refer to resources within the bundle container, with the specific interpretation being depending on the type of bundle container. 

Bundles must have a metadata.csv file. Bundles may have a metadata.json file, a [datapackage.json](http://frictionlessdata.io/guides/data-package/) file, or another form of metadata. Metadata files are always in the root of the bundle container. If the bundle has both metadata.csv and an other form of metadata, the metadata.csv should be considered the most authoritative. [ However, the other file should have been created automatically from the metadata.csv file, so they should have the same information. This feature is primarily intended to allow data bundles to also be Frictionless Data Packages. ]

The metadata component describes the data bundle, and consists of pairs of a property name and a value, most frequently stored in a tabular format, but which may also be stored in other formats, such as rdf or HTML META tags. The metadata properties are defined by existing controlled vocabularies, more significantly, the [Dublin Core metadata standard](http://dublincore.org/) and [Data Documentation Initiative](http://www.ddialliance.org/controlled-vocabularies). [ Linking to the [DataCite Metadata standard](http://schema.datacite.org/meta/kernel-3.1/) may also be very valuable. ]

In a web page, the metadata can be a collection of properties and  links, placed anywhere on the page, that are annotated with [RDFa properties](https://www.w3.org/TR/rdfa-primer) or [Dublin Core HTML elements and attributes](http://dublincore.org/documents/dc-html/) to provide a machine readable versions of the same information that is stored in the metadata file. 

This specification will model metadata as a collection of properties and values. 

## Data 

Data must be stored in a tabular format,  either an Excel worksheet or a CSV file. In either form, the first row of data must be the column headers, each of which follows the column naming requirements. Remaining rows may contain any information that can be stored in an CSV file. Data stored in an Excel worksheet must be exactly equivalent to the same data written to a CSV file and loaded back into Excel; it should not have any information or objects that cannot be represented in CSV, since this information is ignored. 

## Documentation

The documentation can be any human-readable documentation, in any format, although PDF is preferred.

## Bundle URLS

Bundles use a defined URL schema to refer to bundles and components within bundles.

A URL to a bundle may be either:

* A URL referencing a bundle container, such as a ZIP archive or spreadsheet. 

* A URL to a metadata file, either a Metatab file or a JSON conversion of a Metatab file. 

In Metatab, URLs can refer to files within an archive, a tab within a spreadsheet, or a tab in a spreadsheet in an archive. To account for these three levels, Metatab URLs use the URL to refer to the URL resource and the fragment to refer to files or tabs within in the resource. These three components are: 

* URL Resource, the type of file that is fetch when accessing the URL, which excludes the URL fragment. 

* Archive File, a component of the fragment that specifies a file within an archive. 

* Segment, a component of the fragment of that specifies an internal part of a file, either the URL resources or the Archive File.

In Metatab, the same URL structure is used to refer to Metatab packages, resources within metatab files, and within Metatab files to refer to data files and documentation. 

Some examples of Metab URLs that refer to Metatab packages. 

<table>
  <tr>
    <td>URL</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>http://example.com/bundle.zip</td>
    <td>Reference to the bundle container file. The metadata is the metadata.csv file within the zip archive. </td>
  </tr>
  <tr>
    <td>http://example.com/bundle/metadata.csv</td>
    <td>Direct reference to a metadata file on the web</td>
  </tr>
  <tr>
    <td>/bundles/bundle/metatab.csv</td>
    <td>Direct reference to a metadata file in a file system</td>
  </tr>
  <tr>
    <td>http://example.com/bundle/</td>
    <td>Reference to the root of a bundle container. The metadata file is assumed to be http://example.com/bundle/metadata.csv</td>
  </tr>
</table>


Resources in a bundle may be referenced with a URL fragment, so these urls both refer to a datafile within a bundle 

<table>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>http://example.com/bundle.zip#datafile.csv</td>
    <td></td>
  </tr>
  <tr>
    <td>http://example.com/metadata.csv#datafile.csv</td>
    <td></td>
  </tr>
</table>


URLs that refer to data files  may have one or two fragment components, the Archive File and the Segment, separated from the first component with a semicolon ‘;’. Segments are primarily used to indicate a tab within a spreadsheet. If the URL resource is a spreadsheet file, Excel or ODS, for instance, the fragment will have only a file component. If the target object is an archive, and the Archive File is a spreadsheet, the second fragment component, the Segment, refers to a tab. 

<table>
  <tr>
    <td>http://example.com/archive.zip#file_in_zip.csv</td>
    <td></td>
  </tr>
  <tr>
    <td>http://example.com/excel.xls#tab_in_xls</td>
    <td></td>
  </tr>
  <tr>
    <td>http://example.com/archive.zip#excel.xls;tab_in_xls</td>
    <td></td>
  </tr>
</table>


### URL Protocols

Metatab URLs may have a compound schema component to indicate how a URL should be interpreted. Or, the URL can have a custom or alternate scheme. Frequently supported protocols are: 

* Socrata: socrata+[http://chhs.data.ca.gov/api/views/tthg-z4mf](http://chhs.data.ca.gov/api/views/tthg-z4mf)

* Git: git+[https://github.com/CivicKnowledge/metatab-py.git](https://github.com/CivicKnowledge/metatab-py.git)

* Google Spreadsheets gs://1VGEkgXXmpWya7KLkrAPHp3BLGbXibxHqZvfn9zA800w	

Protocols should be included in a URL when the resource URL has a common scheme, like HTTP, but there must be a special interpretation, rather than just fetching the resource. 

[ In the Python code, the url protocol is the scheme when there is no ‘+’ extension, and the extension if there is. ]  	

### Relative Resource paths

Within a bundle, URLs are used to specify the locations of data files, documentation and other resources. These URLs may be absolute URLS, but it is much more flexible to reference resources relative to the bundle container. Relative paths are most important when the data and metadata are contained in a ZIP archive or Spreadsheet. 

All relative paths are relative to the "root" of the container, where the “root” is specific to the type of container. For a ZIP archive or file system Directory, the root is the top level of the directory or archive. For a Spreadsheet, all tabs are in the root. For relative paths, a leading ‘/’ is ignored. 

Relative paths can be attached to a URL to a bundle container as fragments to indicate a component of the bundle:

* Bundle URL: [http://example.com/bundle.zip](http://example.com/bundle.zip)

* File in Bundle: [http://example.com/bundle.zip#data/file1.csv](http://example.com/bundle.zip#data/file1.csv)

When the URL references a metadata file directly, the components of the bundle are not in a container. Instead, the are in a filesystem, or references on the web. In this case,  relative paths are relative to the parent path of the metadata file. So, for the relative path "data/file1.csv"

* Metadata URL: [http://example.com/bundle/metadata.csv](http://example.com/bundle/metadata.csv)

* Data URL: [http://example.com/bundle/data/file1.csv](http://example.com/bundle/data/file1.csv)

Because relative paths are always relative to the root of the container, they do not allow ( and have no use for ) references to a parent directory or the current directory, so ‘.’ and ‘..’ are not valid directory names. 

A URL could be considered a valid reference to a bundle if appending ‘metadata.csv’ to it resolves to a metadata file. This rule would make ‘[http://example.com/bundle/](http://example.com/bundle/)’ a valud bundle URL if ‘[http://example.com/bundle/metadata.csv](http://example.com/bundle/metadata.csv)’ exists. 

TODO: Consider special handling for github urls, as [Frictionless Package Identifiers](http://datapackage.json) do. 

# Metadata Example

This is a typical example of  the primary metadata for a data bundle, in Metatab format, excluding the schema. In an Excel spreadsheet, these data would be in a worksheet tab named ‘meta’.

[ TODO This example doesn’t show Datafiles or Documentation resources. ]

<table>
  <tr>
    <td>Title</td>
    <td>Registered Voters, By County</td>
    <td></td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Percent of the eligible population registered to vote and the percent who voted in statewide elections.</td>
    <td></td>
  </tr>
  <tr>
    <td>Identifier</td>
    <td>cdph.ca.gov-hci-registered_voters-county</td>
    <td></td>
  </tr>
  <tr>
    <td>Version</td>
    <td>201404</td>
    <td></td>
  </tr>
  <tr>
    <td>Obsoletes</td>
    <td>cdph.ca.gov-hci-registered_voters-county-201304</td>
    <td></td>
  </tr>
  <tr>
    <td>Format</td>
    <td>excel</td>
    <td></td>
  </tr>
  <tr>
    <td>Spatial</td>
    <td>California <geoid:04000US06></td>
    <td></td>
  </tr>
  <tr>
    <td>Time</td>
    <td>2002-2014</td>
    <td></td>
  </tr>
  <tr>
    <td>Grain</td>
    <td>County <geoid:05000US></td>
    <td></td>
  </tr>
  <tr>
    <td>Section</td>
    <td>documentation</td>
    <td>title</td>
  </tr>
  <tr>
    <td>Homepage</td>
    <td>https://www.cdph.ca.gov/programs/pages/healthycommunityindicators.aspx</td>
    <td>Healthy Communities Data and Indicators Project (HCI)</td>
  </tr>
  <tr>
    <td>Documentation</td>
    <td>https://www.cdph.ca.gov/programs/Documents/HCI_RegisteredVoters_653_Narrative_and_examples_6-2-14.pdf</td>
    <td>Indicator Documentation for Voter Registration / Participation</td>
  </tr>
  <tr>
    <td>.description</td>
    <td>Voter Registration/Participation: Percent of the eligible population registered to vote and the percent who voted in statewide elections</td>
    <td></td>
  </tr>
  <tr>
    <td>Section</td>
    <td>Contacts</td>
    <td>email</td>
  </tr>
  <tr>
    <td>Creator</td>
    <td>Office of Health Equity</td>
    <td>HCIOHE@cdph.ca.gov</td>
  </tr>
  <tr>
    <td>Wrangler</td>
    <td>Bob Bobson</td>
    <td>bob@civicknowledge.com</td>
  </tr>
  <tr>
    <td>Section</td>
    <td>Notes</td>
    <td></td>
  </tr>
  <tr>
    <td>Note</td>
    <td>This file is an example of a data bundle, a simple format for linking data to metadata using spreadsheets. See the specification for more details.</td>
    <td></td>
  </tr>
  <tr>
    <td>Documentation</td>
    <td>https://docs.google.com/document/d/16tb7x73AyF8pJ6e6IBcaIJAioEZCNBGDEksKYTXfdfg/edit#</td>
    <td></td>
  </tr>
</table>


# Other Issues

## Numbering

The bundles should have unique numbers, such as a purl, doi, etc. There  is an doi registrar, [https://www.datacite.org](https://www.datacite.org), and a related one that seems to index repositories that use a variety of identifiers, [http://www.re3data.org/](http://www.re3data.org/)

It is probably OK for bundles to self assign UUID4 numbers, but doi numbers would be better.  However, it may be more readable to have an alternate system that assigns base 36 numbers ( b/c DOI is case insensitive ) for data packages, and then can register these numbers as DOIs, since DOIs require the registering org to assign its own internal numbers. 

The metadata should handle ORCID for people.

For self-assigned random identifiers, the numbering could base based on UUID4, converted to base 36. FOr instance: 

	python -c 'import numpy, uuid; print numpy.base_repr(uuid.uuid4().int, 36)'

Base 36 reduces the length of a UUID4 from 36 characters to 25. 

Alternative: Always use UUID4. Perhaps all data bundles could self-assign UUID4 numbers, and when those numbers are put into a database, the system could use the shortest prefix of the numbers that is unique across all of the number in that database, like Docker does. 

### Registering DOIs

The DOI system provides a number for an assignment authority and a registration for metadata, but the assignment authority must assign its own numbers. So, to create a DOI, a package creator would have to register package metadata with an assignment authority, and the assignment authority would have to issue a number, then submit both to the DOI registry. 

So, there must be an organization that can run servers to assign data package numbers, or at least to register data packages and forward the registrations to the DOI registry. 

One possible procedure is: 

* Data package tools self-assign a UUID4

* Data publisher creates an account at a data package registry. 

* Data publisher submits package to data package registry. Registry assigns a number. 

* Registry submits data package metadata and number to DOI registry. 

The data package registry could assign a sequential number, but that would require a central authority with a database. An alternative is that the data package number is the shortest prefix of the data package UUID4 for which there is no DOI already registered, with some minimum length. This process would result in a stateless data package registry, so it would be easier to distribute.  

If the minimum data package number is 6 base-36 digits, the system could register 1B packages before there is a 50% chance of a collision, so it would be very rare for a package to require 7 or more digits.  

## Data Standards

GovEx has a list of [civic data standards](http://labs.centerforgov.org/open-data/civic-data-standards/), many of which are defined as collections of CSV files, so they could be implemented as defined data bundles. 

Stephanie Singer’s and Emily Shaw’s [Knight Foundation proposal for data quality](https://www.newschallenge.org/challenge/data/entries/garbage-in-garbage-out-data-quality-uplift-for-government). 

## Authority

How to establish that a bundle is an authoritative release from a publisher?

Bundles can have a ‘creator’ or ‘origin’ name, which is a portion of domain name.  (‘example.com’)

To be authoritative, the bundle has to be downloaded from the domain references in the origin, or from a host that is referenced from the origin in a secure way. 

For instance, the website at the origin could have a file or a DNS record that lists the download hosts for an origin. So maybe ‘example.com’ has an RFC1464 TXT record that lists https://data.example.com as a repository. 

Then metadata at https://data.example.com/bundle/metadata.csv that cites example.com as an origin would be considered authoritative. 

## Relationship to DCAT

When packages are written to a storage system,such as a Filesystem, Object store, etc,  management programs should also write catalog information in DCAT format. Standard DCAT does not allow more than one resource per dataset, but the European APplication profile, DCAT-AP does. 

* [Experiences mapping CKAN to DCAT](https://www.w3.org/2016/11/sdsvoc/SDSVoc16_paper_16)

* OKI’s [Data Catalog Interoperability Protocol](http://spec.dataportals.org/)

* [DCAT-AP Spec](https://joinup.ec.europa.eu/asset/dcat_application_profile/asset_release/dcat-ap-v11)

* [CKAN’s DCAT Mapping](https://github.com/ckan/ckanext-dcat). 

# See Also

* [Metatab](https://docs.google.com/a/civicknowledge.com/document/d/1Ikm0TX_73ws0mZeyv39j5YEWIu4slrKIpaPzoZQKsiI/edit?usp=sharing), the file format used for metadata. 

* [Vocabulary for Data Type Values](https://docs.google.com/document/d/1Sc5BXVuuoCNmqlZi-iDuvDQLoTqYauJVxxTTEc58gsw/edit?usp=sharing), the names used to describe datatypes in the metadata schema. 

* [Spreadsheet of Terms, Namespaces and Schemes](https://docs.google.com/spreadsheets/d/1mO5nHNXpImT2w_M9VlhUJ0OeMp0x2Zq5OwiiTPXJ-M8/edit?usp=sharing).

The USDA Ag Data defines an[ Excel based data package](https://data.nal.usda.gov/manually-creating-data-dictionary).  

[Frictionless Data](http://specs.frictionlessdata.io/)

[DataCite Metadata standard](http://schema.datacite.org/meta/kernel-3.1/)

[Crossref](http://www.crossref.org/), scholarly publishing

[ORCID](http://www.crossref.org/), researcher identifiers, primarily useful to uniquely identify people

[ISNI for Organizations](http://www.ringgold.com/isni)

A Standard for [units of measure](http://unitsofmeasure.org/ucum.html)

[Dewey Decimal classifications](http://www.oclc.org/dewey/)

[IANA Media Types](http://www.iana.org/assignments/media-types/)

[Library of Congress Classification Concepts](http://lcweb.loc.gov/catdir/cpso/lcco/lcco.html)

[Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects)

[National LIbrary of Medicine Classifications](http://wwwcf.nlm.nih.gov/class/)

[Medical Subject Headings](http://www.nlm.nih.gov/mesh/meshhome.html)

[Universal Decimal Classifications](http://www.udcc.org/)

[Getty Geo Names](http://www.getty.edu/research/tools/vocabulary/tgn/index.html)

[Casrai standard dictionary](http://dictionary.casrai.org/Main_Page) of research administration information

[ISA-TAB metadata](http://isatab.sourceforge.net/docs/ISA-TAB_release-candidate-1_v1.0_24nov08.pdf), for bioinformatics. 

