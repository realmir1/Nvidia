from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

nvd= CTk()

nvd.geometry("600x700")

nvd.resizable(0,0)


canvas = CTkCanvas(master=nvd, width=600, height=700)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/nvdia.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")



newframe = CTkFrame(master=nvd,
                    width=563,
                    height=360,
                    corner_radius=30,
                    border_width=15,
                    border_color="#76B903",
                    fg_color="white",
                    bg_color="white"
                    )
newframe.place(relx=0.5,rely=0.53, anchor="center")

degerler=["GTX 1650", "RTX 3060", "RTX 3070", "RTX 3070 Ti", "RTX 3080", 
    "RTX 3080 Ti", "RTX 3090", "RTX 3090 Ti", "RTX 4060", "RTX 4060 Ti", 
    "RTX 4070", "RTX 4070 Ti", "RTX 4080", "RTX 4090"]




gpu_info_label = CTkLabel(master=newframe, text="", text_color="#76B903" ,
                          width=485, 
                          height=230, 
                          corner_radius=12,
                          font=("arial", 16, "bold"),
                          bg_color="white",
                          fg_color="black")
gpu_info_label.place(relx=0.5, rely=0.6, anchor="center")


def update_gpu_info(selected_gpu):
    gpu_info = {

  "GTX 1650": "NVIDIA GTX 1650\n - 4GB GDDR5\n - 896 CUDA çekirdeği\n -75W güç tüketimi\n -14nm üretim\n -PCIe 3.0\n -Alüminyum alaşım ve düşük ısınma sağlayan soğutma sistemi\n -Performans: 1080p oyunlar için uygun.",
  "RTX 3060": "NVIDIA RTX 3060\n - 12GB GDDR6\n -3584 CUDA çekirdeği\n -170W güç tüketimi\n -12nm üretim\n -PCIe 4.0\n -Gelişmiş soğutma ve alüminyum yapılar\n -Performans: 1440p oyunlar, Ray Tracing ve DLSS desteği.",
  "RTX 3070": "NVIDIA RTX 3070\n - 8GB GDDR6\n -5888 CUDA çekirdeği\n -220W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -Bakır ve alüminyum soğutma\n -Performans: 4K oyunlar için mükemmel.",
  "RTX 3070 Ti": "NVIDIA RTX 3070 Ti\n - 8GB GDDR6X\n -6144 CUDA çekirdeği\n -290W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -Yüksek performanslı soğutma ve alüminyum yapılar\n -Performans: 4K ve AI hesaplamaları.",
  "RTX 3080": "NVIDIA RTX 3080\n - 10GB GDDR6X\n -8704 CUDA çekirdeği\n -320W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -Gelişmiş soğutma, alüminyum ve bakır\n -Performans: 4K oyunlar, Ray Tracing.",
  "RTX 3080 Ti": "NVIDIA RTX 3080 Ti\n - 12GB GDDR6X\n -10240 CUDA çekirdeği\n -350W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -Verimli termal yönetim\n -Performans: 4K ve yüksek çözünürlükte üstün performans.",
  "RTX 3090": "NVIDIA RTX 3090\n - 24GB GDDR6X \n-10496 CUDA çekirdeği\n -350W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -Alüminyum ve bakır yapılar\n -Performans: 8K oyunlar ve veri işleme için ideal.",
  "RTX 3090 Ti": "NVIDIA RTX 3090 Ti\n - 24GB GDDR6X\n -10752 CUDA çekirdeği\n -450W güç tüketimi\n -8nm üretim\n -PCIe 4.0\n -İleri düzey soğutma\n -Performans: En zorlu oyunlar ve yapay zeka görevleri.",
  "RTX 4060": "NVIDIA RTX 4060\n - 8GB GDDR6\n -3584 CUDA çekirdeği\n -170W güç tüketimi\n -5nm üretim\n -PCIe 4.0\n -Alüminyum yapılar\n -Performans: 1080p ve 1440p oyunlar için uygun.",
  "RTX 4060 Ti": "NVIDIA RTX 4060 Ti\n - 8GB GDDR6\n \n-4352 CUDA çekirdeği\n -200W güç tüketimi\n -5nm üretim\n -PCIe 4.0\n -Yüksek verimli alüminyum soğutma\n -Performans: 1440p oyunlar, Ray Tracing.",
  "RTX 4070": "NVIDIA RTX 4070\n - 12GB GDDR6X\n -5888 CUDA çekirdeği\n -250W güç tüketimi\n -5nm üretim\n -PCIe 4.0\n -Bakır soğutma boruları\n -Performans: 4K oyunlar, yüksek çözünürlükte performans.",
  "RTX 4070 Ti": "NVIDIA RTX 4070 Ti\n - 12GB GDDR6X\n \n-7680 CUDA çekirdeği\n -300W güç tüketimi\n -5nm üretim\n -PCIe 4.0\n -Yüksek performanslı alüminyum yapılar\n -Performans: 4K oyunlar ve yapay zeka hesaplamaları.",
  "RTX 4080": "NVIDIA RTX 4080\n - 16GB GDDR6X\n \n-9728 CUDA çekirdeği\n -320W güç tüketimi\n -5nm üretim\n -PCIe 5.0\n -Alüminyum ve bakır soğutma\n -Performans: 8K oyunlar ve profesyonel hesaplamalar.",
  "RTX 4090": "NVIDIA RTX 4090\n - 24GB GDDR6X\n \n-6384 CUDA çekirdeği\n -450W güç tüketimi\n -4nm üretim\n -PCIe 5.0\n -Yüksek verimli soğutma, alüminyum ve bakır yapılar\n -Performans: 8K oyunlar ve yapay zeka uygulamaları."
}


    gpu_info_label.configure(text=gpu_info.get(selected_gpu, "Seçilen GPU hakkında bilgi bulunamadı."))

option1 = CTkOptionMenu(master=newframe,
                        width=180, 
                        values=degerler,
                        bg_color="white",
                        height=50,
                        fg_color="#76B903",
                        corner_radius=20,
                        button_color="black",
                        button_hover_color="#76B903",
                        font=("ariel",14,"bold"),
                        command=update_gpu_info)
                        
newframe2 =CTkFrame
option1.place(anchor="center", relx=0.5, rely=0.13)

# Pencereyi kapatmak için fonksiyon
def close_window():
    nvd.destroy()

close_button = CTkButton(master=nvd,
                         text="Kapat",
                         width=100,
                         height=40,
                         corner_radius=20,
                         fg_color="red",
                         hover_color="darkred",
                         text_color="white",
                         font=("Arial", 14, "bold"),
                         bg_color="white",
                         command=close_window)

close_button.place(anchor="center", relx=0.5, rely=0.84)
nvd.mainloop()