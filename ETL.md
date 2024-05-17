---
layout: page
title: ETL
permalink: /ETL/
---

# SQL/Power Query Best Practices

This page serves as the foundation for my preferred **Extract, Transform, Load (ETL)** query structures I have developed over the years and recommend for maximum load efficiency. Sometimes loading millions of rows can be memory-intensive on computers without high-powered GPUs and can take eons. Many organizations that use Power Query understand the pains of loading data from a cloud platform into Power BI/Excel and find themselves frustrated by the bulky lag times they face.

The answer is simple: embed SQL scripts within your Power Query advanced editor screen wherever possible! This ensures that the heavy data processing you need to execute to get your reports refreshed takes place on the server-side as much as possible. This isn't just limited to SQL!

### Basic ETL Process

1. **Extract**:
   - In my preferred method detailed below, the Extract and Transform methods are combined into one seamless query structure. Microsoft Power Query provides users of Excel and Power BI with a powerful 'Advanced Editor' capability. Many people believe Power Query is reliant on linear steps that proceed one after another, but this is not true. **The 'Advanced Editor' button within the Power Query view is the secret to unlocking masterful code-like scripting for combining the Extraction and Transformation steps for your data.**
        <img src="/PowerQuery1.png" alt="Advanced Editor Button" title="Advanced Editor Button" />
        - You can even create set defined variables or set variables to equal a defined NamedRange value from the front-end of the Excel worksheet/report and integrate that value directly into the query.
   - This stage involves connecting to a database server hosted on Azure, AWS, etc. Executing a well-defined query to fetch necessary data efficiently, and ensuring the data is accurately captured for further steps.

    <img src="/Excel1.png" alt="Excel Data Example" title="Excel Data Example" />



2. **Transform**:
   - The raw data is transformed into a more meaningful format. Transformations include cleaning data, selecting only certain columns to load, merging data from multiple sources, converting data types, and applying business logic. This step is crucial for preparing the data for analysis and ensuring its quality and accuracy.
   - Here is an example SQL query embedded within the Power Query 'Source' step. This query utilizes SQL Server's capabilities to handle complex data operations, like window functions for data partitioning and row numbering to isolate the most recent records based on specific criteria.

   ```
   let
       Source = Sql.Database("awsamazon.com", "DatabaseName", [Query="
        // Define a Common Table Expression (CTE) 
        // to identify the most recent records for each entity.
                WITH RecentRecords AS (
                    SELECT
                        [EntityID], [Location], [Date], [AccountName], [TransactionType],
                        ROW_NUMBER() OVER (
                                PARTITION BY [EntityID], [Date], [AccountName]
                                ORDER BY [ModificationDate] DESC)
                        AS RowNumber
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
    // It is reccomended to push as much of your data transformation steps to the server as possible!
    // Heavy merges should be done with JOINS on the server side.
    ChangedType = Table.TransformColumnTypes(Source,{{"Date", type date}}),
    FilteredRevenue = Table.SelectRows(ChangedType, each [Revenue] > 1000),
    AddedMargins = Table.AddColumn(FilteredRevenue, "Profit Margin", each [Revenue] - [Costs]),
    RemovedDuplicates = Table.Distinct(AddedMargins, {"EntityID", "Date"}),
    FinalSort = Table.Sort(RemovedDuplicates, {{"Date", Order.Descending}})
in
       ChangedType
    ```

3. **Load**:
   - The transformed data is loaded into your Excel or Power BI front-end desktop app where the data is further analyzed, visualized, and reported on. This final step in the ETL process involves optimizing the data for quick refresh retrieval and ensuring that it is stored securely and efficiently.
   - If you have numerous tables that you need to load and transform from multiple data sources, the most efficient method is centralizing all of your sources in one single record query.

