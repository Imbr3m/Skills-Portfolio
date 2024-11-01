import random

# Function to load jokes from the file
def load_jokes(filename):
    with open(filename, 'r') as file:
        jokes = file.readlines()
    return jokes

# Joke function
def tell_joke(jokes):
    joke = random.choice(jokes)  
    setup, punchline = joke.split('?') 
    print(setup + '?')  # Present the setup
    input("...\n")  #press enter for nexxt dialogug
    print(punchline.strip())  
    
    print("""
 ░░▓▓▒▒▓▓▓▓████████▓▓██▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██▓▓▓▓
  ░░▒▒▒▒▓▓▓▓▓▓████████▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████▓▓
  ░░░░▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒██▓▓▓▓
  ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒██▓▓▓▓
  ░░░░▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██▓▓▓▓
  ░░░░▒▒▒▒▓▓▒▒▓▓██▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████▓▓▒▒
  ░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒████▓▓  
  ░░░░░░░░▒▒░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██▓▓▒▒  
    ░░░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓    
      ░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░    
      ░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒░░▒▒░░░░░░░░░░░░▓▓      
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒▓▓████▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒        
        ░░░░░░░░        ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒██▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░        
        ░░░░░░        ░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░          
        ░░░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░  ░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░          
          ░░░░        ░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░            
          ░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░            
            ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░          ░░░░░░░░░░░░▒▒░░░░▒▒▒▒░░░░            
          ░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        ░░░░░░░░░░░░░░  ░░░░░░░░░░░░            
                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░        ░░░░░░░░░░░░░░    ░░░░░░░░            
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░          ░░░░░░░░░░  ░░░░░░░░░░░░            
          ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░  ░░░░          ░░░░▒▒░░░░░░░░░░░░░░░░              
          ░░░░  ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░  ░░  ░░        ░░░░▒▒▒▒░░░░░░░░░░░░░░              
          ░░░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░        ░░░░░░▒▒▒▒░░░░░░░░░░░░              
        ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░░░░░                
    ░░  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░                
  ░░░░  ░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░                  
░░░░░░  ░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░                  
░░░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░                    
░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒░░▒▒░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                      
░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░                        
░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒██▒▒░░    ░░░░░░▒▒░░░░░░░░██▒▒▒▒▒▒▒▒░░░░                        
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒░░▒▒▓▓▒▒▒▒  ░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒                            
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒░░                            
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░▓▓▒▒▒▒▒▒▒▒░░                              
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                                
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░                                
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒░░                                  
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░                                    
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░                                      
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                        
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░                                        
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                        
░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░  ░░░░  ░░    ░░                            
░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░    ░░░░░░░░░░                ░░            
          """)

# Main
def main():
    jokes = load_jokes('Assesment 1/Assets/randomJokes.txt')  # Load jokes from file

    while True:
        user_input = input("Type 'Alexa tell me a Joke': \n").strip().lower()
        # checks if input is empty (pressing Enter) or contains the word 'alexa'
        if user_input == "" or "alexa" in user_input:
            tell_joke(jokes)  # Display a joke

            # Ask if another joke
            another = input("\nHey... wanna hear something funny? (yes/no): ").strip().lower()
            if another != "yes":
                print("Tough crowd huh?")
                break
        else:
            print("Please type 'alexa' or press Enter to start.")

if __name__ == "__main__":
    main()
