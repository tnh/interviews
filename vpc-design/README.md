# VPC design scenario

## Scenario

Catch is looking to recreate its AWS environment and needs a way of provisioning VPCs.

Please submit a method of being able to repeatedly deploy a VPC with the below requirements.


## Requirements

### VPC requirements


The VPC must...

* Use a /20 CIDR block
* have a default DHCP options set
* be highly available - with 2 AZs
* have at least one private and one public subnet
* accept http and https traffic from the open internet into the public subnet only
* the private subnet should be able to route out to the internet for software updates
* the private subnet must only support RDS MySQL ports and web ports (http and https)
* provide a clear method of application to be able to find what subnets to use

Additionally if you have time or thoughts, consider how to
* integration with other VPCs 
* talk securely and privately to S3
* talk security and privately to an ECR repo 


### Other requirements 

Please include, if necessary, the most minimal amount of commentary on how to deploy your solution.
