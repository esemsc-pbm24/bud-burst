import flet as ft

#Building Page

def main(page: ft.Page):
    page.bgcolor = "#F5F5F5" 
    page.scroll = ft.ScrollMode.ALWAYS
    #page.auto_scroll = True
    page.window.min_height = 1250
    page.fonts = {
        "Roboto": "/fonts/Roboto/Roboto-Regular.ttf"
    }
   
    #page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    deepgreen = "#2E7D32"
    dc ="#333333"
    sw="#F5F5F5"
    wy= "#FBC02D"
    vo = "#FF9800"
    gray="#E0E0E0"
    appbar = ft.AppBar(actions=[
        ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Navigation Links"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Climate-Focused Forest Management"),
                    ft.PopupMenuItem(
                        text="Invasive Species Control"),
                    ft.PopupMenuItem(
                        text="About Us") 
                        ]
                        )],
    title=ft.Text("EcoVision",size=56, weight=ft.FontWeight.BOLD,
                  text_align="start", color = sw, font_family="Roboto",),
    center_title=False,
    toolbar_height=80,
       bgcolor=deepgreen,
         )
    body = ft.Container(
                    content=ft. Column([ft.Text("EcoVision",size=48,color=sw,
                    weight=ft.FontWeight.BOLD,font_family="Roboto"),
                    ft.Row(),
                   ft.Text("Predicting plant development and Pest Invasions for Smarter Forest and Land Management.",
                   size=18,color=gray,italic=True,font_family="Roboto"),
                   ft.Text(""),
                   ft.Text("""
                Our platform uses real-time climate information and historical data 
                to forecast critical plant development stages and pest invasion timings. 
                By understanding how climate conditions influence tree growth and pest cycles, 
                we provide forest managers, farmers, and environmentalists with essential insights 
                to optimize land management, protect ecosystems, and plan effectively for climate-driven changes.
                """,size=16,font_family="Roboto",color=sw,style= [ft.TextStyle(word_spacing=5)]),
                   ft.ElevatedButton(content=
                   ft.Text("Start Predicting Now",color=deepgreen,size=20,
                   weight=ft.FontWeight.BOLD),bgcolor=vo
                   )
                   ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=deepgreen,
                    width=1000,
                    height=500,
                    border_radius=10,
                )

#     #Input Section with Questions

#     a = ft.TextField(label="Enter Fasting Blood Glucose (mmol/l)",
#               helper_text=""" Round to one decimal place. 
#               Example: 5.5
#               """, 
#              max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
#              icon=ft.icons.PERSON, height = 110, text_size= 15)

#     fg = ft.Row(controls=[a]#alignment=ft.MainAxisAlignment.CENTER)
#     )

#     b = ft.TextField(label="Enter 2-hour Post-Prandial",
#               helper_text=""" Round to one decimal place. 
#               Example: 5.5
#               """, 
#              max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
#              icon=ft.icons.PERSON, height = 110, text_size= 15)#,
#              #helper_style= ft.colors.WHITE)

#     thr = ft.Row(controls=[b]
#     ) 

#     c= ft.TextField(label="Enter entry HbA1C (%):",
#               helper_text=""" Round to one decimal place. 
#               Example: 5.5
#               """, max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
#               icon=ft.icons.PERSON, height = 110, text_size= 15)

#     mets = ft.Text("Does client have Metabolic Syndrome?", size= 15,color="black",
#                    weight=ft.FontWeight.BOLD)         

#     dmq = ft.Text("Previous Diagnosis with Type II DM:", size= 15,color="black",
#                    weight=ft.FontWeight.BOLD)         
#     hb = ft.Row(controls=[c])

#     space1=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
#     space2=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
#     space3=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
#     snack = ft.Column()
#     ansh = ft. Column([ft.Text("RECOMMENDATION", weight=ft.FontWeight.BOLD, 
#     text_align=ft.TextAlign.CENTER)], 
#                               horizontal_alignment=ft.CrossAxisAlignment.CENTER)
#     ans = ft.Column()
#     ans_output= ft.Column([ansh,ans])


#     warning = ft.Text("""
#                       NB: Dosages could change with presence of significant comorbidities such as 
#                           renal impairment""" ,
#                       italic=True,size=18, weight=ft.FontWeight.BOLD)
#     def dmalgo():
        
#         try:
#             num1 = float(a.value)
#         except:
#             num1 = 0
            
#         if num1 == 0:
#             pass
#         elif num1 >= 7:
#             snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Type II Diabetes Mellitus", size = 25))
#             countdm +=1
#         elif num1 >=5.6 and num1 <=6.9:
#             snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Pre-Diabetes Mellitus (Type II)",size = 25))
#             countpdm +=1
#         else:
#             snack.controls.append(ft.Text("Normal Fasting Blood Glucose results",size = 25))
#         page.update()

#     def button_clicked(e):

#         dmalgo()
#         page.update()
        
           
#     enter = ft.FilledButton(text="Submit", on_click= button_clicked,icon="check",
#                             style=ft.ButtonStyle(bgcolor=ft.colors.BLACK))
# #Buttton Controls
   
#     def cleared(e):
            
#         a.value = ""
#         b.value = ""
#         c.value = ""
#         m.value = False
#         m.label = "No"
#         dm.value = False
#         dm.label = "No"
#         snack.controls.clear()
#         ans.controls.clear()

#         page.update()
    
#     clearall = ft.FilledTonalButton(text="Clear", on_click= cleared,icon= "close",
#                                style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_GREY_900))
    
#     resets = ft.Row([enter,clearall])

            
#     def metbutton(e):
        
#         m.label = "Yes"
#         m.value = True
                   
#         page.update()

#     m = ft.Switch(label="No", value=False, on_change=metbutton)
    
#     def clearmet(e):
        
#         m.label = "No"
#         m.value = False
                   
#         page.update()
        
    
#     metc = ft.TextButton(text="Clear", on_click = clearmet, icon= "remove",
#                    style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
#                 icon_color = dc)                        
    
    
#     metb=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),mets,m,metc])
#     def dmbutton(e):
        
#         dm.label = "Yes"
#         dm.value = True
                   
#         page.update()

#     dm = ft.Switch(label="No", value=False, on_change=dmbutton)
    
#     def cleardm(e):
        
#         dm.label = "No"
#         dm.value = False
                   
#         page.update()
        
#     dmc = ft.TextButton(text="Clear", on_click = cleardm, icon= "remove",
#                    style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
#                 icon_color = dc)    
#     dmrow=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),dmq,dm,dmc])

    
#     outline= ft.Row([ft.Column([ft.Column([ft.Text("Enter the following details:", 
#     size=20,text_align=ft.TextAlign.CENTER)],
#                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
#             ft.Text("""
#                     NB: Results can be generated even if some sections have no input
#                     If client has been previously diagnosed with Type II DM, 
#                     """, style=ft.TextThemeStyle.LABEL_MEDIUM),
#         space1, fg,space2, thr,space3,hb,metb,dmrow,resets]),
#                     ft.VerticalDivider(color=dc,width=9, thickness=3),
#                     ft.Container(content=ans_output,
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor= "#f8f8ff", #"#fcfcfc",
#                         width=800,
#                         height=800,
#                         border_radius=10)])
                                
#     layout=ft.Container(content=outline,
#                     margin=10,
#                     padding=10,
#                     alignment=ft.alignment.center,
#                     bgcolor= "#FAF9F6",#bebfc0", #"#b6ccce#",
#                     width=510,
#                     height=750,
#                     border_radius=10)
    
                
    page.add(appbar,body)

ft.app(target=main)#, port=8080,view=ft.WEB_BROWSER)