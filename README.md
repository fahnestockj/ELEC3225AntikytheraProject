# ELEC3225AntikytheraProject

## Conda 
 Assuming you've installed miniconda or anaconda
  * [you can do that here](https://docs.conda.io/en/latest/miniconda.html)

  ### MAKE SURE TO CHECK THE ADD TO PATH BOX
  ![](imgs/unknown.png)

## Env setup
 Move to root directory of this project (ELEC3225AntikytheraProject) 
 
 Run this command:

`conda env create --name antikythera --file=environment.yml`

 This creates a virtual enviroment with the relevant packages that needs to be activated to be used

## Windows is terrible
To set up a conda in Powershell you need to be able to run
`conda init powershell`
This creates a powershell profile which needs permissions

Most likely you'll get a permissions error

To fix this 
* run powershell as an administrator
* run:
 `Set-ExecutionPolicy -ExecutionPolicy Unrestricted` 

* accept all
* rerun `conda init powershell`
* relaunch powershell

You should be able to see your conda env to the left of your path in parenthesis like this:
![img](./imgs/env.png)


Activate the venv:

`conda activate antikythera`

Currently the solarSystem.py file can be run with:

`python solarSystem.py`

# Main Menu
Open up main.py and run it. This is the main menu. You will be given choices:
1. Search in database
2. View solar eclipse dates
3. View lunar eclipse dates
4. View solar conjunction dates
5. View solar system simulation

## 1. Search in database
* Queries the dates of all astronomical events and sorts them from earliest to most recent
## 2. View solar eclipse dates
* Queries the dates of all solar eclipses stored in the database that can be used to start the simulation from
## 3. View lunar eclipse dates
* Queries the dates of all lunar eclipses stored in the database that can be used to start the simulation from
## 4. View solar conjunction dates
* Queries the dates of all solar conjunctions stored in the database that can be used to start the simulation from
## 5. View solar system simulation
* User inputs a date to start the simulation from
* Simulation runs in a separate window
* User can pause, resume, and select view: inner planets or outer planets, depending on what they want to see
