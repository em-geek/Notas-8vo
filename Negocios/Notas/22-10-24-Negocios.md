# ETL
- Dos estrategias para almacenar informacion en un almacen de datos 
	- Enterprise-wide warehouse, top-down, the Inmon methodology
	- Data mart, bottom up, the Kimball Methodology

## The Data Mart Strategy
- The mosto commo approach
- Begins with a single mart and architected marts are added over tome for more subject areas
- Relatively inexpensive and easy to implement
- Can be used as a proof of concept for data warehousing
- Can perpetuate the "silos of information" ´problem
- Can postpone difficult decisions and activitues
- Requires an overall integration plan

The Enterprise-wide Strategy
- A comprehensive warehouse is built initially
- An initiala dependent data mart is 

## Data Sources and Types
- Primarily from legacy, operational systems
- Almost exclusively numerical data at the present time
- External data may be included, often purchased from third-party sources
- Technology exists for storing unstructured data and expect this to become more important over time

## Recent Development: More Frequent Updates{
- Updates can be done in bulk and trickle modes
- Business requeriments, such as trading partner acces toa web site, requires currents data
- For international firms, there is no good time to load the warehouse

## Recent Development: Clickstream Data
- Results from clicks at web sites
- A dialog manager handles user interactions. An ODS (operational data store in the data staging area) helps to custom tailor the dialog
- The clickstream data is filtered and parseand sent to a data warehouse where it is analyzed
- Software is available to analyze the clickstream data

## Data Extraction
- Often performed by COBOL routines (not recommended because of high program maintenance and no automatically generated meta data)
- Sometimes source data is copied to the target database using the replication capabilities of standard RDMS (Not recomended because of "dirty data" in the sources systems)
- Increasing performed by specialized ETL software

## Sample ETL Tools
- Teradata warehouse builder from teradata
- DataStage from Ascential Software
- SAS System from SAS Institute
- Power Mart/ Power Center from Informatica
- Sagent Solution from Sagent Software
- Hummingbird Genio Suite from Hummingbird
- Communications

## Reasons for "Dirty" Data
- Dummy Values
- Absence of Data
- Multipurpose Fields
- Cryptic Data
- Contradicting Data
- Inappropriate Use of Address Lines
- Violation of Business Rules
- Reused Primary Keys
- Non-Unique Identifiers
- Data Integration Problems

## Data Cleaning
- Source systrems contain "Dirty data" that must be cleaned
- ETL software contains rudimentary data cleansing capabilities
- Specialized data cleansing software is often used. Important for performing name and addres correction and householding functions
- Leading data cleansing vendors include Vality (Integrity), Harte-Hanks (Trillium, and Firstlogic(id Centric))