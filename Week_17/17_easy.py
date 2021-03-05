def anml_lst(animals, separator):
     new_lst = separator.join(animals)
     return (new_lst)
    
def rev_lst(animals, separator):
     rev_list = animals[::-1]
     print(separator.join(rev_list))

def skip_lst(animals,separator):
     print(separator.join(animals[::2]))
    
def new_file(anml_lst, animals, separator):
    with open ('output_17_test1.txt', 'w') as f:
        f.write(str(anml_lst(animals, separator)))

def main():
     animals = ["dog", "cat", "bird", "horse", "cow", "wolf", "ant", "bee", "chicken"]
     separator = ", "
     anml_lst(animals, separator)
     rev_lst(animals, separator)
     skip_lst(animals,separator)
     new_file((anml_lst), animals, separator)

if __name__ == '__main__':
     main()