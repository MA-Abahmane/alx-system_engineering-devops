#Distributed Web Infrastructure
[image of distributed web infrastructure](https://github.com/MA-Abahmane/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png?raw=true)

[visit](https://www.figma.com/file/oqsLrgXwNIPoFBajBmFGd2/Untitled?type=design&node-id=0%3A1&mode=design&t=HjTJDuuwlBY0uqJS-1)


- The functioning of the load balancer's distribution algorithm and its configuration.
The load balancer is set up with a distribution algorithm called "Round Robin," which works by taking turns using each server behind the load balancer according to their weights. This algorithm is considered fair and smooth as it equally distributes the servers' processing time. Additionally, the Round Robin algorithm is dynamic, allowing server weights to be adjusted while in operation.

- The type of setup enabled by the load balancer.
The load balancer is set up for an "Active-Passive" setup instead of an "Active-Active" setup. An Active-Active setup distributes workloads across all nodes to prevent any single node from becoming overloaded, which leads to better throughput and response times. However, in an Active-Passive setup, not all nodes are active at all times. For example, in a two-node setup, if the first node is active, the second node is passive or on standby. The next passive node can become an active node only if the preceding node is inactive.

- How a Primary-Replica database cluster works.
In a Primary-Replica setup, one server acts as the Primary server, and the other server acts as a Replica of the Primary server. The Primary server can perform both read and write requests, while the Replica server can only perform read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

- The difference between the Primary and Replica nodes concerning the application.
The Primary node is responsible for all write operations, while the Replica node is capable of processing read operations. This helps decrease read traffic to the Primary node.
