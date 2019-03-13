# Instructions

## About

This script will connect to MS Exchange with the given creds to analyze your inbox.  When it finds an email with you 
being CC'd, it will do two things:
* Autorespond to sender with canned message that you provide.
* Move the email into a designated "CC" folder, and keep it unread.

The intent of this script is to keep your inbox focused on those emails that you have to act upon.

According to Rule #2 from [CBS's Rules for Email etiquette](https://www.cbsnews.com/news/9-keys-to-email-etiquette/):


>If you're on the CC line, don't reply. There are exceptions to the rule, of course, 
>but you're on the CC line for a reason -- and that reason is "for information only." 
>Let the folks on the "to" line do their job, unless someone specifically invites 
>you into the conversation.

 
## Installation

`pip install -r requirements.txt` will install it, preferably within a virtual environment.  From there, run
the script on whatever frequency you desire.

## Execution 
Run this with the following environment variables set:

* EXCHANGE_USER - this is generally your domain\user username.
* EXCHANGE_PASSWORD - the password needed.
* EXCHANGE_SERVER - the fully qualified server name (without https:// and 'asmx' ending.)
* EXCHANGE_CCFOLDER - the name of the Exchange folder to use to trap your CC traffic. This must exist.
* EXCHANGE_EMAIL - your email address that it will compare to. This can be refactored later.
* EXCHANGE_MESSAGE - your autorespond message.

This will log into your MS Exchange server with the appropriate credentials, and will look for the CC Folder specified.

Once found, it will scan your email inbox for any traffic that you are "CC'd" to.

It will then respond to sender, and will move the email into the 'cc folder' specified.

### To run:

`$ python cc-trainer.py`