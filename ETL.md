---
layout: page
title: ETL
permalink: /ETL/
---

This page serves as the foundation for my preferred **Extract, Transform, Load (ETL)** query structures I have developed over the years and recommend for maximum load efficiency. Sometimes loading millions of rows can be memory-intensive on computers without high-powered GPUs and can take eons to refresh. Many organizations that use Power Query understand the pains of loading data from a cloud platform into Power BI/Excel and find themselves frustrated by the bulky lag times they face.

The answer is simple: embed SQL scripts within your Power Query advanced editor screen wherever possible! Additionally, leveraging powerful ETL tools like SAS and Alteryx, along with cloud services like AWS or SQL Server, can significantly improve the efficiency and speed of your data processing workflows. This ensures that the heavy data processing you need to execute to get your reports refreshed takes place on the server-side or cloud as much as possible. 

In the below examples, I showcase how different technologies such as **Python**, **SAS**, **SQL**, **Power Query** (Excel/PowerBI), **Alteryx**, **Apache**, **Google**, **Azure**, and **AWS** can all be similarly used and combined together for data extraction, transformation, and publishing that provides maximum efficiency on your machine! With that, let's dive in!

<div class="tenor-gif-embed" data-postid="20497912" data-share-method="host" data-aspect-ratio="1.77778" data-width="50%"><a href="https://tenor.com/view/sucked-up-by-the-television-mono-little-nightmares2-going-inside-the-television-enter-gif-20497912">Sucked Up By The Television Mono GIF</a>from <a href="https://tenor.com/search/sucked+up+by+the+television-gifs">Sucked Up By The Television GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

<br>

## **ETL Using SAS, Python, and AWS Cloud together**

### Scenario:
You need to process sales data stored in an AWS S3 bucket. The data will be extracted using Python, a basic machine learning model will be applied using scikit-learn, and the results will then be statistically analyzed in SAS. Finally, we'll visualize the results back in Python.

### Step 1: Extract Data from AWS S3 and Apply Machine Learning in Python
In this example, we'll use Python to extract sales data from an AWS S3 bucket, preprocess the data, and apply a machine learning model to predict sales revenue. We'll use boto3 for S3 interaction, pandas for data manipulation, and scikit-learn for the machine learning model. The workflow includes cross-validation to evaluate the model's performance and saves the prediction results to a CSV file for further analysis in SAS. This demonstrates how to integrate cloud data storage and machine learning in Python.

```python
import boto3
import pandas as pd
from io import BytesIO
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Initialize a session using Amazon S3 credentials as a cloud data warehouse example
s3 = boto3.client('s3')
bucket_name = 's3bucketname'
file_key = 'path/to/your/data.csv'

# Download the CSV file from S3 into a pandas dataframe
response = s3.get_object(Bucket=bucket_name, Key=file_key)
sales_data = pd.read_csv(BytesIO(response['Body'].read()))

# Preprocessing, dropping missing values
sales_data = sales_data.dropna() 

# Define features and target variable
X = sales_data[['Quantity', 'UnitPrice']]
y = sales_data['TotalRevenue']

# Split data into standard training and testing sets for cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the model
model = LinearRegression()

# Perform cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')

# Calculate the mean and standard deviation of the cross-validation scores
mean_cv_mse = np.mean(-cv_scores)
std_cv_mse = np.std(-cv_scores)
print(f'Cross-Validation Mean Squared Error: {mean_cv_mse:.2f} ± {std_cv_mse:.2f}')

# Train the model on the full training data
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model on the test data
mse = mean_squared_error(y_test, predictions)
print(f'Test Mean Squared Error: {mse:.2f}')

# Save the results for SAS processing
sales_data['PredictedRevenue'] = model.predict(X)
sales_data.to_csv('sales_data_with_predictions.csv', index=False)
```

### Step 2: Transform and Analyze Data in SAS
Next, we use SAS to import the sales data with predictions from the Python above and perform descriptive statistics, conduct correlation analysis, and run a regression analysis to gain deeper insights into the sales data.

