
sender_domains = {}
sender_subjects = {}
exceptions = {}
subdomains = {}


def add_sender_domain(sender_domain):
    if sender_domain in sender_domains:
        print("Tato doména je již v seznamu odesílatelů spamu.")
    else:
        sender_domains[sender_domain] = True
        print("Doména " + sender_domain + " byla přidána do seznamu odesílatelů spamu.")

def add_sender_subject(sender_subject):
    if sender_subject in sender_subjects:
        print("Tento předmět je již v seznamu odesílatelů spamu.")
    else:
        sender_subjects[sender_subject] = True
        print("Předmět " + sender_subject + " byl přidán do seznamu odesílatelů spamu.")

def add_exception(exception):
    if exception in exceptions:
        print("Tato vyjímka je již v seznamu vyjímek.")
    else:
        exceptions[exception] = True
        print("Vyjímka " + exception + " byla přidána do seznamu vyjímek.")

def add_subdomain(subdomain):
    if subdomain in subdomains:
        print("Tato poddoména je již v seznamu poddomén.")
    else:
        subdomains[subdomain] = True
        print("Poddoména " + subdomain + " byla přidána do seznamu poddomén.")

def show_sender_domains():
    print("Seznam odesílatelů spamu podle domény:")
    for sender_domain in sender_domains:
        print(sender_domain)

def show_sender_subjects():
    print("Seznam odesílatelů spamu podle předmětu:")
    for sender_subject in sender_subjects:
        print(sender_subject)

def show_exceptions():
    print("Seznam vyjímek:")
    for exception in exceptions:
        print(exception)

def show_subdomains():
    print("Seznam poddomén:")
    for subdomain in subdomains:
        print(subdomain)


def spam_filter():
    sender_email = input("Zadejte email odesílatele: ")
    subject = input("Zadejte předmět emailu: ")


    is_spam = False
    print("je to spam")


    sender_domain = sender_email.split("@")[1]
    if sender_domains and sender_domain in sender_domains:
        is_spam = True


    if sender_subjects:
        for sender_subject in sender_subjects:
            if sender_subject in subject:
                is_spam = True
                break
    else:
        
        is_spam = True


    for exception in exceptions:
        if exception in subject:
            is_spam = False
            break

    for subdomain in subdomains:
        if subdomain in sender_domain:
            is_spam = True
            break


    if is_spam:
        print("Email od odesílatele " + sender_email + " s předmětem " + subject + " byl označen jako spam.")
    else:
        print("Email od odesílatele " + sender_email + " s předmětem " + subject + " nebyl označen jako spam.")
        
# Příklad použití funkcí
add_sender_domain("spam.com")
add_sender_subject("Výhra milionů")
add_exception("Nákup")
add_subdomain("sub.spam.com")
show_sender_domains()
show_sender_subjects()
show_exceptions()
show_subdomains()

spam_filter()
