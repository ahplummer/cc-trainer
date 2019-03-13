# Instructions

Run this with the following environment variables set:

* EXCHANGE_USER
* EXCHANGE_PASSWORD
* EXCHANGE_SERVER
* EXCHANGE_CCFOLDER
* EXCHANGE_EMAIL

This will log into your MS Exchange server with the appropriate credentials, and will look for the CC Folder specified.

Once found, it will scan your email inbox for any traffic that you are "CC'd" to.

It will then respond to sender, and will move the email into the 'cc folder' specified.

