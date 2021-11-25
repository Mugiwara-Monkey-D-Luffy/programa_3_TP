#
#Creado por: Diana María Calderón Mora y Natalia Sofía Rodríguez Solano.
#Hora y fecha de creación: 22/11/2021 a las 1:50pm.
#Fecha y hora de finalización: 01/11/2021 a las 3:00pm.
#Versión 3.9.2

#IMPORTACIÓN DE LIBRERÍAS:
import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import subprocess

#VARIABLES:
path="Manual de usuario.pdf" #AYUDA
partidas_predefinidas_faciles={1:[["5","3","","","7","","","",""],
                                  ["6","","","1","9","5","","",""],
                                  ["","9","8","","","","","6",""],
                                  ["8","","","","6","","","","3"],
                                  ["4","","","8","","3","","","1"],
                                  ["7","","","","2","","","","6"],
                                  ["","6","","","","","2","8",""],
                                  ["","","","4","1","9","","","5"],
                                  ["","","","","8","","","7","9"]],
                               2:[["","","","A","","","C","",""],
                                  ["D","F","","","I","G","","",""],
                                  ["A","","I","","","","","F",""],
                                  ["","G","","","","","","C","H"],
                                  ["I","","H","G","C","E","","B","F"],
                                  ["B","C","D","F","","I","","E","A"],
                                  ["","","B","","A","C","F","",""],
                                  ["","D","","","","","","I",""],
                                  ["","","","I","","H","B","G",""]],
                               3:[["","-","%","","","*","","&",""],
                                  ["*","","+","-","&","#","","","/"],
                                  ["","#","","°","","","","*","+"],
                                  ["","+","-","","#","","/","","*"],
                                  ["","","/","+","$","","","-","°"],
                                  ["°","","#","/","","","&","",""],
                                  ["","&","","#","","+","%","","$"],
                                  ["","","°","*","","","","",""],
                                  ["+","","","&","/","","","",""]]}
partidas_predefinidas_medias={1:[["3","","","","","","","2",""],
                                  ["","8","","4","3","2","","1",""],
                                  ["","5","","","","","6","",""],
                                  ["","7","4","8","6","","","",""],
                                  ["","3","","1","","","7","",""],
                                  ["","","","2","9","6","8","7","1"],
                                  ["6","","","","","","3","4",""],
                                  ["","","","4","1","9","","","5"],
                                  ["1","9","","7","","","","","6"]],
                               2:[["","","G","D","A","E","","",""],
                                  ["","","","","","","G","","E"],
                                  ["D","I","B","","","C","H","","E"],
                                  ["","B","","","","","","D",""],
                                  ["","","D","","","F","A","",""],
                                  ["A","","I","","","","","G","C"],
                                  ["","","","","G","","","","A"],
                                  ["","","","H","","","","","I"],
                                  ["F","","A","E","D","","","","G"]],
                               3:[["","","-","/","","&","+","","%"],
                                  ["","","*","","","","","","/"],
                                  ["","","+","","°","","","-",""],
                                  ["*","","","","","-","%","",""],
                                  ["","","%","","","","-","/",""],
                                  ["$","","","%","","","","","#"],
                                  ["%","","","","","","$","","*"],
                                  ["","°","#","+","*","","/","",""],
                                  ["/","","","","","°","#","",""]]}
partidas_predefinidas_dificiles={1:[["","","","","4","","6","1",""],
                                  ["6","","","","","","","",""],
                                  ["5","","1","","","2","","8","4"],
                                  ["","9","","","","7","","","2"],
                                  ["","","","","8","","","",""],
                                  ["2","1","","3","","6","7","",""],
                                  ["1","","5","","6","3","4","",""],
                                  ["9","6","","","1","5","","",""],
                                  ["3","","","","","","","",""]],
                               2:[["","","E","","","","","",""],
                                  ["","F","B","","","","","C",""],
                                  ["C","G","","","B","","","",""],
                                  ["","","","B","","","","",""],
                                  ["","A","H","","I","","E","","D"],
                                  ["D","","F","","","","","H",""],
                                  ["","C","","F","","","","I",""],
                                  ["","","","","","","","B",""],
                                  ["","","G","E","","I","C","F",""]],
                               3:[["","&","","$","","*","/","",""],
                                  ["","","","°","","/","","",""],
                                  ["","%","/","","&","","*","",""],
                                  ["","","","","","","","/","$"],
                                  ["","","/","+","$","","","-","°"],
                                  ["","","*","","#","°","","","-"],
                                  ["","&","","#","","+","%","","$"],
                                  ["#","","","","","","%","*",""],
                                  ["","+","","","*","","","$",""]]}
