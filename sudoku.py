#
#Creado por: Diana María Calderón Mora y Natalia Sofía Rodríguez Solano.
#Hora y fecha de creación: 22/11/2021 a las 1:50pm.
#Fecha y hora de finalización: 01/11/2021 a las 3:00pm.
#Versión 3.9.2

#IMPORTACIÓN DE LIBRERÍAS:
import tkinter as tk
from tkinter import messagebox
from random import randint
from datetime import datetime
import subprocess
from functools import partial
import pickle

#VARIABLES:
path="Manual de usuario.pdf" #AYUDA
##partidas_predefinidas_faciles={1:[["5","3","","","7","","","",""],
##                                  ["6","","","1","9","5","","",""],
##                                  ["","9","8","","","","","6",""],
##                                  ["8","","","","6","","","","3"],
##                                  ["4","","","8","","3","","","1"],
##                                  ["7","","","","2","","","","6"],
##                                  ["","6","","","","","2","8",""],
##                                  ["","","","4","1","9","","","5"],
##                                  ["","","","","8","","","7","9"]],
##                               2:[["","","","1","","","3","",""],
##                                  ["4","6","","","9","7","","",""],
##                                  ["1","","9","","","","","6",""],
##                                  ["","7","","","","","","3","8"],
##                                  ["9","","8","7","3","5","","2","6"],
##                                  ["2","3","4","6","","9","","5","1"],
##                                  ["","","2","","1","3","6","",""],
##                                  ["","4","","","","","","9",""],
##                                  ["","","","9","","8","2","7",""]],
##                               3:[["","8","4","","","2","","3",""],
##                                  ["2","","7","8","3","1","","","9"],
##                                  ["","1","","5","","","","2","7"],
##                                  ["","7","8","","1","","9","","2"],
##                                  ["","","9","7","6","","","8","5"],
##                                  ["5","","1","9","","","3","",""],
##                                  ["","3","","1","","7","4","","6"],
##                                  ["","","5","2","","","","",""],
##                                  ["7","","","3","9","","","",""]]}
##partidas_predefinidas_medias={1:[["3","","","","","","","2",""],
##                                  ["","8","","4","3","2","","1",""],
##                                  ["","5","","","","","6","",""],
##                                  ["","7","4","8","6","","","",""],
##                                  ["","3","","1","","","7","",""],
##                                  ["","","","2","9","6","8","7","1"],
##                                  ["6","","","","","","3","4",""],
##                                  ["","","","4","1","9","","","5"],
##                                  ["1","9","","7","","","","","6"]],
##                               2:[["","","7","4","1","5","","",""],
##                                  ["","","","","","","7","","5"],
##                                  ["4","9","2","","","3","8","","5"],
##                                  ["","2","","","","","","4",""],
##                                  ["","","4","","","6","1","",""],
##                                  ["1","","9","","","","","7","3"],
##                                  ["","","","","7","","","","1"],
##                                  ["","","","8","","","","","9"],
##                                  ["6","","1","5","4","","","","7"]],
##                               3:[["","","8","9","","3","7","","4"],
##                                  ["","","2","","","","","","9"],
##                                  ["","","7","","5","","","8",""],
##                                  ["2","","","","","8","4","",""],
##                                  ["","","4","","","","8","9",""],
##                                  ["6","","","4","","","","","1"],
##                                  ["4","","","","","","6","","2"],
##                                  ["","5","1","7","2","","9","",""],
##                                  ["9","","","","","5","1","",""]]}
##partidas_predefinidas_dificiles={1:[["","","","","4","","6","1",""],
##                                  ["6","","","","","","","",""],
##                                  ["5","","1","","","2","","8","4"],
##                                  ["","9","","","","7","","","2"],
##                                  ["","","","","8","","","",""],
##                                  ["2","1","","3","","6","7","",""],
##                                  ["1","","5","","6","3","4","",""],
##                                  ["9","6","","","1","5","","",""],
##                                  ["3","","","","","","","",""]],
##                               2:[["","","5","","","","","",""],
##                                  ["","6","2","","","","","3",""],
##                                  ["3","7","","","2","","","",""],
##                                  ["","","","2","","","","",""],
##                                  ["","1","8","","9","","5","","4"],
##                                  ["4","","6","","","","","8",""],
##                                  ["","3","","6","","","","9",""],
##                                  ["","","","","","","","2",""],
##                                  ["","","7","5","","9","3","6",""]],
##                               3:[["","3","","6","","2","9","",""],
##                                  ["","","","5","","9","","",""],
##                                  ["","4","9","","3","","2","",""],
##                                  ["","","","","","","","9","6"],
##                                  ["","","9","7","6","","","8","5"],
##                                  ["","","2","","1","5","","","8"],
##                                  ["","3","","1","","7","4","","6"],
##                                  ["1","","","","","","4","2",""],
##                                  ["","7","","","2","","","6",""]]}
##partidas_predefinidas=open("sudoku2021partidas.dat","w")
##partidas_predefinidas.write(str(partidas_predefinidas_faciles))
##partidas_predefinidas.write("\n")
##partidas_predefinidas.write(str(partidas_predefinidas_medias))
##partidas_predefinidas.write("\n")
##partidas_predefinidas.write(str(partidas_predefinidas_dificiles))
##partidas_predefinidas.close()
partidas_predefinidas=open("sudoku2021partidas.dat","r")
texto=partidas_predefinidas.read()
partidas_faciles={}
partidas_medias={}
partidas_dificiles={}
matriz=[]
lista=[]
cont_partidas=0
cont_llaves=0
cont_listas=0
cont=0
for indice,n in enumerate(texto):
     if n=="[" and texto[indice+1]=="[":
          cont_partidas+=1
     if indice<len(texto)-1 and texto[indice+1]!=":":
          if n=="1" or n=="2" or n=="3" or n=="4" or n=="5" or n=="6" or n=="7" or n=="8" or n=="9":
               lista.append(n)
     if n=="'" and texto[indice+1]=="'":
          lista.append("")
     if n=="]" and texto[indice+1]!="]":
          if lista!=[]:
               matriz.append(lista)
               lista=[]
     if n=="]" and texto[indice+1]=="]":
          cont_llaves+=1
          matriz.append(lista)
          if cont_llaves<=3:
               partidas_faciles[cont_partidas]=matriz
          if cont_llaves<=6 and cont_llaves>3:
               if cont_llaves==4:
                    cont=1
               elif cont_llaves==5:
                    cont=2
               else:
                    cont=3
               partidas_medias[cont]=matriz
          if cont_llaves<=9 and cont_llaves>6:
               if cont_llaves==7:
                    cont=1
               elif cont_llaves==8:
                    cont=2
               else:
                    cont=3
               partidas_dificiles[cont]=matriz
          matriz=[]
          lista=[]
