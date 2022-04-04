'''mermaid
 classDiagram
     Board "1" <-- "40" Square
     Piece "*" <-- "1" Square
     Board "1" --> "2-8" Piece
     Board "1" o-- "2" Dice
     Player "1" <-- "1" Piece
     Start_square "1" <-- "1" Square
     Board "1" <-- "1" Start_square
     Board "1" <-- "1" Jail
     Jail "1" <-- "1" Square
     Square "1" --> "1" Street
     Square "1" --> "1" Station
     Square "1" --> "1" Chance
     Chance "1" o-- "*" Card
     Player "1" <-- "*" Street
     Street "1" <-- "1-4" Houses
     Street "1" <-- "1" Hotel
     class Board{
         throwdice()
     }
     class Square{
         id
         next_square
         action()
     }
     class Dice{
         sides
 
     }
     class Piece{
         id
         current_square
     }
     class Player{
         money
 
     }
     class Start_square{
         action()
     }
     class Jail{
         action()
     }
     class Street{
         name
         action()
     }
     class Station{
         name
     }
     class Chance{
         take_card()
     }
     class Houses{
         id
     }
     class Hotel{
         id
     }
     class Card{
         id
         action()
     }
'''	
