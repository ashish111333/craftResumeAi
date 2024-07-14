

import reflex as rx



def index()->rx.Component:
    
    return rx.box(
        
        rx.vstack(
    
        rx.heading("CraftResume AI",size="9",
        style={
            "color":"red",
            
        }
        ),

        rx.vstack(
        user_details(),
        skills(),

        
            
        ),
        
        rx.button("Let's start",color_scheme="cyan",size="5",style={"border-radius":"40px"}),
        
        style={

            "width":"100vw",
            "height":"100vh",
            
            
        },
        
        
        
        
    ),
    
    )
    

def skills()->rx.Component:
    return rx.box(

        
        rx.vstack(
            
            rx.input("skill...= "),

            rx.button("Add skill")
            
        ),
        

        style={

            "width":"400px",
            "length":"500px",
            "box_shadow":"3px 10px",
        },

        
    )

    
def education_details()->rx.Component:
    return rx.box(

      rx.vstack(
          rx.hstack(
             
             rx.input(),
             rx.input()
              
          )

          
      )
        
     
        
    )

    
def user_details()->rx.Component:
      
             
    return rx.form(
       
       rx.hstack(
           
           rx.input(
               
               placeholder="enter your preffered role...",
               size="3",
               
               
           ),
           rx.input(
               placeholder="years of exp",
               size="3",
            ),
           
            
            align="center"
           
       ),
       
    

       
   ),
   


app = rx.App()
app.add_page(index)