elementos_numeros=["1","2","3","4","5","6","7","8","9"]
elementos_letras=["A","B","C","D","E","F","G","H","I"]
elementos_simbolos=["#","*","&","%","°","$","+","-","/"]
bandera_reloj=1
bandera_timer=0
bandera_nivel_facil=1
bandera_nivel_medio=0
bandera_nivel_dificil=0
bandera_top_x=0
bandera_numeros=1
bandera_letras=0
bandera_simbolos=0
bandera_pasa_configuracion=0

gane=1
bandera_boton_picado=0
bandera_inicio_juego=0
elemento_agregar=0
partida=0
elementos_fijos=[]
hr=0
mn=0
sg=0
w=0
bandera_modifica_timer=0
partidas_para_deshacer=[]
f=0
c=0
pila_jugadas_hechas=[]
pila_jugadas_eliminadas=[]
bandera_activa_topx=0

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
          inicio_f()
     else:
          messagebox.showinfo("Usuario"," Debe de ingresar su nombre el mismo debe de \n tener entre 1 y 30 carácteres")

def activa_reloj():
     """
     Funcionalidad: Crea el reloj, lo coloca en la ventana de juego y lo activa.
     Entradas: Ninguna.
     Restricciones: El usuario en la configuración tuvo que haber seleccionado la opción en la configuración.
     Salidas: Crea el reloj y lo pone en la ventana de juego.
     """
     global horas
     global minutos
     global segundos
     global ventana_para_reloj
     global ventana_para_timer
     global hr
     global mn
     global sg
     global reloj_time
     global bandera_activa_topx
     sg+=1
     if sg==60:
          mn+=1
          sg=0
     if mn==60:
          hr+=1
          mn=0
     x="0"
     hours=f"{hr}" if hr>9 else f"0{hr}"
     minutes=f"{mn}" if mn>9 else f"0{mn}"
     seconds=f"{sg}" if sg>9 else f"0{sg}"
     horas.config(text=hours)
     minutos.config(text=minutes)
     segundos.config(text=seconds)
     if bandera_activa_topx==1:
          messagebox.showinfo("Aviso"," Se acaba de desplegar el Top X")
     reloj_time=horas.after(1000,activa_reloj)

def activa_timer():
     """
     Funcionalidad: Crea el timer, lo coloca en la ventana de juego y lo activa.
     Entradas: Ninguna.
     Restricciones: El usuario en la configuración tuvo que haber seleccionado la opción en la configuración.
     Salidas: Crea el timer y lo pone en la ventana de juego.
     """
     global horas_get
     global minutos_get
     global segundos_get
     global horas
     global minutos
     global segundos
     global ventana_para_timer
     global bandera_modifica_timer
     global jugar_v
     global hr
     global mn
     global sg
     global bandera_activa_topx
     horas_get=int(horas_get)
     minutos_get=int(minutos_get)
     segundos_get=int(segundos_get)
     segundos_get-=1
     if segundos_get<=0 and minutos_get>0:
          minutos_get-=1
          if minutos_get>=0:
               segundos_get=59
          else:
               segundos_get=0
     if minutos_get==0 and horas_get>0:
          horas_get-=get
          if horas_get>=0:
               minutos_get=59
          else:
               minutos_1=0
     hours=f"{horas_get}" if horas_get>9 else f"{horas_get}"
     minutes=f"{minutos_get}" if minutos_get>9 else f"{minutos_get}"
     seconds=f"{segundos_get}" if segundos_get>9 else f"{segundos_get}"
     if bandera_modifica_timer==0:
          bandera_modifica_timer=1
          horas=tk.Label(ventana_para_timer,text=hours,font=("Arial Black",10),bg="azure",width=13)
          horas.grid(row=2,column=0)
          minutos=tk.Label(ventana_para_timer,text=minutes,font=("Arial Black",10),bg="azure",width=13)
          minutos.grid(row=2,column=1)
          segundos=tk.Label(ventana_para_timer,text=seconds,font=("Arial Black",10),bg="azure",width=13)
          segundos.grid(row=2,column=2)
     else:
          horas.config(text=hours)
          minutos.config(text=minutes)
          segundos.config(text=seconds)
     if horas_get==0 and minutos_get==0 and segundos_get==0:
          game_over=messagebox.askyesno("Tiempo Expirado"," ¿Desea continuar el mismo juego?")
          if game_over==0:
               jugar_v.destroy()
               jugar_f()
          else:
               return activa_reloj()
     if bandera_activa_topx==1:
          messagebox.showinfo("Aviso"," Se acaba de desplegar el Top X")
     reloj_time=horas.after(1000,activa_timer)

