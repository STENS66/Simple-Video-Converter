# Simple-Video-Converter - Version 1.8
**Available on Microsoft Store (Windows) • Available on Snap Store (Linux)**

# Copyright © Gaëtan Sencie 2025
# All Rights Reserved.

---
**[English Version below - Version Française plus bas]**

---

## Description

"**Simple-Video-Converter**" is a **high-performance**, **secure**, and cross-platform desktop application designed to simplify the video file conversion process. Leveraging the power of FFmpeg and FFprobe in the background, it provides an efficient solution to convert your videos between various formats, with quality and performance options tailored to your needs.

The application offers the advantage of full compatibility with **Linux (Ubuntu)** and **Microsoft Windows**, ensuring maximum flexibility. It features several advanced options, including **hardware detection** and **native support for the AV1 codec (for compatible configurations)**, optimizing performance based on your system setup.

It operates exclusively **locally** on the user's computer, ensuring **maximum privacy**. Validated and published on the **Microsoft Store** and **Snap Store**, it features a robust architecture, a modern interface, and advanced features like **batch processing**.

## Preview

![Screenshot of Simple-Video-Converter application](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/window.png?raw=true)

![Screenshot of Simple-Video-Converter application](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/darkmode.png?raw=true)

![Screenshot of Simple-Video-Converter application](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/neonmode.png?raw=true)

### Compatibility

Desktop application designed for:
* **Windows**: 10 and 11 (64-bit).
* **Linux**: Available via **Snap** package on Ubuntu and compatible distributions.

## Features

The "**Simple-Video-Converter**" application offers a clear user interface and robust features for a complete video conversion experience.

**Interface Language Selection**:
* Choose between **French**, **English**, **German**, and now **Spanish**, **Portuguese (Brazil)**, **Italian** and **Japanese** via the "Languages" tab in the menu bar.

**Flexible File Adding**:
* Easily drag and drop your video files directly into the dedicated area.
* Manually select one or multiple files via a user-friendly dialog box.

**Conversion List Management**:
* View all added files in a detailed table displaying name, duration, size, and status.
* **Advanced List Ergonomics:** Full support for `Ctrl + Click` and `Shift + Click` for multi-selection.
* **Instant Repositioning:** Move multiple selected files directly to the absolute top or bottom of the queue in one click.
* **Visual Drag & Drop:** Fluidly reorder files manually using the mouse.
* **Delta Storage Insights:** A dedicated "Output / Gain" column showing exact storage space saved or lost in Megabytes (MB) and Percentages (%) immediately after processing.
* **Multi-stream Support**: Right-click on one or more files in the list and select "Select streams" to manage multiple audio tracks and subtitles.
* Reorder files in the list for precise sequential processing.
* Remove unwanted files from the list before conversion.

**Customizable Output Options**:
* **Output Directory**: Easily choose the folder where your converted videos will be saved.
* **Output Formats**: Convert your videos to popular formats such as MKV, MP4, AVI, and WebM.

**Advanced Video Control & Hardware**:

* **Target Size with 2-pass Encoding:** Set the exact desired final size for your video (adjustable limit from 1 to 50,000 MB).

**Advantages:** Ideal for adhering to strict size limits when sharing on platforms like Discord, social media, or via email, while ensuring the best possible visual quality for that size.

**Accuracy & Technology:** The system utilizes FFmpeg's 2-pass encoding mode. You can expect an accuracy of 92% to 98% relative to the requested target (e.g., for a 100 MB request, the final file will generally be between 92 and 98 MB). This safety margin ensures that the set limit is never exceeded, adapting to the dynamic constraints of the scenes, the container, and the audio.

* **Universal "Copy" Mode (Passthrough):** Ability to instantly remux or extract audio and subtitle streams without re-encoding the video track. Achieves lightning-fast speeds (64x to 68x) with absolute zero quality loss.
* **Advanced Hardware Detection**: The application automatically identifies available hardware (NVIDIA GPU, AMD, Intel) and adapts encoding options accordingly.
* **Video Codecs**: Extensive support including H.264, HEVC, VP9, Xvid, and the addition of **AV1 support** (for compatible hardware).
* **Dynamic Codec Management**: Smart detection of available codecs based on the FFmpeg version (embedded or GPL).
* **Video Quality**: Adjust quality with the Constant Rate Factor (CRF) or define a specific bitrate.
* **Encoding Presets**: Apply presets (ultrafast, medium, veryslow, etc.) to balance speed and file size.
* **Resolution**: Resize your videos (1080p, 720p, etc.) or define a custom resolution.

