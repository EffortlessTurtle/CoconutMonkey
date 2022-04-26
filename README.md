# CoconutMonkey
This is the CLI and python port of the wanorexia program (https://github.com/EffortlessTurtle/Wanorexia)

v1.0- launched

There are a few tweaks I'd like to make to v1.1:
     -place in /bin/ folder for linux to save on typing when starting the script
     -detect OS type, react accordingly (commands to make directories, etc...)
     -default target the desktop 
     
OVERALL Design Goals:
     -user decides whether to copy or move the files from the folder
     -appropriate help messages
     -command: coconutmonkey "<target file tree>" "<recipient folder>"
     -verbose and quiet thing
     -Only works when tageting /home/ or C:/ folder when user inputs hardcoded password "IKnowWhatImDoing!!!"(to ensure the user doesn't
  activate by accident). Then displays an "are you sure you want to do this?" message before running. [I may not add this functionality to the
  publicly distributed version, only working while tageting folders that ARE NOT /home/ or C:/ ]
