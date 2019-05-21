def main():
    name=str(input())
    size=int(input())
    name=name[:size]
    name=name.replace(' ', '%20')
    print (name)

if __name__ == "__main__":
    main()