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
