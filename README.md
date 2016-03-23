# Orctrix

*Creating altmetric-informed narratives of your research*

## Purpose

+ Holistic Portfolio-style presentation of work
  + Illustrate research and career trajectories
+ Provide narrative or visual context for quantitiave impact data
  + Show connection between aspects of your work

### Benefits

+ Highlight aspects of work not captured by a 'traditional' CV
+ Easier to consume for employers
+ Easier to consume for funders

## Requirements

+ ORCID
+ Research outputs with DOIs
+ URLs for external media components (imgur, youtube)

## Software Workflow Description

User enters ORCID code --> API fetched via python --> Matched with Altmetric API data (with python!) --> JSON
User modifies template script --> Pulls data from JSON and Script into Narrative template --> HTML

## Key Features

+ Narrative Creation Tutorial
+ Automated translation of ORCID API (With Altmetric data) to HTML Template
  + User created script 
    + Persistent Identifier(s)
    + Include text box? (narrative)
    + Include media files? (visulatisatiosn)
    + Include altmetric data (donut!)

## Outputs and Uses

+ Output Format
  + HTML 
Possible Uses
  + Staff Page
  + Project About Page
  + Personal Website
  
# Development

Please use virtualen.

You can create a new environment with

~~~
$ python3 -m virtualenv .
~~~

You can load the environment with

~~~
$ source ./bin/activate
~~~

Run

~~~
$ python3 Orctrix/main.py ORCID_ID
~~~
