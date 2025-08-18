# Simple-Video-Converter - Version 1.0

# Copyright © Gaëtan Sencie 2025

# Tous droits réservés.



## Description



"**Simple-Video-Converter**" est une application de bureau **performante** et **sécurisée** conçue pour simplifier le processus de conversion de fichiers vidéo. Utilisant la puissance de FFmpeg et FFprobe en arrière-plan, elle offre une solution efficace pour convertir vos vidéos entre différents formats, avec des options de qualité et de performance adaptées à vos besoins.


## Prévisualisation

![Capture d'écran de l'application Simple-Video-Converter](https://github.com/STENS66/Simple-Video-Converter/blob/main/images/window.png?raw=true)


### Compatibilité


Application de bureau conçue pour Windows 10 et 11 (64 bits).


## Fonctionnalités



L'application "**Simple-Video-Converter**" propose une interface utilisateur claire et des fonctionnalités robustes pour une expérience de conversion vidéo complète.



**Ajout de fichiers flexible** :



* Glissez-déposez facilement vos fichiers vidéo directement dans la zone dédiée.
* Sélectionnez manuellement un ou plusieurs fichiers via une boîte de dialogue conviviale.



**Gestion de la liste de conversion** :



* Visualisez tous les fichiers ajoutés dans un tableau détaillé affichant le nom, la durée, la taille et le statut.
* Réorganisez l'ordre des fichiers dans la liste pour un traitement séquentiel précis.
* Supprimez les fichiers indésirables de la liste avant la conversion.



**Options de sortie personnalisables** :



* Répertoire de sortie : Choisissez facilement le dossier où vos vidéos converties seront sauvegardées.
* Formats de sortie : Convertissez vos vidéos vers les formats populaires tels que MKV, MP4, AVI et WebM.



**Contrôle avancé de la vidéo** :



* Accélération matérielle : Détection et utilisation des encodeurs matériels disponibles (NVIDIA NVENC, Intel Quick Sync, AMD AMF) pour des conversions ultra-rapides.
* Codecs vidéo : Choisissez parmi une gamme de codecs vidéo (H.264/libx264, HEVC/libx265, VP9/libvpx-vp9, Xvid/libxvid) en fonction de l'encodeur sélectionné et du format de sortie.
* Qualité vidéo : Ajustez la qualité de la vidéo avec le facteur de qualité constant (CRF) pour les codecs H.264/HEVC, ou définissez un bitrate vidéo spécifique pour d'autres codecs (ex: VP9).
* Presets d'encodage : Appliquez des presets x264/x265 (ultrafast, medium, veryslow, etc.) pour équilibrer la vitesse de conversion et la taille du fichier.
* Résolution : Redimensionnez vos vidéos à des résolutions prédéfinies (1080p, 720p, etc.) ou définissez une résolution personnalisée.



**Options audio** :



Codecs audio : Sélectionnez le codec audio désiré (AAC, MP3, Opus, Vorbis) ou choisissez de copier le flux audio original sans re-encodage.

Bitrate audio : Définissez un bitrate audio spécifique pour contrôler la qualité du son.



**Gestion des conflits de fichiers** :



* Choisissez l'action à entreprendre si un fichier de sortie existe déjà : demander à l'utilisateur, écraser, ignorer ou renommer automatiquement le nouveau fichier.



**Automatisation et commodité** :



* Option de supprimer les fichiers originaux après une conversion réussie pour économiser de l'espace.
* Option d'ouvrir automatiquement le dossier de sortie une fois toutes les conversions terminées.



**Suivi en temps réel** :



* Une barre de progression détaillée et des mises à jour de statut en temps réel pour chaque fichier et pour la progression globale de la conversion.
* Un journal des événements intégré affiche toutes les opérations et les messages importants de FFmpeg.



### Expérience Utilisateur Améliorée

*   **Réglages Intelligents** : Pour éviter les erreurs et garantir des conversions de qualité, l'application propose des réglages pré-configurés et des plages de valeurs (sliders) adaptées à chaque codec. Cela réduit le risque de choisir des paramètres incompatibles et assure un résultat optimal sans nécessiter de connaissances techniques approfondies.
*   **Thèmes Visuels** : Personnalisez votre expérience avec un thème par défaut (clair) et un thème sombre, accessibles depuis le menu pour un meilleur confort visuel.
*   **Guidage Intuitif** : Chaque option, même la plus complexe, est accompagnée d'une info-bulle (tooltip) explicative. Passez simplement la souris sur un réglage pour comprendre son utilité et son impact sur la conversion.


## Licences et Codecs FFmpeg

Pour des raisons de licence, l'application embarque une version de FFmpeg qui inclut uniquement des codecs sous licence **LGPL**. Cela garantit que le logiciel peut être distribué librement.

Cependant, certains codecs très populaires comme le **H.264 (libx264)** et le **HEVC (libx265)** sont sous licence **GPL**, et ne peuvent donc pas être inclus par défaut.

**Pour activer la prise en charge de tous les codecs :**

1.  L'application détectera si ces codecs sont manquants et vous en informera.
2.  Vous devrez télécharger vous-même une version de FFmpeg incluant les codecs GPL. Nous recommandons les builds "essentials" ou "full" disponibles sur des sites de confiance comme [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
3.  Une fois le fichier téléchargé et décompressé, utilisez l'option dans le menu `Configuration > Configurer les chemins FFmpeg/FFprobe...` pour indiquer à l'application où se trouvent les nouveaux fichiers `ffmpeg.exe` et `ffprobe.exe`.
4.  Après un redémarrage, l'application reconnaîtra les nouveaux codecs et vous offrira toutes ses fonctionnalités.


## Technologies Utilisées

Ce projet est développé en utilisant les technologies suivantes :

1. **Python 3.13.3** : Le langage de programmation principal.

2. **PySide6** : Un ensemble de liaisons Python pour la bibliothèque Qt, utilisé pour construire l'interface utilisateur graphique (GUI) de l'application.

3. Modules Python standards.



### Public Cible



Ce programme est destiné à un large public, des utilisateurs occasionnels aux créateurs de contenu qui ont besoin d'un outil simple et efficace pour convertir des vidéos. Il est idéal pour ceux qui recherchent une solution rapide et sans tracas pour adapter leurs fichiers vidéo à différentes plateformes ou appareils, sans avoir à naviguer dans des paramètres complexes. La prise en charge de l'accélération matérielle le rend particulièrement utile pour les utilisateurs souhaitant des conversions rapides sur des systèmes compatibles.



**Avantages en termes de sécurité**:



* "**Simple-Video-Converter**" offre des avantages significatifs en matière de sécurité et de confidentialité :
* **Fonctionnement hors ligne** : L'application fonctionne entièrement hors ligne. Elle ne nécessite aucune connexion Internet pour effectuer les conversions.
* **Protection des données** : Vos fichiers vidéo restent sur votre ordinateur et ne sont jamais téléchargés vers un serveur externe. Cela garantit une confidentialité maximale de vos données personnelles et sensibles.
* **Indépendance** : L'application est autonome et ne dépend d'aucun service cloud, réduisant ainsi les risques liés aux violations de données ou aux interruptions de service en ligne.



## Installation (Windows 10/11 - 64 bits)



1. Téléchargez le fichier exécutable de la dernière version ici: https://github.com/STENS66/Simple-Video-Converter/releases
2. Faites un double-clic sur le fichier téléchargé pour lancer l'application.
3. Suivez les instructions à l'écran pour compléter l'installation.




## Contact



Pour toute question ou assistance supplémentaire, vous pouvez me contacter à l'adresse email : app.sencie@gmail.com.

Merci d'utiliser "**Simple-Video-Converter**" !