```sas
/* Import the data from the python output CSV file */
proc import datafile='/path/to/sales_data_with_predictions.csv' 
    out=work.sales_data  /* Output dataset location in the WORK library */
    dbms=csv  /* Specify the type of file being imported */
    replace;  /* Replace the existing dataset if it already exists */
    getnames=yes;  /* Use the first row of the file as variable names */
run;

/* Perform descriptive statistics */
proc means data=work.sales_data n mean std min max;
    /* Specify the dataset to analyze */
    var Quantity UnitPrice TotalRevenue PredictedRevenue;
    /* List of variables to include in the analysis */
run;

/* Perform correlation analysis */
proc corr data=work.sales_data;
    /* Specify the dataset to analyze */
    var Quantity UnitPrice TotalRevenue PredictedRevenue;
    /* List of variables to include in the correlation analysis */
run;

/* Regression analysis */
proc reg data=work.sales_data;
    /* Specify the dataset to analyze */
    model TotalRevenue = Quantity UnitPrice;
    /* Define the regression model with TotalRevenue as the dependent variable
       and Quantity and UnitPrice as independent variables */
    output out=work.regression_results p=PredictedTotalRevenue;
    /* Output the results to a new dataset, including predicted values (p=PredictedTotalRevenue) */
run;
quit;

```

### Step 3: Visualize Results in Python
Finally, we'll retrieve the results from SAS and visualize them back in Python. This can obviously be switched out for whatever interface you need to use for your data visualization, such as Power Query, R, C++, or you can just keep the end result in SAS if that is your preferred method!

```python
import pandas as pd
import matplotlib.pyplot as plt
from saspy import SASsession

# Start a SAS session using saspy SASsession
sas = SASsession()

# Retrieve the regression results from SAS
regression_results = sas.sasdata('regression_results', 'work')

# Convert the SAS dataset to a Pandas DataFrame
df_results = regression_results.to_df()

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(df_results['Quantity'], df_results['TotalRevenue'], label='Actual Revenue')
plt.plot(df_results['Quantity'], df_results['PredictedTotalRevenue'], color='red', label='Predicted Revenue')
plt.xlabel('Quantity')
plt.ylabel('Revenue')
plt.title('Regression Analysis of Total Revenue')
plt.legend()
plt.show()

# End the SAS session
sas.endsas()


```
### Benefits of Combining SAS, Python, and AWS:
- *Scalability*: AWS provides scalable storage solutions with S3, making it especially easy to handle large datasets with Python extraction. AWS can of course be swapped with Azure, Google, Snowflake, or SQL Server data warehouse solutions in this context.
- *Flexibility*: Using Python for both the initial data extraction and final visualization allows for a seamless and flexible workflow that dips into SAS only for the regression calculations and uses Plotly for in-house charting.
<br><br>
The visualization output from Python would look something like the below chart. Keep in mind this is only conceptual.
<img src="/Regex.png" alt="Output Example" title="Output Example" style="border: 10px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">
<br><br>

## **Basic Power Query ETL Process**

### 1. Extract:
- In this method, you are actually combining the Extract and Transform methods into a single seamless query structure. Microsoft Power Query provides users of Excel and Power BI with a powerful 'Advanced Editor' capability. Many people believe Power Query is reliant on linear steps that proceed one after another, but this is not true. **The 'Advanced Editor' button within the Power Query view is the secret to unlocking masterful code-like scripting for combining the Extraction and Transformation steps for your data.**

    <img src="/images//PowerQuery1.png" alt="Advanced Editor Button" title="Advanced Editor Button" style="border: 10px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">


    - You can even create set defined variables or set variables to equal a defined NamedRange value from the front-end of the Excel worksheet/report and integrate that value directly into the query.

- This stage involves connecting to a database server hosted on Azure, AWS, etc. Executing a well-defined query to fetch necessary data efficiently, and ensuring the data is accurately captured for further steps.

<img src="/images/Excel1.png" alt="Excel Data Example" title="Excel Data Example" style="border: 10px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;"/>



### 2. Transform:
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



### 3. Load:
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

### Power Query ETL Summary

