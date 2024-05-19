---
layout: page
title: ETL
permalink: /ETL/
---

# SQL/Power Query Best Practices

This page serves as the foundation for my preferred **Extract, Transform, Load (ETL)** query structures I have developed over the years and recommend for maximum load efficiency. Sometimes loading millions of rows can be memory-intensive on computers without high-powered GPUs and can take eons to refresh. Many organizations that use Power Query understand the pains of loading data from a cloud platform into Power BI/Excel and find themselves frustrated by the bulky lag times they face.

The answer is simple: embed SQL scripts within your Power Query advanced editor screen wherever possible! This ensures that the heavy data processing you need to execute to get your reports refreshed takes place on the server-side as much as possible. This isn't just limited to SQL!

### Basic ETL Process

## 1. Extract:
- In this method, you are actually combining the Extract and Transform methods into a single seamless query structure. Microsoft Power Query provides users of Excel and Power BI with a powerful 'Advanced Editor' capability. Many people believe Power Query is reliant on linear steps that proceed one after another, but this is not true. **The 'Advanced Editor' button within the Power Query view is the secret to unlocking masterful code-like scripting for combining the Extraction and Transformation steps for your data.**

    <img src="/images//PowerQuery1.png" alt="Advanced Editor Button" title="Advanced Editor Button" style="border: 10px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">


    - You can even create set defined variables or set variables to equal a defined NamedRange value from the front-end of the Excel worksheet/report and integrate that value directly into the query.

- This stage involves connecting to a database server hosted on Azure, AWS, etc. Executing a well-defined query to fetch necessary data efficiently, and ensuring the data is accurately captured for further steps.

<img src="/images/Excel1.png" alt="Excel Data Example" title="Excel Data Example" style="border: 10px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;"/>



## 2. Transform:
- The raw data is transformed into a more meaningful format. Transformations include cleaning data, selecting only certain columns to load, merging data from multiple sources, converting data types, and applying business logic. This step is crucial for preparing the data for analysis and ensuring its quality and accuracy.
- Here is an example SQL query embedded within the Power Query 'Source' step. This query utilizes SQL Server's capabilities to handle complex data operations, like window functions for data partitioning and row numbering to isolate the most recent records based on specific criteria.

