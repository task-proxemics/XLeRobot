<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

> [!NOTE] 
> Actualmente en desarrollo activo. Podría haber información incorrecta. Planeamos terminar la primera versión **XLeRbot 0.1.0** en unos días, eliminaremos esta nota cuando la primera versión esté terminada. Por favor, ten paciencia....

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

**🚀 Llevando la IA Incorporada a Todos - ¡Más Barato que un iPhone! 📱**  
*Construido sobre los gigantes: [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 ¿Por qué XLeRobot? 🌟
Respondemos esto por separado ya que **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### ¿Por qué el núcleo "LeRobot"?
- **Materiales Económicos** 💴: 90% impreso en 3D, con motores y electrónica baratos.
- **Montaje Fácil** 🔨: Atornilla durante 2 horas y listo.
- **Plug-&-Play** 🧩: Haz que los robots funcionen con una simple instalación pip y ejecutando unas pocas líneas.
- **Comunidad Próspera** 🌍:
  La comunidad de robótica de bajo costo más grande del mundo con
  - Múltiples modelos de IA de vanguardia🧠, conjuntos de datos📊 y herramientas🔨 para implementación directa. 
  - Más de 5000 mentes brillantes para lluvia de ideas y discusiones🧑‍🤝‍🧑.
    
    </td>
    </tr>
    <tr>
    <td>
 
### ¿Por qué la mejora "XL"? 
- 🏠 Actualmente, hay una falta de robots móviles domésticos asequibles, estables y de propósito general con brazos duales que sean tan fáciles de construir como LeRobot.
- 🖨️ Los marcos impresos en 3D tienen durabilidad, estabilidad y capacidad de carga limitadas, además de ser complejos de ensamblar e imprácticos para el uso diario.
- ⚡ El suministro de energía sigue siendo un desafío para los robots móviles DIY, lo que resulta en configuraciones de cableado complicadas.
- 🤖 **XLerobot** utiliza la misma configuración que la mayoría de los SO100 de doble brazo de sobremesa en la comunidad LeRobot, lo que hace que la transferencia de código y políticas sea sencilla.
  
    </td>
  </tr>
 </table>       
 
### Ventajas/Objetivos Generales de XLeRobot

- **Rentable** 💴: construcción completa por ~\$660, con actualizaciones desde SO100Arm y Lekiwi existentes por ~\$250.
- **Fácil actualización** ⏫ (física y eléctrica) para **Lekiwi** y **SO100**
    - Hardware: No se requieren cambios de ID de motor ni modificaciones de hardware
    - Software: Misma configuración de sobremesa de brazo único/doble, transfiere directamente tu política entrenada desde el brazo SO100 de sobremesa hasta aquí
- **Práctico y confiable** 💪: capaz de completar muchas tareas diarias realizadas por robots móviles de doble brazo de $20,000 en el mercado.
    - Por ejemplo👇 
    - <img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />
    - Aunque estas👆 son solo fotos preparadas, muestran lo que la plataforma **XLeRobot** es capaz de hacer dentro de sus límites de hardware. (Disculpa que las escenas estén un poco desordenadas, pero hey, ¡así es la vida!)
    - Más tareas demostradas en el hackathon de Lerobot en [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) y [Mountain View](https://x.com/asierarranz/status/1905306686648132061).
    - **Nota**: Actualmente no está diseñado para tareas que requieran destreza en la mano 🤹, levantamiento de objetos pesados (más de 1kg por brazo) 🏋️, o movimientos altamente dinámicos 🏃
- **Abundantes recursos de código abierto** 📕
    - Código plug-and-play de LeRobot🧩 y numerosos modelos de IA🧠
    - Respaldado por una comunidad activa y creciente de colaboradores🧑‍🤝‍🧑






---
## 🎯 Demo 0.0.5 🎯
> [!NOTE]
> Actualmente solo una versión de un solo brazo implementando directamente Lekiwi, teleoperado por el otro brazo seguidor. Velocidad 3x.

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 Costo Total 💵

> [!NOTE] 
> No incluye el costo de impresión 3D, herramientas, envíos e impuestos.

| Precio| EE.UU.  | UE  | CN |
|---------|----:|----:|----:|
| **Construir desde cero** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **Actualizar desde 2 brazos SO100**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **Actualizar desde 1 Lekiwi** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **Actualizar desde 1 Lekiwi y 1 brazo SO100** |  **~$250**  |  **~€240**  |  **~¥1200**  |

Para más detalles, consulta la [Lista de Materiales](BOM.md).

---
---
## 🚀 Primeros Pasos (Tutorial Detallado) 🚀PENDIENTE
> [!NOTE] 
> Yo mismo soy principiante en hardware, así que quiero asegurarme de que este tutorial sea amigable para todos los principiantes.
1. 💵 **Compra tus piezas**: [Lista de Materiales](BOM.md)
2. 🖨️ **Imprime tus componentes**: [Instrucciones de impresión 3D](3Dprint.md)
3. 🔨 ~~Vengadores~~: [**¡Ensamblen**!](Assembly.md)
4. 💻 **Software**: ¡Haz que tu robot se mueva!
---
---
> [!NOTE] 
> El contenido anterior proporciona instrucciones eficientes para construir el **XLeRobot**. El contenido a continuación explica el propósito y la visión del proyecto con mayor detalle.

## 🛠️ Introducción al Hardware 🛠️

**XLeRobot** = Lekiwi + 1x brazo SO100 + **Carrito RÅSKOG de IKEA** + **Batería Anker**

= 2x Brazos SO100 + 3x ruedas omnidireccionales + RasberryPi + **Carrito RÅSKOG de IKEA** + **Batería Anker**

> [!NOTE]
> *Todo el procesamiento lo maneja tu PC - Raspberry Pi solo gestiona la comunicación de datos vía wifi 📶*

<table>
  <tr>
    <td>
      
### ¿Por qué el carrito RÅSKOG de IKEA?
- 🌎 Disponibilidad global con diseño estandarizado
- 💰 Económico
- 🏗️ Estructura simple pero construcción robusta
- 🔧 Base de malla metálica que permite fácil montaje de componentes
- 📦 Perfecto para almacenamiento y transporte de artículos
- 📏 Altura ideal para superficies domésticas comunes—desde la estufa hasta la mesa de café

    </td>
    </tr>
    <tr>
    <td>
    
### ¿Por qué la estación de energía Anker SOLIX C300? 
- 🌍 Disponibilidad global
- ⚡ Capacidad de 288Wh, potencia máxima de salida de 300W, potencia máxima de carga de 280W
- 🔌 Alimenta tanto los brazos de 12V, la base y la Raspberry Pi a plena capacidad a través de tres cables de carga Tipo-C—eliminando el complejo sistema de cableado
- 🔋 Vida de batería excepcional: 10 horas con uso normal, 6 horas bajo operación intensiva, y solo 1 hora para carga completa
- 💡 Iluminación integrada para operación nocturna
- ☀️ Montaje opcional de panel solar para suministro continuo de energía
- 🎒 Versátil y desmontable—sirve más allá de la robótica en la vida diaria como fuente de energía de emergencia o para camping

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

Incluso si ya no juegas con robots (esperemos que eso no suceda), estos dos productos aún pueden desempeñar un papel en tu vida diaria.

---

## 💻 Introducción al Software 💻
Aquí hay una idea general de cómo puedes controlar el robot y hacerlo inteligente:

### 🕹️ Control Básico

- Control de **articulaciones** (ángulo del motor) → control de brazo líder-seguidor

- Control de **pose del efector final** → control remoto con VR
  
> [!NOTE]
> Para la primera versión nos enfocamos principalmente en el hardware. El código de LeRobot aún no ha sido modificado. Puedes ejecutar la demo original de Lekiwi conectando un brazo a la RaspberryPi y otro brazo al escritorio para recrear la Demo 0.0.5 mediante control remoto. El código de Lerobot para XLeRobot se actualizará pronto con la máxima prioridad.


### 🧠 Caminos hacia la Inteligencia de Máquina Incorporada General (PENDIENTE)






### 🔈🇦🇩 Tiempo de publicidad:
- **Nuestro laboratorio**: [Rice RobotPI Lab](https://robotpilab.github.io/)
    - Una de nuestras visiones: usar [Caging in Time](https://robotpilab.github.io/publication/caging/) y metodología de manipulación basada en embudo para realizar manipulación robusta de objetos bajo situaciones imperfectas del mundo real como ruido de percepción, retraso de red, [contacto rico](https://robotpilab.github.io/publication/collision-inclusive-manipulation/), etc.
- **Plataforma de simulación** (mi preferencia personal): [Maniskill](https://www.maniskill.ai/)
    - 🚀Aceleración rápida de GPU para simulaciones paralelas
    - 🎨Excelente visual fotorrealista mediante ray-tracing
    - 🪶Ligero, consistente, fácil de usar (comparado con Isaac Lab, en mi opinión)
    - 🤖Soporte para [múltiples robots](https://maniskill.readthedocs.io/en/latest/robots/index.html) (incluyendo [brazo SO100](https://x.com/Stone_Tao/status/1910101218241978537))


---
## Planes Futuros

### Hardware
<table>
  <tr>
    <td>
      
**Urgente**

- 🔧 Añadir dos opciones de base para brazos: sujetada con abrazadera (actual) o montada con tornillos
- 🛠️ Añadir una placa conectora totalmente compatible con la malla metálica del carrito IKEA
    </td>
    </tr>
    <tr>
    <td>
    
**En un futuro próximo**

- 📸 Añadir una cámara de profundidad RealSense a la cabeza para complementar las cámaras RGB de las manos para una percepción ambiental precisa
- 👆 Sensibilidad táctil básica
    </td>
  </tr>
</table>


> [!NOTE]
> Aunque mejoras más sofisticadas son totalmente posibles (como cambiar a un procesador Jetson, mejorar el chasis o usar mejores motores), estas contradecirían la misión central de este proyecto: **crear la plataforma universal de robots de código abierto más asequible, fácil de instalar y plug-and-play del mundo**. Pero estas mejoras pueden listarse como complementos opcionales en el futuro en lugar de la vía principal.

### Software

(las actualizaciones de software también dependerán del desarrollo de la comunidad LeRobot)
<table>
  <tr>
    <td>
      
**Urgente**

- ⚙️ Algoritmos de control básicos
- 🎮 Control optimizado del efector final
- 🎲 Entorno de simulación Maniskill
- 🕶️ Control VR Quest3 y teleoperación
- 🤖 Tareas simples usando modelos VLA existentes de la base de código Lerobot
    </td>
    </tr>
    <tr>
    <td>
    
**En un futuro próximo**

- 🎯 Calibración precisa basada en AprilTag
- 🗺️ Navegación autónoma con una sola cámara RGBD
- 🌐 Alineación de gemelo digital para aplicaciones sim2real
- 🧠 Modelo del mundo y manipulación robusta basada en física
- 💬 Conectar con MCP para utilizar directamente LLMs
    </td>
  </tr>
</table>

---

## 🎯 ¿Para quién es XLerobot?

- 🚀 **Startups y Laboratorios**: Construye prototipos más rápido con la plataforma modular más barata del mundo
- 👩🔬 **Investigadores Independientes**: Experimenta con IA incorporada sin gastar una fortuna 💸
- 🎓 **Héroes de la Educación**:
  - Profesores de Secundaria: Lleva la robótica de vanguardia a las clases STEM 🧪
  - Profesores Universitarios: Plataforma asequible para cursos de robótica/IA 📚
  - Estudiantes: Desde principiantes hasta investigadores 🎒→🎓
- 🤖 **Entusiastas del DIY**: Perfecto para proyectos de interior - cuidado de plantas, robots de entrega, automatización del hogar 🌱📦
---

## Limitaciones

(Hey, por este precio, ¿qué más podrías pedir?)

- 🔒 Altura fija—añadir una plataforma de elevación estable aumentaría significativamente los costos y la dificultad de montaje
- 📏 Espacio de trabajo más pequeño comparado con Aloha—aunque intentamos utilizar completamente el espacio de trabajo del SO100, el tamaño del brazo tiene límites—aunque XLeRobot aún puede manejar la mayoría de sus tareas
- ⚖️ Capacidad de carga limitada para un solo brazo—por eso está aquí el carrito IKEA
- 🛒 La precisión del movimiento de la base puede verse afectada por las ruedas del carrito IKEA—puede abordarse mediante control de retroalimentación de bucle cerrado

Considerando todo—costo, soporte comunitario, facilidad de montaje y utilidad práctica—XLeRobot destaca como el robot de bajo costo más atractivo para aplicaciones de interior


---

### Principales Colaboradores

Actualmente solo [yo](https://vector-wangel.github.io/). 

Esto es solo un pequeño ladrillo en las pirámides, definitivamente no sería posible sin [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), y [Bambot](https://github.com/timqian/bambot). ¡Gracias de nuevo por estos proyectos detallados y profesionales realizados por sus talentosos colaboradores!

¡Espero colaborar con cualquier persona interesada en hacer contribuciones para este proyecto!

No afiliado con IKEA (¡pero nos encantan las albóndigas suecas! 🍝)
