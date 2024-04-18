# Why hadoop needed?
single central storage
Serial processing 
Lack of ability to process unstructured data

<img width="322" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/4c64a98e-55a7-4f9c-adb4-e1f7f33cb378">

<img width="526" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/4830ff63-dddc-454d-8753-e156fd11cf67">

 ## Master-Slave:
  In a master-slave architecture, one node (the master) controls one or more other nodes (the slaves). The master node coordinates and delegates tasks to the slave nodes, while the slave nodes execute the tasks assigned by the master. This architecture is commonly used in distributed systems for workload distribution and fault tolerance.

   ## Name Node:
   In Hadoop's HDFS (Hadoop Distributed File System), the NameNode is the master node responsible for managing the metadata and namespace of the file system. It keeps track of the directory tree, file permissions, and the mapping of blocks to DataNodes. The NameNode does not store actual file data; it only stores metadata.

  ##  Data Node:
 DataNodes are the slave nodes in HDFS. They store the actual data blocks of files in the distributed file system. DataNodes receive instructions from the NameNode and are responsible for reading, writing, and replicating data blocks across the cluster. They report back to the NameNode about the status of data blocks and perform actions as directed.

  ## Metadata:
  Metadata refers to the data that describes other data. In the context of distributed file systems like HDFS, metadata includes information about file names, file sizes, file permissions, directory structure, replication factor, block locations, and other attributes. The metadata is managed and stored by the NameNode.

## Replication Factor:
  The replication factor is the number of copies of each data block that are stored across the cluster in HDFS. Replication provides fault tolerance and high availability by ensuring that data is not lost if a DataNode fails. The default replication factor in HDFS is typically set to 3, meaning that each data block is replicated three times across different DataNodes.

## Block Size:
  Block size refers to the size of data blocks into which a file is divided in HDFS. HDFS stores large files as a series of blocks, each typically of the same size except for the last block. A larger block size can improve throughput and reduce the overhead of managing a large number of small blocks.

## Heartbeat:
  Heartbeat is a signal sent by nodes in a distributed system to indicate that they are alive and functioning properly. In Hadoop, DataNodes send periodic heartbeats to the NameNode to report their status and availability. If a DataNode fails to send a heartbeat within a certain time interval, the NameNode may consider it as unavailable and take corrective action, such as replicating its data to other nodes.

## Difference Hadoop 1 and 2.0
![image](https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/9b085141-fc3f-434d-8c4d-8e404672ca2b)

<img width="592" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/4d34f5f2-06ae-4829-86b7-8aef179b175e">

<img width="594" alt="image" src="https://github.com/0904-mansi/NucleusTeq_python_Training/assets/81081105/a7ae52b6-5d95-470b-b9f0-60d6a86987b2">
