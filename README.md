# ReVisPort
ReVisPort is a Python command line reporting tool which enable users to create simple reports. The reports provide the user with descriptive summary in order to compare countries in terms of various indices. The indices are mainly related to [climate data](https://ourworldindata.org/co2-and-greenhouse-gas-emissions). Nevertheless, the users can also select more general indices, such as GDP or population.

In addition, ReVisPort offers the users to add the created reports to their personalized favourites list. Notes or findings can be added to simplify the taks of finding interesting data insights. 

 

TODO: screenshot or record

[View](https://re-vis-port-06a4efd9c1c6.herokuapp.com/) the app on-line.
---

## Table of Contents
- [UX](#ux)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies](#technologies)
- [Credits & Inspirations](#credits&inspirations)
- [Acknowledgements](#acknowledgemetns)

---
## UX

### User Stories

### 

- Main Menu ![Main Menu](./docs/ux/logical_flow_main_menu.png)
- Report Menu ![Report Menu](./docs/ux/logical_flow_report_menu.png)
- Favourite Menu ![Favourite Menu](./docs/ux/logical_flow_favourite_menu.png)



---
## Features

### Differences to Design
### Future Enhancements

## Testing

## Deployment

### Clone Repository
In order to clone the repository locally, follow the steps:

1. On Git
    - Go to the repository, i.e. https://github.com/brodsa/re-vis-port
    - You see the content of the repository, i.e. all the files are listed. On the right side at the top of the list, find the Code drop down button and click on it.
    - Copy the repository HTTPS link to the clipboard.
2. In the terminal (Note: git must be preinstalled) 
    - Open the terminal and navigate, where you want to clone the repository.
    - Type `git clone` and insert the content from the clipboard, leading to the command `git clone https://github.com/brodsa/re-vis-port.git`. 
    - Once the project is cloned, you can start using the repository locally.


### Deploy on Heroku

In order to deploy the app on Heroku, an account is required. The steps for the deyploments are as follows:
1. Click "New" and "Create new App" from the menu at right top.
2. Insert a app name and select a region. Click "Create App".
3. Select the "GitHub" deployment method.
4. Search for a repository to connect and a branch to deploy.
5. In the "Setting" tab, go in the section "Buildpacks" and add two buildpacks in the following order: 
    - `heroku/python`
    - `heroku/nodejs`
6. In the "Config Var" section, add two variables:
    - `PORT`: 8000
    - `CREDS`: credentials to connect with a google worksheet
7. In the "Domain" section, copy the URL to view the app.



## Technologies
### Languages
- Python
- Markdown

### Technologies & Tools
- [Lucid](https://lucid.app/documents#/documents?folder_id=recent) to create a flow chart.


## Credits & Inspiration
- Data Sources
    - [Our Word in Data](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv)
    - [List of the EU countries](https://european-union.europa.eu/principles-countries-history/country-profiles_en)
- Documentation of [gspred](https://docs.gspread.org/en/latest/user-guide.html)



## Acknowledgements
I would like to thank my mentors, [Gareth McGirr](https://github.com/Gareth-McGirr) and [TODO](todo), for their guidance through my project and their valuable inputs. And my special thanks go to my husband for being supportive during the development of the program.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!