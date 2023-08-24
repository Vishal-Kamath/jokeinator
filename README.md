# Introducing Jokeinator

Jokeinator is a playful Python program that brings a constant stream of jokes right to your terminal. With the help of the Linux "say" command, Jokeinator not only displays jokes on your screen but also vocalizes them to add an auditory twist to your comedic experience.

## Making of Jokeinator

Jokeinator was made using the [JokeAPI](https://v2.jokeapi.dev/). The program is designed to fetch jokes from the JokeAPI and present them in both text and speech formats.

## The Inner Workings

Let's take a look at the inner workings of Jokeinator. Here is the Python code of Jokeinator

```python
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
            if key == 'joke':
                os.system("clear")
                joke = fetch_joke()
                print(f"\"{joke}\"")
                os.system(f"say \"{joke}\"")
                continue
            elif key == 'q':
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
```

## Features and Usage

1. **Fetching Jokes:** Jokeinator utilizes the JokeAPI to fetch jokes, ensuring they are safe and appropriate for all audiences. By making an API call, the program acquires a single joke that's sure to tickle your funny bone.

2. **Text and Speech Output:** Jokes are presented both in text format on your terminal and in spoken form using the "say" command. This auditory aspect adds an engaging dimension to the humor, making your laughter-filled experience even more immersive.

3. **User-Friendly Interface:** Jokeinator boasts a user-friendly interface. Simply input "joke" to receive a joke or "q" to bid farewell to the program. The interface makes it easy to interact with the program and enjoy a continuous stream of jokes.

## Getting Started

**Install Dependencies:** Before running Jokeinator, ensure you have the required dependencies installed. You can install them using the following command:

```
pip install requests
```

**Run the Program:** Run the Python script in your terminal by executing the following command:

```
python jokeinator.py
```

**Enjoy the Laughter:** Follow the on-screen instructions. Type "joke" to receive a joke and have it read aloud to you using the "say" command. Type "q" to exit the program.
