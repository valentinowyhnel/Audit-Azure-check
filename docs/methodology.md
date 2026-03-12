# Méthodologie d'Audit AD & Azure

Cette méthodologie s'inspire des approches Red Team, Mandiant et des recommandations Microsoft (ESAE/Zero Trust).

## 📅 Phases du Projet

### Phase 1 – Planification & Kickoff
- **Objectifs** : Définir le périmètre, recueillir l’architecture, établir la gouvernance.
- **Livrables** : Charte d’audit, planning, accès/credentials.

### Phase 2 – Inventaire & Cartographie AD On-Prem
- **Objectifs** : Inventorier les DCs, OUs, Sites, FSMO, Trusts et GPOs.
- **Livrables** : Rapport d’inventaire AD, diagrammes de forêts.

### Phase 3 – Pentest & Énumérations AD On-Prem
- **Objectifs** : Découverte de vulnérabilités (ACLs, SPN, Délégations) et simulation d'attaques (Kerberoast, DCSync).
- **Outils** : BloodHound, PingCastle, PowerView.

### Phase 4 – Attack Path Modeling
- **Objectifs** : Cartographier formellement les chemins d’attaque vers les Domain Admins.
- **Livrables** : Graphes BloodHound, priorisation des risques.

### Phase 5 – Audit Azure AD / Entra ID
- **Objectifs** : Analyse de la sécurité cloud (MFA, Conditional Access, Roles, Applications).
- **Points clés** : Durcissement des conditions d'accès, inventaire des Service Principals.

### Phase 6 – Audit Hybrid Identity (AD Connect)
- **Objectifs** : Examen de l’infrastructure de synchronisation et des flux d'authentification (PTA/PHS).
- **Livrables** : Rapport AD Connect, recommandations de filtrage.

### Phase 7 – Audit Monitoring et Détection
- **Objectifs** : Évaluer la couverture de détection (logs AD, Sentinel, Defender for Identity).
- **Livrables** : Playbooks de détection, configuration de logging.

### Phase 8 – Rapport Final et Remédiation
- **Objectifs** : Consolidation des findings et priorisation des risques.
- **Livrables** : Rapport détaillé, Executive Summary, Plan de remédiation.

---

## ⚙️ Hypothèses et Variables d’Audit

- **Taille de l'infrastructure** : Adaptable (Petite/Moyenne/Grosse infra).
- **Niveau d'accès** : Accès *Lecture Seule* privilégié (Read-Only) recommandé pour l'audit.
- **Licences** : Requiert idéalement **Entra ID P1/P2** pour un accès complet aux logs.
- **Environnement** : Firewall ouvert pour les flux Azure Connect / Sentinel.
