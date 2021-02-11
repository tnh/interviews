# Fix CloudFormation stack 

## Background

The exiting team member has created a CloudFormation stack that doesn't seem right.

The application also contains a database of users. The business demands a 100% uptime of the application and it must be highly available and cost. Lastly, there are three environments and it doesnt appear that the CloudFormation stack is able to be used for all three environments.

### Issues that the team has noticed 

* there are concerns with the cost of the infrastructure
* there appears to be issues with environmental portability
* there appears to be issues with resiliency

### What would be nice

* The website doesn't support HTTPS - It would be good to support it
* It would be good to have a constant tagging of resources within AWS 
* The only state is in the database, it would be good to be able to scale the application nodes
s
## The CloudFormation stack 

The stack is listed in this directory as `template.yaml`


## What to submit

Please submit changes to the CloudFormation stack so that it meets the meet the business objectives.

### Optionally 

Please also submit a method of being able to deploy this CloudFormation via the command line
