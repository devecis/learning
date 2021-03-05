def anml_lst(animals, separator):
     new_lst = separator.join(animals)
     with open('output.txt', 'w') as f:
         f.write(new_lst)
     print(new_lst)
               
def rev_lst(animals, separator):
     back_lst = separator.join(animals[::-1])
     with open('output.txt', 'a') as f:
         f.write('\n' + (back_lst))
     print(back_lst)
     
def skip_lst(animals,separator):
    next_lst = separator.join(animals[::2])
    with open('output.txt', 'a') as f:
        f.write('\n' + (next_lst))
    print(next_lst)
        
    
def main():
     animals = ["dog", "cat", "bird", "horse", "cow", "wolf", "ant", "bee", "chicken"]
     separator = ", "
     anml_lst(animals, separator)
     rev_lst(animals, separator)
     skip_lst(animals,separator)
     
if __name__ == '__main__':
     main()