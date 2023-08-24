import os
import requests

def fetch_joke():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit&type=single")
        response.raise_for_status()
        return response.json()["joke"]
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return None

if __name__ == "__main__":
    try:
        os.system("clear")
        os.system("say \"Welcome to Joke Inator\"")
        while True:
            key = input("Enter \"joke\" for a Joke and \"q\" to exit: ")
            if key == 'joke':  # Enter
                os.system("clear")
                joke = fetch_joke()
                print(f"\"{joke}\"")
                os.system(f"say \"{joke}\"")
                continue
            elif key == 'q':  # Escape
                os.system("clear")
                os.system("say \"Bye Bye\"")
                print("Bye Bye")
                break  
            else:
                pass 
    except KeyboardInterrupt:
        print("\nUser interrupted. Exiting...")
    except:
        pass