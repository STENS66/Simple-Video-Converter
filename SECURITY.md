# Security Policy

I take the security of **Simple-Video-Converter** very seriously. As an independent developer, I built this application with a strong focus on privacy (offline operation, no data collection). Therefore, I am committed to promptly resolving any security issues that could compromise the application's integrity or user experience.

## Supported Versions

Only the versions listed below currently receive security updates.

| Version | Supported | Notes |
| :--- | :--- | :--- |
| 1.3.x | ✅ | Current version (Windows & Linux) |
| 1.2.x | ❌ | Please update to v1.3 |
| < 1.2 | ❌ | End-of-Life / Obsolete |


## Reporting a Vulnerability

If you discover a security vulnerability in **Simple-Video-Converter**, please **do not** open a public issue on GitHub immediately. This could expose users to risk before a fix is available.

Please follow this **responsible disclosure** procedure:
1. Send a detailed email to **app.sencie@gmail.com**.
2. Include "SECURITY" in the subject line.
3. Describe the vulnerability, steps to reproduce it, and the environment used (Windows or Linux).

### My Commitment

* I will acknowledge receipt of your report within **48 to 72 hours**.
* I will keep you informed of the progress of the fix.
* Once the vulnerability is patched and the update is published on Stores (Microsoft & Snap), I will publicly credit you (if you wish) in the release notes to thank you for your help.

## Note regarding FFmpeg

Simple-Video-Converter uses **FFmpeg** as its conversion engine.

* If the vulnerability directly concerns the `ffmpeg.exe` binary or FFmpeg libraries (and not my interface or file handling), please refer to the [FFmpeg Security Policy](https://ffmpeg.org/security.html).
* However, if my application uses FFmpeg in an insecure way, this falls under my responsibility and should be reported to me.

Thank you for helping keep Simple-Video-Converter safe for everyone!

---

# Politique de Sécurité

Je prends la sécurité de **Simple-Video-Converter** très au sérieux. En tant que développeur indépendant, j'ai conçu cette application en mettant l'accent sur la confidentialité (fonctionnement hors ligne, pas d'envoi de données). Je m'engage donc à résoudre rapidement tout problème de sécurité qui pourrait compromettre l'intégrité de l'application ou l'expérience utilisateur.

## Versions Supportées

Seules les versions listées ci-dessous bénéficient actuellement de mises à jour de sécurité.

| Version | Supportée | Notes |
| :--- | :--- | :--- |
| 1.3.x | ✅ | Version actuelle (Windows & Linux) |
| 1.2.x | ❌ | Veuillez mettre à jour vers la v1.3 |
| < 1.2 | ❌ | Obsolète |


## Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité de sécurité dans **Simple-Video-Converter**, je vous demande de **ne pas** ouvrir d'issue publique sur GitHub immédiatement. Cela pourrait exposer les utilisateurs à des risques avant qu'un correctif ne soit disponible.

Merci de suivre la procédure de **divulgation responsable** suivante :
1. Envoyez-moi un email détaillé à **app.sencie@gmail.com**.
2. Incluez "SÉCURITÉ" ou "SECURITY" dans l'objet de votre email.
3. Décrivez la vulnérabilité, les étapes pour la reproduire, et l'environnement utilisé (Windows ou Linux).

### Mon engagement

* J'accuserai réception de votre rapport sous **48 à 72 heures**.
* Je vous tiendrai informé de l'avancement de la correction.
* Une fois la faille corrigée et la mise à jour publiée sur les Stores (Microsoft & Snap), je vous créditerai publiquement (si vous le souhaitez) dans les notes de version pour vous remercier de votre aide.

## Note concernant FFmpeg

Simple-Video-Converter utilise **FFmpeg** comme moteur de conversion.

* Si la vulnérabilité concerne directement le binaire `ffmpeg.exe` ou les bibliothèques FFmpeg (et non mon interface ou ma gestion des fichiers), merci de vous référer à la [Politique de sécurité de FFmpeg](https://ffmpeg.org/security.html).
* Toutefois, si mon application utilise FFmpeg d'une manière non sécurisée, cela relève de ma responsabilité et doit m'être signalé.

Merci de m'aider à garder Simple-Video-Converter sûr pour tous !
