# ELEC3225AntikytheraProject

## Conda 
 Assuming you've installed miniconda or anaconda
  * [you can do that here](https://docs.conda.io/en/latest/miniconda.html)

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

