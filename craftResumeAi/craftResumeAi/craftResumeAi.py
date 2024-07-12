

import reflex as rx



def index()->rx.Component:
    
    return rx.box(
        
        rx.vstack(
    
        rx.heading("CraftResume AI",size="9",
        style={
            "color":"white",
            
        }
            
        ),
        get_user_details(),
        rx.button("Let's start",color_scheme="cyan",size="5",style={"border-radius":"40px"}),
        
        style={

            "width":"100vw",
            "height":"100vh",
            
            
        },
        
        
        align="center",
        
    ),
    
    )
    



def get_user_details()->rx.Component:
      
             
    return rx.form(
       
       rx.vstack(
           
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