def terminar_juego_f():
     global gane
     global jugar_v
     global bandera_inicio_juego
     terminar=messagebox.askyesno("Terminar"," ¿Está seguro de terminar el juego?")
     if terminar==0:
          if bandera_inicio_juego==0:
               messagebox.showinfo("ERROR"," No se a iniciado el juego")
     else:
          gane=2
          jugar_v.destroy()
          jugar_f()
"""
def guardar_partida_f():
     global
     guarda=open()
"""
def activa_bandera_topx():
     global bandera_activa_topx
     bandera_activa_topx=1
     ########otra llamadaaaaaaaaaaaaaaaaaaaaa

class Jugadas_hechas:
     def __init__(self,fila,columna,elemento):
          self.fila=fila
          self.columna=columna
          self.elemento=elemento
     def obtener_jugada_hecha(self):
          return self.fila,self.columna,self.elemento
     def obtiene_fila_columna(self):
          return self.fila,self.columna
     def obtiene_valor(self):
          return self.elemento

def deshacer_partida_f():
     global pila_jugadas_eliminadas
     global pila_jugadas_hechas
     global matriz_botones
     global matriz_botones_2
     global bandera_inicio_juego
     if bandera_inicio_juego==1:
          if len(pila_jugadas_hechas)==0:
               messagebox.showinfo("ERROR"," No hay jugadas para deshacer")
          elif len(pila_jugadas_hechas)==1:
               ultima_jugada=pila_jugadas_hechas.pop()
               partida_ultima=ultima_jugada.obtener_jugada_hecha()
               matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0].config(text="")
               matriz_botones_2[partida_ultima[0]][partida_ultima[1]]=(matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0],"")
               je=Jugadas_eliminadas(ultima_jugada.fila,ultima_jugada.columna,ultima_jugada.elemento)
               pila_jugadas_eliminadas.append(je)
          else:
               if len(pila_jugadas_hechas)>=2:
                    mismo2=pila_jugadas_hechas[-2]
                    mismo1=pila_jugadas_hechas[-1]
                    ultima_jugada=pila_jugadas_hechas.pop()
                    mismo_1=mismo1.obtiene_fila_columna()
                    mismo_2=mismo2.obtiene_fila_columna()
                    valor=mismo2.obtiene_valor()
                    if mismo_1==mismo_2:
                         partida_ultima=ultima_jugada.obtener_jugada_hecha()
                         matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0].config(text=valor)
                         matriz_botones_2[partida_ultima[0]][partida_ultima[1]]=(matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0],valor)
                         je=Jugadas_eliminadas(ultima_jugada.fila,ultima_jugada.columna,ultima_jugada.elemento)
                         pila_jugadas_eliminadas.append(je)
                    else:
                         partida_ultima=ultima_jugada.obtener_jugada_hecha()
                         matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0].config(text="")
                         matriz_botones_2[partida_ultima[0]][partida_ultima[1]]=(matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0],"")
                         je=Jugadas_eliminadas(ultima_jugada.fila,ultima_jugada.columna,ultima_jugada.elemento)
                         pila_jugadas_eliminadas.append(je)
     else:
          messagebox.showinfo("ERROR"," No se ha iniciado el juego")

class Jugadas_eliminadas:
     def __init__(self, fila, columna, elemento):
          self.fila=fila
          self.columna=columna
          self.elemento=elemento
     def obtener_jugada_eliminada(self):
          return self.fila,self.columna,self.elemento
     def obtiene_fila(self):
          return self.fila
     def obtiene_columna(self):
          return self.columna
     def obtiene_valor(self):
          return self.elemento
def rehacer_partida_f():
     global matriz_botones
     global matriz_botones_2
     global pila_jugadas_eliminadas
     global bandera_inicio_juego
     if bandera_inicio_juego==1:
          if len(pila_jugadas_eliminadas)==0:
               messagebox.showinfo("ERROR"," No hay jugadas para rehacer")
          else:
               mismo1=pila_jugadas_eliminadas[-1]
               ultima_jugada=pila_jugadas_eliminadas.pop()
               partida_ultima=ultima_jugada.obtener_jugada_eliminada()
               fil=mismo1.obtiene_fila()
               col=mismo1.obtiene_columna()
               valor=mismo1.obtiene_valor()
               matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0].config(text=valor)
               matriz_botones_2[partida_ultima[0]][partida_ultima[1]]=(matriz_botones_2[partida_ultima[0]][partida_ultima[1]][0],valor)
               jo=Jugadas_hechas(fil,col,valor)
               pila_jugadas_hechas.append(jo)
     else:
          messagebox.showinfo("ERROR"," No se ha iniciado el juego")

