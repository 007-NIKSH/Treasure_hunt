from time import sleep
import os

def Clear():
    os.system("clear")

Start_List = [  "[                    ]", 
                "[##                  ]", 
                "[####                ]", 
                "[######              ]", 
                "[########            ]", 
                "[##########          ]", 
                "[############        ]", 
                "[##############      ]", 
                "[################    ]", 
                "[##################  ]", 
                "[####################]"]
Loading_List = ["CREATING CODES AND CLUES:", "LOADING CODES AND CLUES:", "STARTING GAME:"]

def starting():
    Clear()
    sleep(1)

    for y in range(0, len(Loading_List)):
        for x in range(0, len(Start_List)):
            print(Loading_List[y], Start_List[x])
            sleep(0.35)
            Clear()
            x += 1
        y += 1

clue_code = [1,2]
clue_info = ["CLUE 1", "CLUE 2"]
clue_no = 0

def Game():
    starting()
    sleep(1)

    no = clue_no
    game_running = True

    while game_running == True:
        if len(clue_info) == (no):
            sleep(1)
            Clear()
            print("\nCONGRATULATION ON FINDING THE TREASURE\n")
            sleep(1)
            print("THANK YOU FOR PLAYING\n")
            sleep(1)
            game_running = False

        else:
            print(f'CLUE: {clue_info[no]}')
            input_code = input("ENTER CODE: ")
            
            if input_code == "q":
                sleep(1)
                Clear()
                print("\nTHANK YOU FOR PLAYING\n")
                game_running = False

            elif int(input_code) == clue_code[no]:
                sleep(1)
                Clear()
                print("\nCODE ACCEPTED\n")
                no += 1
                continue

            else:
                sleep(1)
                Clear()
                print("\nINVALID CLUE\n")
                continue

Game()