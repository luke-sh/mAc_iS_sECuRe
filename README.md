# mAc_iS_sECuRe
Tool which generates Mac OS malware.
Is Mac Os really that more secure? I think not, is just less targetted so I made this tool (exclusively for demonstration and educational porpuses).

## Requirements
- Python 3.6 +
- Golang 1.14 +

## Installation
### Windows:
  - run setup.bat
  
  Note: on windows use Git Bash to run the program, otherwise you will need to build the malware from the src code manually
### Linux & Mac os:
  - run setup.sh

## Usage
The tool is interactive and easy to use.
### Commands:
  -Ransomware : generates a ransomware working for all mac os versions
  
  -Spy : generates a spyware for mac
  
  -Keylog : generates a keylogger for mac
  
  -Revshell : generates an executable which triggers a reverse shell
  
  -Back : generates a backdoor for mac
  
  -Listen : starts listening on a given port
  
  -FakeRans : generates a fake ransomware that in reality is just renaming files, to troll
  
  -info (or -i) : displays some infos about the tool
  
  -help (or -h) : displays these commands
  
  -clear : clears the screen as it would in an UNIX terminal

### Note:
The commands -Spy and -Back are not available yet since I haven't made the malware yet.

## TO-DO
- Make the spyware and the backdoor
- Add custom, random malware obfuscation
