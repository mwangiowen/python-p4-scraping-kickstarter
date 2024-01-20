from bs4 import BeautifulSoup
import ipdb
import os  # Import the os module for checking the current directory

# projects: kickstarter.select("li.project.grid_4")[0]
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")


def create_project_dict():
    # Print the current working directory for debugging
    print("Current Directory:", os.getcwd())

    html = ""
    with open("../fixtures/kickstarter.html") as file:
        html = file.read()
    kickstarter = BeautifulSoup(html, "html.parser")
    projects = {}
    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        projects[title] = {
            "image_link": project.select("div.project-thumbnail a img")[0]["src"],
            "description": project.select("p.bbcard_blurb")[0].text,
            "location": project.select("ul.project-meta span.location-name")[0].text,
            "percent_funded": project.select("ul.project-stats li.first.funded strong")[
                0
            ].text.replace("%", ""),
        }
    # return the projects dictionary
    return projects


# Uncomment the following line to check the current working directory
# print("Current Directory:", os.getcwd())

projects_data = create_project_dict()
print(projects_data)
