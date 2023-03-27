import socket #cette bibliothèque permet de programmer des accès réseau 


def is_connected():
    try:
        # tente de se connecter à google.com et nous dit s'il est accessible
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

print(is_connected())