def configurar_v():
     """
     Funcionalidad: Despliega la ventana para hacer la configuarción.
     Entradas: Ninguna.
     Restricciones: Los datos del timer tienen que ser correctos.
     Salidas: Ventana para hacer la confirmación.
     """
     global bandera_reloj
     global bandera_timer
     global segundos1
     global minutos1
     global horas1
     global horas_1
     global minutos_1
     global segundos_1
     global bandera_nivel_facil
     global bandera_nivel_medio
     global bandera_nivel_dificil
     global bandera_top_x
     global partidas_topx
     global bandera_numeros
     global bandera_letras
     global bandera_simbolos
     global bandera_pasa_configuracion
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
     def validaciones_configuracion():
          global bandera_timer
          global horas1
          global minutos1
          global segundos1
          global horas_1
          global minutos_1
          global segundos_1
          global partidas_topx
          global bandera_pasa_configuracion
          if bandera_timer==1:
               horas_1=horas1.get()
               minutos_1=minutos1.get()
               segundos_1=segundos1.get()
               if horas_1=="" and minutos_1=="" and segundos_1=="":
                    messagebox.showinfo("Error"," Al menos uno de las casillas debe de ser llenada")
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
               if not int(horas_1)>=0 and not int(horas_1)<=4:
                    messagebox.showinfo("Error"," La cantidad de horas debe de estar entre 0 y 4")
               if not int(minutos_1)>=0 and not int(minutos_1)<=59:
                    messagebox.showinfo("Error"," La cantidad de minutos deben de estar entre 0 y 59")
               if not int(segundos_1)>=0 and not int(segundos_1)<=59:
                    messagebox.showinfo("Error"," La cantidad de segundos deben de estar entre 0 y 59")
          partidas_top_x=partidas_topx.get()
          if partidas_top_x!="" and int(partidas_top_x)>=0 and int(partidas_top_x)<=100:
               bandera_top_x=partidas_top_x
               bandera_pasa_configuracion=1
          else:
               messagebox.showinfo("Error"," La cantidad de partidas en el Top X \n debe de estar entre 0 y 100")
          if bandera_pasa_configuracion==1:
               #open("sudoku2021configuración.dat")
               configura.destroy()
     def activa_bandera_facil():
          global bandera_nivel_facil
          global bandera_nivel_medio
          global bandera_nivel_dificil
          banadera_nivel_facil=1
          bandera_nivel_medio=0
          bandera_nivel_dificil=0
          minutos1.delete(0,"end")
          segundos1.delete(0,"end")
          horas1.delete(0,"end")
          minutos1.insert(0,"30")
     def activa_bandera_medio():
          global bandera_nivel_facil
          global bandera_nivel_medio
          global bandera_nivel_dificil
          banadera_nivel_facil=0
          bandera_nivel_medio=1
          bandera_nivel_dificil=0
          minutos1.delete(0,"end")
          segundos1.delete(0,"end")
          horas1.delete(0,"end")
          horas1.insert(0,"1")
     def activa_bandera_dificil():
          global bandera_nivel_facil
          global bandera_nivel_medio
          global bandera_nivel_dificil
          banadera_nivel_facil=0
          bandera_nivel_medio=0
          bandera_nivel_dificil=1
          minutos1.delete(0,"end")
          segundos1.delete(0,"end")
          horas1.delete(0,"end")
          horas1.insert(0,"2")
     def activa_elementos_numeros():
          global bandera_numeros
          global bandera_letras
          global bandera_simbolos
          bandera_numeros=1
          bandera_letras=0
          bandera_simbolos=0
     def activa_elementos_letras():
          global bandera_numeros
          global bandera_letras
          global bandera_simbolos
          bandera_numeros=0
          bandera_letras=1
          bandera_simbolos=0
     def activa_elementos_simbolos():
          global bandera_numeros
          global bandera_letras
          global bandera_simbolos
          bandera_numeros=0
          bandera_letras=0
          bandera_simbolos=1
     #Niveles
     label_nivel=tk.Label(configura,text="1. Nivel:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_nivel.grid(row=0,column=0)
     nivel=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_nivel=tk.IntVar()
     facil=tk.Radiobutton(nivel,text="Fácil",variable=valor_nivel,value=1,bg="AntiqueWhite1",command=lambda:activa_bandera_facil())
     facil.grid(row=0,column=0)
     intermedio=tk.Radiobutton(nivel,text="Intermedio",variable=valor_nivel,value=2,bg="AntiqueWhite1",command=lambda:activa_bandera_medio())
     intermedio.grid(row=0,column=1)
     dificil=tk.Radiobutton(nivel,text="Difícil",variable=valor_nivel,value=3,bg="AntiqueWhite1",command=lambda:activa_bandera_dificil())
     dificil.grid(row=0,column=2)
     nivel.grid(row=2,column=0)
     #Reloj
     label_reloj=tk.Label(configura,text="2. Reloj:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_reloj.grid(row=3,column=0)
     reloj=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_reloj=tk.IntVar()
     si=tk.Radiobutton(reloj,text="Si",value=1,variable=valor_reloj,bg="AntiqueWhite1",command=lambda:activa_bandera_reloj())
     si.grid(row=0,column=0)
     no=tk.Radiobutton(reloj,text="No",value=2,variable=valor_reloj,bg="AntiqueWhite1",command=lambda:desactiva_bandera_reloj())
     no.grid(row=0,column=1)
     timer=tk.Radiobutton(reloj,text="Timer",value=3,variable=valor_reloj,bg="AntiqueWhite1",command=lambda:activa_bandera_timer())
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
     minutos1.insert(0,"30")
     segundos1=tk.Entry(reloj_tabla,bg="azure")
     segundos1.grid(row=1,column=3)
     reloj_tabla.grid(row=5,column=0)
     #Cantidad de partidas en el Top X
     label_top_x=tk.Label(configura,text="3. Cantidad de partidas en el Top X:",font=("Arial Black",10),bg="AntiqueWhite1")
     label_top_x.grid(row=6,column=0)
     partidas_topx=tk.Entry(configura,bg="azure")
     partidas_topx.grid(row=7,column=0)
     #Elementos para la Cuadrícula
     elementos_tablero=tk.Label(configura,text="4. Elementos para la Cuadrícula:",font=("Arial Black",10),bg="AntiqueWhite1")
     elementos_tablero.grid(row=8,column=0)
     elementos_table=tk.Frame(configura,bg="AntiqueWhite1",height=200,width=200)
     valor_elementos=tk.IntVar()
     numeros=tk.Radiobutton(elementos_table,text="Números",variable=valor_elementos,value=1,bg="AntiqueWhite1",command=lambda:activa_elementos_numeros())
     numeros.grid(row=0,column=0)
     letras=tk.Radiobutton(elementos_table,text="Letras",variable=valor_elementos,value=2,bg="AntiqueWhite1",command=lambda:activa_elementos_letras())
     letras.grid(row=0,column=1)
     simbolos=tk.Radiobutton(elementos_table,text="Símbolos",variable=valor_elementos,value=3,bg="AntiqueWhite1",command=lambda:activa_elementos_simbolos())
     simbolos.grid(row=0,column=2)
     elementos_table.grid(row=9,column=0)
     #Aceptar
     aceptar=tk.Button(configura,text="Aceptar",bg="alice blue",font=("Arial Black",8),command=lambda:validaciones_configuracion())
     aceptar.grid(row=10,column=3)
     configura.mainloop()
def borrar_juego_f():
     global elementos_fijos
     global matriz_botones_2
     global bandera_inincio_juego
     borrar=messagebox.askyesno("Borrar"," ¿Está seguro de borrar el juego?")
     if borrar==0:
          if bandera_inicio_juego==0:
               messagebox.showinfo("ERROR"," No se a iniciado el juego")
     else:
          for indice,lista in enumerate(matriz_botones_2):
               for indice1,boton in enumerate(lista):
                    if not boton[0] in elementos_fijos:
                         boton[0].config(text="")
def inicio_f():
     global partidas_faciles
     global partidas_medias
     global partidas_dificiles
     global bandera_nivel_facil
     global bandera_nivel_medio
     global bandera_nivel_dificil
     global partida
     global iniciar_juego
     global matriz_botones_2
     global tablero_g
     global bandera_simbolos
     global bandera_letras
     global elementos_fijos
     global bandera_inicio_juego
     global horas
     global minutos
     global segundos
     global horas_1
     global minutos_1
     global segundos_1
     global horas_get
     global minutos_get
     global segundos_get
     global hr
     global mn
     global sg
     if bandera_timer==1:
          horas_get=horas.get()
          minutos_get=minutos.get()
          segundos_get=segundos.get()
          hr=int(horas.get())
          mn=int(minutos.get())
          sg=int(segundos.get())
          if horas_get=="" or minutos_get=="" or segundos_get=="":
               messagebox.showinfo("Error"," Al menos uno de las casillas debe de ser llenada")
          elif int(horas_get)==0 and int(minutos_get)==0 and int(segundos_get)==0:
               messagebox.showinfo("Error"," Al menos uno de las casillas debe de ser llenada")
          elif int(horas_get)<0 or int(horas_get)>4:
               messagebox.showinfo("Error"," La cantidad de horas debe de estar entre 0 y 4")
          elif int(minutos_get)<0 or int(minutos_get)>59:
               messagebox.showinfo("Error"," La cantidad de minutos deben de estar entre 0 y 59")
          elif int(segundos_get)<0 or int(segundos_get)>59:
               messagebox.showinfo("Error"," La cantidad de segundos deben de estar entre 0 y 59")
          else:
               bandera_inicio_juego=1
     else:
          bandera_inicio_juego=1
     if bandera_inicio_juego==1:
          cantidad_de_partidas_faciles=len(partidas_faciles)
          cantidad_de_partidas_medias=len(partidas_medias)
          cantidad_de_partidas_dificiles=len(partidas_dificiles)
          if bandera_nivel_facil==1:
               llave_partida_facil=randint(1,cantidad_de_partidas_faciles)
               partida=partidas_faciles[llave_partida_facil]
          elif bandera_nivel_medio==1:
               llave_partida_media=randint(1,cantidad_de_partidas_medias)
               partida=partidas_medias[llave_partida_media]
          else:
               llave_partida_dificil=randint(1,cantidad_de_partidas_dificiles)
               partida=partidas_dificiles[llave_partida_dificil]
          for indice,lista in enumerate(matriz_botones_2):
               for indice1,boton in enumerate(lista):
                    if partida[indice][indice1]!="":
                         if bandera_letras==1:
                              if partida[indice][indice1]=="1":
                                   texto="A"
                              elif partida[indice][indice1]=="2":
                                   texto="B"
                              elif partida[indice][indice1]=="3":
                                   texto="C"
                              elif partida[indice][indice1]=="4":
                                   texto="D"
                              elif partida[indice][indice1]=="5":
                                   texto="E"
                              elif partida[indice][indice1]=="6":
                                   texto="F"
                              elif partida[indice][indice1]=="7":
                                   texto="G"
                              elif partida[indice][indice1]=="8":
                                   texto="H"
                              else:
                                   texto="I"
                              matriz_botones_2[indice][indice1][0].config(text=texto)
                              matriz_botones_2[indice][indice1]=(matriz_botones_2[indice][indice1][0],texto)
                         elif bandera_simbolos==1:
                              if partida[indice][indice1]=="1":
                                   texto="#"
                              elif partida[indice][indice1]=="2":
                                   texto="*"
                              elif partida[indice][indice1]=="3":
                                   texto="&"
                              elif partida[indice][indice1]=="4":
                                   texto="%"
                              elif partida[indice][indice1]=="5":
                                   texto="°"
                              elif partida[indice][indice1]=="6":
                                   texto="$"
                              elif partida[indice][indice1]=="7":
                                   texto="+"
                              elif partida[indice][indice1]=="8":
                                   texto="-"
                              else:
                                   texto="/"
                              matriz_botones_2[indice][indice1][0].config(text=texto)
                              matriz_botones_2[indice][indice1]=(matriz_botones_2[indice][indice1][0],texto)
                         else:
                              matriz_botones_2[indice][indice1][0].config(text=partida[indice][indice1])
                              matriz_botones_2[indice][indice1]=(matriz_botones_2[indice][indice1][0],partida[indice][indice1])
                         elementos_fijos.append(matriz_botones_2[indice][indice1][0])
          if bandera_timer==1:
               iniciar_juego.config(state="disabled")
               activa_timer()
          elif bandera_reloj==1:
               iniciar_juego.config(state="disabled")
               activa_reloj()
          else:
               iniciar_juego.config(state="disabled")
def asigna_valor(x,y):
     global matriz_botones
     global matriz_botones_2
     global elemento_agregar
     global jugar_v
     global gane
     global w
     global bandera_boton_picado
     global f
     global c
     global pila_jugadas_hechas
     global lista_mismos
     global valor
     bandera_validacion=0
     if matriz_botones[x][y] in elementos_fijos:
          bandera_validacion=1
          messagebox.showinfo("Error"," Jugada no es valida porque \n este es un elemento fijo")
     i=x
     j=y
     if x>=8:
          i=x-2
     elif x>=4:
          i=x-1
     if y>=8:
          j=y-2
     elif y>=4:
          j=y-1
     #JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA
     if bandera_validacion==0:
          for indice,boton in enumerate(matriz_botones_2[i]):
               if boton[1]==str(elemento_agregar):
                    boton[0].config(bg="red")
                    messagebox.showinfo("Error"," Jugada no es válida porque el \n elemento ya está en la fila")
                    boton[0].config(bg="lavender")
                    bandera_validacion=1
     #JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA
     if bandera_validacion==0:
          for indice,boton in enumerate(matriz_botones_2):
               if boton[j][1]==str(elemento_agregar):
                    boton[j][0].config(bg="red")
                    messagebox.showinfo("Error"," Jugada no es válida porque el \n elemento ya está en la columna")
                    boton[j][0].config(bg="lavender")
                    bandera_validacion=1
     #JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA CUADRÍCULA
     if bandera_validacion==0:
          cuadricula_1=[matriz_botones_2[0][0],matriz_botones_2[0][1],matriz_botones_2[0][2],matriz_botones_2[1][0],matriz_botones_2[1][1],matriz_botones_2[1][2],matriz_botones_2[2][0],matriz_botones_2[2][1],matriz_botones_2[2][2]]
          cuadricula_2=[matriz_botones_2[0][3],matriz_botones_2[0][4],matriz_botones_2[0][5],matriz_botones_2[1][3],matriz_botones_2[1][4],matriz_botones_2[1][5],matriz_botones_2[2][3],matriz_botones_2[2][4],matriz_botones_2[2][5]]
          cuadricula_3=[matriz_botones_2[0][6],matriz_botones_2[0][7],matriz_botones_2[0][8],matriz_botones_2[1][6],matriz_botones_2[1][7],matriz_botones_2[1][8],matriz_botones_2[2][6],matriz_botones_2[2][7],matriz_botones_2[2][8]]
          cuadricula_4=[matriz_botones_2[3][0],matriz_botones_2[3][1],matriz_botones_2[3][2],matriz_botones_2[4][0],matriz_botones_2[4][1],matriz_botones_2[4][2],matriz_botones_2[5][0],matriz_botones_2[5][1],matriz_botones_2[5][2]]
          cuadricula_5=[matriz_botones_2[3][3],matriz_botones_2[3][4],matriz_botones_2[3][5],matriz_botones_2[4][3],matriz_botones_2[4][4],matriz_botones_2[4][5],matriz_botones_2[5][3],matriz_botones_2[5][4],matriz_botones_2[5][5]]
          cuadricula_6=[matriz_botones_2[3][6],matriz_botones_2[3][7],matriz_botones_2[3][8],matriz_botones_2[4][6],matriz_botones_2[4][7],matriz_botones_2[4][8],matriz_botones_2[5][6],matriz_botones_2[5][7],matriz_botones_2[5][8]]
          cuadricula_7=[matriz_botones_2[6][0],matriz_botones_2[6][1],matriz_botones_2[6][2],matriz_botones_2[7][0],matriz_botones_2[7][1],matriz_botones_2[7][2],matriz_botones_2[8][0],matriz_botones_2[8][1],matriz_botones_2[8][2]]
          cuadricula_8=[matriz_botones_2[6][3],matriz_botones_2[6][4],matriz_botones_2[6][5],matriz_botones_2[7][3],matriz_botones_2[7][4],matriz_botones_2[7][5],matriz_botones_2[8][3],matriz_botones_2[8][4],matriz_botones_2[8][5]]
          cuadricula_9=[matriz_botones_2[6][6],matriz_botones_2[6][7],matriz_botones_2[6][8],matriz_botones_2[7][6],matriz_botones_2[7][7],matriz_botones_2[7][8],matriz_botones_2[8][6],matriz_botones_2[8][7],matriz_botones_2[8][8]]
          def auxiliar_error(boton):
               global matriz_botones
               boton.config(bg="red")
               messagebox.showinfo("Error"," Jugada no es válida porque el \n elemento ya está en la cudrícula")
               boton.config(bg="lavender")
          def recorre_cuadricula(c):
               global w
               for boton in c:
                    if boton[1]==str(elemento_agregar):
                         w=1
                         auxiliar_error(boton[0])
          if w==0 and x<3 and y<3:
               recorre_cuadricula(cuadricula_1)
          elif w==0 and x<3 and y<7 and y>3:
               recorre_cuadricula(cuadricula_2)
          elif w==0 and x<3 and y>7:
               recorre_cuadricula(cuadricula_3)
          elif w==0 and x<7 and x>3 and y<3:
               recorre_cuadricula(cuadricula_4)
          elif w==0 and x<7 and x>3 and y<7 and y>3:
               recorre_cuadricula(cuadricula_5)
          elif w==0 and x<7 and x>3 and y>7:
               recorre_cuadricula(cuadricula_6)
          elif w==0 and x>7 and y<3:
               recorre_cuadricula(cuadricula_7)
          elif w==0 and x>7 and y<7 and y>3:
               recorre_cuadricula(cuadricula_8)
          elif w==0 and x>7 and y>7:
               recorre_cuadricula(cuadricula_9)
          if elemento_agregar==0:
               messagebox.showinfo("ERROR"," Falta seleccionar un elemento")
          else:
               if w==0:
                    matriz_botones[x][y].config(text=str(elemento_agregar))
                    matriz_botones_2[i][j]=(matriz_botones_2[i][j][0],str(elemento_agregar))
                    bandera_boton_picado.config(bg="turquoise")
                    f=i
                    c=j
                    jo=Jugadas_hechas(f,c,elemento_agregar)
                    pila_jugadas_hechas.append(jo)
                    elemento_agregar=0
                    for fila in  matriz_botones_2:
                         for boton in fila:
                              if boton[1]=="":
                                   gane=0
                    if gane==1:
                         gane=2
                         messagebox.showinfo("Gane"," ¡EXELENTE! \n JUEGO COMPLETADO")
                         #llama a función para top x**************************************
                         jugar_v.destroy()
                         jugar_f()
     w=0
     return x,y

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
     global horas_1
     global minutos_1
     global segundos_1
     global elementos_numeros
     global elementos_letras
     global elementos_simbolos
     global bandera_numeros
     global bandera_letras
     global bandera_simbolos
     global bandera_boton_picado
     global partida
     global iniciar_juego
     global matriz_botones
     global matriz_botones_2
     global tablero_g
     global horas
     global minutos
     global segundos
     global jugar_v
     global gane
     global bandera_inicio_juego
     global elemento_agregar
     global partida
     global hr
     global mn
     global sg
     global ventana_para_timer
     global bandera_timer
     global bandera_reloj
     if gane!=2:
          menu_p.destroy()
     if gane==2:
          gane=1
          bandera_boton_picado=0
          bandera_inicio_juego=0
          elemento_agregar=0
          partida=0
          elementos_fijos=[]
          hr=0
          mn=0
          sg=0
          w=0
          bandera_modifica_timer=0
     jugar_v=tk.Tk()
     jugar_v.iconbitmap("x.ico")
     jugar_v.title("SUDOKU")
     jugar_v.geometry("950x720")
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

     #TABLERO DEL JUEGO:
     tablero_g=tk.Frame(jugar_v,bg="turquoise")
     matriz_botones=[]
     matriz_botones_2=[]
     for x in range (0,11):
          fila_botones=[]
          fila_botones_2=[]
          for y in range (0,11):
               if x==3 or x==7 or y==3 or y==7:
                    none=tk.Label(tablero_g,bg="turquoise")
                    none.grid(row=x,column=y)
                    fila_botones.append(none)
               else:
                    casilla=tk.Button(tablero_g,bg="lavender",activebackground="bisque",height=2,width=5,command=partial(asigna_valor,x,y))
                    casilla.grid(row=x,column=y,padx=2,pady=2)
                    fila_botones.append(casilla)
                    fila_botones_2.append((casilla,""))
          if fila_botones_2!=[]:
               matriz_botones_2.append(fila_botones_2)
          matriz_botones.append(fila_botones)
     tablero_g.grid(row=3,column=2)
     def meter_elemento(numero,b):
          global elemento_agregar
          global bandera_boton_picado
          if bandera_boton_picado!=0:
               bandera_boton_picado.config(bg="turquoise")
          b.config(bg="steel blue")
          bandera_boton_picado=b
          elemento_agregar=numero
     #ELEMENTOS DEL TABLERO:
     if bandera_numeros==1:
          texto=elementos_numeros
     if bandera_letras==1:
          texto=elementos_letras
     if bandera_simbolos==1:
          texto=elementos_simbolos
     elementos=tk.Frame(jugar_v,bg="SkyBlue1")
     uno=tk.Button(elementos,text=texto[0],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[0],uno))
     uno.grid(row=0,column=0,padx=2,pady=2)
     dos=tk.Button(elementos,text=texto[1],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[1],dos))
     dos.grid(row=0,column=1,padx=2,pady=2)
     tres=tk.Button(elementos,text=texto[2],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[2],tres))
     tres.grid(row=0,column=2,padx=2,pady=2)
     cuatro=tk.Button(elementos,text=texto[3],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[3],cuatro))
     cuatro.grid(row=1,column=0,padx=2,pady=2)
     cinco=tk.Button(elementos,text=texto[4],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[4],cinco))
     cinco.grid(row=1,column=1,padx=2,pady=2)
     seis=tk.Button(elementos,text=texto[5],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[5],seis))
     seis.grid(row=1,column=2,padx=2,pady=2)
     siete=tk.Button(elementos,text=texto[6],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[6],siete))
     siete.grid(row=2,column=0,padx=2,pady=2)
     ocho=tk.Button(elementos,text=texto[7],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[7],ocho))
     ocho.grid(row=2,column=1,padx=2,pady=2)
     nueve=tk.Button(elementos,text=texto[8],bg="turquoise",activebackground="bisque",font=("Arial Black",11),width=2,command=lambda:meter_elemento(texto[8],nueve))
     nueve.grid(row=2,column=2,padx=2,pady=2)
     elementos.grid(row=3,column=4,padx=2,pady=2)
     
     #RELOJ:
     if bandera_reloj==1:
          ventana_para_reloj=tk.Frame(jugar_v,bg="AntiqueWhite1",height=200,width=200)
          none=tk.Label(ventana_para_reloj,text="Reloj",font=("Arial Black",10),bg="cyan",width=13)
          none.grid(row=0,column=0)
          none=tk.Label(ventana_para_reloj,text="Horas",font=("Arial Black",10),bg="green4",width=13)
          none.grid(row=1,column=0)
          none=tk.Label(ventana_para_reloj,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
          none.grid(row=1,column=1)
          none=tk.Label(ventana_para_reloj,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
          none.grid(row=1,column=2)
          horas=tk.Label(ventana_para_reloj,text="              00            :",font=("Arial Black",10),bg="azure",width=13)
          horas.grid(row=2,column=0)
          minutos=tk.Label(ventana_para_reloj,text="              00            :",font=("Arial Black",10),bg="azure",width=13)
          minutos.grid(row=2,column=1)
          segundos=tk.Label(ventana_para_reloj,text="              00            ",font=("Arial Black",10),bg="azure",width=13)
          segundos.grid(row=2,column=2)
          ventana_para_reloj.grid(row=4,column=2)
     #TIMER:
     if bandera_timer==1:
          ventana_para_timer=tk.Frame(jugar_v,bg="AntiqueWhite1",height=200,width=200)
          none=tk.Label(ventana_para_timer,text="Timer",font=("Arial Black",10),bg="cyan",width=13)
          none.grid(row=0,column=0)
          none=tk.Label(ventana_para_timer,text="Horas",font=("Arial Black",10),bg="green4",width=13)
          none.grid(row=1,column=0)
          none=tk.Label(ventana_para_timer,text="Minutos",font=("Arial Black",10),bg="green2",width=13)
          none.grid(row=1,column=1)
          none=tk.Label(ventana_para_timer,text="Segundos",font=("Arial Black",10),bg="green4",width=13)
          none.grid(row=1,column=2)
          horas=tk.Entry(ventana_para_timer,bg="azure")
          horas.grid(row=2,column=0)
          horas.insert(0,horas_1)
          minutos=tk.Entry(ventana_para_timer,bg="azure")
          minutos.grid(row=2,column=1)
          minutos.insert(0,minutos_1)
          segundos=tk.Entry(ventana_para_timer,bg="azure")
          segundos.grid(row=2,column=2)
          segundos.insert(0,segundos_1)
          ventana_para_timer.grid(row=4,column=2)
     #BOTONES:
     elementos_para_tablero=tk.Frame(jugar_v,bg="AntiqueWhite1")
     iniciar_juego=tk.Button(elementos_para_tablero,text=" INICIAR \n JUEGO",bg="OliveDrab2",height=2,font=("Arial Black",10),command=lambda:nombre())
     iniciar_juego.grid(row=0,column=0)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=0,column=1)

     deshacer_jugada=tk.Button(elementos_para_tablero,text=" DESHACER \n JUGADA",bg="sky blue",height=2,font=("Arial Black",10),command=lambda:deshacer_partida_f())
     deshacer_jugada.grid(row=0,column=2)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=0,column=3)

     rehacer_jugada=tk.Button(elementos_para_tablero,text=" REHACER \n JUGADA",bg="sky blue",height=2,font=("Arial Black",10),command=lambda:rehacer_partida_f())
     rehacer_jugada.grid(row=0,column=4)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=0,column=5)

     guardar_juego=tk.Button(elementos_para_tablero,text="GUARDAR \n JUEGO",bg="pale green",height=2,font=("Arial Black",8))
     guardar_juego.grid(row=0,column=6)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=1,column=0)

     top_x=tk.Button(elementos_para_tablero,text=" TOP \n X",bg="gold",height=2,font=("Arial Black",10),command=lambda:activa_bandera_topx())
     top_x.grid(row=2,column=0)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=2,column=1)

     borrar_juego=tk.Button(elementos_para_tablero,text=" BORRAR \n JUEGO",bg="salmon1",height=2,font=("Arial Black",10),command=lambda:borrar_juego_f())
     borrar_juego.grid(row=2,column=2)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=2,column=3)

     terminar_juego=tk.Button(elementos_para_tablero,text=" TERMINAR \n JUEGO",bg="coral2",height=2,font=("Arial Black",10),command=lambda:terminar_juego_f())
     terminar_juego.grid(row=2,column=4)
     none=tk.Label(elementos_para_tablero,text="  ",bg="AntiqueWhite1")
     none.grid(row=2,column=5)

     cargar_juego=tk.Button(elementos_para_tablero,text="CARGAR \n JUEGO",bg="pale green",height=2,font=("Arial Black",8))
     cargar_juego.grid(row=2,column=6)
     elementos_para_tablero.grid(row=4,column=4,padx=2,pady=2)
     jugar_v.mainloop()

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
