# Browser application deployment solution scenario

## Background

Catch is looking to move to browser based applications.

The marketing team at Catch are looking for a method to deploy a new website called i-love-catch.com.au and we think that this might be a good chance to implement a brand new solution.

We use AWS extensively and we would prefer that these sites be hosted in-house on AWS.

## Requirements

### Infrastructure requirements 

*The solution*

* consider security implications of running the website; the most minimal surface area is preferred
* the website solution ideally should be as fast as possible 
* the solution should be cost effective 
* in development, there might be two or three people working on 'features'
* the website should be monitored from a third party location  

### Workflow (CI) process requirements 

* developers want to be able to make changes quickly - and branch in a codebase and push to a branch and test 
* when code is 'merged to master', it should be deployed 



## What to submit

Submit high level architectural diagrams with some annotated comments of

* The Deployment environment of the website
* The CI flows from code commit to being deployed to production

Optionally

* Any configuration of code for the website and/or example pipeline for your preferred CI
