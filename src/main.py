from textnode import TextNode, TextType

def main():
    dict = {
        "key" : "value"
    }

    def print_method(d):
        for key in d:
            print(f"{key} and {d[key]}")
        return
    
    print_method(dict)

if __name__ == "__main__":
    main()