This ETL process is essential for situations when you need to extract multiple data sources and merge them together in a manner that keeps your reporting files lean and mean! **Whether you are working within cloud platforms (Azure, AWS), traditional SQL databases, or any other data sources that are callable from Power Query (even PDFs and websites!), Microsoft's Advanced Editor feature allows easy SQL integration directly within your queries, optimizing the extraction process and ensuring that heavy data processing tasks are handled with maxium speed and efficiency.** If you happen to be working with terabytes of data, you will need to skip Power Query altogether and go directly into multicore-processing concepts within Python machine learning libraries (and of course, some fancy GPUs).

By consolidating data sources and transformations into a single centralized query, you enhance the scalability and maintainability of your file that relies on heavy calculated business logic for shaping up your end reports. This ensures you are running on optimized performance and efficiency, providing a solid foundation for scaling up your reporting and business data. **All that is required is getting familiar with that Advanced Editor button!**

Thank you for reading my ETL process page! If you are interested in learning more about this concept or others, feel free to drop a message on the Home page! I am also actively looking for a new role, so if your team is hiring, let's chat!


<br><br>

## **Alteryx and SAS for Multifamily Data Analysis**

Here is a more complex example that demonstrates how to use Alteryx and SAS together for a hypothetical investment bank that needs to aggregate underwriting and demographic data on a particular multifamily property asset.

The workflow involves extracting data from a SQL server using Alteryx, performing transformations within the Alteryx workflow, and then using SAS to provide statistical analysis against a wider dataset with comparable properties.

### Step 1: Extract, Transform, and Load Data from SQL Server Using Alteryx

First, we will use Alteryx to connect to the SQL server and extract underwriting and Yardi data. Since I do not have access to an Alteryx platform currently, I will showcase the hypothetical linear workflow steps below: 

```
1. Input Data Tool: Connect to SQL Server
   - Server: your_sql_server
   - Database: multifamily_db
   - Table: underwriting_data, yardi_matrix_data
2. Select Tool: Choose necessary columns
   - underwriting_data: PropertyID, UnderwritingValue, NOI, CapRate
   - yardi_data: PropertyID, OccupancyRate, RentPerUnit
   ```

Next, we perform transformations in Alteryx to clean and prepare the data for analysis.
```
3. Join Tool: Merge underwriting_data and yardi_data on PropertyID
   - Join Fields: PropertyID
4. Formula Tool: Calculate additional metrics
   - CashFlow = [NOI] - ([UnderwritingValue] * [CapRate])
5. Filter Tool: Filter properties with OccupancyRate > 90%
   - Expression: [OccupancyRate] > 0.90
6. Summarize Tool: Aggregate data by PropertyID
   - Group By: PropertyID
   - Sum: CashFlow, RentPerUnit
```

Export the cleaned and transformed data from Alteryx to a CSV file for further analysis in SAS.
```
7. Output Data Tool: Save the transformed data to a CSV file
   - File Path: /path/to/transformed_multifamily_data.csv
```

