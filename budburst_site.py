import flet as ft

#Building Page

def main(page: ft.Page):
    page.bgcolor = "#EDEADE" 
    page.scroll = ft.ScrollMode.ALWAYS
    #page.auto_scroll = True
    page.window_min_height = 1250
   
    #page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    bc = "#034c81"
    ic ="#fffff0"
    appbar = ft.AppBar(
      leading=ft.Row([ft.IconButton(ft.icons.INFO, icon_size = 50, icon_color=ic), ft.IconButton(
          ft.icons.SCIENCE, icon_size = 50, icon_color=ic)]
          ), 
      leading_width=100,
    title=ft.Text("EcoVision",size=30, 
                  text_align="start", color = "#fffff0"),
    center_title=True,
    toolbar_height=80,
       bgcolor=bc,
       actions=[ft.IconButton(ft.IconButton(ft.icons.INFO, icon_size = 50, icon_color=ic))
         ])

    #Input Section with Questions

    a = ft.TextField(label="Enter Fasting Blood Glucose (mmol/l)",
              helper_text=""" Round to one decimal place. 
              Example: 5.5
              """, 
             max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
             icon=ft.icons.PERSON, height = 110, text_size= 15)

    fg = ft.Row(controls=[a]#alignment=ft.MainAxisAlignment.CENTER)
    )

    b = ft.TextField(label="Enter 2-hour Post-Prandial Blood Glucose (mmol/l)",
              helper_text=""" Round to one decimal place. 
              Example: 5.5
              """, 
             max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
             icon=ft.icons.PERSON, height = 110, text_size= 15)#,
             #helper_style= ft.colors.WHITE)

    thr = ft.Row(controls=[b]
    ) 

    c= ft.TextField(label="Enter entry HbA1C (%):",
              helper_text=""" Round to one decimal place. 
              Example: 5.5
              """, max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
              icon=ft.icons.PERSON, height = 110, text_size= 15)

    mets = ft.Text("Does client have Metabolic Syndrome?", size= 15,color="black",
                   weight=ft.FontWeight.BOLD)         

    dmq = ft.Text("Previous Diagnosis with Type II DM:", size= 15,color="black",
                   weight=ft.FontWeight.BOLD)         
    hb = ft.Row(controls=[c])

    space1=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
    space2=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
    space3=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
    snack = ft.Column()
    ansh = ft. Column([ft.Text("RECOMMENDATION", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)], 
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    ans = ft.Column()
    ans_output= ft.Column([ansh,ans])


    warning = ft.Text("""
                      NB: Dosages could change with presence of significant comorbidities such as 
                          renal impairment""" ,
                      italic=True,size=18, weight=ft.FontWeight.BOLD)
    def dmalgo():
        
        try:
            num3 = float(c.value)
        except:
            num3 = 0
        
        if num3 == 0:
           pass
        elif num3 >= 9:
            ans.controls.append(ft.Column())
        countpdm =0 
        try:
            num1 = float(a.value)
        except:
            num1 = 0
            
        if num1 == 0:
            pass
        elif num1 >= 7:
            snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Type II Diabetes Mellitus", size = 25))
            countdm +=1
        elif num1 >=5.6 and num1 <=6.9:
            snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Pre-Diabetes Mellitus (Type II)",size = 25))
            countpdm +=1
        else:
            snack.controls.append(ft.Text("Normal Fasting Blood Glucose results",size = 25))
        page.update()
        
        
        
        
    enter = ft.FilledButton(text="Submit", on_click= button_clicked,icon="check",
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLACK))
#Buttton Controls
   
    def cleared(e):
            
        a.value = ""
        b.value = ""
        c.value = ""
        m.value = False
        m.label = "No"
        dm.value = False
        dm.label = "No"
        snack.controls.clear()
        ans.controls.clear()

        page.update()
    
    clearall = ft.FilledTonalButton(text="Clear", on_click= cleared,icon= "close",
                               style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_GREY_900))
    
    resets = ft.Row([enter,clearall])

            
    def metbutton(e):
        
        m.label = "Yes"
        m.value = True
                   
        page.update()

    m = ft.Switch(label="No", value=False, on_change=metbutton)
    
    def clearmet(e):
        
        m.label = "No"
        m.value = False
                   
        page.update()
        
    
    metc = ft.TextButton(text="Clear", on_click = clearmet, icon= "remove",
                   style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
                icon_color = bc)                        
    
    
    metb=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),mets,m,metc])
    def dmbutton(e):
        
        dm.label = "Yes"
        dm.value = True
                   
        page.update()

    dm = ft.Switch(label="No", value=False, on_change=dmbutton)
    
    def cleardm(e):
        
        dm.label = "No"
        dm.value = False
                   
        page.update()
        
    dmc = ft.TextButton(text="Clear", on_click = cleardm, icon= "remove",
                   style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
                icon_color = bc)    
    dmrow=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),dmq,dm,dmc])

    
    outline= ft.Row([ft.Column([ft.Column([ft.Text("Enter the following details:", size=20,text_align=ft.TextAlign.CENTER)],
               horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Text("""
                    NB: Results can be generated even if some sections have no input
                    If client has been previously diagnosed with Type II DM, 
                    the recommendations would be based on the HbA1C.
                    """, style=ft.TextThemeStyle.LABEL_MEDIUM),
        space1, fg,space2, thr,space3,hb,metb,dmrow,resets]),
                    ft.VerticalDivider(color=bc,width=9, thickness=3),ft.Container(content=ans_output,
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor= "#f8f8ff", #"#fcfcfc",
                        width=800,
                        height=800,
                        border_radius=10)])
                                
    layout=ft.Container(content=outline,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor= "#FAF9F6",#bebfc0", #"#b6ccce#",
                    width=510,
                    height=750,
                    border_radius=10)
    
                
    page.add(appbar,layout)

ft.app(target=main)#, port=8080,view=ft.WEB_BROWSER)