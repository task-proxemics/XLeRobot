<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-brown.svg)](README_CN.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README_ES.md)
[![de](https://img.shields.io/badge/lang-de-orange.svg)](README_DE.md)
[![fr](https://img.shields.io/badge/lang-fr-white.svg)](README_FR.md)
[![日本語](https://img.shields.io/badge/lang-日本語-yellow.svg)](README_JP.md)

> [!NOTE] 
> **XLeRobot 0.1.0** est officiellement disponible ! La version actuelle comprend une **liste détaillée des matériaux**, des **modèles et instructions d'impression 3D**, et un **guide d'assemblage étape par étape**. Bien que le code ne soit pas encore disponible, vous pouvez **exécuter le test de téléopération** sur une version à un seul bras (contrôlé avec un autre bras suiveur) directement en utilisant le code original de Lekiwi.

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---

**🚀 L'IA incarnée pour tous - Moins cher qu'un iPhone ! 📱**  
*Construit sur les épaules des géants : [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 Pourquoi XLeRobot ? 🌟
Décomposons cela puisque **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### Pourquoi le cœur "LeRobot" ?
- **Matériaux économiques** 💴 : 90% des composants imprimés en 3D avec des moteurs et de l'électronique abordables.
- **Assemblage facile** 🔨 : Seulement 2 heures d'assemblage nécessaires.
- **Plug-&-Play** 🧩 : Faites fonctionner les robots avec une simple installation pip et quelques lignes de code.
- **Communauté LeRobot florissante** 🌍 :
  La plus grande communauté mondiale de robotique à faible coût proposant
  - De multiples modèles d'IA préentraînés à la pointe de la technologie 🧠, des ensembles de données 📊 et des outils 🔨 prêts à être déployés.
  - Plus de 5 000 esprits brillants pour le brainstorming et les discussions 🧑‍🤝‍🧑.
    
    </td>
    </tr>
    <tr>
    <td>
 
### Pourquoi l'amélioration "XL" ? 
- 🏠 Le domaine/marché manque de robots domestiques à double bras abordables et stables qui correspondent à la facilité d'assemblage de LeRobot.
- 🖨️ Les châssis traditionnels imprimés en 3D souffrent d'une durabilité, d'une stabilité et d'une capacité de charge limitées, ce qui les rend peu pratiques pour une utilisation quotidienne.
- ⚡ Les robots mobiles DIY font face à des défis d'alimentation électrique, entraînant des configurations de câblage complexes.
- 🤖 **XLerobot** maintient la compatibilité avec la configuration de table à double bras SO100 de la communauté LeRobot, permettant un transfert transparent du code et des politiques.
  
    </td>
  </tr>
 </table>       
 
### Avantages/Objectifs généraux de XLeRobot

- **Rentable** 💴 : La construction complète coûte environ 660 $, ou mise à niveau à partir d'un SO100Arm et Lekiwi existants pour environ 250 $.
- **Mise à niveau facile** ⏫ (physique et électrique) pour **Lekiwi** et **SO100**
    - Matériel : Aucun changement d'ID de moteur ou modification matérielle nécessaire
    - Logiciel : Configuration de table à un bras/double bras identique — transférez directement vos politiques entraînées depuis le bras SO100
- **Pratique et fiable** 💪 : Effectue de nombreuses tâches quotidiennes comparables aux alternatives du marché à 20 000 $.
 
    - Plus de tâches démontrées lors du hackathon LeRobot à [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) et [Mountain View](https://x.com/asierarranz/status/1905306686648132061).
    - **Remarque** : Actuellement non conçu pour la dextérité manuelle 🤹, le levage lourd (plus de 1 kg par bras) 🏋️, ou les mouvements hautement dynamiques 🏃
- **Ressources open-source riches** 📕
    - Code plug-and-play de LeRobot 🧩 et bibliothèque étendue de modèles d'IA 🧠
    - Soutenu par une communauté active et croissante de contributeurs 🧑‍🤝‍🧑

<img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />

Ces photos 👆 sont mises en scène, mais elles démontrent ce que la plateforme XLeRobot peut réaliser dans les limites de son matériel. (Les scènes sont un peu désordonnées, mais c'est la vie !)




---
## 🎯 Démo 0.1.0 🎯
> [!NOTE]
> Actuellement une **version à un seul bras** implémentant Lekiwi, téléopérée par l'autre bras suiveur à **3x la vitesse**.

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 Coût total 💵

> [!NOTE] 
> Le coût exclut l'impression 3D, les outils, l'expédition et les taxes.

| Prix | US  | EU  | CN |
|---------|----:|----:|----:|
| **Construction à partir de zéro** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **Mise à niveau à partir de 2 bras SO100**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **Mise à niveau à partir d'1 Lekiwi (base + bras)** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **Mise à niveau à partir d'1 Lekiwi et 1 bras SO100** |  **~$250**  |  **~€240**  |  **~¥1200**  |

Pour plus de détails, veuillez consulter la [Liste des matériaux](BOM.md).

---
---
## 🚀 Commencer 🚀
> [!NOTE] 
> Je suis moi-même un débutant en matériel, donc je veux rendre ce tutoriel accessible à tous les autres débutants.
1. 💵 **Achetez vos pièces** : [Liste des matériaux](BOM.md)
2. 🖨️ **Imprimez vos pièces** : [Impression 3D](3Dprint.md)
3. 🔨 ~~Avengers~~ : [**Assemblez** !](Assembly.md)
4. 💻 **Logiciel** : [Faites bouger votre robot !](Software.md)
---
---
> [!NOTE] 
> Le contenu ci-dessus fournit des instructions efficaces pour construire le **XLeRobot**. Le contenu ci-dessous explique plus en détail l'objectif et la vision du projet.

## 🛠️ Introduction au matériel 🛠️

**XLeRobot** = Lekiwi + 1x bras SO100 + **Chariot IKEA RÅSKOG** + **Batterie Anker**

= 2x Bras SO100 + 3x roues omnidirectionnelles + RasberryPi + **Chariot IKEA RÅSKOG** + **Batterie Anker**

> [!NOTE]
> *Tous les calculs sont gérés par votre PC — le Raspberry Pi ne gère que la communication des données via WiFi 📶*

<table>
  <tr>
    <td>
      
### Pourquoi le chariot IKEA RÅSKOG ?
- 🌎 Disponibilité mondiale avec conception standardisée
- 💰 Rentable
- 🏗️ Construction simple mais robuste
- 🔧 Le fond en maille métallique permet un montage facile des composants
- 📦 Parfait pour le stockage et le transport
- 📏 Hauteur idéale pour les surfaces domestiques courantes — de la cuisinière à la table basse
- 📏 Encombrement compact qui s'adapte à presque toutes les pièces (grâce à la conception réfléchie d'IKEA)


    </td>
    </tr>
    <tr>
    <td>
    
### Pourquoi la station d'alimentation Anker SOLIX C300 ? 
- 🌍 Disponibilité mondiale
- ⚡ Capacité de 288Wh, puissance de sortie maximale de 300W, puissance de charge maximale de 280W
- 🔌 Alimente les deux bras 12V, la base et le Raspberry Pi à pleine capacité via trois câbles de charge USB-C — éliminant le câblage complexe
- 🔋 Autonomie exceptionnelle : 12+ heures d'utilisation normale, 8 heures de fonctionnement intensif, charge complète en 1 heure
- 💡 Éclairage intégré pour le fonctionnement nocturne
- ☀️ Montage optionnel de panneau solaire pour une alimentation continue
- 🎒 Polyvalent et détachable — sert également d'alimentation de secours d'urgence ou de source d'alimentation pour le camping

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

Même lorsque vous n'utilisez pas activement le robot, ces deux produits restent précieux pour un usage quotidien.
---

## 💻 Introduction au logiciel 💻
Voici comment vous pouvez contrôler le robot et le rendre intelligent :

### 🕹️ Contrôle de base

- Contrôle des **articulations** (angle du moteur) → contrôle du bras leader-suiveur

- Contrôle de la **pose de l'effecteur terminal** → contrôle à distance VR
  
> [!NOTE]
> Pour la première version, nous nous concentrons principalement sur le matériel. Le code LeRobot reste inchangé. Vous pouvez recréer la Démo 0.1.0 en connectant un bras au RaspberryPi et l'autre au bureau pour le contrôle à distance. **Le code LeRobot pour XLeRobot** sera bientôt mis à jour en priorité.


### 🧠 Chemins vers l'intelligence machine incarnée générale (À FAIRE)






### 🔈Publicité :
- **Notre laboratoire** : [Rice RobotPI Lab](https://robotpilab.github.io/)
    - Notre vision inclut l'utilisation des méthodes [**Caging in Time**](https://robotpilab.github.io/publication/caging/) et **Manipulation basée sur l'entonnoir** pour réaliser une manipulation d'objets robuste dans des conditions réelles imparfaites — y compris le bruit de perception, la latence du réseau et les environnements [riches en contacts](https://robotpilab.github.io/publication/collision-inclusive-manipulation/).
- **Plateforme de simulation** (ma préférence personnelle) : [Maniskill](https://www.maniskill.ai/)
    - 🚀Accélération GPU rapide pour les simulations parallèles
    - 🎨Visuels photoréalistes magnifiques grâce au ray-tracing
    - 🪶Léger, cohérent et convivial (par rapport à Isaac Lab, à mon avis)
    - 🤖Support pour [plusieurs robots](https://maniskill.readthedocs.io/en/latest/software/index.html) (y compris le [bras SO100](https://x.com/Stone_Tao/status/1910101218241978537))


---
## Plans futurs

### Matériel
<table>
  <tr>
    <td>
      
**Urgent**

- 🔧 Ajouter deux options de base pour les bras : maintenu par pince (actuel) ou monté par vis
- 🛠️ Ajouter une plaque de connexion entièrement compatible avec le maillage métallique du chariot IKEA
    </td>
    </tr>
    <tr>
    <td>
    
**Dans un avenir proche**

- 📸 Ajouter une caméra de profondeur RealSense à la tête pour compléter les caméras RGB des mains pour une perception précise de l'environnement
- 🔦 Ajouter un Lidar et des capacités SLAM pour une navigation domestique de type Roomba
- 👆 Détection tactile de base
    </td>
  </tr>
</table>


> [!NOTE]
> Bien que des améliorations plus sophistiquées soient tout à fait possibles (comme passer à un processeur Jetson, améliorer le châssis ou utiliser de meilleurs moteurs), celles-ci contrediraient la mission fondamentale de ce projet : **créer la plateforme robotique open source universelle la plus abordable, facile à installer et plug-and-play au monde**. Mais ces améliorations peuvent être répertoriées comme des modules complémentaires optionnels à l'avenir plutôt que sur la piste principale.

### Logiciel

(les mises à jour logicielles dépendront également du développement de la communauté LeRobot)
<table>
  <tr>
    <td>
      
**Urgent**

- ⚙️ Algorithmes de contrôle de base
- 🎮 Contrôle optimisé de l'effecteur terminal
- 🎲 Environnement de simulation Maniskill
- 🕶️ Contrôle VR Quest3 et téléopération
- 🤖 Tâches simples utilisant les modèles VLA existants de la base de code Lerobot
    </td>
    </tr>
    <tr>
    <td>
    
**Dans un avenir proche**

- 🎯 Calibration précise basée sur AprilTag
- 🗺️ Navigation autonome
- 🌐 Alignement du jumeau numérique pour les applications sim2real
- 🧠 Modèle du monde et manipulation robuste basée sur la physique
- 💬 Connexion avec MCP pour utiliser directement les LLM
    </td>
  </tr>
</table>

---

## 🎯 À qui s'adresse XLeRobot ?

- 🚀 **Startups & Laboratoires** : Construisez des prototypes plus rapidement avec la plateforme modulaire la moins chère au monde
- 👩🔬 **Chercheurs indépendants** : Expérimentez l'IA incarnée sans vous ruiner 💸
- 🎓 **Héros de l'éducation** :
  - Enseignants du secondaire : Apportez la robotique de pointe aux cours STEM 🧪
  - Professeurs d'université : Plateforme abordable pour les cours de robotique/IA 📚
  - Étudiants : Des débutants aux chercheurs 🎒→🎓
- 🤖 **Enthousiastes DIY** : Parfait pour les projets d'intérieur - soin des plantes, robots de livraison, domotique 🌱📦
---

## Limitations

(Hé, pour ce prix, que pourriez-vous demander de plus ?)

- 🔒 Hauteur fixe — l'ajout d'une plateforme élévatrice stable augmenterait considérablement les coûts et la difficulté d'assemblage
- 📏 Espace de travail plus petit par rapport à Aloha — bien que nous maximisions l'espace de travail SO100, le bras a des limitations de taille, bien que XLeRobot gère toujours efficacement la plupart des tâches
- ⚖️ Capacité de charge limitée pour un seul bras — c'est pourquoi nous utilisons le chariot IKEA
- 🛒 La précision du mouvement de la base peut être affectée par les roues du chariot IKEA — cela peut être résolu par un contrôle en boucle fermée
  
Tout bien considéré — coût, support communautaire, facilité d'assemblage et utilité pratique — XLeRobot se distingue comme l'un des robots à faible coût les plus convaincants pour les applications intérieures !


---

### Principaux contributeurs

Actuellement juste [moi](https://vector-wangel.github.io/). 

Ce n'est qu'une petite brique dans la pyramide, rendue possible par [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), et [Bambot](https://github.com/timqian/bambot). Merci à tous les contributeurs talentueux derrière ces projets détaillés et professionnels.

J'ai hâte de collaborer avec toute personne intéressée à contribuer à ce projet !

Non affilié à Anker ou IKEA (mais nous adorons les boulettes suédoises ! 🍝)