elementos_numeros=["1","2","3","4","5","6","7","8","9"]
elementos_letras=["A","B","C","D","E","F","G","H","I"]
elementos_simbolos=["#","*","&","%","°","$","+","-","/"]
bandera_reloj=0
bandera_timer=0
bandera_inicio_juego=0

def nombre():
     """
     Funcionalidad: Valida que el nombre tenga entre 1 y 30 caracteres.
     Entradas: Ninguna.
     Restricciones: El nombre del jugador debe de tener entre 1 y 30 caracteres.
     Salidas: showMessage si el nombre del usuario no tiene entre 1 y 30 caracteres.
     """
     global nombre_j
     nom=nombre_j.get()
     if len(nom)>0 and len(nom)<30:
          inicio()
     else:
          messagebox.showinfo("Usuario"," Debe de ingresar su nombre el mismo debe de \n tener entre 1 y 30 carácteres")

def activa_reloj():
     """
     Funcionalidad: Crea el reloj, lo coloca en la ventana de juego y lo activa.
     Entradas: Ninguna.
     Restricciones: El usuario en la configuración tuvo que haber seleccionado la opción en la configuración.
     Salidas: Crea el reloj y lo pone en la ventana de juego.
     """
     global horas_
     global minutos_
     global segundos_
     global bandera_gane
     global reloj_time
     global pares
     segundos_+=1
     if segundos_==60:
          minutos_+=1
          segundos_=0
     if minutos_==60:
          horas_+=1
          minutos_=0
     #ptop10=horas_+":"+minutos_+":"+segundos_
     hours=f"{horas_}" if horas_>9 else f"0{horas_}"
     minutes=f"{minutos_}" if minutos_>9 else f"0{minutos_}"
     seconds=f"{segundos_}" if segundos_>9 else f"0{segundos_}"
      
     relojito=tk.Label(ventana1,text=hours+"              :              "+minutes+"              :              "+seconds,bg="azure",width=41,font=("Arial Black",10))
     relojito.grid(row=9,column=2)
     if bandera_gane==1:
          relojito.after_cancel(reloj_time)
          showMessage("¡Gananaste!"," FELICIDADES")
          ventana1.destroy()
          pares=[]
          bandera_gane=0
          jugar()
     reloj_time=x.after(1000,activa_reloj)