**Audio Options**:
* **Audio Codecs**: Select the desired codec (AAC, MP3, Opus, Vorbis) or copy the original stream.
* **Audio Bitrate**: Define a specific bitrate to control sound quality.

**File Conflict Management**:
* Choose automatic action: ask, overwrite, skip, or rename the new file.

**Automation and Convenience**:
* **Settings Persistence**: Your preferences (sliders, positions, themes) are saved and restored between sessions.
* Option to delete original files after success.
* Option to open the output folder upon completion.

**Real-Time Monitoring**:
* Progress bar and real-time status updates.
* **Intelligent Global ETA:** Advanced weight-based progression tracking (processed bytes instead of simple file count) for ultra-stable time estimation.
* **Post-Batch Session Report:** Summary of average bitrate, speed factors, total time spent, and total space recovered printed inside the event log window.
* **Enhanced Log Management**: Built-in event log for better tracking of operations and debugging.

### Enhanced User Experience
* **Smart Settings**: To avoid errors, the application offers pre-configured settings and value ranges adapted to each codec.
* **Visual Themes**: Customize your experience with 4 themes: **Light** (default), **Dark**, and the new **Neon** and **Cyberpunk** themes.
* **Intuitive Guidance**: Explanatory tooltips on every option.
* **Fixes**: Improved interface and text for clarity and stability.

## Licenses and FFmpeg Codecs

For licensing reasons, the application embeds a version of FFmpeg including only **LGPL** licensed codecs. This ensures free distribution on Stores.
However, some popular codecs (H.264, HEVC) are under **GPL** license and are not included by default.

The application will detect missing codecs. Here is how to enable full support (GPL Builds) depending on your system:

### On Windows

