import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Ask the user for page titles and show details."""
    title = input("Enter page title: ").strip()

    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()