### Step 2: Perform Statistical Analysis in SAS and Upload Results to SQL Server
Finally, we use SAS to analyze the transformed multifamily data and compare it against a wider dataset with comparable properties. This example demonstrates importing data from the Alteryx csv output file, performing extra data transformations, conducting advanced statistical analysis, and exporting the results back up into a new SQL Server table.
```sas
/* Import the transformed multifamily data from the CSV file */
proc import datafile='/path/to/transformed_multifamily_data.csv' 
    out=work.transformed_data 
    dbms=csv 
    replace;
    getnames=yes;
run;

/* Import a wider dataset with comparable properties from another CSV file */
proc import datafile='/path/to/comparable_properties_data.csv' 
    out=work.comps_data 
    dbms=csv 
    replace;
    getnames=yes;
run;

/* Merge the transformed multifamily data with the comparable properties data */
data work.merged_data;
    merge work.transformed_data (in=a) work.comps_data (in=b);
    by PropertyID;
    /* Keep only the rows that are present in both datasets */
    if a and b;
run;

/* Perform data transformation and create new variables */
data work.analysis_data;
    set work.merged_data;
    /* Calculate Price per Unit */
    PricePerUnit = UnderwritingValue / Units;
    /* Calculate Rent to Value Ratio */
    RentToValueRatio = RentPerUnit / UnderwritingValue;
    /* Flag properties with high occupancy rate */
    HighOccupancy = (OccupancyRate > 0.90);
run;

/* Generate descriptive statistics for the transformed variables */
proc means data=work.analysis_data n mean std min max;
    var CashFlow RentPerUnit PricePerUnit RentToValueRatio;
run;

/* Perform correlation analysis to understand relationships between variables */
proc corr data=work.analysis_data;
    var CashFlow RentPerUnit PricePerUnit RentToValueRatio OccupancyRate;
run;

/* Conduct multiple regression analysis to model CashFlow */
proc reg data=work.analysis_data;
    model CashFlow = RentPerUnit OccupancyRate CapRate PricePerUnit RentToValueRatio;
    /* Output predicted values and residuals */
    output out=work.regression_results p=PredictedCashFlow r=Residuals;
run;
quit;

/* Identify properties with significant deviations from predicted cash flow */
data work.outliers;
    set work.regression_results;
    if abs(Residuals) > 2 * std(Residuals) then Outlier = 1;
    else Outlier = 0;
run;

/* Define the connection to the new SQL server */
libname mydblib odbc dsn='NewSQLServerDSN' user='your_username' password='your_password';

/* Upload the regression results to the new SQL server */
proc sql;
    create table mydblib.regression_results as
    select * from work.regression_results;
quit;

/* Upload the outliers to the new SQL server */
proc sql;
    create table mydblib.outliers as
    select * from work.outliers;
quit;

```

### Alteryx and SAS Summary
In this example, we showcased the transformative power of Alteryx for ETL processes used in combination with SQL Server and SAS for data extraction, transformation, statistical analysis, and insertion. In Alteryx, we connected to a SQL server and extracted critical underwriting and demographics data for a prospective multifamily property. While we used Alteryx, this process can also be seamlessly executed with Power Query for those deeply integrated with Microsoft Power products.

Once the transformed Alteryx data was exported to a CSV file, SAS took center stage to perform some more advanced statistical analysis. We delved into descriptive statistics to understand the data's core characteristics, explored correlation analysis to uncover relationships between variables, and executed regression analysis to compare our property against a broader dataset of comparable properties. Finally, the regression results and identified outliers were uploaded back into a new SQL server location for further use and reporting if necessary.

This workflow showcases the dynamic duo of Alteryx for efficient ETL processes and SAS for robust statistical analysis. Together, they provide comprehensive and actionable insights in a highly efficient manner, providing well-equipped financial professions with the data-driven intelligence needed to make informed decisions about multifamily property investments.

Alteryx is specifically one of my favorite technologies to use, as it provides a transparent no-code developer structure that any data professional can learn to use. Unfortunately I can not include specific Alteryx screenshots, as my free-trial ran out years ago when I got certified, so sorry about that!   
<br><br>

## Closing

In this page, we've explored a variety of powerful ETL methodologies using tools like Power Query, Python, SAS, Alteryx, and cloud services like AWS and SQL Server. By embedding SQL scripts within Power Query, we streamline data processing in Excel and Power BI. We also demonstrated how Python and SAS can be combined for efficient data extraction, transformation, and statistical analysis.

Additionally, we showcased a complex workflow using Alteryx and SAS to handle multifamily property data, highlighting how to extract and transform data from SQL servers, perform advanced analysis, and upload results back to SQL servers. This example emphasized the synergy between Alteryx's user-friendly interface and SAS's robust analytics.

Overall, the discussed techniques provide a solid foundation for optimizing ETL processes, ensuring efficient data processing and insightful analysis. Whether using cloud platforms, traditional databases, or advanced analytical tools, these strategies help achieve maximum efficiency and scalability in data workflows.

Thank you for exploring these ETL concepts with me. If you have any questions or are interested in learning more, feel free to reach out. I'm also actively seeking new opportunities, so if your team is hiring, let's connect!

Best, <br>
Benjamin Pachter 