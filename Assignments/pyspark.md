# fault tolerance
Fault refers to failure, thus fault tolerance in Apache Spark is the capability to operate and to recover loss after a failure occurs. If we want our system to be fault tolerant, it should be redundant because we require a redundant component to obtain the lost data. The faulty data recovers by redundant data.

<img width="700" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/bc26081f-a009-4672-992e-d213e8a960f6">

# Spark Architecture

The Spark follows the master-slave architecture. Its cluster consists of a single master and multiple slaves.

The Spark architecture depends upon two abstractions:

    Resilient Distributed Dataset (RDD)
    Directed Acyclic Graph (DAG)

Resilient Distributed Datasets (RDD)

The Resilient Distributed Datasets are the group of data items that can be stored in-memory on worker nodes. Here,

    Resilient: Restore the data on failure.
    Distributed: Data is distributed among different nodes.
    Dataset: Group of data.

<img width="600" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/48a2fe41-799e-472a-9f78-691ff583039d">

Driver Program

The Driver Program is a process that runs the main() function of the application and creates the SparkContext object. The purpose of SparkContext is to coordinate the spark applications, running as independent sets of processes on a cluster.

To run on a cluster, the SparkContext connects to a different type of cluster managers and then perform the following tasks: -

    It acquires executors on nodes in the cluster.
    Then, it sends your application code to the executors. Here, the application code can be defined by JAR or Python files passed to the SparkContext.
    At last, the SparkContext sends tasks to the executors to run.

Cluster Manager

    The role of the cluster manager is to allocate resources across applications. The Spark is capable enough of running on a large number of clusters.
    It consists of various types of cluster managers such as Hadoop YARN, Apache Mesos and Standalone Scheduler.
    Here, the Standalone Scheduler is a standalone spark cluster manager that facilitates to install Spark on an empty set of machines.

Worker Node

    The worker node is a slave node
    Its role is to run the application code in the cluster.

Executor

    An executor is a process launched for an application on a worker node.
    It runs tasks and keeps data in memory or disk storage across them.
    It read and write data to the external sources.
    Every application contains its executor.

Task

    A unit of work that will be sent to one executor.

Driver: The central component that converts user code into tasks and schedules them on the cluster. It runs the main() function of the application and performs parallel operations on the cluster.

Cluster Manager: Manages the resources of the cluster. It allocates resources to the driver and executors. Common cluster managers include Spark Standalone, YARN, Mesos, and Kubernetes.

Executors: Distributed across the cluster, executors are worker nodes responsible for executing tasks. They run computations and store data for applications.

Tasks: The smallest unit of work in Spark, tasks are executed by the executors. Each task operates on a partition of the data.

DAG Scheduler: Breaks down jobs into stages of tasks based on data shuffling and task dependencies. It optimizes and plans task execution.

Task Scheduler: Responsible for task scheduling within each stage. It sends tasks to executors based on data locality and resource availability.

SQL Context / Hive Context: Allows execution of SQL queries on Spark data.

RDD (Resilient Distributed Dataset): Core abstraction in Spark, representing an immutable, distributed collection of objects. RDDs can be transformed through operations like map, filter, and reduce.
