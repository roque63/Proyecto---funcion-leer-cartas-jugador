# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
   
     (
         ["4","0","0","3","0"],
        ["", "Jugador1","r1:","c1:","r2:","c2:",
   "0 0 3 0"
         ],
        '''Ejecucion del programa:
        4
        Jugador1
        r1:0
        c1:0
        r2:3
        c2:0
        
        '''
    ),
    (
         ["5", "0","0",    "3","0",   "0","0",  "0","1",  "4","1",  "0","0",  "1","1"],
        ["", "Jugador2",  "r1:","c1:",   "r1:","c1:",   "r1:","c1:",    "r1:","c1:",   "r1:","c1:",   "r2:","c2:",  "r2:","c2:",
         "4 1 1 1",
        ],
        '''Ejecucion del programa:
       2
Jugador2
r1:0
c1:0
r1:3
c1:0
r1:0
c1:0
r1:0
c1:1
r1:4
c1:1
r2:0
c2:0
r2:1
c2:1

        '''
    ),
    (
         ["6",  "1","0", "1","2",   "1","1",  "1","2",  "5","5"],
        ["", "Jugador23", "r1:", "c1:",   "r1:", "c1:",   "r2:","c2:",  "r2:","c2:",  "r2:","c2:",
    "1 2 5 5"
         ],
        '''Ejecucion del programa:
       ...
       '''
    )
    
    


]
