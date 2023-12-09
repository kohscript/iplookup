import requests

def get_ip_info(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(api_url)
        data = response.json()

        print("Informations pour l'IP", ip_address)
        print("IP:", data.get("ip"))
        print("Ville:", data.get("city"))
        print("Région:", data.get("region"))
        print("Pays:", data.get("country"))
        print("Code Postal:", data.get("postal"))
        print("Localisation:", data.get("loc"))
        print("Fournisseur de services Internet:", data.get("org"))

        print("\nOptions supplémentaires :")
        print("ASN:", data.get("asn"))
        print("Host:", data.get("hostname"))
        print("Adresse réseau:", data.get("network"))
        print("Type de connexion:", data.get("connection_type"))

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")

if __name__ == "__main__":
    ip_address_to_check = input("Quelle IP veux-tu vérifier? ")

    get_ip_info(ip_address_to_check)
