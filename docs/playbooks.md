# 📖 Playbooks & Analyses d'Attaques

Ce document détaille les vecteurs d'attaque modernes sur Azure et Active Directory.

## 🎯 Analyses d'Attaques Azure AD

### 1. Bypass MFA & OAuth
- **OAuth Consent Phishing** : Contourner le MFA en incitant un utilisateur à accorder des permissions à une application malveillante.
- **Token Theft** : Vol de jetons de session ou de PRT (Primary Refresh Token).

### 2. Persistance & Backdoors
- **PTA & PHS Spy** : Utilisation de `AADInternals` pour intercepter les mots de passe lors de l'authentification Pass-Through (PTA).
- **Service Principal Abuse** : Création de secrets sur des applications avec des privilèges élevés (Microsoft Graph).

### 3. Escalade de Privilèges
- **Graphes BloodHound** : Identifier le chemin le plus court vers un rôle "Global Admin".
- **PIM Abuse** : Abuser des processus d'élévation de privilèges (Privileged Identity Management).

## 🛡️ Stratégies de Détection
- **Monitoring Sentinel** : Utiliser les journaux `SignInLogs` et `AuditLogs`.
- **Defender for Identity** : Détection des anomalies sur les contrôleurs de domaine (DCSync, Pass-the-Hash).