1. Download an FFmpeg version including GPL codecs (e.g., "ffmpeg-7.1.1-essentials_build" or "full_build"). We recommend [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
2. Unzip the archive.
3. In the application, go to `Configuration > Configure FFmpeg/FFprobe paths...`.
4. Point to the location of your `ffmpeg.exe` and `ffprobe.exe` files.
5. Restart the application.

### On Linux (Ubuntu/Snap)

**Plug & Play Experience**: The Linux version (Snap) is a **strictly confined**, all-in-one package. Unlike the Windows version, configuration is fully automatic: the "Configuration" menu for selecting FFmpeg paths is disabled as the application manages the conversion engine internally.

**Intelligent Adaptive Engine:** The Linux (Snap) version is now equipped with a unique adaptive detection system. It features two distinct conversion engines:

   * **Engine 8.1 (High Performance):** Used for recent hardware and the latest drivers.

   * **Engine 7.1 (Maximum Compatibility):** Used as an automatic fallback to ensure NVIDIA hardware acceleration remains operational, even on older configurations.
    The application analyzes your system at startup and selects the most efficient engine without any intervention on your part.

**Open Source Compliance (FFmpeg):** This application includes pre-compiled FFmpeg binaries (Versions 8.1 and 7.1).

   * **License:** These binaries are distributed under the GNU General Public License (GPL) version 3.
   
   * **Source Code:** The source code and compilation scripts are available on the BtbN/FFmpeg-Builds repository or on the official ffmpeg.org website. Simple-Video-Converter acts as a proprietary graphical interface for these tools.


⚠️ **Note on External Drives (USB/SD)**: Because the application runs in a secure sandbox ("Strict confinement"), it cannot access your external drives by default. If your videos are stored on a USB stick or a secondary hard drive, you must grant permission by running this command once in your terminal:

```
sudo snap connect simple-video-converter:removable-media
```


## Target Audience

This program is intended for a wide audience, from casual users to content creators on **Windows and Linux**. It is ideal for those looking for a quick solution to adapt their video files without complex settings. Support for hardware acceleration and the **AV1** codec makes it particularly performant on modern systems.

**Security Benefits**:
* "**Simple-Video-Converter**" offers total security and privacy.
* **Offline Operation**: No Internet connection required to convert.
* **Data Protection**: Your videos stay on your hard drive; no cloud uploads.
* **Independence**: Standalone, with no dependence on third-party services.

## Download

- [Microsoft Store (Windows 10/11)](https://apps.microsoft.com/detail/9P990VQJTRTK?hl=en-us&gl=US)
  
- [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/fr/snap-store-black.svg)](https://snapcraft.io/simple-video-converter)

- Or install via terminal:
  
  ```
  sudo snap install simple-video-converter
  ```
  
- [GitHub Releases](https://github.com/STENS66/Simple-Video-Converter/releases)

## Contact

- Email: app.sencie@gmail.com
- LinkedIn: [Gaëtan Sencie](https://www.linkedin.com/in/ga%C3%ABtan-sencie-applications-python)
- GitHub: [STENS66](https://github.com/STENS66)

Thank you for using "**Simple-Video-Converter**"!

---

## References & Keywords

Developed by **Gaëtan Sencie**, Python developer.

**Simple-Video-Converter** is officially available on the **Microsoft Store**, **GitHub**, and the **Snap Store**, ensuring reliable and validated distribution.

**Keywords**: video conversion, video compression, target size, 2-pass encoding, file size reduction, Discord limit, FFmpeg, FFprobe, privacy, offline application, data security, hardware acceleration, NVENC, Quick Sync, AMF, video codecs, AV1, MKV, MP4, AVI, WebM, Windows 10, Windows 11, Linux, Ubuntu, Snap Store, Python, GUI, video remuxing, video passthrough, stream extractor, batch video reorder, FFmpeg GUI, space reduction tracker, multi-selection queue.

---

# Simple-Video-Converter - Version 1.8
**Disponible sur le Microsoft Store (Windows) • Disponible sur le Snap Store (Linux)**

# Copyright © Gaëtan Sencie 2025
# Tous droits réservés.

## Description

"**Simple-Video-Converter**" est une application de bureau **performante**, **sécurisée** et multiplateforme conçue pour simplifier le processus de conversion de fichiers vidéo. Utilisant la puissance de FFmpeg et FFprobe en arrière-plan, elle offre une solution efficace pour convertir vos vidéos entre différents formats, avec des options de qualité et de performance adaptées à vos besoins.

L'application offre l'avantage d'une compatibilité complète sur **Linux (Ubuntu)** et **Microsoft Windows**, garantissant une flexibilité maximale. Elle intègre plusieurs options avancées, notamment une **détection matérielle** et le **support natif du codec AV1 (pour les configurations compatibles)**, optimisant ainsi les performances selon votre configuration.

Elle fonctionne exclusivement **en local** sur l’ordinateur de l’utilisateur, garantissant ainsi une **confidentialité maximale**. Validée et publiée sur le **Microsoft Store** et le **Snap Store**, elle offre une architecture robuste, une interface moderne et des fonctionnalités avancées comme le **traitement par lots**.

## Prévisualisation

![Capture d'écran de l'application Simple-Video-Converter](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/window.png?raw=true)

![Capture d'écran de l'application Simple-Video-Converter](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/darkmode.png?raw=true)

![Capture d'écran de l'application Simple-Video-Converter](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/neonmode.png?raw=true)

### Compatibilité

Application de bureau conçue pour :
* **Windows** : 10 et 11 (64 bits).
* **Linux** : Disponible via paquet **Snap** sur Ubuntu et distributions compatibles.

## Fonctionnalités

L'application "**Simple-Video-Converter**" propose une interface utilisateur claire et des fonctionnalités robustes pour une expérience de conversion vidéo complète.

**Choix des langues de l'interface**:
* Choisissez entre le **Français**, l'**Anglais**, l'**Allemand**, et désormais l'**Espagnol**, **Portugais (Brésil)**, **Italien** et **Japonais** via l'onglet "Langues" dans la barre de menu.

**Ajout de fichiers flexible** :
* Glissez-déposez facilement vos fichiers vidéo directement dans la zone dédiée.
* Sélectionnez manuellement un ou plusieurs fichiers via une boîte de dialogue conviviale.

**Gestion de la liste de conversion** :
* Visualisez tous les fichiers ajoutés dans un tableau détaillé affichant le nom, la durée, la taille et le statut.
* **Ergonomie Avancée :** Support complet des combinaisons `Ctrl + Clic` et `Maj + Clic` pour la sélection multiple.
* **Repositionnement Éclair :** Déplacez un groupe de fichiers sélectionnés tout en haut ou tout en bas de la liste en un seul clic.
* **Glisser-Déposer Visuel :** Réorganisez l'ordre de passage des fichiers de manière fluide directement à la souris.
* **Bilan de Stockage en Temps Réel :** Une colonne dédiée "Sortie / Gain" affiche l'espace disque gagné ou perdu en Mégaoctets (Mo) et en Pourcentages (%) dès la fin du traitement.
* **Support Multi-flux** : Faites un clic droit sur un ou plusieurs fichiers de la liste et choisissez "Sélectionner les flux" pour gérer les différentes pistes audio et les sous-titres.
* Réorganisez l'ordre des fichiers dans la liste pour un traitement séquentiel précis.
* Supprimez les fichiers indésirables de la liste avant la conversion.

**Options de sortie personnalisables** :
* **Répertoire de sortie** : Choisissez facilement le dossier où vos vidéos converties seront sauvegardées.
* **Formats de sortie** : Convertissez vos vidéos vers les formats populaires tels que MKV, MP4, AVI et WebM.

**Contrôle avancé de la vidéo & Hardware** :

* **Ciblage de la taille (Target Size) avec Encodage 2-passes :** Définissez le poids final exact souhaité pour votre vidéo (limite ajustable de 1 à 50 000 Mo).

**Avantages :** Idéal pour respecter les limites strictes de taille lors du partage sur des plateformes comme Discord, les réseaux sociaux, ou par e-mail, tout en garantissant la meilleure qualité visuelle possible pour ce poids.

**Précision & Technologie :** Le système utilise le mode d'encodage en double passe (2-pass) de FFmpeg. Vous pouvez vous attendre à une précision de 92 % à 98 % par rapport à la cible demandée (ex: pour une demande de 100 Mo, le fichier final pèsera généralement entre 92 et 98 Mo). Cette marge garantit de ne jamais dépasser le plafond fixé, en s'adaptant aux contraintes dynamiques des scènes, du conteneur et de l'audio.

* **Mode "Copie" Universel (Passthrough) :** Permet de réincorporer ou d'extraire instantanément des pistes audio et des sous-titres sans ré-encoder la piste vidéo. Atteint des vitesses foudroyantes (64x à 68x) avec une perte de qualité absolument nulle.
* **Détection Hardware Avancée** : L'application identifie automatiquement le matériel disponible (GPU NVIDIA, AMD, Intel) et adapte les options d'encodage en conséquence.
* **Codecs vidéo** : Support étendu incluant H.264, HEVC, VP9, Xvid et l'ajout du **support AV1** (pour les matériels compatibles).
* **Gestion dynamique des codecs** : Détection intelligente des codecs disponibles selon la version de FFmpeg (embarquée ou GPL).
* **Qualité vidéo** : Ajustez la qualité avec le facteur de qualité constant (CRF) ou définissez un bitrate spécifique.
* **Presets d'encodage** : Appliquez des presets (ultrafast, medium, veryslow, etc.) pour équilibrer vitesse et taille.
* **Résolution** : Redimensionnez vos vidéos (1080p, 720p, etc.) ou définissez une résolution personnalisée.

**Options audio** :
* **Codecs audio** : Sélectionnez le codec désiré (AAC, MP3, Opus, Vorbis) ou copiez le flux original.
* **Bitrate audio** : Définissez un bitrate spécifique pour contrôler la qualité du son.

**Gestion des conflits de fichiers** :
* Choisissez l'action automatique : demander, écraser, ignorer ou renommer le nouveau fichier.

**Automatisation et commodité** :
* **Persistence des réglages** : Vos préférences (sliders, positions, thèmes) sont sauvegardées et restaurées entre les sessions.
* Option de supprimer les fichiers originaux après succès.
* Option d'ouvrir le dossier de sortie à la fin.

**Suivi en temps réel** :
* Barre de progression et statuts en temps réel.
* **ETA Global Intelligent :** Calcul du temps restant basé rigoureusement sur le poids des fichiers (octets traités) plutôt que sur le simple nombre de fichiers, garantissant une estimation ultra-stable.
* **Rapport de Fin de Session :** Résumé complet affiché dans le journal des événements (bitrate moyen, vitesse globale, temps total passé et total d'espace disque récupéré).
* **Gestion des logs améliorée :** Journal des événements intégré pour un meilleur suivi des opérations et du débogage.

### Expérience Utilisateur Améliorée
* **Réglages Intelligents** : Pour éviter les erreurs, l'application propose des réglages pré-configurés et des plages de valeurs adaptées à chaque codec.
* **Thèmes Visuels** : Personnalisez votre expérience avec 4 thèmes : **Clair** (défaut), **Sombre**, et les nouveaux thèmes **Neon** et **Cyberpunk**.
* **Guidage Intuitif** : Info-bulles (tooltips) explicatives sur chaque option.
* **Corrections** : Interface et textes améliorés pour plus de clarté et de stabilité.

## Licences et Codecs FFmpeg

Pour des raisons de licence, l'application embarque une version de FFmpeg incluant uniquement des codecs sous licence **LGPL**. Cela garantit une distribution libre sur les Stores.
Cependant, certains codecs populaires (H.264, HEVC) sont sous licence **GPL** et ne sont pas inclus par défaut.

L'application détectera les codecs manquants. Voici comment activer la prise en charge complète (Builds GPL) selon votre système :

### Sur Windows

1. Téléchargez une version de FFmpeg incluant les codecs GPL (ex: "ffmpeg-7.1.1-essentials_build" ou "full_build"). Nous recommandons [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
2. Décompressez l'archive.
3. Dans l'application, allez dans `Configuration > Configurer les chemins FFmpeg/FFprobe...`.
4. Indiquez l'emplacement de vos fichiers `ffmpeg.exe` et `ffprobe.exe`.
5. Redémarrez l'application.

### Sur Linux (Ubuntu/Snap)

**Expérience Clé en Main (Plug & Play)** : La version Linux (Snap) est un paquet "tout-en-un" **en confinement strict**. Contrairement à la version Windows, la configuration est entièrement automatique : le menu "Configuration" permettant de choisir les chemins FFmpeg est désactivé car l'application gère elle-même le moteur de conversion en interne.

**Moteur Adaptatif Intelligent :** La version Linux (Snap) est désormais équipée d'un système de détection adaptative unique. Elle embarque deux moteurs de conversion distincts :

   * **Moteur 8.1 (Haute Performance) :** Utilisé pour les matériels récents et les derniers pilotes.

   * **Moteur 7.1 (Compatibilité Maximale) :** Utilisé comme solution de repli automatique pour garantir que l'accélération matérielle NVIDIA reste opérationnelle, même sur des configurations plus anciennes.
    L'application analyse votre système au démarrage et sélectionne le moteur le plus performant sans aucune intervention de votre part.

**Conformité Open Source (FFmpeg) :** Cette application inclut des binaires pré-compilés de FFmpeg (Versions 8.1 et 7.1).

  * **Licence :** Ces binaires sont distribués sous la licence GNU General Public License (GPL) version 3.

  * **Code Source :** Le code source et les scripts de compilation sont disponibles sur le dépôt BtbN/FFmpeg-Builds ou sur le site officiel ffmpeg.org. Simple-Video-Converter agit comme une interface graphique propriétaire pour ces outils.


⚠️ **Note concernant les disques externes (USB/SD)** : L'application s'exécutant dans un environnement sécurisé ("Confinement strict"), elle ne peut pas accéder à vos disques externes par défaut. Si vos vidéos sont stockées sur une clé USB ou un second disque dur, vous devez autoriser l'accès en exécutant cette commande une seule fois dans votre terminal :

```
sudo snap connect simple-video-converter:removable-media
```

## Public Cible

Ce programme est destiné à un large public, des utilisateurs occasionnels aux créateurs de contenu sur **Windows et Linux**. Il est idéal pour ceux qui recherchent une solution rapide pour adapter leurs fichiers vidéo sans paramètres complexes. La prise en charge de l'accélération matérielle et du codec **AV1** le rend particulièrement performant sur les systèmes modernes.

**Avantages en termes de sécurité**:

* "**Simple-Video-Converter**" offre une sécurité et une confidentialité totales.
* **Fonctionnement hors ligne** : Aucune connexion Internet requise pour convertir.
* **Protection des données** : Vos vidéos restent sur votre disque dur ; aucun upload vers le cloud.
* **Indépendance** : Autonome, sans dépendance à des services tiers.

## Téléchargement

- [Microsoft Store (Windows 10/11)](https://apps.microsoft.com/detail/9P990VQJTRTK?hl=fr-be&gl=BE&ocid=pdpshare)
  
- [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/fr/snap-store-black.svg)](https://snapcraft.io/simple-video-converter)

- Ou via le terminal :
  
  ```
  sudo snap install simple-video-converter
  ```
  
- [Releases GitHub](https://github.com/STENS66/Simple-Video-Converter/releases)

## Contact

- Email : app.sencie@gmail.com
- LinkedIn : [Gaëtan Sencie](https://www.linkedin.com/in/ga%C3%ABtan-sencie-applications-python)
- GitHub : [STENS66](https://github.com/STENS66)

Merci d'utiliser "**Simple-Video-Converter**" !

---

## Références & Mots-clés

Développé par **Gaëtan Sencie**, développeur Python.

**Simple-Video-Converter** est officiellement disponible sur le **Microsoft Store**, **GitHub** et le **Snap Store**, garantissant une diffusion fiable et validée.

**Mots-clés** : conversion vidéo, compression vidéo, taille cible, encodage 2-passes, réduction de taille, limite Discord, FFmpeg, FFprobe, confidentialité, application hors ligne, sécurité des données, accélération matérielle, NVENC, Quick Sync, AMF, codecs vidéo, AV1, MKV, MP4, AVI, WebM, Windows 10, Windows 11, Linux, Ubuntu, Snap Store, Python, GUI, remuxing vidéo, passthrough vidéo, extraction de flux, réordonnancement par lot, interface graphique FFmpeg, calcul de gain d'espace, file d'attente.
