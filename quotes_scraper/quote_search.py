from mongoengine import connect
from models import Author, Quote

def search_quotes():
    while True:
        command = input("Input command (name: [name]| tag: [tag] | tags: [tag1, tag2] | exit): ").strip()
        
        if command.startswith("name:"):
            author_name = command.split("name:")[1].strip()
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(f"{quote.author.fullname}: {quote.quote}")
            else:
                print(f"Author with name '{author_name}' not found.")
        
        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            quotes = Quote.objects(tags=tag)
            if quotes:
                for quote in quotes:
                    print(f"{quote.author.fullname}: {quote.quote}")
            else:
                print(f"No quotes found with tag '{tag}'.")
        
        elif command.startswith("tags:"):
            tags = [tag.strip() for tag in command.split("tags:")[1].strip().split(",")]
            quotes = Quote.objects(tags__in=tags)
            if quotes:
                for quote in quotes:
                    print(f"{quote.author.fullname}: {quote.quote}")
            else:
                print(f"No quotes found with tags '{tags}'.")
        
        elif command == "exit":
            print("Bye bye.")
            break
        
        else:
            print("Unknown command. Try again.")

search_quotes()