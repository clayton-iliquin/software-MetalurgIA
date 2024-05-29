from PIL import Image, ImageDraw, ImageFont

class DrawBalances:
    def __init__(self):
        self.font = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf"
        self.font_size = 14
        self.space = 6


    def draw_direct_circuit_balance(self, chart, image = "./Imagenes/direct_circuit.png"):
        """
        This function take the values calculated by DirectGrinding module and 
        order tho show in a image. 

        """
        image = Image.open(image)
        draw = ImageDraw.Draw(image)

        try: 
            font = ImageFont.truetype(self.font,self.font_size)
        except:
            font = ImageFont.truetype("arial.ttf",self.font_size)
        
        # Values for Fresh feed
        draw.multiline_text((90, 405), f"{chart.iloc[0,1]:,.2f}\n{chart.iloc[3,1]:,.2f}\n{chart.iloc[6,1]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for UnderFlow
        draw.multiline_text((170, 195), f"{chart.iloc[0,7]:,.2f}\n{chart.iloc[3,7]:,.2f}\n{chart.iloc[6,7]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Mill Feed
        draw.multiline_text((325, 405), f"{chart.iloc[0,2]:,.2f}\n{chart.iloc[3,2]:,.2f}\n{chart.iloc[6,2]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Mill discharge
        draw.multiline_text((725, 425), f"{chart.iloc[0,4]:,.2f}\n{chart.iloc[3,4]:,.2f}\n{chart.iloc[6,4]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Cyclon Feed
        draw.multiline_text((805, 110), f"{chart.iloc[0,6]:,.2f}\n{chart.iloc[3,6]:,.2f}\n{chart.iloc[6,6]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Cyclon overflow
        draw.multiline_text((565, 70), f"{chart.iloc[0,8]:,.2f}\n{chart.iloc[3,8]:,.2f}\n{chart.iloc[6,8]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for water to mill
        draw.text((485, 530), f"{chart.iloc[3,3]:,.2f}", font=font, fill="black", align = "right")

        # Values for water to sump
        draw.text((805, 320), f"{chart.iloc[3,5]:,.2f}", font=font, fill="black", align = "right")

        # Circ Load
        draw.text((815, 215), f"{chart.iloc[0,7]/chart.iloc[0,8]:.3f}", font=font, fill="black", align = "right")
        
        return image

    def draw_reverse_circuit_balance(self, chart, image = "./Imagenes/reverse_circuit.png"):
        """
        This function take the values calculated by DirectGrinding module and 
        order tho show in a image. 

        """
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        
        try: 
            font = ImageFont.truetype(self.font,self.font_size)
        except:
            font = ImageFont.truetype("arial.ttf",self.font_size)

        # Values for Fresh feed
        draw.multiline_text((85, 195), f"{chart.iloc[0,1]:,.2f}\n{chart.iloc[3,1]:,.2f}\n{chart.iloc[6,1]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for UnderFlow
        draw.multiline_text((965, 195), f"{chart.iloc[0,7]:,.2f}\n{chart.iloc[3,7]:,.2f}\n{chart.iloc[6,7]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Mill Feed
        draw.multiline_text((725, 195), f"{chart.iloc[0,2]:,.2f}\n{chart.iloc[3,2]:,.2f}\n{chart.iloc[6,2]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Mill discharge
        draw.multiline_text((405, 195), f"{chart.iloc[0,4]:,.2f}\n{chart.iloc[3,4]:,.2f}\n{chart.iloc[6,4]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Cyclon Feed
        draw.multiline_text((725, 445), f"{chart.iloc[0,6]:,.2f}\n{chart.iloc[3,6]:,.2f}\n{chart.iloc[6,6]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for Cyclon overflow
        draw.multiline_text((565, 65), f"{chart.iloc[0,8]:,.2f}\n{chart.iloc[3,8]:,.2f}\n{chart.iloc[6,8]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)
        
        # Values for water to mill
        draw.text((890, 340), f"{chart.iloc[3,3]:,.2f}", font=font, fill="black", align = "right")

        # Values for water to sump
        draw.text((85, 360), f"{chart.iloc[3,5]:,.2f}", font=font, fill="black", align = "right")

        # Circ Load
        draw.text((490, 445), f"{chart.iloc[0,7]/chart.iloc[0,8]:.3f}", font=font, fill="black", align = "right")
        
        return image

    def draw_hydrocyclon_simple_balance(self, chart, image ="./Imagenes/hydrocyclon_mass_balance.png"):
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        self.font_size = 12

        try: 
            font = ImageFont.truetype(self.font,self.font_size)
        except:
            font = ImageFont.truetype("arial.ttf",self.font_size)
        
        # Values for Feed flow
        draw.multiline_text((190, 207), f"{chart.iloc[0,1]:,.2f}\n{chart.iloc[3,1]:,.2f}\n{chart.iloc[6,1]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Over flow
        draw.multiline_text((190, 90), f"{chart.iloc[0,2]:,.2f}\n{chart.iloc[3,2]:,.2f}\n{chart.iloc[6,2]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Under flow
        draw.multiline_text((190, 325), f"{chart.iloc[0,3]:,.2f}\n{chart.iloc[3,3]:,.2f}\n{chart.iloc[6,3]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Circ Load
        draw.text((90, 360), f"{chart.iloc[0,3]/chart.iloc[0,2]:.3f}", font=font, fill="black", align = "right")
        
        return image

    def draw_d_sag_mass_balance(self, chart,image ="./Imagenes/d_sag_circuit.png" ):
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        self.font_size = 16

        try: 
            font = ImageFont.truetype(self.font,self.font_size)
        except:
            font = ImageFont.truetype("arial.ttf",self.font_size)

        # Values for Feed flow
        draw.multiline_text((35, 200), f"{chart.iloc[0,1]:,.2f}\n{chart.iloc[3,1]:,.2f}\n{chart.iloc[6,1]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for SAG Discharge
        draw.multiline_text((305, 200), f"{chart.iloc[0,3]:,.2f}\n{chart.iloc[3,3]:,.2f}\n{chart.iloc[6,3]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Pebbles
        draw.multiline_text((490, 200), f"{chart.iloc[0,4]:,.2f}\n{chart.iloc[3,4]:,.2f}\n{chart.iloc[6,4]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Under Trommel
        draw.multiline_text((490, 343), f"{chart.iloc[0,5]:,.2f}\n{chart.iloc[3,5]:,.2f}\n{chart.iloc[6,5]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Mill Discharge
        draw.multiline_text((670, 200), f"{chart.iloc[0,8]:,.2f}\n{chart.iloc[3,8]:,.2f}\n{chart.iloc[6,8]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Over Flow
        draw.multiline_text((853, 54), f"{chart.iloc[0,12]:,.2f}\n{chart.iloc[3,12]:,.2f}\n{chart.iloc[6,12]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for Mill Feed
        draw.multiline_text((853, 200), f"{chart.iloc[0,6]:,.2f}\n{chart.iloc[3,6]:,.2f}\n{chart.iloc[6,6]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for underflow
        draw.multiline_text((1125, 200), f"{chart.iloc[0,11]:,.2f}\n{chart.iloc[3,11]:,.2f}\n{chart.iloc[6,11]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Values for cyclon feed
        draw.multiline_text((1125, 510), f"{chart.iloc[0,11]:,.2f}\n{chart.iloc[3,11]:,.2f}\n{chart.iloc[6,11]:.2f} ", font=font, fill="black", align = "right",spacing = self.space)

        # Circ Load SAG Mill
        draw.text((400, 440), f"{chart.iloc[0,4]/chart.iloc[0,5]:.3f}", font=font, fill="black", align = "right")

        # Circ Load Ball Mill
        draw.text((945, 485), f"{chart.iloc[0,11]/chart.iloc[0,12]:.3f}", font=font, fill="black", align = "right")

        # Values for water to SAG
        draw.text((35, 465), f"{chart.iloc[3,2]:,.2f}", font=font, fill="black", align = "right")
        
        # Values for water to mill
        draw.text((1035, 415), f"{chart.iloc[3,7]:,.2f}", font=font, fill="black", align = "right")

        # Values for water to sump
        draw.text((490, 585), f"{chart.iloc[3,9]:,.2f}", font=font, fill="black", align = "right")

        return image