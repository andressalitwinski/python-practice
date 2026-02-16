import sys
import os
import requests

COINCAP_URL = "https://rest.coincap.io/v3/assets/bitcoin"


class UsageError(Exception):
    # Erro de uso do programa (CLI).
    pass


class ExternalServiceError(Exception):
    # Erro ao acessar serviço externo.
    pass


def get_amount_from_argv():
    try:
        return float(sys.argv[1])
    except IndexError:
        raise UsageError("Missing command-line argument")
    except ValueError:
        raise UsageError("Command-line argument is not a number")


def fetch_bitcoin_price(api_key):
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(COINCAP_URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ExternalServiceError("Request to CoinCap failed") from e

    data = response.json().get("data")
    if not data or "priceUsd" not in data:
        raise ExternalServiceError("Invalid response from CoinCap")

    return float(data["priceUsd"])


def main():
    API_KEY = os.getenv("COINCAP_API_KEY")
    if not API_KEY:
        sys.exit("Missing COINCAP_API_KEY")

    try:
        amount = get_amount_from_argv()
        price = fetch_bitcoin_price(API_KEY)
        total = amount * price
        print(f"${total:,.4f}")
    except (UsageError, ExternalServiceError) as e:
        sys.exit(e)


if __name__ == "__main__":
    main()
