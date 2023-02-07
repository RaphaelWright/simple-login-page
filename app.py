from flet import *


def main(page: Page):
    BG = '#E27D60'
    BG2 = "#41B3A3"
    BTN = "#E8A87C"

    welcome_page_view = Container(
        width = 300,
        height = 600,
        bgcolor=BTN,
        border_radius=30,
    )
        


    

    main_page = Container(
        width = 300,
        height = 600,
        bgcolor=BG,
        border_radius=30,
        content = Column(
            height = 600,
            width = 300,
            controls=[
                Container(
                    content = Text(
                                value="R A P H A E L",
                                size = 35,
                                color = BG2,
                                weight = FontWeight.BOLD,
                                ),
                    padding = padding.only(top=100, left = 45) 
                    ),
                
            
                Container(
                    content= Text("Name",size = 17,color = 'black'),
                    padding = padding.only(top=100, left=35),
                    
                ),
                Container(
                    content= TextField(
                        height=40,
                        content_padding=10,color = 'black',focused_border_color = 'black',
                        cursor_color='black'
                        ),
                    width = 260,
                    border_radius=35,
                    padding = padding.only(left= 35),
                    
                ),
                Container(
                    content= Text("Password",size = 17,color = 'black' ),
                    padding = padding.only(left=35),
                    
                ),
                Container(
                    content= TextField(
                        height=40,
                        content_padding=10,password = True, 
                        color = 'black',
                        focused_border_color = 'black',
                        can_reveal_password=True,
                        cursor_color='black'
                        ),
                    width = 260,
                    border_radius=35,
                    padding = padding.only(left= 35),
                ),
                Container(height = 15),
                Container(
                    width=260,
                    height=50,
                    content= ElevatedButton("Continue", bgcolor=BTN, color = 'black', ),
                    padding=padding.only(left = 35),
                )
                
            ]
        )
    )

    # fullname = main_page.content.controls[2].value
    
    def printname():
        print(fullname)



    page.add(main_page)












app(target=main) 