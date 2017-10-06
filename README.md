# Base project for python/Cement CLI application
This project is a template for building Command Line Interface applications in python 
using the Cement framework

## Features

### Configuration
Configuration is stored inside the config.conf file in the root of this project.

The [App] Section holds information about the application such as version, description etc.

### Version / Banner
Version is stored in the configuration file.

The banner is generated from data in the configuration file while using the banner.txt file
as a template. If you wish to change the licensing or copyright, modify the banner.txt file.

### Scaffolding
There is basic scaffolding for new files via the cli-tool.py tool, which is a Cement
app itself. It will read templates from the lib/skel directory, ask a few questions and then
generate the file in the correct spot.

Scaffolding is a work in progress.

#### Scaffolds currently supported:

##### controllers
```{r, engine='bash', count_lines}
cli-tool.py generate controller users
```
The controller generator takes one argument as the name of the controller, and add the word
'Controller' to the name of the controller. If you specify the name 'users'. It will generate
'UsersController'.

There are a couple of things you will need to do to activate the controller once it has been generated:
 
- Add the name of the controller to the handlers list in ```App/project.py```
- Import the controller into the ```App/project.py``` file.