<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>let
    Source = Sql.Database("awsamazon.com", "DatabaseName", [Query="
    // Define a Common Table Expression (CTE)
    // to identify the most recent records for each entity.
    WITH RecentRecords AS (
        SELECT
            [EntityID], [Location], [Date], [AccountName], [TransactionType],
            ROW_NUMBER() OVER (
                PARTITION BY [EntityID], [Date], [AccountName]
                ORDER BY [ModificationDate] DESC
            ) AS RowNumber
        FROM
            [DatabaseSchema].[FinancialRecords]
    ),
    // Filter to only include the most recent records based on RowNumber.
    FilteredData AS (
        SELECT *
        FROM RecentRecords
        WHERE RowNumber = 1
    )
    // Select and pivot data to transform account names into column headers.
    SELECT [EntityID], [Location], [Date],
           [Revenue], [Costs], [Losses], [Gains]
    FROM FilteredData
    PIVOT (
        MAX([TransactionType])
        FOR [AccountName] IN ([Revenue], [Costs], [Losses], [Gains])
    ) AS PivotTable
    ORDER BY [EntityID], [Date] DESC;
"]),
    // Extra Power Query Transformation steps after the SQL is loaded if necessary...
    // Push as many of your transformation steps to the server side as possible.
    // Heavy merges should be done with JOINS on the server side.
    ChangedType = Table.TransformColumnTypes(Source,Date),
    FilteredRevenue = Table.SelectRows(ChangedType, each [Revenue] > 1000),
    RemovedDuplicates = Table.Distinct(AddedMargins, {"EntityID", "Date"}),
    FinalSort = Table.Sort(RemovedDuplicates, Date)
in
    FinalSort
</code></pre>
</div>

- By embedding SQL queries into Power Query, you can leverage the full power of your database server to handle complex data operations. This method is not limited to traditional SQL databases; you can also apply it to various cloud databases such as Azure SQL Database and Google BigQuery. For instance, with Azure SQL Database, you can connect using Sql.Database("myazureserver.database.windows.net", "DatabaseName"), and with Google BigQuery, you can use the GoogleBigQuery.Database("myproject") connector.

- Additionally, you can utilize scripting languages like Python and R to perform similar data extraction and transformation tasks. In Python, you might use a library like pyodbc to run your SQL queries and process the data further, while in R, you could use the DBI package to connect and execute SQL queries. These versatile techniques enable you to integrate, transform, and analyze data from multiple sources efficiently, making your ETL processes robust and scalable.

Here are some other examples:

**Azure SQL Database:**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>let
    Source = Sql.Database("myazureserver.database.windows.net", "DatabaseName",
    [Query="
    -- SQL Query
    "]),
    --Excel/Power BI PowerQuery Steps
in
    FinalStep
</code></pre>
</div>

**Google BigQuery:**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>let
    Source = GoogleBigQuery.Database("myproject"),
    Dataset = Source{[Name="mydataset"]}[Data],
    Query = Value.NativeQuery(Dataset, "
    -- SQL Query
    ")
in
    Query
</code></pre>
</div>

**Python:**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>import pandas as pd
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=myserver;DATABASE=mydatabase')

query = """
-- SQL Query
"""

df = pd.read_sql(query, conn)
# Perform further transformations in Python if needed
</code></pre>
</div>


**Apache Spark**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder \
    .appName("ETL Example") \
    .getOrCreate()s

# Read data from a source
df = spark.read.format("jdbc").options(
    url="jdbc:mysql://awsamazon.com/DatabaseName",
    driver="com.mysql.jdbc.Driver",
    dbtable="FinancialRecords",
    user="username",
    password="password").load()

# Transform data
df_filtered = df.filter(df['Revenue'] > 1000) \
    .withColumn("Profit_Margin", col("Revenue") - col("Costs")) \
    .dropDuplicates(["EntityID", "Date"]) \
    .orderBy(col("Date").desc())

# Show the result
df_filtered.show()

</code></pre>
</div>


**R:**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>library(DBI)

con <- dbConnect(odbc::odbc(), 
                 Driver = "SQL Server", 
                 Server = "myserver", 
                 Database = "mydatabase")

query <- "
-- SQL Query
"

df <- dbGetQuery(con, query)
# Perform further transformations in R if needed
</code></pre>
</div>




Rather than relying on bulky M and DAX, these more streamlined examples illustrate the ease of combining SQL with other technologies to enhance your ETL workflows with, ensuring your Excel and PowerBI reports are loaded as quickly and efficently as possible. And of course, Python and R allow for much more immense data manipulation using their all-encompassing library structures.



## 3. Load:
- Typically, now that we have combined the E and T components of ETL data flows, we would go ahead and load the result of this query into our Excel/Power BI file. **However, I want to take this opportunity to showcase how you can centralize multiple queries together for even more powerful leverage within your file.**
- Another amazing component of the Advanced Editor view within Power Query is the fact that you can store a multitude of sources that you will need to reference within your Excel/Power BI file **in a single centralized query**.

**Centralized ETL Query:**
<div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>{% raw %}let
    // Function to access Salesforce Data
    FnSalesforceData = (name as text) =>
        let
            Source = Salesforce.Data("https://login.salesforce.com/",[ApiVersion=48]),
            Data = Source{[Name=name]}[Data]
        in
            Data,

    // Function for Contacts from Salesforce
    FnSalesforceContacts = () =>
        let
            Source = FnSalesforceData("Contact"),
            SelectedColumns = Table.SelectColumns(Source, {"Id", "Name", "Email"}),
            // Other Power Query/SQL transformative steps
        in
            FinalStep,


    // Function for Transactions from SQL Server
    FnSQLServerTransactions = () =>
        let
            Source = Sql.Database("sqlserver.company.com", "FinanceDB"),
            TransactionsTable = Source{[Schema='dbo', Item='Transactions']}[Data],
            // Other Power Query/SQL transformative steps
        in
            FinalStep,


    // Function for Leads from Azure
    FnAzureLeads = () =>
        let
            Source = Sql.Database('azure.database.windows.net', 'LeadsDB'),
            LeadsTable = Source{[Schema='dbo', Item='Leads']}[Data],
            // Other Power Query/SQL transformative steps
        in
            FinalStep,

    // Function for Accounts from AWS with embedded SQL
    FnAWSAccounts = () =>
        lethttp://127.0.0.1:4000/ETL/
            Source = Sql.Database("aws.amazon.com", "AccountsDB", [Query="
                SELECT 
                    AccountID AS ID, 
                    AccountName
                FROM dbo.Accounts
                WHERE AccountStatus = 'Active'
            "])
        in
            Source,


    // Consolidating all functions into a single record
    ConsolidatedData = [
        SalesforceContacts = FnSalesforceContacts(),
        SQLServerTransactions = FnSQLServerTransactions(),
        AzureLeads = FnAzureLeads(),
        AWSAccounts = FnAWSAccounts()
in
    ConsolidatedData
{% endraw %}
</code></pre>
</div>


- Now, you will be able to quickly grab any of your datasources with a simple call from a new Query! Assuming the above query is named "CentralQuery", the call structure to grab your Salesforce Contact object table looks like this:

 <div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>let
    Source = CentralQuery(SalesforceContacts)
in
    Source
</code></pre>
</div>

Or your AWS Accounts:

 <div style="width: 100%; overflow: auto; margin: 20px 0; border: 1px solid #ddd; padding: 10px;">
<pre><code>let
    Source = CentralQuery(AWSAccounts)
in
    Source
</code></pre>
</div>

You get the idea! 

Through these methods, you can use a single source query to centralize numerous Extract and Transform components together, and then quickly call the end-result steps in a new query for Loading! All of this is a good reason for me to keep the 'Blank Query' button handy on my quick access tool bars. So you can quickly spring up a call to one of these objects.

## Summary

This ETL process is essential for situations when you need to extract multiple data sources and merge them together in a manner that keeps your reporting files lean and mean! **Whether you are working within cloud platforms (Azure, AWS), traditional SQL databases, or any other data sources that are callable from Power Query (even PDFs and websites!), Microsoft's Advanced Editor feature allows easy SQL integration directly within your queries, optimizing the extraction process and ensuring that heavy data processing tasks are handled with maxium speed and efficiency.** If you happen to be working with terabytes of data, you will need to skip Power Query altogether and go directly into multicore-processing concepts within Python machine learning libraries (and of course, some fancy GPUs).

By consolidating data sources and transformations into a single centralized query, you enhance the scalability and maintainability of your file that relies on heavy calculated business logic for shaping up your end reports. This ensures you are running on optimized performance and efficiency, providing a solid foundation for scaling up your reporting and business data. **All that is required is getting familiar with that Advanced Editor button!**

Thank you for reading my ETL process page! If you are interested in learning more about this concept or others, feel free to drop a message on the Home page! I am also actively looking for a new role, so if your team is hiring, let's chat!