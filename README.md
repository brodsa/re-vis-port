# ReVisPort
ReVisPort is a Python command line reporting tool which enable users to create simple reports. The reports provide the user with descriptive summary of climate data [climate data](https://ourworldindata.org/co2-and-greenhouse-gas-emissions) of EU countries. Besides that, ReVisPort offers the users to add the created reports to their personalized favourites list. Notes or findings can be added to simplify the taks of finding interesting data insights. 

 

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
The goal of ReVisPort is to explore interesting insights of climate data. ReVisPort targets particully users interesting in climate data and data generally. Users does not have to any knowledge about statistic or reporting, ReVisPort navigates users step by step. 

### User Stories
- As a User, I would like create a report without any programming nor statistic knowledge.
- As a User, I would like to be able to change choices I made.
- As a User, I would like to display a created report with all standard aspects.
- As a User, I would like to make notes to about the data instights
- As a User, I would like to have a possibility to save a report.
- As a User, I would like to see all my saved reports and come back to each of them.
- As a User, I would like to delete a saved report, which I do not need anymore.
- ? As a User, I would like to modify some aspekt of a created report later on.
- As a User, I would like to write reference or contact the application developer.

### Colors
Color text using ANSI Code was considered to make the command line application more user-friendly. In total 5 colors were selected. Each color was used only for one purpose, see Table below.

| Color  | ANSI Code | Purpose                                         | Examples                                |
|--------|-----------|-------------------------------------------------|-----------------------------------------|
| White  | [95m      | displayed information, no question, user inputs |                                         |
| Green  | [92m      | actions, successes or asking for user inputs    | Saving...; Enter your choice:           |
| Purple | [95m      | generated tables and report                     |                                         |
| Yellow | [33m      | warnings                                        | Invalid data                            |
| Cyan   | [96m      | questions or menus                              | Select a time period from 2000 and 2020 |

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
- [Empty directory](https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder)
- [Color definition](https://www.geeksforgeeks.org/print-colors-python-terminal/)
- [ANSI color coding][https://codehs.com/tutorial/andy/ansi-colors]
- Python Package Documentation
    - [gspread](https://docs.gspread.org/en/v5.1.0/index.html)
    - [pandas](https://pandas.pydata.org/docs/)



## Acknowledgements
I would like to thank my mentors, [Gareth McGirr](https://github.com/Gareth-McGirr) and [TODO](todo), for their guidance through my project and their valuable inputs. And my special thanks go to my husband for being supportive during the development of the program.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

