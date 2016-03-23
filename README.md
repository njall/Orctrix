# Orctrix

*Creating altmetric-informed narratives of your research*

## Purpose

Orctrix allows researchers to create rich narratives of their career and research trajectories by surrounding your publication and citation data in descriptive and visual context.

### Benefits

By wrapping your citations in narrative text, you can explore aspects of your work&mdash;its origins, aims, and pathways&mdash;that are not captured by traditional CVs. Moreover, it provides potentional collaborators, funders and employers with an intuitive and visually appealing introduction to you and your work.

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
$ cd flaskapp/
$ python mainapp.py
~~~

## Profiles to test

- [Benjamin Laken](http://localhost:5000/0000-0003-2021-6258)
- [Heather Ford](http://localhost:5000/0000-0002-3500-9772)
- [Jens Nielson](http://localhost:5000/0000-0002-8112-8449)
- [Melodee Beals](http://localhost:5000/0000-0002-2907-3313)
- [Niall Beard](http://localhost:5000/0000-0002-2627-0231)
- [Olivia Guest](http://localhost:5000/0000-0002-1891-0972)
- [Raniere Silva](http://localhost:5000/0000-0002-8381-3749)
