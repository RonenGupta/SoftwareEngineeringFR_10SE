# Preliminary Software Engineering Assessment Task 1

***

## Requirements Definition

***

### Functional Requirements

***

**Data Retrieval: What does the user need to be able to view in the system?**

- A: User must be able to view images from any future chosen NASA API, as well as the information, date, and URL of that NASA image, as well as any external information that the user may want to know.

**User Interface: What is required for the user to interact with the system?**

- A: The user must have the NASA API installed, as well as any python functions in the requirements.txt file at the latest version, to access the information displayed in either GUI or Text Based format.

**Data Display: What information does the user need to obtain from the system?**

- A: Information could include NASA APOD images, Earth Imaging, Mars Rover Photos/Weather and Near Earth Object Services.

***

### Non-Functional Requirements

**Performance: How well does the system need to perform?**

- A: The system must be able to complete basic operations in under 10 seconds, including displaying certain images of APODS and must be able to give access to the user in saving certain information.

**Reliability: How reliable does the system and data need to be?**

- A: As the information derived is specifically space related, the system and data must be specifically from NASA, the most notable organisation I can think of.

**Usability and Accessibility: How easy to navigate does the system need to be? What instructions will we need for users to access the system?**

- A: The system should be relatively easy to navigate, as it will most probably be GUI based leading to a quick and easy access of the data. Following the information in the README, cloning the repository and then installing any of the python commands in the requirements file will allow for accessing the system.

***

### Functional Specifications

**User Requirements - What does the user need to be able to do? List all specifications here.**

- A: User must be able to:

1. View any NASA images from the API's chosen.

2. Be able to save and remove these images to a favourites list and the information related with it. 

3. If any graphs are involved, they should be able to view them in matplotlib graphs and furthermore save them to a list.

**Inputs & Outputs - What inputs will the system need to accept and what outputs will it need to display?**

- A: Inputs and Ouputs accepted and displayed would be:

1. Must accept input of a mouse click on a button in the GUI, it will display any information, images, or graphs regarding that mouse click in that position.

2. If it is text based, it should be able to accept integers as an input such as option 1, option 2, etc. It would then output the image in a pywebview function tab, and the related information would also be outputted with the corresponding information of saving any data.

**Core Features - At its core, what specifically does the program need to be able to do?**

- A: The program must be able to read data from any chosen NASA API and output that information to the user, with the option of saving the data and viewing it on a later date if necessary.

**User Interaction - How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?**

- A: Either command-line or GUI, it should be able to provide choices such as option 1 etc for text based, and for GUI must be able to depict any tabs for viewing certain information such as graphs in a seperate tab, saved information, daily APOD, etc.

**Error Handling - What possible errors could you face that need to be handled by the system?**

- A: Possibly the images may not render in the GUI due to network issues or the NASA API in general. To combat this, I make custom error messages in relation to those problems and suggest fixes for the problem at hand.

***

### Non-Functional Specifications

**Performance - How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?**

- A: Under 10 seconds of loading time for an image and the text will suffice for user engagement. Keeping the code clean and using functions and loops will allow for the peak efficiency of the program.

**Usability / Accessibility - How might you make your application more accessible? What could you do with the User Interface to improve usability?**

- A: Use a notebook function in the GUI. By doing so, I can maximise accessibility and usability, as functions are easily viewable. 

**Reliability - What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Duplicate data? API retrieval crash?**

- A: API retrieval may pose an issue, due to problems with the NASA API in general or network issues. As for any data issues, NASA will have the highest data integrity and duplicate data can be solved by preventing the idea of saving information twice in a list. Additionally, a name can be given to the data in order to sort the list.

***

### Use Case

Actor: User (Astronomer / Space Nerd)

Preconditions: Internet acess, NASA API's, Python Functions (Matplotlib, Tkinter, Pandas, Requests, etc.)

Main Flow:

1. Open System - User opens the GUI, revealing the options that can be made.

2. Search NASA Image/Information - User can find a NASA image or any information based on date or they can derive the newest or oldest API based on user preferences.

3. Save NASA Image/Information - User can save the image and the information corresponding to that in a list, giving it a custom name.

4. Visualise NASA Image/Information - User can visualise the image and the information next to that corresponding image, based on a call from the list they saved it in or by a certain date.

5. Remove Image/Information - User can remove the image and corresponding information through the date or the name they have given it in the list.

Postconditions: Image and Information is retrieved, stored, or removed successfully.

***

## Design

***

### Gantt Chart

***

### Structure Chart

***

### Algorithms

***

### Data Dictionary