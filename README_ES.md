<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-brown.svg)](README_CN.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README_ES.md)
[![de](https://img.shields.io/badge/lang-de-orange.svg)](README_DE.md)
[![fr](https://img.shields.io/badge/lang-fr-white.svg)](README_FR.md)
[![日本語](https://img.shields.io/badge/lang-日本語-yellow.svg)](README_JP.md)

> [!NOTE] 
> ¡La primera versión de **XLeRobot 0.1.0** está oficialmente disponible! La versión actual incluye una detallada **lista de materiales**, **modelos e instrucciones de impresión 3D**, y una **guía de montaje paso a paso**. Aunque el código aún no está disponible, puedes **ejecutar la prueba de teleoperación** en una versión de un solo brazo (controlada con otro brazo seguidor) directamente usando el código original de Lekiwi.

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---



**🚀 Llevando la IA Incorporada a Todos - ¡Más Barato que un iPhone! 📱**  
*Construido sobre los hombros de gigantes: [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 ¿Por qué XLeRobot? 🌟
Analicemos esto ya que **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### ¿Por qué el núcleo "LeRobot"?
- **Materiales Económicos** 💴: 90% componentes impresos en 3D con motores y electrónica asequibles.
- **Montaje Sencillo** 🔨: Solo se requieren 2 horas de tiempo de montaje.
- **Plug-&-Play** 🧩: Pon en marcha robots con una simple instalación pip y unas pocas líneas de código.
- **Próspera Comunidad LeRobot** 🌍:
  La comunidad de robótica de bajo costo más grande del mundo con
  - Múltiples modelos de IA de vanguardia preentrenados🧠, conjuntos de datos📊 y herramientas🔨 listos para implementar. 
  - Más de 5,000 mentes brillantes para intercambio de ideas y discusiones🧑‍🤝‍🧑.
    
    </td>
    </tr>
    <tr>
    <td>
 
### ¿Por qué la mejora "XL"? 
- 🏠 El campo/mercado carece de robots domésticos de doble brazo asequibles y estables que igualen la facilidad de montaje de LeRobot.
- 🖨️ Los chasis tradicionales impresos en 3D sufren de durabilidad, estabilidad y capacidad de carga limitadas, lo que los hace poco prácticos para el uso diario.
- ⚡ Los robots móviles DIY enfrentan desafíos de suministro de energía, lo que lleva a configuraciones de cableado complejas.
- 🤖 **XLerobot** mantiene compatibilidad con la configuración de doble brazo SO100 de sobremesa de la comunidad LeRobot, permitiendo una transferencia perfecta de código y políticas.
  
    </td>
  </tr>
 </table>       
 
### Ventajas/Objetivos Generales de XLeRobot

- **Rentable** 💴: La construcción completa cuesta ~$660, o actualiza desde SO100Arm y Lekiwi existentes por ~$250.
- **Fácil actualización** ⏫ (física y eléctrica) para **Lekiwi** y **SO100**
    - Hardware: No se necesitan cambios de ID de motor ni modificaciones de hardware
    - Software: Configuración de sobremesa de un solo brazo/doble brazo idéntica—transfiere tus políticas entrenadas directamente desde el brazo SO100
- **Práctico y confiable** 💪: Realiza muchas tareas diarias comparables a alternativas del mercado de $20,000.
 
    - Más tareas demostradas en el hackathon de LeRobot en [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) y [Mountain View](https://x.com/asierarranz/status/1905306686648132061).
    - **Nota**: Actualmente no está diseñado para destreza en mano 🤹, levantamiento pesado (más de 1kg por brazo) 🏋️, o movimientos altamente dinámicos 🏃
- **Abundantes recursos de código abierto** 📕
    - Código plug-and-play de LeRobot🧩 y extensa biblioteca de modelos de IA🧠
    - Respaldado por una comunidad activa y creciente de colaboradores🧑‍🤝‍🧑

<img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />

Estas👆 son fotos preparadas, pero demuestran lo que la plataforma XLeRobot puede lograr dentro de sus limitaciones de hardware. (¡Las escenas están un poco desordenadas, pero hey, así es la vida!)




---
## 🎯 Demo 0.1.0 🎯
> [!NOTE]
> Actualmente una **versión de un solo brazo** implementando Lekiwi, teleoperada por el otro brazo seguidor a **velocidad 3x**.

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 Costo Total 💵

> [!NOTE] 
> El costo excluye impresión 3D, herramientas, envío e impuestos.

| Precio| EE.UU.  | UE  | CN |
|---------|----:|----:|----:|
| **Construir desde cero** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **Actualizar desde 2 brazos SO100**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **Actualizar desde 1 Lekiwi (base + brazo)** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **Actualizar desde 1 Lekiwi y 1 brazo SO100** |  **~$250**  |  **~€240**  |  **~¥1200**  |

Para más detalles, consulta la [Lista de Materiales](BOM.md).

---
---
## 🚀 Primeros Pasos 🚀
> [!NOTE] 
> Yo mismo soy principiante en hardware, así que quiero hacer este tutorial amigable para todos los principiantes.
1. 💵 **Compra tus piezas**: [Lista de Materiales](BOM.md)
2. 🖨️ **Imprime tus componentes**: [Impresión 3D](3Dprint.md)
3. 🔨 ~~Vengadores~~: [**¡Ensamblen**!](Assembly.md)
4. 💻 **Software**: [¡Pon en movimiento tu robot!](Software.md)
---
---
> [!NOTE] 
> El contenido anterior proporciona instrucciones eficientes para construir el **XLeRobot**. El contenido a continuación explica el propósito y la visión del proyecto con mayor detalle.

## 🛠️ Introducción al Hardware 🛠️

**XLeRobot** = Lekiwi + 1x brazo SO100 + **Carrito RÅSKOG de IKEA** + **Batería Anker**

= 2x Brazos SO100 + 3x ruedas omnidireccionales + RasberryPi + **Carrito RÅSKOG de IKEA** + **Batería Anker**

> [!NOTE]
> *Toda la computación es manejada por tu PC—Raspberry Pi solo gestiona la comunicación de datos vía WiFi 📶*

<table>
  <tr>
    <td>
      
### ¿Por qué el carrito RÅSKOG de IKEA?
- 🌎 Disponibilidad global con diseño estandarizado
- 💰 Rentable
- 🏗️ Construcción simple pero robusta
- 🔧 Base de malla metálica que permite fácil montaje de componentes
- 📦 Perfecto para almacenamiento y transporte
- 📏 Altura ideal para superficies domésticas comunes—desde la estufa hasta la mesa de café
- 📏 Huella compacta que cabe en casi cualquier habitación (gracias al diseño considerado de IKEA)


    </td>
    </tr>
    <tr>
    <td>
    
### ¿Por qué la estación de energía Anker SOLIX C300? 
- 🌍 Disponibilidad global
- ⚡ Capacidad de 288Wh, potencia máxima de salida de 300W, potencia máxima de carga de 280W
- 🔌 Alimenta ambos brazos de 12V, la base y Raspberry Pi a plena capacidad a través de tres cables de carga USB-C—eliminando el cableado complejo
- 🔋 Excepcional duración de batería: 12+ horas de uso normal, 8 horas de operación intensiva, 1 hora de carga completa
- 💡 Iluminación integrada para operación nocturna
- ☀️ Montaje opcional de panel solar para suministro continuo de energía
- 🎒 Versátil y desmontable—funciona también como energía de respaldo de emergencia o fuente de energía para acampar

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

Incluso cuando no estás usando activamente el robot, estos dos productos siguen siendo valiosos para el uso cotidiano.
---

## 💻 Introducción al Software 💻
Así es como puedes controlar el robot y hacerlo inteligente:

### 🕹️ Control Básico

- Control de **articulaciones** (ángulo del motor) → control de brazo líder-seguidor

- Control de **pose del efector final** → control remoto VR
  
> [!NOTE]
> Para la primera versión, nos enfocamos principalmente en el hardware. El código de LeRobot permanece sin modificar. Puedes recrear el Demo 0.1.0 conectando un brazo a la RaspberryPi y el otro al escritorio para control remoto. **El código LeRobot para XLeRobot** se actualizará pronto como nuestra máxima prioridad.


### 🧠 Caminos hacia la Inteligencia de Máquina Incorporada General (PENDIENTE)






### 🔈Publicidad:
- **Nuestro laboratorio**: [Rice RobotPI Lab](https://robotpilab.github.io/)
    - Nuestra visión incluye usar [**Caging in Time**](https://robotpilab.github.io/publication/caging/) y métodos de **Manipulación basada en Embudo** para lograr una manipulación robusta de objetos en condiciones del mundo real imperfectas — incluyendo ruido de percepción, retraso de red y entornos [ricos en contacto](https://robotpilab.github.io/publication/collision-inclusive-manipulation/).
- **Plataforma de simulación** (mi preferencia personal): [Maniskill](https://www.maniskill.ai/)
    - 🚀Aceleración GPU rápida para simulaciones paralelas
    - 🎨Hermosos visuales fotorrealistas mediante ray-tracing
    - 🪶Ligero, consistente y fácil de usar (comparado con Isaac Lab, en mi opinión)
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

- 📸 Añadir una cámara de profundidad RealSense a la cabeza para complementar las cámaras RGB de la mano para una percepción ambiental precisa
- 🔦 Añadir un Lidar y capacidades SLAM para navegación doméstica tipo Roomba
- 👆 Sensibilidad táctil básica
    </td>
  </tr>
</table>


> [!NOTE]
> Aunque mejoras más sofisticadas son totalmente posibles (como cambiar a un procesador Jetson, actualizar el chasis o usar mejores motores), estas contradirían la misión central de este proyecto: **crear la plataforma universal de robots de código abierto más asequible, fácil de instalar y plug-and-play del mundo**. Pero estas mejoras pueden listarse como complementos opcionales en el futuro en lugar de la vía principal.

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
- 🤖 Tareas simples usando modelos VLA existentes del código base de Lerobot
    </td>
    </tr>
    <tr>
    <td>
    
**En un futuro próximo**

- 🎯 Calibración precisa basada en AprilTag
- 🗺️ Navegación autónoma
- 🌐 Alineación de gemelo digital para aplicaciones sim2real
- 🧠 Modelo del mundo y manipulación robusta basada en física
- 💬 Conectar con MCP para utilizar directamente LLMs
    </td>
  </tr>
</table>

---

## 🎯 ¿Para quién es XLeRobot?

- 🚀 **Startups y Laboratorios**: Construye prototipos más rápido con la plataforma modular más barata del mundo
- 👩🔬 **Investigadores Independientes**: Experimenta con IA incorporada sin arruinarte 💸
- 🎓 **Héroes de la Educación**:
  - Profesores de Secundaria: Lleva robótica de vanguardia a las clases STEM 🧪
  - Profesores Universitarios: Plataforma asequible para cursos de robótica/IA 📚
  - Estudiantes: Desde principiantes hasta investigadores 🎒→🎓
- 🤖 **Entusiastas DIY**: Perfecto para proyectos de interior - cuidado de plantas, robots de entrega, automatización del hogar 🌱📦
---

## Limitaciones

(Hey, por este precio, ¿qué más podrías pedir?)

- 🔒 Altura fija—añadir una plataforma de elevación estable aumentaría significativamente los costos y la dificultad de montaje
- 📏 Espacio de trabajo más pequeño comparado con Aloha—aunque maximizamos el espacio de trabajo del SO100, el brazo tiene limitaciones de tamaño, aunque XLeRobot sigue manejando la mayoría de las tareas eficazmente
- ⚖️ Capacidad de carga limitada para un solo brazo—por eso usamos el carrito IKEA
- 🛒 La precisión del movimiento de la base puede verse afectada por las ruedas del carrito IKEA—esto puede abordarse mediante control de retroalimentación de bucle cerrado
  
Considerando todo—costo, soporte comunitario, facilidad de montaje y utilidad práctica—¡XLeRobot destaca como uno de los robots de bajo costo más atractivos para aplicaciones de interior!


---

### Principales Colaboradores

Actualmente solo [yo](https://vector-wangel.github.io/). 

Esto es solo un pequeño ladrillo en la pirámide, hecho posible por [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), y [Bambot](https://github.com/timqian/bambot). Gracias a todos los talentosos colaboradores detrás de estos proyectos detallados y profesionales.

¡Espero colaborar con cualquier persona interesada en contribuir a este proyecto!

No afiliado con Anker o IKEA (¡pero nos encantan las albóndigas suecas! 🍝)
