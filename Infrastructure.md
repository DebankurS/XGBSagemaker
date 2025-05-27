# Infrastructure setup

1. Load Balancing:

    In most cases we can consider using a simple round-robin when there is a consistent traffic or least-connection based when the load may not be consistent. There are other strategies which we can implement depending on the use-case

2. Auto-Scaling:

    Auto-scaling typically is of two types- Vertical and Horizontal. The decisions for scaling typically depends on the incoming traffic. We do not want to provision too much resources when there is low traffic.
    
    The minimium for vertical scaling is the resources that is required for a single api call or the average api calls in a day. Additional instances can be scaled up horizontally keeping in mind that they get scaled down when the usage is lower.

    In case of Lambda functions, it has own auto-scaling provisioned since it by nature is a fully managed service and will scale up or down depending on the usage. We can however set upper bound or minimum concurrency requirements

3. Monitoring and logging:

    Monitoring defines essentially the system usage and logging is more about the application specific logs.
    In case of AWS we can setup cloudwatch for both of the above scenarios.

    The main things in consideration is to make sure nothing breaks in the system, for example sudden spikes causing service to be unavailable. That should trigger alerts to the stakeholders. They should be setup on the system.

    In addition, changes to be done on the infra should also be considered. For example, The CPU utilisation reaching 90% consistently is a call to action for scaling up the system with more reserved capacity.

4. Security:

    Primary points of security is to ensure the suface of attack is as less as possible.
    Standard checklist for security:
    1. TLS encryption wherever possible, meaning no http endpoints for communication
    2. AWS IAM Roles: Properly configured roles, to ensure only the essential systems should be able to talk to each other and have only the necessary access
    3. VPC and Security Groups: This will ensure that the traffic can only flow in defined network pathways