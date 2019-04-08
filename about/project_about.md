!['image'](../media/projectP.gif)
# Projects App

> An app to display your work as an index that lets viewers sort it by category.

## Project Requirements

1. Portfolio page should include published works and be edited in admin section.
2. The overall design should be able to be used by anyone, regardless of programming experience.
3. There should be a way to view the projects overall information 
4. Larger projects should be able to display all component parts easily
5. User should be able to post links for each section 
6. Projects should have a main image
7. Projects category should be sortable
8. Each project has a customizable intro, an outcome, and a description

### Functional Requirements:

  * Projects selected from project index page link to children pages 
    - The project index page defines function to display info of all direct children pages
    - The project page functions as index page, but links to urls defined in children pages from user admin 
    - main project description can be viewed through pop up on project page 
  * Categories selected on index page display on header and filter projects
    - project category class as register snippet mapped to project page and index page with many-to-many relationship
    - categories defined on index page will filter categories defined on project page as grid-items
  * Related links defines name and url object and maps to project page   
    - project page defines function to return name and url which can be called from template to link accordingly 
    - urls are selected in admin portal through inline panels 
  * User defines main image for project pages 
    - Project Index page defines main_image function which is called by templates of project pages 
  * User defines main image for project objects
    - Project page gallery image is foreign key to project page and is instantiated as object in content panels 
  * Project pages define 3 fields for user input
    - intro objects are standard django models and recieve data from user in field panel on project page 
    - Description is rich text field and apperas in pop up when overview link is selected
    - outcome is rich text field and appears as blockquote when overview link is selected 
    
 ### Code Highlights
