# Backend API deployment solution scenario

## Background

Catch has many backend systems and is looking for a new way to package and deploy a PHP Restful API with a MySQL database.
We use AWS extensively and we would prefer that these sites be hosted in-house on AWS.

## Requirements

### Infrastructure requirements 

*The solution*

* consider security implications of running an API; the most minimal surface area is preferred
* the API is publicly exposed and must be able to respond to load 
* the API must be resilient and fault tolerant 
* the solution should be cost effective 
* in development, there might be two or three people working on 'features'
* the API should be monitored from a third party location  

### Workflow (CI) process requirements 

* developers want to be able to make changes quickly - and branch in a codebase and push to a branch and test 
* when code is 'merged to master', it should be deployed 



## What to submit

Submit high level architectural diagrams with some annotated comments of

* The deployment environment of the API
* The CI flows from code commit to being deployed to production

Optionally

* Any configuration of code for the API and/or example pipeline for your preferred CI
