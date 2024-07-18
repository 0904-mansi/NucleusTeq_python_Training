## Snowflake Architecture

<img width="300" alt="image" src="https://github.com/user-attachments/assets/2df02b39-0b2b-4808-b018-df66438f8e56">

Snowflake’s architecture is a hybrid of traditional shared-disk and shared-nothing database architectures. Similar to shared-disk architectures, Snowflake uses a central data repository for persisted data that is accessible from all compute nodes in the platform. But similar to shared-nothing architectures, Snowflake processes queries using MPP (massively parallel processing) compute clusters where each node in the cluster stores a portion of the entire data set locally. This approach offers the data management simplicity of a shared-disk architecture, but with the performance and scale-out benefits of a shared-nothing architecture.

![image](https://github.com/user-attachments/assets/64ff05e5-89e6-47b1-9247-23629ec7428f)

Snowflake’s unique architecture consists of three key layers:

    Database Storage

    Query Processing

    Cloud Services

### Database Storage

When data is loaded into Snowflake, Snowflake reorganizes that data into its internal optimized, compressed, columnar format. Snowflake stores this optimized data in cloud storage.

### Query Processing

Query execution is performed in the processing layer. Snowflake processes queries using “virtual warehouses”. Each virtual warehouse is an MPP(Massively parallel processing) compute cluster composed of multiple compute nodes allocated by Snowflake from a cloud provider.

Each virtual warehouse is an independent compute cluster that does not share compute resources with other virtual warehouses. As a result, each virtual warehouse has no impact on the performance of other virtual warehouses.

### Cloud Services

The cloud services layer is a collection of services that coordinate activities across Snowflake. These services tie together all of the different components of Snowflake in order to process user requests, from login to query dispatch. The cloud services layer also runs on compute instances provisioned by Snowflake from the cloud provider.

# Zero copy cloning

Replicating real-time data from a production environment into development or staging environments is a common need in project development. In the past, this process was often marred by several challenges: 

Complex Cloning: Cloning another table or an entire database was a complex and time-consuming endeavor, requiring a deep understanding of database structures and often leading to errors. 

Storage Dilemma: Making copies of data involved significant storage requirements, which not only led to increased costs but also created concerns about how to manage and maintain the additional data. 

Cost Issues: The need for additional storage resulted in higher operational costs, often stretching project budgets. 

Time-Consuming: The process of creating and maintaining these copies was lengthy, causing delays in development and testing. 

## What is Zero Copy Cloning in Snowflake? 

Zero Copy Cloning in Snowflake is a powerful feature that offers an efficient way to duplicate a database, schema, or table without incurring any additional costs. It simplifies data replication by creating a copy that shares the same underlying storage as the original object. 

## The Power of Snowflake Zero Copy Clone

In response to these challenges, Snowflake introduced the groundbreaking concept of Zero Copy Clone in Snowflake. This feature not only streamlines data replication but also introduces the concept of cloning, revolutionizing the way data is managed: 

Effortless Cloning: Zero clone copy simplifies the once cumbersome task of cloning tables or databases. It eliminates the complexities, making it accessible to a broader range of users. 

No Additional Storage Costs: Unlike traditional replication methods, Zero Copy Cloning doesn’t incur additional storage costs, thus alleviating the financial burden associated with making duplicate data copies. 

Cost-Efficiency: By eliminating the need for extra storage, Zero Copy Cloning reduces operational costs, freeing up resources for other aspects of project development. 

Swift Replication: With Zero Copy Cloning, the process of replicating data is much faster, eliminating the long waiting times and ensuring project timelines are met. 

## We can clone more objects using a simple SQL statement as shown below. 
```
CREATE DATABASE new_database CLONE old_database; 

CREATE SCHEMA new_schema CLONE old_schema; 

CREATE TABLE new_table CLONE old_table; 

CREATE STREAM new_stream CLONE old_stream; 

CREATE STAGE new_stage CLONE old_stage; 

CREATE FILE FORMAT new_file_format CLONE old_file_format; 

CREATE SEQUENCE new_sequence CLONE old_sequence; 

CREATE TASK new_task CLONE old_task; 
```
## Summary of Snowflake’s Zero Copy Cloning: 

Zero-Copy Cloning in Snowflake is a cost-effective and efficient data replication feature. When you clone a table, it shares the same storage as the original, incurring no extra costs. Changes made in the clone don’t affect the source, ensuring independence. New micro-partitions are created for clone changes, guarded by Continuous Data Protection (CDP). This feature simplifies data management and accelerates provisioning while offering flexibility and cost savings. 


# Materialized Views

A materialized view is a pre-computed data set derived from a query specification (the SELECT in the view definition) and stored for later use. Because the data is pre-computed, querying a materialized view is faster than executing a query against the base table of the view. This performance difference can be significant when a query is run frequently or is sufficiently complex. As a result, materialized views can speed up expensive aggregation, projection, and selection operations, especially those that run frequently and that run on large data sets.

<img width="300" alt="image" src="https://github.com/user-attachments/assets/6f3da98c-3cdc-46bb-9473-fa4cc4c9d248">

Materialized views are faster than tables because of their “cache” (i.e. the query results for the view); in addition, if data has changed, they can use their “cache” for data that hasn’t changed and use the base table for any data that has changed.

<img width="300" alt="image" src="https://github.com/user-attachments/assets/3a6fdc4a-0ead-44ce-bb5e-9c8f7baf5d18">

# FAIL safe 

Fail-safe is a data recovery service that is provided on a best effort basis and is intended only for use when all other recovery options have been attempted.

Fail-safe is not provided as a means for accessing historical data after the Time Travel retention period has ended. It is for use only by Snowflake to recover data that may have been lost or damaged due to extreme operational failures.

Data recovery through Fail-safe may take from several hours to several days to complete.

## Snowflake Time Travel & Fail-safe

Snowflake provides powerful features for ensuring the maintenance and availability of your historical data (i.e. data that has been changed or deleted):

        Querying, cloning, and restoring historical data in tables, schemas, and databases for up to 90 days through Snowflake Time Travel.

        Disaster recovery of historical data (by Snowflake) through Snowflake Fail-safe.

These features are included standard for all accounts, i.e. no additional licensing is required; however, standard Time Travel is 1 day. Extended Time Travel (up to 90 days) requires Snowflake Enterprise Edition. In addition, both Time Travel and Fail-safe require additional data storage, which has associated fees.


## Introduction to Time Travel

Snowflake allows access to past historical data that may have been updated or deleted in the present. Using time travel functionality, we can handle the ’N’ number of situations. For example, if any update happened accidentally on data we would want to revert. So using this time travel functionality, we can recover and query data before the update runs on that data. Similarly, if someone accidentally ran the drop table command, we can easily undo that table and return to the previous state. Also, from a data analysis perspective, we can perform queries on a table over a particular period using the time travel functionality.

Using time travel we can easily perform the below functionalities:

a. We can query the previous data that has been updated or deleted.

b. We can restore databases, tables & schemas that may have been dropped.

c. We can also clone databases, tables & schemas of a specific time. This feature is a combination of both cloning and time travel together.

# Snowflake offers three types of tables namely, Temporary, Transient & Permanent. The default is Permanent.

  ## Temporary tables:
  Only exist within the session in which they were created and persist only for the remainder of the session.
        They are not visible to other users or sessions and do not support some standard features such as cloning.
        Once the session ends, data stored in the table is purged completely from the system and, therefore, is not recoverable, either by the user who created the table or Snowflake.
## Transient tables
  Persist until explicitly dropped and are available to all users with the appropriate privileges.
        Specifically designed for transitory data that needs to be maintained beyond each session (in contrast to temporary tables)
## Permanent Tables (DEFAULT)
  Similar to transient tables, the key difference is that they do have a Fail-safe period. Which provides an additional level of data protection and recovery.
