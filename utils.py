from telebot import types
from functions import *
from models import User

# âī¸ â đ âĄī¸ âŦī¸ âŠī¸ đ° Editar *ī¸âŖ  Eliminar â   đ đ đŊ đ đ


def get_botonera_inicial():
      markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
      llaverosButton = types.KeyboardButton('Llaveros đ')
      stickersButton = types.KeyboardButton('Stickers đ')
      eventosButton = types.KeyboardButton('Eventos đ')
      estatuillasButton = types.KeyboardButton('Estatuillas đŊ')
      carritoButton = types.KeyboardButton("Carrito đ")
      markup.row(llaverosButton,stickersButton)
      markup.row(estatuillasButton,eventosButton)
      markup.row(carritoButton)
      return markup
      
def get_botonera_admin():
      markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
      llaverosButton = types.KeyboardButton('Llaveros đ')
      stickersButton = types.KeyboardButton('Stickers đ')
      eventosButton = types.KeyboardButton('Eventos đ')
      estatuillasButton = types.KeyboardButton('Estatuillas đŊ')
      agregarButton = types.KeyboardButton("Agregar Producto â")
      markup.row(llaverosButton,stickersButton)
      markup.row(estatuillasButton,eventosButton)
      markup.row(agregarButton)
      return markup

def get_botonera_agregando_producto():
      markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
      returnButton = types.KeyboardButton("Cancelar âŠī¸")
      markup.add(returnButton)
      return markup

def get_botonera_edicion_producto():

      markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

      nombreButton = types.KeyboardButton("Nombre âī¸") 
      detallesButton = types.KeyboardButton ("Detalles đ")
      precioButton = types.KeyboardButton("Precio đ°")
      fotoButton = types.KeyboardButton("Foto đŧ")
      returnButton = types.KeyboardButton("Regresar âŠī¸")

      markup.row(nombreButton,detallesButton)
      markup.row(precioButton,limiteButton)
      markup.row(fotoButton,returnButton)
      return markup
      
def get_productos_menu():
      comprarButton = types.KeyboardButton('Hacer compra đ°')
      carritoButton = types.KeyboardButton('Carrito đ')
      deshacerButton = types.KeyboardButton('Regresar âŠī¸')
      
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      markup.row(comprarButton)
      markup.row(carritoButton,deshacerButton)

      return markup

def get_botonera_carrito():
      
      comprarButton = types.KeyboardButton('Hacer compra đ°')
      refrescarCarritoButton = types.KeyboardButton('Refrescar Carrito đ')
      vaciarCarritoButton = types.KeyboardButton('Vaciar carrito âģī¸') 
      regresarButton = types.KeyboardButton('Regresar âŠī¸')
      
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      markup.row(comprarButton,refrescarCarritoButton)
      markup.row(vaciarCarritoButton,regresarButton)

      return markup

def info_renovar_botonera():
      sms = '''```
   â ī¸Advertenciaâ ī¸
El producto sobre el cual desea
consultar, ha sido renovado o eliminado
. Porfavor vuelva a consultar los productos
directamente desde las categorÃ­as.
      ```'''
      return sms

def info_producto_para_carrito(nombre,precio,cantidad):
      sms = f'''```
\n{cantidad}x {nombre} ({precio} cup c/u)```'''
      return sms

def get_botonera_cancelar(categorias):
      markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
      if categorias:
            llaverosButton = types.KeyboardButton('Llaveros đ')
            stickersButton = types.KeyboardButton('Stickers đ')
            eventosButton = types.KeyboardButton('Eventos đ')
            estatuillasButton = types.KeyboardButton('Estatuillas đŊ')
            cancelarButton = types.KeyboardButton('Cancelar âŠī¸')
            markup.add(llaverosButton,stickersButton,estatuillasButton,eventosButton,cancelarButton)
      else:
            cancelarButton = types.KeyboardButton('Cancelar âŠī¸')
            markup.add(cancelarButton)
      return markup

def get_inline_b(producto,user,len,cantidad,index,admin):

      keyboard = []

      # Buscamos la cantidad temporal, no real:
      # cantidad = cantidad_de_producto_en_carro_t(producto,user)

      # ide del producto
      p_id = producto.id

      categoria = producto.categoria

      length = get_cantidad_en_categoria(categoria) - 1

      print(f'Showing index :{index} , length: {length}')

      if cantidad > 0 :
            emoji_check = "â"
      else:
            emoji_check = "âī¸"

      emoji_carrito = "đ"
      emoji_sgt = "âĄī¸"
      emoji_ant = "âŦī¸"

      # agregando botonera
      comprarButton = types.InlineKeyboardButton(
                              text= f'Cantidad a comprar: {cantidad} {emoji_check}',
                              callback_data= f'charge_{p_id}_{cantidad}_{index}_{categoria}'
                        )

      descontar_carritoButton = types.InlineKeyboardButton(
                              text = f'Bajar una unidad {emoji_carrito}',
                              callback_data= f'reduce_{p_id}_{cantidad}_{index}_{categoria}'
                        )

      keyboard.append([comprarButton])
      keyboard.append([descontar_carritoButton])

      sgte = False
      ant = False

      if index < length:   
            sgte = True
      
      if index > 0 or (index == length and length!=0):
            ant = True
           
      arrows = []

      if ant :

            antButton = types.InlineKeyboardButton(
                        text = f'{emoji_ant}',
                        callback_data=f'prev_{index}_{categoria}'
                  )
            
            arrows.append(antButton)

      if sgte:

            sgteButton = types.InlineKeyboardButton(
                        text = f'{emoji_sgt}',
                        callback_data=f'next_{index}_{categoria}'
                  )
            
            arrows.append(sgteButton)
      
      if arrows != []:
            keyboard.append(arrows)      
  
      if admin:

            editarButton = types.InlineKeyboardButton(
                        text = f'Editar *ī¸âŖ',
                        callback_data=f'edit_{p_id}'
                  )
            
            eliminarButton = types.InlineKeyboardButton(
                  text = f'Eliminar â',
                  callback_data=f'delete_{p_id}'
            )

            keyboard.append([editarButton,eliminarButton])

      markup = types.InlineKeyboardMarkup(keyboard)
      markup.row_width = 2
      
      return markup 

def welcome_message():
      return '''```
      Hola! Bienvenido al bot no oficial y de pruebas de Gremio Store!
    ```'''

def comandos_info():
      sms = '''
      ```
/decir <id> - <texto>  -> Envia el texto al usuario segun su id

/ban <id> -> Banea al usuario

/unban <id> -> Desbanea al usuario

/i_u <id> -> Inspecciona al usuario

/anunciar <texto> -> Envia el texto a todos los usuarios
      ```
      '''

      return sms

def hacer_sms_producto(producto):
      if producto.precio != 0:
      
            sms = f'''```
      {producto.nombre}

      {producto.detalles}

      Precio: {producto.precio}cup
                              ```'''
      else:
            
            sms = f'''```
      {producto.nombre}

      {producto.detalles}
                              ```'''
            
      return sms