def activa_timer():
     """
     Funcionalidad: Crea el timer, lo coloca en la ventana de juego y lo activa.
     Entradas: Ninguna.
     Restricciones: El usuario en la configuración tuvo que haber seleccionado la opción en la configuración.
     Salidas: Crea el timer y lo pone en la ventana de juego.
     """
     global horas_1
     global minutos_1
     global segundos_1
     horas_1=int(horas_1)
     minutos_1=int(minutos_1)
     segundos_1=int(segundos_1)
     segundos_1-=1
     if segundos_1<=0 and minutos_1>0:
          minutos_1-=1
          if minutos_1>=0:
               segundos_1=59
          else:
               segundos_1=0
     if minutos_1==0 and horas_1>0:
          horas_1-=1
          if horas_1>=0:
               minutos_1=59
          else:
               minutos_1=0
     hours=f"{horas_1}" if horas_1>9 else f"{horas_1}"
     minutes=f"{minutos_1}" if minutos_1>9 else f"{minutos_1}"
     seconds=f"{segundos_1}" if segundos_1>9 else f"{segundos_1}"
          
     ventana_x=tk.Frame(ventana1,bg="AntiqueWhite1",height=200,width=200)
     reloj=tk.Label(ventana_x,text="Timer",font=("Arial Black",10),bg="cyan",width=13)
     reloj.grid(row=0,column=0)
            
     h=tk.Label(ventana_x,text="Horas",font=("Arial Black",10),bg="green4",width=13)
     h.grid(row=1,column=0)
     m=tk.Label(ventana_x,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
     m.grid(row=1,column=1)
     s=tk.Label(ventana_x,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
     ventana_x.grid(row=8,column=2)
     s.grid(row=1,column=2)
     x=tk.Label(ventana1,text=hours+"              :              "+minutes+"              :              "+seconds,bg="azure",width=41,font=("Arial Black",10))
     x.grid(row=10,column=2)
     if horas_1==0 and minutos_1==0 and segundos_1==0:
          messagebox.showinfo("Game Over"," El tiempo se a expirado")
          ventana1.destroy()
          jugar()
     reloj_time=x.after(1000,activa_timer)

def terminar_juego_f():
     terminar=messagebox.askyesno("Terminar"," ¿Está seguro de terminar el juego?")
     if terminar==0:
          if bandera_inicio_juego==0:
               messagebox.showinfo("ERROR"," No se a iniciado el juego")
          
     #else:
          #llama_funcion_inicio************
def configurar_v():
     """
     Funcionalidad: Despliega la ventana para hacer la configuarción.
     Entradas: Ninguna.
     Restricciones: Los datos del timer tienen que ser correctos.
     Salidas: Ventana para hacer la confirmación.
     """
     global bandera_reloj
     global bandera_timer
     global horas1
     global minutos1
     global segundos1
     global horas_1
     global minutos_1
     global segundos_1
     #open("2048configuración.dat")
     configura=tk.Tk()
     configura.iconbitmap("x.ico")
     configura.title("Configurar")
     configura.geometry("435x275")
     configura.config(bg="AntiqueWhite1")
     configura.resizable(False,False)
     #RELOJ:
     def activa_bandera_reloj():
          """
          Funcionalidad: Activa una bandera para que en la ventan de juego salga el reloj.
          Entradas: Ninguna.
          Restricciones: Ninguna.
          Salidas: Ninguna. 
          """
          global bandera_reloj
          global bandera_timer
          bandera_reloj=1
          bandera_timer=0
     def desactiva_bandera_reloj():
          """
          Funcionalidad: Desactiva una bandera para que en la ventan de juego salga el reloj.
          Entradas: Ninguna.
          Restricciones: Ninguna.
          Salidas: Ninguna.
          """
          global bandera_reloj
          global bandera_timer
          bandera_reloj=0
          bandera_timer=0
     def activa_bandera_timer():
          """
          Funcionalidad: Activa una bandera para que en la ventan de juego salga el timer.
          Entradas: Ninguna.
          Restricciones: Ninguna.
          Salidas: Ninguna.
          """
          global bandera_reloj
          global bandera_timer
          bandera_reloj=0
          bandera_timer=1
     #Niveles
     label_nivel=tk.Label(configura,text="1. Nivel:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_nivel.grid(row=0,column=0)
     #none=tk.Label(configura,text="",bg="AntiqueWhite1")
     #none.grid(row=1,column=0)
     
     nivel=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_nivel=tk.IntVar()
     facil=tk.Radiobutton(nivel,text="Fácil",variable=valor_nivel,value=1,bg="AntiqueWhite1",command=lambda:activa_bandera_reloj())
     facil.grid(row=0,column=0)
     intermedio=tk.Radiobutton(nivel,text="Intermedio",variable=valor_nivel,value=2,bg="AntiqueWhite1",command=lambda:desactiva_bandera_reloj())
     intermedio.grid(row=0,column=1)
     dificil=tk.Radiobutton(nivel,text="Difícil",variable=valor_nivel,value=3,bg="AntiqueWhite1",command=lambda:activa_bandera_timer())
     dificil.grid(row=0,column=2)
     nivel.grid(row=2,column=0)
     #Reloj
     label_reloj=tk.Label(configura,text="2. Reloj:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_reloj.grid(row=3,column=0)
     reloj=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_reloj=tk.IntVar()
     si=tk.Radiobutton(reloj,text="Si",variable=valor_reloj,value=1,bg="AntiqueWhite1",command=lambda:activa_bandera_reloj())
     si.grid(row=0,column=0)
     no=tk.Radiobutton(reloj,text="No",variable=valor_reloj,value=2,bg="AntiqueWhite1",command=lambda:desactiva_bandera_reloj())
     no.grid(row=0,column=1)
     timer=tk.Radiobutton(reloj,text="Timer",variable=valor_reloj,value=3,bg="AntiqueWhite1",command=lambda:activa_bandera_timer())
     timer.grid(row=0,column=2)
     reloj.grid(row=4,column=0)
     #Tabla de tiempo
     reloj_tabla=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     h=tk.Label(reloj_tabla,text="Horas",font=("Arial Black",10),bg="green4",width=13)
     h.grid(row=0,column=1)
     m=tk.Label(reloj_tabla,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
     m.grid(row=0,column=2)
     s=tk.Label(reloj_tabla,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
     s.grid(row=0,column=3)
     horas1=tk.Entry(reloj_tabla,bg="azure")
     horas1.grid(row=1,column=1)
     minutos1=tk.Entry(reloj_tabla,bg="alice blue")
     minutos1.grid(row=1,column=2)
     segundos1=tk.Entry(reloj_tabla,bg="azure")
     segundos1.grid(row=1,column=3)
     reloj_tabla.grid(row=5,column=0)

     label_top_x=tk.Label(configura,text="3. Cantidad de partidas en el Top X:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_top_x.grid(row=6,column=0)
     partidas_topx=tk.Entry(configura,bg="azure")
     partidas_topx.grid(row=7,column=0)
     partidas_top_x=partidas_topx.get()

     elementos_tablero=tk.Label(configura,text="4. Elementos para la Cuadrícula:",font=("Arial Black",10),bg="AntiqueWhite1")
     elementos_tablero.grid(row=8,column=0)
     elementos_table=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_elementos=tk.IntVar()
     numeros=tk.Radiobutton(elementos_table,text="Números",variable=valor_elementos,value=1,bg="AntiqueWhite1",command=lambda:activa_bandera_reloj())
     numeros.grid(row=0,column=0)
     letras=tk.Radiobutton(elementos_table,text="Letras",variable=valor_elementos,value=2,bg="AntiqueWhite1",command=lambda:desactiva_bandera_reloj())
     letras.grid(row=0,column=1)
     simbolos=tk.Radiobutton(elementos_table,text="Símbolos",variable=valor_elementos,value=3,bg="AntiqueWhite1",command=lambda:activa_bandera_timer())
     simbolos.grid(row=0,column=2)
     elementos_table.grid(row=9,column=0)

     aceptar=tk.Button(configura,text="Aceptar",bg="alice blue",font=("Arial Black",8),command=lambda:valida_timer())
     aceptar.grid(row=10,column=3)
     configura.mainloop()
     def valida_timer():
          global horas_1
          global minutos_1
          global segundos_1
          horas_1=horas1.get()
          minutos_1=minutos1.get()
          segundos_1=segundos1.get()
          if horas_1=="" and minutos_1=="" and segundos_1=="":
               messagebox.showinfo("Error"," Al menos uno de las casillas debe de ser llenada")
               configura.destroy()
               configurar()
          if horas_1!="" and minutos_1!="":
               segundos_1=0
          elif minutos_1!="" and segundos_1!="":
               horas_1=0
          elif segundos_1!="" and horas_1!="":
               minutos_1=0
          if horas_1=="" and minutos_1=="":
               horas_1=0
               minutos_1=0
          if minutos_1=="" and segundos_1=="":
               segundos_1=0
               minutos_1=0
          if segundos_1=="" and horas_1=="":
               segundos_1=0
               horas_1=0
          if not int(horas_1)>=0 and not int(horas_1)<=99:
               messagebox.showinfo("Error"," La cantidad de horas debe de estar entre 0 y 99")
               configura.destroy()
               configurar()
          if not int(minutos_1)>=0 and not int(minutos_1)<=0:
               messagebox.showinfo("Error"," La cantidad de minutos deben de estar entre 0 y 59")
               configura.destroy()
               configurar()
          if not int(segundos_1)>=0 and not int(segundos_1)<=0:
               messagebox.showinfo("Error"," La cantidad de segundos deben de estar entre 0 y 59")
               configura.destroy()
               configurar()
          configura.destroy()

#JUGAR:
def jugar_f():
     """
     Funcionalidad: Crea la ventana donde se van a encontrar todos lo botones e interfaz nesesaria para poder jugar.
     Entradas: Ninguna.
     Restricciones: Debe de ser accionada por la opción jugar en el menú.
     Salidas: Ventana de juego.
     """
     global menu_p
     global nombre_j
     menu_p.destroy()
     jugar_v=tk.Tk()
     jugar_v.iconbitmap("x.ico")
     jugar_v.title("SUDOKU")
     jugar_v.geometry("1050x720")
     jugar_v.config(bg="AntiqueWhite1")
     jugar_v.resizable(False,False)
     titulo=tk.Label(jugar_v,text="S U D O K U",font=("Arial Black",20),bg="AntiqueWhite1")
     titulo.grid(row=0,column=2)

     #NOMBRE DEL JUGADOR:
     jugador=tk.Label(jugar_v,text="Jugador",font=("Arial Black",10),bg="AntiqueWhite1")
     jugador.grid(row=1,column=0)
     nombre_j=tk.Entry(jugar_v,width=50)
     nombre_j.grid(row=1,column=2)
     none=tk.Label(jugar_v,bg="AntiqueWhite1")
     none.grid(row=2,column=2)

     #TABLERO DEL JUEGO:**************************************************
     def asigna_valor(x,y):
          for indice,fila in enumerate(matriz_botones):
               for indice1,columna in enumerate(x):
                    if fila==x and columna==y:
                         print(x,y)
     tablero_g=tk.Frame(jugar_v,bg="turquoise")
     matriz_botones=[]
     for x in range (0,11):
          fila_botones=[]
          for y in range (0,11):
               if x==3 or x==7 or y==3 or y==7:
                    none=tk.Label(tablero_g,bg="turquoise")
                    none.grid(row=x,column=y)
                    fila_botones.append(none)
               else:
                    casilla=tk.Button(tablero_g,bg="lavender",activebackground="bisque",height=2,width=5,command=lambda:asigna_valor(x,y))
                    casilla.grid(row=x,column=y,padx=2,pady=2)
                    fila_botones.append(casilla)
     tablero_g.grid(row=3,column=2)
     #ELEMENTOS DEL TABLERO:
     elementos=tk.Frame(jugar_v,bg="SkyBlue1",height=200,width=200)
     uno=tk.Button(elementos,text="1",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     uno.grid(row=0,column=0,padx=2,pady=2)
     dos=tk.Button(elementos,text="2",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     dos.grid(row=0,column=1,padx=2,pady=2)
     tres=tk.Button(elementos,text="3",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     tres.grid(row=0,column=2,padx=2,pady=2)
     cuatro=tk.Button(elementos,text="4",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     cuatro.grid(row=1,column=0,padx=2,pady=2)
     cinco=tk.Button(elementos,text="5",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     cinco.grid(row=1,column=1,padx=2,pady=2)
     seis=tk.Button(elementos,text="6",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     seis.grid(row=1,column=2,padx=2,pady=2)
     siete=tk.Button(elementos,text="7",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     siete.grid(row=2,column=0,padx=2,pady=2)
     ocho=tk.Button(elementos,text="8",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     ocho.grid(row=2,column=1,padx=2,pady=2)
     nueve=tk.Button(elementos,text="9",bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2)#,command=lambda:)
     nueve.grid(row=2,column=2,padx=2,pady=2)
     elementos.grid(row=3,column=5,padx=2,pady=2)
     #BOTONES:
     iniciar_juego=tk.Button(jugar_v,text=" INICIAR \n JUEGO",bg="OliveDrab2",height=2,font=("Arial Black",10),command=lambda:nombre())
     iniciar_juego.grid(row=4,column=3)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=4,column=4)

     deshacer_jugada=tk.Button(jugar_v,text=" DESHACER \n JUGADA",bg="sky blue",height=2,font=("Arial Black",10))#,command=lambda:nueva_p(cuadricula,pares))
     deshacer_jugada.grid(row=4,column=5)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=4,column=6)

     rehacer_jugada=tk.Button(jugar_v,text=" REHACER \n JUGADA",bg="sky blue",height=2,font=("Arial Black",10))#,command=lambda:sal())
     rehacer_jugada.grid(row=4,column=7)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=4,column=8)

     guardar_juego=tk.Button(jugar_v,text="GUARDAR \n JUEGO",bg="pale green",height=2,font=("Arial Black",8))
     guardar_juego.grid(row=4,column=9)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=5,column=4)

     top_x=tk.Button(jugar_v,text=" TOP \n X",bg="gold",height=2,font=("Arial Black",10))
     top_x.grid(row=6,column=3)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=6,column=4)

     borrar_juego=tk.Button(jugar_v,text=" BORRAR \n JUEGO",bg="salmon1",height=2,font=("Arial Black",10))#,command=lambda:salirr())
     borrar_juego.grid(row=6,column=5)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=6,column=6)

     terminar_juego=tk.Button(jugar_v,text=" TERMINAR \n JUEGO",bg="coral2",height=2,font=("Arial Black",10),command=lambda:terminar_juego_f())
     terminar_juego.grid(row=6,column=7)
     none=tk.Label(jugar_v,text="  ",bg="AntiqueWhite1")
     none.grid(row=6,column=8)

     cargar_juego=tk.Button(jugar_v,text="CARGAR \n JUEGO",bg="pale green",height=2,font=("Arial Black",8))
     cargar_juego.grid(row=6,column=9)
     jugar_v.mainloop()
     #RELOJ:
     """
     #ventana_x=tk.Frame(ventana1,bg="AntiqueWhite1",height=200,width=200)
     if bandera_reloj==1:
          ventana_x=tk.Frame(ventana1,bg="AntiqueWhite1",height=200,width=200)
          reloj=tk.Label(ventana_x,text="Reloj",font=("Arial Black",10),bg="cyan",width=13)
          reloj.grid(row=0,column=0)
            
          h=tk.Label(ventana_x,text="Horas",font=("Arial Black",10),bg="green4",width=13)
          h.grid(row=1,column=0)
          m=tk.Label(ventana_x,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
          m.grid(row=1,column=1)
          s=tk.Label(ventana_x,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
          ventana_x.grid(row=8,column=2)
          s.grid(row=1,column=2)
          x=tk.Label(ventana1,text="00            :             00            :           00",font=("Arial Black",10),bg="azure",width=41)
          x.grid(row=9,column=2)
          ventana_x.grid(row=8,column=2)
     if bandera_timer==1:
          ventana_x=tk.Frame(ventana1,bg="AntiqueWhite1",height=200,width=200)
          timer=tk.Label(ventana_x,text="Timer",font=("Arial Black",10),bg="cyan",width=13)
          timer.grid(row=0,column=0)

          h=tk.Label(ventana_x,text="Horas",font=("Arial Black",10),bg="green4",width=13)
          h.grid(row=1,column=0)
          m=tk.Label(ventana_x,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
          m.grid(row=1,column=1)
          s=tk.Label(ventana_x,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
          s.grid(row=1,column=2)

          hora_1=tk.Entry(ventana_x,bg="azure")
          hora_1.grid(row=2,column=0)
          hora_1.insert(0,horas_1)
          minuto_1=tk.Entry(ventana_x,bg="azure")
          minuto_1.grid(row=2,column=1)
          minuto_1.insert(0,minutos_1)
          segundo_1=tk.Entry(ventana_x,bg="azure")
          segundo_1.grid(row=2,column=2)
          segundo_1.insert(0,segundos_1)
          ventana_x.grid(row=8,column=2)
          
          if bandera_mejorj==1:
               mejor_jugador=tk.Label(ventana1,text="Mejor jugador: ",font=("Arial Black",12),bg="AntiqueWhite1")
               mejor_jugador.grid(row=7,column=0)

     """
    

#MENÚ:
def menu():
     global menu_p
     global path
     menu_p=tk.Tk()
     menu_p.iconbitmap("x.ico")
     menu_p.geometry("220x300")
     menu_p.title("SUDOKU")
     menu_p.config(bg="teal")
     menu_p.resizable(False,False)
     p=tk.Label(menu_p,text="              ",bg="teal")
     p.grid(row=1,column=0)
     p=tk.Label(menu_p,text="Bienvenido",font=("Arial Black",15),bg="teal")
     p.grid(row=0,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=1,column=2)
     #Primer botón:
     jugar=tk.Button(menu_p,text="Jugar",command=lambda:jugar_f())
     jugar.grid(row=2,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=3,column=2)
     #Segundo botón:
     configurar=tk.Button(menu_p,text="Configurar",command=lambda:configurar_v())
     configurar.grid(row=4,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=5,column=2)
     #Tercer botón:
     ayuda=tk.Button(menu_p,text="Ayuda",command=lambda:subprocess.Popen([path],shell=True))
     ayuda.grid(row=6,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=7,column=2)
     #Cuarto botón:
     acerca_de=tk.Button(menu_p,text="Acerca de",command=lambda:messagebox.showinfo("Acerca de"," Nombre del programa:          Sudoku \n Versión:                                   1.0.0 \n Fecha de creación:                 22/11/2021 \n Autores:                                  Diana María Calderón Mora \n                                                 Natalia Sofía Rodríguez Solano"))
     acerca_de.grid(row=8,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=9,column=2)
     #Quinto botón:
     salir_menu=tk.Button(menu_p,text="Salir",command=lambda:menu_p.destroy())
     salir_menu.grid(row=10,column=2)
     p=tk.Label(menu_p,text=" ",bg="teal")
     p.grid(row=11,column=2)
     menu_p.mainloop()

#PROGRAMA PRINCIPAL:
menu()
