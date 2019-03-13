from exchangelib import Message, Mailbox, DELEGATE, Account, Credentials,  Configuration
import os

exchangeServer = os.environ['EXCHANGE_SERVER']
exchangeUser = os.environ['EXCHANGE_USER']
exchangePassword = os.environ['EXCHANGE_PASSWORD']
exchangeEmail = os.environ['EXCHANGE_EMAIL']
exchangeCCFolder = os.environ['EXCHANGE_CCFOLDER']
messageToSend = os.environ['EXCHANGE_MESSAGE']

config = Configuration(server=exchangeServer, credentials = Credentials(username=exchangeUser, password=exchangePassword))

account = Account(
    primary_smtp_address=exchangeEmail,
    autodiscover=False,
    config=config,
    access_type=DELEGATE)


def get_ccfolder():
    ccfolder = None
    for folder in account.root._folders_map:
        foldername = account.root._subfolders[folder].name
        if foldername == exchangeCCFolder:
            print(folder, " is the cc folder")
            ccfolder = account.root._subfolders[folder]
    return ccfolder


def walk_inbox():
    itemsToProcess = []
    for item in account.inbox.all():
        if item.cc_recipients is not None:
            if exchangeEmail in item.cc_recipients and item.is_read == False:
                itemsToProcess.append(item)
    return itemsToProcess


def process_cc(itemsToProcess, ccfolder):
    for item in itemsToProcess:
        print(item.author.email_address, " - ", item.subject, ": sending warning back to sender.")
        # need to reply, but also move...
        m = Message(
            account=account,
            folder=account.sent,
            subject='Regarding your email: ' + item.subject,
            body=messageToSend,
            to_recipients=[Mailbox(email_address=item.author.email_address)]
        )
        m.send_and_save()
        item.move(to_folder=ccfolder)


if __name__ == "__main__":
    ccFolder = get_ccfolder()
    if ccFolder is None:
        print("Please specify a valid CC Folder")
        exit(1)
    else:
        items = walk_inbox()
        process_cc(items, ccFolder)